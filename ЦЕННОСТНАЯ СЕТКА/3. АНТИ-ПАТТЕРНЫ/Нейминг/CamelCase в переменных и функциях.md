#нейминг 
***

> [!cite] Описание
>_Иногда данные приходят в альтернативном стиле написания из-за того, что они создавались на другом языке, например, JavaScript, в котором правила отличаются от Python._

***
### 💡 Пример


**Плохо:**
```python
class Postcard(BaseModel):
    holidayId: str
    name_ru: str
    body: Union[str, List[str]]
```

**Хорошо:**
```python
class Postcard(BaseModel):
    holiday_id: str = Field(alias='holidayId')
    name_ru: str
    body: Union[str, List[str]]
```

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
