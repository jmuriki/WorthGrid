***

>[!quote] Описание
_Иногда требуется игнорировать исключение.
Игнорировать ошибку лучше с помощью контекстного менеджера suppress вместо блока try except._

***
### Пример 1

> [!fail]
> ```python
> try:
>     function()
> except UnimportantError:
>     pass
> ```

> [!success]
> ```python
> from contextlib import suppress
> 
> with suppress(UnimportantError):
>     function()
> ```

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***
### Пример 2

> [!fail]
> ```python
> try:
>     function()
> except UnimportantError:
>     continue
> ```

> [!success]
> ```python
> from contextlib import suppress
> 
> with suppress(UnimportantError):
>     function()
> ```

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
