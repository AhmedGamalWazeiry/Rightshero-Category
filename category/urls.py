from django.urls import  path
from category.views import category_view,get_create_subcategories,get_children_by_id

urlpatterns = [
    path('', category_view, name='categories'),
    path('<uuid:pk>/', get_create_subcategories, name='add_or_get_children'),
    path('<uuid:pk>/all/', get_children_by_id, name='get_children_by_id'),   
]


