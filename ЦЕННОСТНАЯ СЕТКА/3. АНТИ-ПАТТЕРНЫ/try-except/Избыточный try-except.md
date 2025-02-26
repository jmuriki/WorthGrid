***
```url
github.com/jmuriki/WorthGrid/wiki/Избыточный-try-except#избыточное-использование-try-except
```
# Избыточное использование try-except
- [ ] Анти-паттерн: Избыточное использование try-except

_Использовать try-except и исключения следует в тех случаях, когда нет более простых или встроенных способов справиться с возможной ошибкой._

***
```url
github.com/jmuriki/WorthGrid/wiki/Избыточный-try-except#try-except-вместо-метода-get
```
### try-except вместо метода .get()
- [ ] Пример: try-except вместо метода .get()

```python
"""Плохо"""
try:
    value = my_dict['key']
except KeyError:
    value = None


"""Хорошо"""
value = my_dict.get('key')
```

```python
capitals = {
    'Россия': 'Москва',
    'Англия': 'Лондон',
}


"""Плохо"""
def get_capitals(country):
    try:
        capital = capitals[country]
    except KeyError:
        capital = None
    finally:
        return capital

"""Хорошо"""
def get_capitals(country):
   return capitals.get(country)


print(get_capitals('Китай'))
```

[[SOURCE CODE PY]]

[[SOURCE CODE PY#Бегло проследить поток исполнения программы]]

***
```url
github.com/jmuriki/WorthGrid/wiki/Избыточный-try-except#try-except-вместо-метода-isinstance
```
### try-except вместо метода .isinstance()
- [ ] Пример: try-except вместо метода .isinstance()

```python
"""Плохо"""
def calculate(num1, num2):
	try:
		result = num1 + num2
		return result
	except TypeError:
		logging.warning('Ошибка: аргументы должны быть числами.')


"""Хорошо"""
def calculate(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        result = num1 + num2
        return result
    logging.warning('Ошибка: аргументы должны быть числами.')


print(calculate(1, '2'))
```

[[SOURCE CODE PY]]

[[SOURCE CODE PY#Бегло проследить поток исполнения программы]]

***
```url
github.com/jmuriki/WorthGrid/wiki/Избыточный-try-except#контакты
```
# [[Контакты]]
Если не удалось найти ничего подходящего или есть идея по улучшению, [пиши сюда](https://github.com/jmuriki/WorthGrid/wiki/Контакты).
