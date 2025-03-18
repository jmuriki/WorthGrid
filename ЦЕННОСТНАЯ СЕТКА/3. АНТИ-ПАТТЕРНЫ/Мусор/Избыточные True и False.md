#мусор 
***

> [!cite] Описание
>_Зачем лишний раз упоминать True или False, когда Python позволяет писать более лаконичный код? Следует пользоваться данной возможностью._

***
### 💡 Пример 1
При сравнении двух значений всегда возвращается bool. Поэтому, можно не использовать True и False явно, и высушить код. Заодно код избавляется и от [[Избыточные if-else|избыточных if-else]].

**Плохо:**
```python
def get_link_status(link):
	...
	if link_status:
		return True
	else:
		return False
```

**Хорошо:**
```python
def get_link_status(link):
	...
	return link_status
```

***
### 💡 Пример 2
При сравнении двух значений всегда возвращается bool. Поэтому, можно не использовать True и False явно, и высушить код.

**Плохо:**
```python
SECONDS_LIMIT = 3600

def check_visit_length(duration, seconds_limit=SECONDS_LIMIT):
	seconds_on = duration.total_seconds()
	if seconds_on > seconds_limit:
		return True
	return False

def main():
	...
	duration = ...
	is_strange_visit = check_visit_length(duration)
	...
```

**Хорошо:**
```python
SECONDS_LIMIT = 3600

def check_visit_length(duration, seconds_limit=SECONDS_LIMIT):
	seconds_on = duration.total_seconds()
	return seconds_on > seconds_limit

def main():
	...
	duration = ...
	is_strange_visit = check_visit_length(duration)
	...
```

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
