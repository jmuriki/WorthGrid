#!/usr/bin/env python3

import os
import re
import logging
import argparse
import subprocess

from datetime import datetime


logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s')
logger = logging.getLogger(__name__)

SUCCESS_SIGN = '\u2705'
WARNING_SIGN = '\U000026A0\U0000FE0F'
CANCEL_SIGN = '\U0001F6AB'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
WORTH_GRID_PATH = os.path.join(BASE_DIR, '..', 'ЦЕННОСТНАЯ СЕТКА')

INTERFACE_LABEL = '🖥️'
USER_LABEL = '👤'
FUNCTION_LABEL = '𝑓'
CASE_LABEL = '✔'
ANTI_PATTERNS_LABEL = '❌'
ANTI_PATTERN_ATTRIBUTE = '>- [x] [['
LABELS = [USER_LABEL, FUNCTION_LABEL, CASE_LABEL, ANTI_PATTERNS_LABEL, ANTI_PATTERN_ATTRIBUTE]


def create_parser():
    parser = argparse.ArgumentParser(
        description='Скрипт для обновления репозитория Ценностной Сетки (WorthGrid) и создания отчётов.',
    )
    parser.add_argument(
        '-c', '--clear', action='store_true',
        help='Обнулить чек-боксы.',
    )
    parser.add_argument(
        '-d', '--detailed', action='store_true',
        help='Детализированный отчёт.',
    )
    parser.add_argument(
        '-e', '--erase', action='store_true',
        help='Стереть любые изменения, включая незапушенные коммиты.',
    )
    parser.add_argument(
        '-n', '--name', type=str, default='ЦС_отчёт',
        help='Задать альтернативное название отчёта.',
    )
    parser.add_argument(
        '-p', '--preview', action='store_true',
        help='Вывести превью отчёта в консоль.',
    )
    parser.add_argument(
        '-u', '--update', action='store_true',
        help='Обновить репозиторий ЦС.',
    )
    return parser


