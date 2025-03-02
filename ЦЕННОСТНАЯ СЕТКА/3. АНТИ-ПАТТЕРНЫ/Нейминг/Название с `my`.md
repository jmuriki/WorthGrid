***

> [!cite] Описание
>_Местоимение `my` является излишним и способно больше запутать, чем помочь понять код._

***
### 💡 Пример 1


**Плохо:**
```python
with open(file_path, "w") as my_file:
    ...
```

**Хорошо:**
```python
with open(file_path, "w") as file:
    ...
```

***
### 💡 Пример 2


**Плохо:**
```python
from environs import Env

def main():
    env = Env()
    env.read_env()
    my_vk_access_token =  env.str('VK_ACCESS_TOKEN')
```

**Хорошо:**
```python
from environs import Env

def main():
    env = Env()
    env.read_env()
    vk_access_token =  env.str('VK_ACCESS_TOKEN')
```

***
### 💡 Пример 3


**Плохо:**
```python
def get_my_user_info(user_id):
    ...
```

**Хорошо:**
```python
def get_user_info(user_id):
    ...
```

***

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
