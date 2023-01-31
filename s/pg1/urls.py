from django.urls import path
from .views import index_pg1


urlpatterns = [

    path('', index_pg1),
]
