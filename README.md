Для взаимодействия с ресурсами настроены следующие эндпоинты:
  
- api/v1/products/?page=1&search=mur&ordering=price (GET): получить полный спискок товаров.
- api/v1/products/{id}/ (GET): получить информацию о конкретном товаре по id.
- api/v1/categories/ (GET): получить полный список категорий товаров.
- api/v1/categories/slug/ (GET): получить все товары конкретной категории по slug.
  
  
- api/auth/users/ (POST): регистрация пользователя на сайте. Обязательные параметры: email, password. Необязательные параметры: first_name, last_name, phone_number, adress.
- api/auth/token/login/ (POST): получение токена для пользователя. Обязательные параметры: email, password.
- api/auth/token/logout/ (POST): обнуление токена пользователя.
- api/auth/users/me/ (GET): получение информации о текущем пользователе.
- api/auth/users/me/ (PATCH): Редактировать данные о пользователе. Необязательные параметры: email, first_name, last_name, phone_number, adress.
- api/auth/users/me/ (DELETE): Удаление аккаунта пользователя. Обязательные параметры: current_password.
  
  
- api/v1/products/{id}/cart/ (POST): добавление товара id в корзину.
- api/v1/products/{id}/cart/ (DELETE): удаление товара id из корзины.
cvcv
