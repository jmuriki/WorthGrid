#!/usr/bin/env python3

import os
import re
import argparse
import subprocess

from datetime import datetime


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
WORTH_GRID_PATH = os.path.join(BASE_DIR, '..', 'ЦЕННОСТНАЯ СЕТКА')

INTERFACE_LABEL = '## 🖥️'
USER_LABEL = 'Тип Пользователя'
FUNCTION_LABEL = 'Ключевая Функция'
CASE_LABEL = '>>- ['
ANTI_PATTERN_LABEL = '>- [ ] [['
LABELS = [USER_LABEL, FUNCTION_LABEL, CASE_LABEL, ANTI_PATTERN_LABEL]

SUCCESS_SIGN = '\u2705'
WARNING_SIGN = '\U000026A0\U0000FE0F'
CANCEL_SIGN = '\U0001F6AB'


def create_parser():
    parser = argparse.ArgumentParser(description='Скрипт для обновления репозитория Ценностной Сетки (WorthGrid) и создания отчётов.')
    parser.add_argument('-c', '--clear', action='store_true', help='Обнулить чек-боксы.')
    parser.add_argument('-d', '--detailed', action='store_true', help='Детализированный отчёт.')
    parser.add_argument('-e', '--erase', action='store_true', help='Стереть любые изменения, включая незапушенные коммиты.')
    parser.add_argument('-n', '--name', type=str, default='ЦС_отчёт', help='Задать альтернативное название отчёта.')
    parser.add_argument('-p', '--preview', action='store_true', help='Вывести превью отчёта в консоль.')
    parser.add_argument('-u', '--update', action='store_true', help='Обновить репозиторий ЦС.')
    return parser


