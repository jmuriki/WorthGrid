***
```url
github.com/jmuriki/WorthGrid/wiki/of-в-названии#использование-of-в-названиях-переменных-функций-или-классов
```
# Использование `of` в названиях переменных, функций или классов
- [ ] Анти-паттерн: Использование `of` в названии переменной, функции или класса

_Названия переменных не должны быть слишком длинными или содержать излишнюю информацию, если того не требует контекст.
Предлог `of` создаёт избыточность в названии._

***
```url
github.com/jmuriki/WorthGrid/wiki/of-в-названии#of-в-названии-переменной
```
### `of` в названии переменной
- [ ] Пример: `of` в названии переменной

```python
"""Плохо"""
number_of_active_users = ...


"""Хорошо"""
active_users_num = ...
```

[[SOURCE CODE PY]]

[[SOURCE CODE PY#Бегло проследить поток исполнения программы]]

***
```url
github.com/jmuriki/WorthGrid/wiki/of-в-названии#of-в-названии-функции
```
### `of` в названии функции
- [ ] Пример: `of` в названии функции

```python
"""Плохо"""
def get_info_of_user(user_id):
    ...


"""Хорошо"""
def get_user_info(user_id):
    ...
```

[[SOURCE CODE PY]]

[[SOURCE CODE PY#Бегло проследить поток исполнения программы]]

***
```url
github.com/jmuriki/WorthGrid/wiki/of-в-названии#of-в-названии-класса
```
### `of` в названии класса
- [ ] Пример: `of` в названии класса

```python
"""Плохо"""
class ProductOfCompany:
    def __init__(self, name, price):
        self.name = name
        self.price = price


"""Хорошо"""
class CompanyProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

[[SOURCE CODE PY]]

[[SOURCE CODE PY#Бегло проследить поток исполнения программы]]

***
```url
github.com/jmuriki/WorthGrid/wiki/of-в-названии#контакты
```
# [[Контакты]]
Если не удалось найти ничего подходящего или есть идея по улучшению, [пиши сюда](https://github.com/jmuriki/WorthGrid/wiki/Контакты).
