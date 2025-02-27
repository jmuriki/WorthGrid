***

>[!quote] Описание
_Если ошибки похожи, то лучше обрабатывать их в одном блоке except.
Такой подход позволяет уменьшить кол-во кода и улучшить читаемость._

***
### Копипаста в try-except

> [!fail]
> ```python
> try:
>     function()
> except ValueError:
>     logging.error('Value error')
> except IndexError:
>     logging.error('Index error')
> ```

> [!success]
> ```python
> try:
>     function()
> except (ValueError, IndexError) as e:
>     logging.error(f'Error: {e}')
> ```

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
