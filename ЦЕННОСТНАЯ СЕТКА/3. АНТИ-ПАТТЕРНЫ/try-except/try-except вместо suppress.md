***

>[!quote] Описание
_Иногда требуется игнорировать исключение.
Игнорировать ошибку лучше с помощью контекстного менеджера suppress вместо блока try except._

***
### 💡 Пример 1


**Плохо:**
```python
try:
    do_something()
except UnimportantError:
    pass
```

**Хорошо:**
```python
from contextlib import suppress

with suppress(UnimportantError):
    do_something()
```

***
### 💡 Пример 2


**Плохо:**
```python
try:
    do_something()
except UnimportantError:
    continue
```

**Хорошо:**
```python
from contextlib import suppress

with suppress(UnimportantError):
    do_something()
```

***

> [!example] Связанные кейсы
> - Интерфейс: [[SOURCE CODE PY]]
> 	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
