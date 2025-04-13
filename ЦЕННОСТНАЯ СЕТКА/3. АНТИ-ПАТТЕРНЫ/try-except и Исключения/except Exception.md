#исключения
***

>[!quote] Описание
_Не рекомендуется использовать базовое исключение `Exception` вместо того, чтобы избирательно и целенаправленно отлавливать и обрабатывать ошибки.
Как максимум, оно может быть использовано в дополнение к ожидаемым исключениям.
Бывают ситуации, когда могут возникнуть неожиданные исключения, и тогда в завершающем `except` можно ловить `Exception`._

***
### 💡 Пример


**Плохо:**
```python
try:
	do_something()
except Exception:
	logging.error('Произошла ошибка')
```

**Хорошо:**
```python
try:
	do_something()
except FileNotFoundError:
	logging.error('Файл не найден!')
except PermissionError:
	logging.error('Нет прав доступа к файлу!')
```

**Хорошо:**
```python
try:
	do_something()
except FileNotFoundError:
	logging.error('Файл не найден!')
except PermissionError:
	logging.error('Нет прав доступа к файлу!')
except Exception as e:
	logging.error(f'Произошла ошибка: {e}.')
```

> [!example] Связанные кейсы
> - Интерфейс: [[SOURCE CODE PY]]
> 	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
