#!/usr/bin/env python3

import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description='''
            Программа имитирует эхо,
            выводя в консоль введённый текст
            заданное количество раз.
        '''
    )
    parser.add_argument(
        '-t', '--text', type=str, default='Ауу',
        help='Текст для повторения'
    )
    parser.add_argument(
        '-r', '--repeat', type=int, default=10,
        help='Количество повторений'
    )
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    text = args.text
    repeat = args.repeat

    if not text:
        print('Ошибка: необходимо указать текст.')
        return

    if repeat <= 0:
        print('Ошибка: количество повторений должно быть больше 0.')
        return

    echo = ''
    pause = '...'
    for repeat_num in range(1, repeat + 1):
        echo += text + (pause * repeat_num)

    print(echo)


if __name__ == '__main__':
    main()
