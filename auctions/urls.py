from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("details/<str:pk>", views.details, name="details"),
    path("bid/<str:pk>", views.bid, name="bid"),
    path('categories/', views.categories, name='categories'),
    path('categories/<str:category>/', views.category, name='category'),
    path("<int:pk>/watchlist/add", views.add_to_watchlist, name="add_to_watchlist"),
    path("<int:pk>/watchlist/remove", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("watchlist", views.watchlist_view, name="watchlist"),
    path("close_listing/<int:pk>", views.close_listing, name="close_listing"),
    path("comment/<int:pk>", views.comment, name="comment"),
    path("all-closed-listings", views.all_closed_listings, name="all-closed-listings")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
