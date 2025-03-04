***

> [!cite] Описание
>_При вызове метода QuerySet.get() может оказаться, что искомой записи в базе не будет, и возникнет исключение DoesNotExist, а программа завершится с исключением.
В данном случае пользователь просто не получит желаемый продукт и программа продолжит работать._

***
### 💡 Пример 1
В данном случае исключение `DoesNotExist` берётся прямо из используемой модели.

**Плохо:**
```python
product = Product.objects.get(id=product_id)
```

**Хорошо:**
```python
def get_product(product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        logger.error(f'Продукт с id={product_id} не сущуствует.')
        product = None
    return product
```

***
### 💡 Пример 2
Здесь используется общее для всех моделей исключение `ObjectDoesNotExist`.

**Плохо:**
```python
product = Product.objects.get(id=product_id)
```

**Хорошо:**
```python
from django.core.exceptions import ObjectDoesNotExist

def get_product(product_id):
    try:
        product = Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        logger.error(f'Продукт с id={product_id} не сущуствует.')
        product = None
    return product
```

***
### 💡 Пример 3
В случае отсутствия объекта в БД `get_object_or_404` поднимает исключение `Http404`, которое вернёт 404 ошибку, сообщив, что такой страницы не существует.

**Плохо:**
```python
def view_product(request, product_id):
    product = Product.objects.get(id=product_id)
    ...
    render(request, 'product.html', context=context)
```

**Хорошо:**
```python
from django.shortcuts import get_object_or_404

def view_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    ...
    render(request, 'product.html', context=context)
```

***

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
