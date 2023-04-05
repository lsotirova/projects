from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.new_post, name="new_post"),
    path("profile/<str:username>", views.profile, name="profile"),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    path("following", views.following, name="following"),
    path("edit/<int:post_id>/", views.edit, name="edit"),
    path("profile/edit/<int:post_id>", views.edit, name="edit"),
    path("toggle_like/<int:post_id>", views.toggle_like, name="toggle_like"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)