def check_repo_updates(remote='origin', branch='main'):
    try:
        subprocess.run(['git', 'fetch', remote], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Подсчитываем количество коммитов, которые есть в удалённом репозитории, но отсутствуют в локальном
        new_commits_cmd = ['git', 'rev-list', '--count', f'{branch}..{remote}/{branch}']
        new_commits = subprocess.check_output(new_commits_cmd).strip().decode('utf-8')
    except subprocess.CalledProcessError:
        msg = f'{CANCEL_SIGN} Ошибка: Проверьте, что репозиторий корректен и Git установлен.'

    try:
        commits_to_pull = int(new_commits)
    except (UnboundLocalError, ValueError):
        commits_to_pull = 0

    if commits_to_pull:
        msg = f'{WARNING_SIGN} Cвежая версия Ценностной Сетки доступна для скачивания.'
    else:
        msg = f'{SUCCESS_SIGN} Установлена свежая версия Ценностной Сетки.'

    return msg


def get_repo_updates(remote='origin', branch='main'):
    try:
        # Подсчитываем количество коммитов, которые есть в локальном репозитории, но не запушены в удалённый
        ahead_commits_cmd = ['git', 'rev-list', '--count', f'{remote}/{branch}..{branch}']
        ahead_commits = subprocess.check_output(ahead_commits_cmd).strip().decode('utf-8')
    except subprocess.CalledProcessError:
        msg = f'{CANCEL_SIGN} Ошибка: Проверьте, что репозиторий корректен и Git установлен.'

    try:
        commits_to_push = int(ahead_commits)
    except ValueError:
        commits_to_push = 0

    if commits_to_push:
        msg = f'{WARNING_SIGN} Предупреждение: у вас есть незапушенные коммиты! Обновите репозиторий вручную.'
    else:
        try:
            subprocess.run(['git', 'pull'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
            msg = f'{SUCCESS_SIGN} Установлена свежая версия Ценностной Сетки.'
        except subprocess.CalledProcessError:
            try:
                subprocess.run(['git', 'stash'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
                subprocess.run(['git', 'pull'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
                # subprocess.run(['git', 'stash', 'pop'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
                msg = f'{WARNING_SIGN} Установлена свежая версия Ценностной Сетки. Внесённые ранее изменения можно накатить с помощью команды "git shash pop".'
            except subprocess.CalledProcessError:
                msg = f'{CANCEL_SIGN} Ошибка: Попробуйте скачать обновление репозитория вручную.'

    return msg


def find_md_files():
    md_filepaths = []
    for dirpath, _, filenames in os.walk(WORTH_GRID_PATH):
        for filename in filenames:
            if filename.endswith('.md'):
                md_filepaths.append(os.path.join(dirpath, filename))
    return md_filepaths


def get_interface_name(md_path):
    basename = os.path.basename(md_path)
    name, _ = os.path.splitext(basename)
    with open(md_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    interface_pattern = re.compile(r'^##\s*.*Интерфейс.*$')
    for line in lines:
        interface_match = interface_pattern.match(line)
        if interface_match:
            return f'{name} - {line.replace('## 🖥️ ', '').strip()}'


def get_report_lines(md_filepaths, is_detailed):
    report_lines = []

    for md_path in md_filepaths:
        with open(md_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        new_lines = []
        marked_lines = []

        case_line = ''
        case_line_index = None
        function_line = ''
        function_line_index = None
        user_line = ''
        user_line_index = None
        interface_line = 'Interface'
        interface_line_index = None

        for index, line in enumerate(lines):

            if CASE_LABEL in line:
                case_line = line
                case_line_index = index
            elif FUNCTION_LABEL in line:
                case_line = ''
                case_line_index = None
                function_line = line
                function_line_index = index
            elif USER_LABEL in line:
                case_line = ''
                case_line_index = None
                function_line = ''
                function_line_index = None
                user_line = line
                user_line_index = index
            elif INTERFACE_LABEL in line:
                case_line = ''
                case_line_index = None
                function_line = ''
                function_line_index = None
                user_line = ''
                user_line_index = None
                interface_line = line
                interface_line_index = index

            if line.strip().startswith('- [x]'):

                if interface_line:
                    marked_lines.append(f'\n{interface_line.strip()}')
                    new_lines[interface_line_index] = checked_interface_line
                    interface_line = None
                    interface_line_index = None

                if user_line and '- [x]' not in user_line:
                    checked_user_line = user_line.replace('- [ ]', '- [x]')
                    marked_lines.append(f'\n{checked_user_line.strip()}')
                    new_lines[user_line_index] = checked_user_line

                    user_line = ''
                    user_line_index = None

                if function_line and '- [x]' not in function_line:
                    checked_function_line = function_line.replace('- [ ]', '- [x]')
                    marked_lines.append(f'\n{checked_function_line.strip()}')
                    new_lines[function_line_index] = checked_function_line

                    function_line = ''
                    function_line_index = None

                if case_line and '- [x]' not in case_line:
                    checked_case_line = case_line.replace('- [ ]', '- [x]')
                    marked_lines.append(f'\n{checked_case_line.strip()}')
                    new_lines[case_line_index] = checked_case_line

                    case_line = ''
                    case_line_index = None

                if is_detailed:
                    marked_lines.append(f'{line.strip()}')
                elif any(keyword in line for keyword in LABELS):
                    marked_lines.append(f'{line.strip()}')

            new_lines.append(line)

        with open(md_path, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)

        if marked_lines:
            marked_lines.insert(0, f'# {get_interface_name(md_path)}')
            if report_lines:
                report_lines.extend('\n')
            report_lines.extend(marked_lines)

    refined_lines = refine_report_lines(report_lines)
    return refined_lines


def refine_report_lines(report_lines):
    if report_lines:
        for index, line in enumerate(report_lines):
            if USER_LABEL in line:
                report_lines[index] = f'    {line}'
            elif FUNCTION_LABEL in line:
                report_lines[index] = f'        {line}'
            elif CASE_LABEL in line:
                report_lines[index] = f'            {line}'
            elif ANTI_PATTERN_LABEL in line:
                report_lines[index] = line
            elif '- [x]' in line:
                report_lines[index] = f'                {line}'
    return report_lines


def create_report(marked_lines, name):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    reports_directory = os.path.join(BASE_DIR, '..', 'reports')
    os.makedirs(reports_directory, exist_ok=True)

    report_file_path = os.path.join(reports_directory, f'{timestamp}_{name}.md')

    with open(report_file_path, 'w', encoding='utf-8') as file:
        file.writelines(line + '\n' for line in marked_lines)

    return report_file_path


def erase_changes(remote='origin', branch='main'):
    try:
        subprocess.run(['git', 'reset', '--hard', f'{remote}/{branch}'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        msg = f'{SUCCESS_SIGN} Все изменения в репозитории сброшены.'
    except subprocess.CalledProcessError:
        msg = f'{CANCEL_SIGN} Ошибка: Проверьте, что репозиторий корректен и Git установлен.'
    return msg


def clear_check_boxes(md_filepaths):
    for md_path in md_filepaths:
        with open(md_path, 'r+', encoding='utf-8') as file:
            content = file.read().replace('- [x]', '- [ ]')
            file.seek(0)
            file.write(content)
            file.truncate()


def main():
    parser = create_parser()
    args = parser.parse_args()

    is_clear = args.clear
    is_detailed = args.detailed
    is_erase = args.erase
    report_name = args.name
    is_preview = args.preview
    is_update = args.update

    repo_update_msg = check_repo_updates()
    print(repo_update_msg)
    if not is_update and 'доступна' in repo_update_msg:
        print(f'{WARNING_SIGN} Запустите скрипт с флагом "-u" для обновления.')

    md_filepaths = find_md_files()
    report_lines = get_report_lines(md_filepaths, is_detailed)

    if report_lines and is_preview:
        print('\n'.join(report_lines))
    elif report_lines:
        report_file_path = create_report(report_lines, report_name)
        print(f'{SUCCESS_SIGN} Отчёт успешно сформирован.')
        print('Полный путь к отчёту:')
        print(f'"{report_file_path}"')
    else:
        print(f'{WARNING_SIGN} Все чек-боксы пусты. Формирование отчёта приостановлено.')

    if is_erase:
        result_msg = erase_changes()
        print(result_msg)
    elif is_clear and report_lines:
        clear_check_boxes(md_filepaths)
        print(f'{SUCCESS_SIGN} Чек-боксы успешно сброшены.')

    if is_update and 'доступна' in repo_update_msg:
        update_msg = get_repo_updates()
        print(update_msg)


if __name__ == '__main__':
    main()
