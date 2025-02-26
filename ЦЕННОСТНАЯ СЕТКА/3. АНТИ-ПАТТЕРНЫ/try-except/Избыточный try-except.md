- [ ] Отметить
***

>[!quote] Описание
_Использовать try-except и исключения следует в тех случаях, когда нет более простых или встроенных способов справиться с возможной ошибкой._

***
### try-except вместо метода .get()

> [!fail]
> ```python
> try:
>     value = my_dict['key']
> except KeyError:
>     value = None
> ```

> [!success]
> ```python
> value = my_dict.get('key')
> ```


> [!fail]
> ```python
> capitals = {
 >   'Россия': 'Москва',
>    'Англия': 'Лондон',
>}
>
>
> def get_capitals(country):
>     try:
>         capital = capitals[country]
>     except KeyError:
>         capital = None
>     finally:
>         return capital
>
>
> print(get_capitals('Китай'))
> ```

> [!success]
> ```python
> capitals = {
>   'Россия': 'Москва',
>   'Англия': 'Лондон',
>}
>
>
> def get_capitals(country):
>    return capitals.get(country)
> 
> 
> print(get_capitals('Китай'))
> ```

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***
### try-except вместо метода .isinstance()

> [!fail]
> ```python
> def calculate(num1, num2):
> 	try:
> 		result = num1 + num2
> 		return result
> 	except TypeError:
> 		logging.warning('Ошибка: аргументы должны быть числами.')
>
>
> print(calculate(1, '2'))
> ```

> [!success]
> ```python
> def calculate(num1, num2):
>     if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
>         result = num1 + num2
>         return result
>     logging.warning('Ошибка: аргументы должны быть числами.')
> 
> 
> print(calculate(1, '2'))
> ```

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
