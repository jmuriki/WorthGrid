***

>[!quote] Описание
_Избегайте использования нескольких `except` блоков для идентичной обработки разных исключений.
Если ошибки похожи, то лучше обрабатывать их в одном блоке except - такой подход позволяет уменьшить кол-во кода и улучшить читаемость._

***
### 💡 Пример


**Плохо:**
```python
try:
	do_something()
except ValueError:
	logging.error('Value error')
except IndexError:
	logging.error('Index error')
```

**Хорошо:**
```python
try:
	do_something()
except (ValueError, IndexError) as e:
	logging.error(f'Error: {e}')
```

> [!example] Связанные кейсы
> - Интерфейс: [[SOURCE CODE PY]]
> 	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
