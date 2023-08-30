from django.urls import path
from . import views
urlpatterns = [
	path('shops/', views.CreateShop.as_view()),
	path('shops/<int:pk>', views.UpdateDestroyShop.as_view()),
	path('signup/', views.signup),
	path('login/', views.signup),

]