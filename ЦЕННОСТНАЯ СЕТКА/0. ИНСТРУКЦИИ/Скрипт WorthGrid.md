***
```url
github.com/jmuriki/WorthGrid/wiki/Скрипт-WorthGrid#как-пользоваться-скриптом-wgpy
```
# Как пользоваться скриптом wg.py?
_Описанные ниже опции можно свободно комбинировать между собой._
***
```url
github.com/jmuriki/WorthGrid/wiki/Скрипт-WorthGrid#справка-по-функциям-скрипта
```
## Справка по функциям скрипта

`WorthGrid.wiki/scripts/`
```sh
./wg.py -h
```

***
```url
github.com/jmuriki/WorthGrid/wiki/Скрипт-WorthGrid#создание-отчёта
```
## Создание отчёта

Создать отчёт об отмеченных `Интерфейсах`, `Функциях`, `Историях` и `Анти-паттернах`:

`WorthGrid.wiki/scripts/`
```sh
./wg.py
```

***
```url
github.com/jmuriki/WorthGrid/wiki/Скрипт-WorthGrid#детализированный-отчёт
```
## Детализированный отчёт

Создать детализированный отчёт с пунктами проверки `Историй`:

`WorthGrid.wiki/scripts/`
```sh
./wg.py -d
```

***
```url
github.com/jmuriki/WorthGrid/wiki/Скрипт-WorthGrid#превью-отчёта
```
## Превью отчёта

Вывести в консоль превью отчёта без формирования файла отчёта:

`WorthGrid.wiki/scripts/`
```sh
./wg.py -p
```

***
```url
github.com/jmuriki/WorthGrid/wiki/Скрипт-WorthGrid#наименование-отчёта
```
## Наименование отчёта

Кастомизировать название отчёта:

`WorthGrid.wiki/scripts/`
```sh
./wg.py -n <кастомизированное название>
```

***
```url
github.com/jmuriki/WorthGrid/wiki/Скрипт-WorthGrid#cброс-чек-боксов
```
## Cброс чек-боксов

Сбросить отмеченные чек-боксы:

`WorthGrid.wiki/scripts/`
```sh
./wg.py -c
```

***
```url
github.com/jmuriki/WorthGrid/wiki/Скрипт-WorthGrid#cброс-любых-изменений
```
## Cброс любых изменений

Сбросить любые внесённые изменения, включая незапушенные коммиты, можно с помощью скрипта с флагом `-e:

`WorthGrid.wiki/scripts/`
```sh
./wg.py -e
```

***
```url
github.com/jmuriki/WorthGrid/wiki/Скрипт-WorthGrid#обновление-цс
```
## Обновление ЦС

Обновляйте репозиторий перед каждым использованием, так как ЦС находится в стадии активной разработки:

`WorthGrid.wiki/scripts/`
```sh
./wg.py -u
```

***
```url
github.com/jmuriki/WorthGrid/wiki/Скрипт-WorthGrid#контакты
```
# [[Контакты]]
Вопросы и предложения можно направлять [сюда](https://github.com/jmuriki/WorthGrid/wiki/Контакты).
