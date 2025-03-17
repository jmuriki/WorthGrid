***

> [!cite] Описание
>_HTTP статус позволяет гарантировать, что запрос был выполнен успешно и сервер вернул ожидаемый ответ. Не проверив HTTP статус ответа, вы рискуете получить неожиданные данные, которые обязательно сломают программу, но уже в другом месте._

***
### 💡 Пример


**Плохо:**
```python
def do_something(url, params):
	response = requests.get(url, params=params)
	...
```

**Хорошо:**
```python
def do_something(url, params):
	try:
		response = requests.get(url, params=params)
		response.raise_for_status()
		...
	except requests.exceptions.HTTPError as e:
		logging.error(f'Ошибка HTTPError: {e}')
		...
	except requests.exceptions.ConnectionError as e:
		logging.error(f'Ошибка ConnectionError: {e}')
		...
```

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
