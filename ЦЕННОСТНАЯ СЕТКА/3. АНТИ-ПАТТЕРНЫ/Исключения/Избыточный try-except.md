#исключения #try-except 
***

>[!quote] Описание
_Использовать try-except и исключения следует в тех случаях, когда нет более простых или встроенных способов справиться с возможной ошибкой._

***
### 💡 Пример 1


**Плохо:**
```python
try:
	value = collection['key']
except KeyError:
	value = None
```

**Хорошо:**
```python
value = collection.get('key')
```

***
### 💡 Пример 2
`try-except вместо метода .get()`

**Плохо:**
```python
capitals = {
	'Россия': 'Москва',
	'Англия': 'Лондон',
}


def get_capitals(country):
	try:
		capital = capitals[country]
	except KeyError:
		capital = None
	finally:
		return capital


print(get_capitals('Китай'))
```

**Хорошо:**
```python
capitals = {
	'Россия': 'Москва',
	'Англия': 'Лондон',
}


def get_capitals(country):
   return capitals.get(country)


print(get_capitals('Китай'))
```

***
### 💡 Пример 3
`try-except вместо метода .isinstance()`

**Плохо:**
```python
def calculate(num1, num2):
	try:
		result = num1 + num2
		return result
	except TypeError:
		logging.warning('Ошибка: аргументы должны быть числами.')


print(calculate(1, '2'))
```

**Хорошо:**
```python
def calculate(num1, num2):
	if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
		result = num1 + num2
		return result
	logging.warning('Ошибка: аргументы должны быть числами.')


print(calculate(1, '2'))
```

***

> [!example] Связанные кейсы
> - Интерфейс: [[SOURCE CODE PY]]
>   - Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
