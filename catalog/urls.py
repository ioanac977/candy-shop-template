from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('items/', views.ItemListView.as_view(), name='items'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('wishlists/', views.WishListView.as_view(), name='wishlists'),
    path("category/<int:pk>/add_wishlist", views.CategoryDetailView.as_view(), name="add_item_to_wishlist"),

    # path('wishlist/<int:pk>', views.WishListDetailView.as_view(), name='wishlist-detail'),
]

urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
]

# Add URLConf for librarian to renew a book.
urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

# Add URLConf to create, update, and delete authors
urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

# Add URLConf to create, update, and delete books
urlpatterns += [
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]

urlpatterns += [
    path('item/<int:pk>/addToWishlist/', views.add_to_wishlist, name='wishlist-add-item'),
]
# Add URLConf to create, update, and delete categories
urlpatterns += [
    path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),
]

urlpatterns += [
    path('item/create/', views.ItemCreate.as_view(), name='item_create'),
    path('item/<int:pk>/update/', views.ItemUpdate.as_view(), name='item_update'),
    path('item/<int:pk>/delete/', views.ItemDelete.as_view(), name='item_delete'),
]
