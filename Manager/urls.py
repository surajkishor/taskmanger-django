from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("update/<int:pk>/", views.editt, name="update"),
    path("delete/<int:pk>/", views.deletee, name="delete"),
    path("register/", views.register, name="register"),
    path("login/", views.login_in, name='login'),
    path('logout/', views.logout_it, name='logout')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)