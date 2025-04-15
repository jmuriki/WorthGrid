***

> [!cite] Описание
>_List comprehensions позволяют легко создавать коллекции, но использовать данный функционал рекомендуется только для простых циклов for._

***
### 💡 Пример 1


**Плохо:**
```python
comments = []
for comment in tag_comments:
	comments.append(comment.find('span').text)
```

**Хорошо:**
```python
comments = [comment.find('span').text for comment in tag_comments]
```

***
### 💡 Пример 2


**Плохо:**
```python
numbers = [...]
even_numbers = []
for number in numbers:
	if number % 2 == 0:
		even_numbers.append(number)
```

**Хорошо:**
```python
numbers = [...]
even_numbers = [num for num in numbers if num % 2 == 0]
```

***

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
