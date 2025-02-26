***
```url
github.com/jmuriki/WorthGrid/wiki/Exception-вместо-избирательной-обработки#использование-exception-вместо-избирательной-обработки-исключений
```
# Использование `Exception` вместо избирательной обработки исключений
- [ ] Анти-паттерн: Использование `Exception` вместо избирательной обработки исключений

_Не рекомендуется использовать базовое исключение `Exception` вместо того, чтобы избирательно и целенаправленно отлавливать и обрабатывать ошибки.
Как максимум, оно может быть использовано в дополнение к ожидаемым исключениям.
Бывают ситуации, когда могут возникнуть неожиданные исключения, и тогда в завершающем except можно ловить Exception._

***
```url
github.com/jmuriki/WorthGrid/wiki/Exception-вместо-избирательной-обработки#вредный-exception-когда-есть-ограниченный-список-актуальных-исключений
```
### Вредный Exception, когда есть ограниченный список актуальных исключений
- [ ] Пример: Вредный Exception, когда есть ограниченный список актуальных исключений

```python
"""Плохо"""
try:
    function()
except Exception as e:
   logging.error('Произошла ошибка!')


"""Хорошо"""
try:
    function()
except FileNotFoundError:
    logging.error('Файл не найден!')
except PermissionError:
    logging.error('Нет прав доступа к файлу!')
```

[[SOURCE CODE PY]]

[[SOURCE CODE PY#Бегло проследить поток исполнения программы]]

***
```url
github.com/jmuriki/WorthGrid/wiki/Exception-вместо-избирательной-обработки#exception-как-дополнение-к-списку-актуальных-исключений
```
### Exception как дополнение к списку актуальных исключений
- [ ] Пример: Exception как дополнение к списку актуальных исключений

```python
"""Плохо"""
try:
    function()
except Exception as e:
   logging.error('Произошла ошибка!')


"""Приемлено"""
try:
    function()
except FileNotFoundError:
    logging.error('Файл не найден!')
except PermissionError:
    logging.error('Нет прав доступа к файлу!')
except Exception as e:
   logging.error(f'Произошла ошибка: {e}.')
```

[[SOURCE CODE PY]]

[[SOURCE CODE PY#Бегло проследить поток исполнения программы]]

***
```url
github.com/jmuriki/WorthGrid/wiki/Exception-вместо-избирательной-обработки#контакты
```
# [[Контакты]]
Если не удалось найти ничего подходящего или есть идея по улучшению, [пиши сюда](https://github.com/jmuriki/WorthGrid/wiki/Контакты).
