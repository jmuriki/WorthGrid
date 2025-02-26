- [ ] Отметить
***

>[!quote] Описание
_Названия переменных не должны быть слишком длинными или содержать излишнюю информацию, если того не требует контекст.
Предлог `of` создаёт избыточность в названии._

***
### Пример 1

> [!fail]
> ```python
> number_of_active_users = ...
> ```

> [!success]
> ```python
> active_users_num = ...
> ```

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***
### Пример 2

> [!fail]
> ```python
> def get_info_of_user(user_id):
>     ...
> 
> 
> ```

> [!success]
> ```python
> def get_user_info(user_id):
>     ...
> ```

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***
### Пример 3

> [!fail]
> ```python
> class ProductOfCompany:
>     def __init__(self, name, price):
>         self.name = name
>         self.price = price
> 
> 
> ```

> [!success]
> ```python
> class CompanyProduct:
>     def __init__(self, name, price):
>         self.name = name
>         self.price = price
> ```

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
