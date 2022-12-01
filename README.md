Для взаимодействия с ресурсами настроены следующие эндпоинты:

- api/v1/categories/ (GET): получить полный список категорий товаров. Уровень доступа: все пользователи.
- api/v1/categories/ (POST): добавить новую категорию. Обязательные поля: name, slug. Уровень доступа: только админы.
- api/v1/categories/slug/ (GET): получить все товары конкретной категории по slug.
- api/v1/categories/slug/ (PATCH): редактировать название категории. Необязательные поля: name. Уровень доступа: только админы.
- api/v1/categories/slug/ (DELETE): удалить категорию. Уровень доступа: только админы.

- api/v1/products/?page=1&search=mur&ordering=price (GET): получить полный спискок товаров. Доступные параметры: page=(int), search=(name), ordering=price  Уровень доступа: все пользователи.
- api/v1/products/ (POST): добавить новый товар. Обязательные поля: name, description, price. Уровень доступа: только админы.
- api/v1/products/{id}/ (GET): получить информацию о товаре по id. Уровень доступа: все пользователи.
- api/v1/products/{id}/ (PATCH): редактировать информацию о конкретном товаре по id. Уровень доступа: только админы.
- api/v1/products/{id}/ (DELETE): удалить товар по id. Уровень доступа: только админы.


- api/auth/users/ (POST): регистрация пользователя на сайте. Обязательные поля: email, password. Необязательные поля: first_name, last_name, phone_number, adress.
- api/auth/token/login/ (POST): получение токена для пользователя. Обязательные поля: email, password.
- api/auth/token/logout/ (POST): обнуление токена пользователя.
- api/auth/users/me/ (GET): получение информации о текущем пользователе.
- api/auth/users/me/ (PATCH): Редактировать данные о пользователе. Необязательные поля: email, first_name, last_name, phone_number, adress.
- api/auth/users/me/ (DELETE): Удаление аккаунта пользователя. Обязательные поля: current_password.


- api/v1/products/{id}/cart/ (POST): добавление товара id в корзину. Уровень доступа: авторизованные пользователи.
- api/v1/products/{id}/cart/ (DELETE): удаление товара id из корзины. Уровень доступа: авторизованные пользователи.
- api/v1/cart/ (GET): получение корзины текущего пользователя. Уровень доступа: авторизованные пользователи.
