# Django Bookstores
This is Django based application with following features:

* User Management using Django's built-in Authentication System
* Ability to create, edit and delete Book Stores
* Ability to create, edit and delete Books
* Fetches Google's Book ID for the books added using Google's Books API

## Technologies Used
* Django
* Bootstrap 5 for basic theming
* Requests: to Query Google Books API

## How to Deploy

> Checkout the source code
```shell
$ git clone https://github.com/nehakumari2008/django-bookstores.git
```
> Create Virtual Environment using Python 3
```shell
$ cd django-bookstores
$ python -m venv venv
```
> Install Dependencies
```shell
$ source venv/bin/activate
$ pip install -r requirements.txt
```
> Start the server
```shell
$ python manage.py runserver
```
> Go to http://localhost:8000 to use the application

## Endpoints
###Authentication System
> User Registration
```http request
/accounts/register/
```
> User Login
```http request
/accounts/login/
```
> User Logout
```http request
/accounts/logout/
```
### Book Store Management
> View all book stores
```http request
/store/
```
> Create book store
```http request
/store/create/
```
> Edit book store
```http request
/store/<int:store_id>/edit/
```
> Delete book store
```http request
/store/<int:store_id>/delete/
```
### Books Management
> View all books in a store
```http request
/store/<int:store_id>/books/
```
> Create a book
```http request
/store/<int:store_id>/books/create/
```
> View book details
```http request
/store/<int:store_id>/books/<int:book_id>/
```
> Edit book details
```http request
/store/<int:store_id>/books/<int:book_id>/edit/
```
> Delete a book
```http request
/store/<int:store_id>/books/<int:book_id>/delete/
```
## Screenshot
<img width="737" alt="screenshot" src="https://user-images.githubusercontent.com/441799/160857106-ae6d68c3-36f6-4f1a-9a91-52693438415b.png">