def check_repo_updates(remote='origin', branch='main'):
    try:
        subprocess.run(['git', 'fetch', remote], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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

        case_line = function_line = user_line = anti_patterns_line = ''
        case_line_index = function_line_index = user_line_index = None
        anti_patterns_level = None

        for current_line_index, line in enumerate(lines):

            if ANTI_PATTERNS_LABEL in line:
                anti_patterns_line = line
                anti_patterns_level = line.count('#')
            elif CASE_LABEL in line:
                case_line = line
                case_line_index = current_line_index
            elif FUNCTION_LABEL in line:
                case_line = ''
                case_line_index = None
                function_line = line
                function_line_index = current_line_index
            elif USER_LABEL in line:
                case_line = ''
                case_line_index = None
                function_line = ''
                function_line_index = None
                user_line = line
                user_line_index = current_line_index
            elif line.strip().startswith(('- [x]', '>- [x]')):

                if line.strip().startswith(ANTI_PATTERN_ATTRIBUTE) and anti_patterns_line:
                    if anti_patterns_level < 4:
                        case_line = ''
                        case_line_index = None
                        if anti_patterns_level < 3:
                            function_line = ''
                            function_line_index = None
                            if anti_patterns_level < 2:
                                user_line = ''
                                user_line_index = None

                if user_line:
                    user_check_box_line_index = user_line_index + 1
                    user_check_box_line = lines[user_check_box_line_index].replace('- [ ]', '- [x]')
                    marked_lines.append(f'{user_line.strip()}')
                    if user_check_box_line_index < current_line_index:
                        new_lines[user_check_box_line_index] = user_check_box_line

                    user_line = ''
                    user_line_index = None

                if function_line:
                    function_check_box_line_index = function_line_index + 1
                    function_check_box_line = lines[function_check_box_line_index].replace('- [ ]', '- [x]')
                    marked_lines.append(f'{function_line.strip()}')
                    if function_check_box_line_index < current_line_index:
                        new_lines[function_check_box_line_index] = function_check_box_line

                    function_line = ''
                    function_line_index = None

                if case_line:
                    case_check_box_line_index = case_line_index + 5
                    case_check_box_line = lines[case_check_box_line_index].replace('- [ ]', '- [x]')
                    marked_lines.append(f'{case_line.strip()}')
                    if case_check_box_line_index < current_line_index:
                        new_lines[case_check_box_line_index] = case_check_box_line

                    case_line = ''
                    case_line_index = None

                if anti_patterns_line:
                    marked_lines.append(f'{anti_patterns_line.strip()}')
                    anti_patterns_line = ''

                if is_detailed or ANTI_PATTERN_ATTRIBUTE in line:
                    marked_lines.append(f'{line.strip()}')

            new_lines.append(line)

        with open(md_path, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)

        if marked_lines:
            marked_lines.insert(0, f'# {get_interface_name(md_path)}')
            if report_lines:
                report_lines.extend('\n')
            report_lines.extend(marked_lines)

    return report_lines


def finalize_report_lines(report_lines):
    if report_lines:
        finalized_report_lines = ['\nОтчёт об использованных Интерфейсах, Функциях, Историях и Анти-паттернах:\n']
        for line in report_lines:
            if ANTI_PATTERNS_LABEL in line:
                finalized_report_lines.append(f'{line.replace('[', '').replace(']', '')}:')
            elif ANTI_PATTERN_ATTRIBUTE in line:
                finalized_report_lines.append(line.replace('>- [x] ', ''))
            elif FUNCTION_LABEL in line:
                finalized_report_lines.append(f'{line.replace('𝑓', '𝑓 Функция:')}')
            elif CASE_LABEL in line:
                finalized_report_lines.append(f'{line.replace('✔', '✔ История:')}')
            elif '- [x]' in line:
                finalized_report_lines.append(f'                {line}')
            else:
                finalized_report_lines.append(line)
        finalized_report_lines.append('\n')
        return finalized_report_lines


def save_report(marked_lines, name):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    reports_directory = os.path.join(BASE_DIR, '..', 'reports')
    os.makedirs(reports_directory, exist_ok=True)

    report_file_path = os.path.join(reports_directory, f'{timestamp}_{name}.md')

    with open(report_file_path, 'w', encoding='utf-8') as file:
        file.writelines(line + '\n' for line in marked_lines)

    return report_file_path


def erase_changes(remote='origin', branch='main'):
    try:
        subprocess.run(
            ['git', 'reset', '--hard', f'{remote}/{branch}'],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
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

    should_clear = args.clear
    is_detailed = args.detailed
    should_erase = args.erase
    report_name = args.name
    is_preview = args.preview
    should_update = args.update

    repo_update_msg = check_repo_updates()
    logger.info(repo_update_msg)
    if not should_update and 'доступна для скачивания' in repo_update_msg:
        logger.info(f'{WARNING_SIGN} Запустите скрипт с флагом "-u" для обновления.')

    md_filepaths = find_md_files()
    report_lines = get_report_lines(md_filepaths, is_detailed)
    finalized_report_lines = finalize_report_lines(report_lines)

    if finalized_report_lines and is_preview:
        print('\n'.join(finalized_report_lines))
    elif finalized_report_lines:
        report_file_path = save_report(finalized_report_lines, report_name)
        logger.info(f'{SUCCESS_SIGN} Отчёт успешно сформирован.')
        print('\nПолный путь к отчёту:')
        print(f'"{report_file_path}"\n')
    else:
        logger.info(f'{WARNING_SIGN} Все чек-боксы пусты. Формирование отчёта приостановлено.')

    if should_erase:
        result_msg = erase_changes()
        logger.info(result_msg)
    elif should_clear and finalized_report_lines:
        clear_check_boxes(md_filepaths)
        logger.info(f'{SUCCESS_SIGN} Чек-боксы успешно сброшены.')

    if should_update and 'доступна для скачивания' in repo_update_msg:
        update_msg = get_repo_updates()
        logger.info(update_msg)


if __name__ == '__main__':
    main()
