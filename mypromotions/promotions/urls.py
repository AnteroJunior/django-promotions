from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:promotion_id>', views.promotion, name='promotion'),
]