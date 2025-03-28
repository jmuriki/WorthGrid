#декомпозиция 
***

> [!cite] Описание
>_lambda функции хороши для коротких выражений, а использование их для сложной логики снижает читаемость кода._

***
### 💡 Пример


**Плохо:**
```python
do_something = lambda num: num**2 + 2*num - 1 if num > 0 else num**2 - 2*num + 1
```

**Хорошо:**
```python
def do_something(num):
	if num > 0:
		return num**2 + 2*num - 1
	else:
		return num**2 - 2*num + 1
```

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
