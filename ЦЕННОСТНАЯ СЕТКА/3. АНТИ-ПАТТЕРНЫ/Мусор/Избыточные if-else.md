#мусор 
***

> [!cite] Описание
>_Избыточные проверки if-else усложняют чтение кода._

***
### 💡 Пример 1
При таком высушивании код избавляется ещё и от [[../Мусор/Избыточные True и False|избыточных True и False]].

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


**Плохо:**
```python
def is_active_user(user):
	...
	user_status = False
	return True if user_status else False
```

**Хорошо:**
```python
def is_active_user(user):
	...
	user_status = False
	return user_status
```

***
### 💡 Пример 3
В данном случае проверять `image_src` беcсмысленно. Функция всё равно вернёт какое-то значение отличное от `None`.

**Плохо:**
```python
def get_book_image_url(soup, book_page_url):
	img_rel_path = soup.find('div', class_='bookimage').find('img')['src']
	img_src = urljoin(book_page_url, img_rel_path)
	return img_src

...
image_src = get_book_image_url(soup, book_url)
if image_src:
	download_image(image_src)
```

**Хорошо:**
```python
def get_book_image_url(soup, book_page_url):
	img_rel_path = soup.find('div', class_='bookimage').find('img')['src']
	img_src = urljoin(book_page_url, img_rel_path)
	return img_src

...
image_src = get_book_image_url(soup, book_url)
download_image(image_src)
```

***

> [!example] Связанные кейсы
>- Интерфейс: [[SOURCE CODE PY]]
>	- Функция: [[SOURCE CODE PY#𝑓 Бегло проследить поток исполнения программы|Бегло проследить поток исполнения программы]]

***

> [!info]
> Если не удалось найти ничего подходящего или есть идея по улучшению, [[Контакты|пиши сюда]].
