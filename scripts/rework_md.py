#!/usr/bin/env python3

import os
import re
import argparse


WIKI_BASE_URL = 'github.com/jmuriki/WorthGrid/wiki/'

SCRIPTS_PATH = os.path.abspath(os.path.dirname(__file__))
BASE_PATH = os.path.join(SCRIPTS_PATH, '..')
WORTH_GRID_PATH = os.path.join(SCRIPTS_PATH, '..', 'ЦЕННОСТНАЯ СЕТКА')
TEMPLATES_PATH = os.path.join(SCRIPTS_PATH, '..', 'templates')
ANTI_PATTERNS_PATH = os.path.join(WORTH_GRID_PATH, '3. АНТИ-ПАТТЕРНЫ')

SYMBOLS_TO_REMOVE_FROM_LINK = "\"!#$%&'()*+,./:;<=>?@\\^_`{}[]~"

SUCCESS_SIGN = '\u2705'
WARNING_SIGN = '\U000026A0\U0000FE0F'
CANCEL_SIGN = '\U0001F6AB'


def create_parser():
    parser = argparse.ArgumentParser(description='Скрипт для шаблонной правки файлов Ценностной Сетки.')
    parser.add_argument('-p', '--path', type=str, default=WORTH_GRID_PATH, help='Путь к директории с .md файлами.')
    return parser


def get_md_paths(directory, limits=None):
    md_paths = []

    for root_path, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.md'):
                md_path = os.path.join(root_path, filename)
                md_paths.append(md_path)

    return md_paths


def rework_md_by_patterns(md_path):
    with open(md_path, "r", encoding="utf-8") as file:
        content = file.read()

    new_content = content

    # new_content = new_content.replace('# [[Контакты]]', '## [[Контакты]]')

    # new_content = new_content.replace('[пиши сюда](https://github.com/jmuriki/WorthGrid/wiki/Контакты)', '[[Контакты|пиши сюда]]')

    # # Удаление пустой строки между *** и ```
    # pattern = re.compile(r'(?<=^\*{3}\n)[ \t]*\n(?=^```)', re.MULTILINE)
    # match = pattern.search(content)
    # if match:
    #     new_content = pattern.sub('', content)

    # # Удаление всего до Coming soon... включительно
    # pattern = re.compile(r'# \*\*Coming soon\.\.\.\*\*', re.IGNORECASE)
    # match = pattern.search(content)
    # if match:
    #     new_content = content[match.end():].lstrip()
    #     content = new_content

    with open(md_path, "w", encoding="utf-8") as file:
        file.write(new_content)
        print('Обновленный файл сохранен.')


def get_page_name(md_path):
    basename = os.path.basename(md_path)
    name, _ = os.path.splitext(basename)
    page_name = name.replace(' ', '-')
    return page_name


def remove_patterns(lines):
    new_lines = []
    # pattern = re.compile(r'\*\*\*')
    # for index, line in enumerate(lines):
    #     match = pattern.search(line)
    #     if match:
    #         new_lines = lines[index:]
    #         return new_lines

    is_example = False
    for line in lines:
        line = line.replace('[!fail]', '**Плохо:**').replace('[!success]', '**Хорошо:**')
        if '> [!quote]' in line:
            line = line.replace('> [!quote] Плохо', '**Плохо:**').replace('> [!quote] Хорошо', '**Хорошо:**')
        elif '> [!example] Связанные кейсы' in line:
            is_example = False
        if 'Пример' in line or is_example is True:
            is_example = True
            line = line.replace('> ', '').replace('>', '')
        new_lines.append(line)
    return new_lines


def fix_wrong_labels(lines):
    fixed_lines = []
    wrong_correct_labels = {
        'Вид интерфейса': 'Вид Интерфейса',
        'Тип пользователя': 'Тип Пользователя',
        'Ключевая функция': 'Ключевая Функция',
        'Типичная история': 'Типичная История',
    }
    for line in lines:
        for wrong_label, correct_label in wrong_correct_labels.items():
            if wrong_label in line:
                line = line.replace(wrong_label, correct_label)
        fixed_lines.append(line)
    return fixed_lines


def get_header_url(header_match, page_name):
    header_text = header_match.group(2)
    header_text = header_text.lower().replace(' ', '-')
    header_text = re.sub(r'\[\[([^|\]]+)\|[^\]]+\]\]', r'\1', header_text)
    header_text = re.sub(f'[{re.escape(SYMBOLS_TO_REMOVE_FROM_LINK)}]', '', header_text)
    page_url = f'{WIKI_BASE_URL}{page_name}'
    header_url = f'```url\n{page_url}#{header_text}\n```\n'
    return header_url


def renew_check_boxes(lines):
    new_lines = []
    for line in lines:
        if '- [ ]' in line:
            pass
        new_lines.append(line)
    return new_lines


def renew_links(lines, md_path, page_name):
    new_lines = []

    url_pattern = re.compile(r'^```url')
    header_pattern = re.compile(r'^(#+)\s(.+)')

    total_lines = len(lines)
    next_line_num = 0
    while next_line_num < total_lines:
        line = lines[next_line_num]

        url_match = url_pattern.match(line)
        if url_match:
            next_line_num += 3
            continue

        new_lines.append(line)

        # header_match = header_pattern.match(line)
        # if header_match:
        #     header_url = get_header_url(header_match, page_name)
        #     new_lines.insert(len(new_lines) - 1, header_url)

        next_line_num += 1

    return new_lines


def insert_example_sign(lines):
    new_lines = []
    for line in lines:
        line = line.replace('# Пример', '# 💡 Пример')
        new_lines.append(line)
    return new_lines


def replace_patterns(lines):
    new_lines = []

    bad_line_num = 0
    good_line_num = 0

    total_lines = len(lines)
    next_line_num = 0
    while next_line_num < total_lines:
        line = lines[next_line_num]

        if '> [!fail]' in line:
            return lines
        elif '```python' in line:
            new_lines.append('> [!fail]\n')
            new_lines.append(f'> {line}')
        elif 'Плохо' in line:
            bad_line_num = next_line_num
        elif bad_line_num and 'Хорошо' not in line:
            new_lines.append(f'> {line}')
        elif 'Хорошо' in line:
            bad_line_num = 0
            new_lines.append('> ```\n\n')
            good_line_num = next_line_num
            new_lines.append('> [!success]\n')
            new_lines.append('> ```python\n')
        elif good_line_num and '```' not in line:
            new_lines.append(f'> {line}')
        elif good_line_num and '```' in line:
            good_line_num = 0
            new_lines.append(f'> {line}\n')
        else:
            new_lines.append(line)

        next_line_num += 1

    return new_lines


def main():
    parser = create_parser()
    args = parser.parse_args()

    md_paths = get_md_paths(args.path)
    # md_paths = get_md_paths(ANTI_PATTERNS_PATH)
    for md_path in md_paths:
        # rework_md_by_patterns(md_path)

        with open(md_path, 'r', encoding='utf-8') as file:
            base_lines = file.readlines()

        if base_lines:
            lines = base_lines.copy()
            page_name = get_page_name(md_path)
            # lines = remove_patterns(base_lines)
            # lines = fix_wrong_labels(lines)
            # lines = renew_check_boxes(lines)
            # lines = renew_links(lines, md_path, page_name)
            # lines = insert_example_sign(lines)
            # lines = replace_patterns(lines)

            with open(md_path, 'w', encoding='utf-8') as file:
                file.writelines(lines)


if __name__ == '__main__':
    main()
