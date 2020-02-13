from  django.urls import path
from . import views
urlpatterns = [
     path('', views.index, name='index'),
     path('categories', views.category_page, name='category'),
     path('category/books/<int:id>', views.books_list, name='BooksInCategory'),
     path('description/<int:id>', views.books_description, name='description'),
     path('newBooks', views.get_newBooks, name='newBooks'),
     path('mostDownloaded', views.popular_books, name='mostDownloaded'),
     path('uploadBook', views.upload_book, name="uploadBook"),
     path('aurthor/<int:pk>', views.aurthor_details, name='aurthor'),
     path('books/phone', views.phone_books, name="phone"),
     path('books/users', views.BooksByUsers, name="usersBooks"),
     path('searchresults/', views.SearchBooks, name="search")
 ]