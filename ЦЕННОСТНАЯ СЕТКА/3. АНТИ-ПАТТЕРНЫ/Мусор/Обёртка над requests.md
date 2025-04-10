#мусор #декомпозиция 
***

> [!cite] Описание
>_Если функция не упрощает код, то от нее лучше избавиться. Лишняя абстракция затруднит понимание и усложнит внесение правок. Функции полезны, когда они инкапсулируют сложность, прячут её внутри себя и таким образом упрощают внешний код._

***
### 💡 Пример


**Плохо:**
```python
import requests


def send_request(url):
	response = requests.get(url)
	response.raise_for_status()
	return response


def main():
	...
	try:
		response = send_request(url)
	except:
		...
```

**Хорошо:**
```python
import requests


def main():
	...
	try:
		response = requests.get(url)
		response.raise_for_status()
	except:
		...
```

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
