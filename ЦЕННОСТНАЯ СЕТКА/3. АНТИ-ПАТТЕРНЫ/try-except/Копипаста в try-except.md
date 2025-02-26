***
```url
github.com/jmuriki/WorthGrid/wiki/Копипаста-в-try-except#использование-нескольких-except-блоков-для-идентичной-обработки-разных-исключений
```
# Использование нескольких `except` блоков для идентичной обработки разных исключений
- [ ] Анти-паттерн: Использование нескольких `except` блоков для идентичной обработки разных исключений

_Если ошибки похожи, то лучше обрабатывать их в одном блоке except.
Такой подход позволяет уменьшить кол-во кода и улучшить читаемость._

***
```url
github.com/jmuriki/WorthGrid/wiki/Копипаста-в-try-except#копипаста-в-try-except
```
### Копипаста в try-except
- [ ] Пример: копипаста в try-except

```python
"""Плохо"""
try:
    function()
except ValueError:
    logging.error('Value error')
except IndexError:
    logging.error('Index error')


"""Хорошо"""
try:
    function()
except (ValueError, IndexError) as e:
    logging.error(f'Error: {e}')
```

[[SOURCE CODE PY]]

[[SOURCE CODE PY#Бегло проследить поток исполнения программы]]

***
```url
github.com/jmuriki/WorthGrid/wiki/Копипаста-в-try-except#контакты
```
# [[Контакты]]
Если не удалось найти ничего подходящего или есть идея по улучшению, [пиши сюда](https://github.com/jmuriki/WorthGrid/wiki/Контакты).
