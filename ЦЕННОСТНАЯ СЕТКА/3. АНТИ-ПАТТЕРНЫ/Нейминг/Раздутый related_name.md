***

> [!cite] Описание
>_Нет смысла в `related_name` дублировать название модели - в прикладном коде `related_name` и так всегда следует за названием модели данных. Высушите названия `related_name`._

***
### 💡 Пример
Сравните масло-масляный вариант и высушенный - очевидно, что короткий вариант лучше, с какой стороны ни посмотри.

**Плохо:**
```python
flat.flats_owners
```

**Хорошо:**
```python
flat.owners
```

**Плохо:**
```python
from django.db import models

class Owner(models.Model):
	...
	flats = models.ManyToManyField(
		'Flat',
		verbose_name='Квартиры в собственности',
		related_name='flats_owners',
	)
	...
```

**Хорошо:**
```python
from django.db import models

class Owner(models.Model):
	...
	flats = models.ManyToManyField(
		'Flat',
		verbose_name='Квартиры в собственности',
		related_name='owners',
	)
	...
```

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
