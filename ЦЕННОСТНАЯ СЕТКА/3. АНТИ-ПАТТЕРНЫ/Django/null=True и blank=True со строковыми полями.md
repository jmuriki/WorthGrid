#django
***

> [!quote] Описание
>_При работе с любыми строковыми полями в `Django`, важно понимать различие между параметрами `null` и `blank`._
>
>_`null=True` означает, что в БД для данного поля может храниться значение `NULL`._
>
>_`blank=True` отвечает за валидацию на уровне форм: поле может быть оставлено пустым при вводе данных._

***
### 💡 Пример
Для строковых полей рекомендуется использовать `blank=True`, но не `null=True`, потому что в БД принято хранить «пустое» значение для строк как пустую строку '', а не как  `NULL`. Установка  `null=True` создаёт двусмысленность: отсутствие данных может быть представлено, в таком случае, и как NULL, и как пустая строка.

**Плохо:**
```python
from django.db import models


class Article(models.Model):
	title = models.CharField(max_length=200)
	summary = models.TextField(null=True, blank=True, default="")
	url = models.URLField(null=True, blank=True, default="")

	def __str__(self):
		return self.title
```

**Хорошо:**
```python
from django.db import models


class Article(models.Model):
	title = models.CharField(max_length=200)
	summary = models.TextField(blank=True, default="")
	url = models.URLField(blank=True, default="")

	def __str__(self):
		return self.title
```

***

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]
>		- История: [[SOURCE CODE PY#✔ Без спотыкания и застревания в Анти-паттернах|Без спотыкания и застревания в Анти-паттернах]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
