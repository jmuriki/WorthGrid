***
```url
github.com/jmuriki/WorthGrid/wiki/try-except-вместо-suppress#использование-try-except-вместо-suppress
```
# Использование try-except вместо suppress
- [ ] Анти-паттерн: Использование try-except вместо suppress

_Иногда требуется игнорировать исключение.
Игнорировать ошибку лучше с помощью контекстного менеджера suppress вместо блока try except._

***
```url
github.com/jmuriki/WorthGrid/wiki/try-except-вместо-suppress#try-except-pass-вместо-suppress
```
### try-except pass вместо suppress
- [ ] Пример: try-except pass вместо suppress

```python
"""Плохо"""
try:
    function()
except UnimportantError:
    pass


"""Хорошо"""
from contextlib import suppress

with suppress(UnimportantError):
    function()
```

[[[[SOURCE CODE PY]]

[[SOURCE CODE PY#Бегло проследить поток исполнения программы]]

***
```url
github.com/jmuriki/WorthGrid/wiki/try-except-вместо-suppress#try-except-continue-вместо-suppress
```
### try-except continue вместо suppress
- [ ] Пример: try-except continue вместо suppress

```python
"""Плохо"""
try:
    function()
except UnimportantError:
    continue


"""Хорошо"""
from contextlib import suppress

with suppress(UnimportantError):
    function()
```

[[SOURCE CODE PY]]

[[SOURCE CODE PY#Бегло проследить поток исполнения программы]]

***
```url
github.com/jmuriki/WorthGrid/wiki/try-except-вместо-suppress#контакты
```
# [[Контакты]]
Если не удалось найти ничего подходящего или есть идея по улучшению, [пиши сюда](https://github.com/jmuriki/WorthGrid/wiki/Контакты).
