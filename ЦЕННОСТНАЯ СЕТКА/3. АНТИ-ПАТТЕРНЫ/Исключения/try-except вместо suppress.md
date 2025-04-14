#исключения #try-except 
***

>[!quote] Описание
_Иногда требуется игнорировать исключение.
Вместо блока try except игнорировать ошибку лучше с помощью контекстного менеджера suppress._

***
### 💡 Пример


**Плохо:**
```python
try:
	do_something()
except NotImportantError:
	pass
```

**Плохо:**
```python
try:
	do_something()
except NotImportantError:
	continue
```

**Хорошо:**
```python
from contextlib import suppress

with suppress(NotImportantError):
	do_something()
```

> [!example] Связанные кейсы
> - Интерфейс: [[SOURCE CODE PY]]
> 	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
