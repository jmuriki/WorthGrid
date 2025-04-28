#нейминг 
***

> [!cite] Описание
>_Нет смысла дублировать название модели в related_name - в прикладном коде он и так всегда следует за названием модели данных. Высушите related_name._

***
### 💡 Пример
Сравните масло-масляный вариант и высушенный - очевидно, что короткий вариант лучше, с какой стороны ни посмотри.

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

```python
flat.flats_owners
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

```python
flat.owners
```

***

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
