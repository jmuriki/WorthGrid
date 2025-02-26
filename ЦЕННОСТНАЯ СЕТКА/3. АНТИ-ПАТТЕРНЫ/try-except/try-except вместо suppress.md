***
# Использование try-except вместо suppress
- [ ] Анти-паттерн: Использование try-except вместо suppress

_Иногда требуется игнорировать исключение.
Игнорировать ошибку лучше с помощью контекстного менеджера suppress вместо блока try except._

***
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
## [[Контакты]]
Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
