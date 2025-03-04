***

> [!cite] Описание
>_Отладочных print вообще не должно быть в рабочем коде. Если что-то нужно выводить в консоль, используйте logging._

***
### 💡 Пример 1


**Плохо:**
```python
def do_something(value):
    print(value)
    ...
```

**Хорошо:**
```python
def do_something(value):
    ...
```

***
### 💡 Пример 2


**Плохо:**
```python
try:
   do_something()
except AnyException as e:
   print(e)
```

**Хорошо:**
```python
try:
    do_something()
except AnyException as e:
    logging.error(e)
```

***

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
