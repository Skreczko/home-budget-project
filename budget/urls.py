
from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name="list"),
    path('add', views.ProjectCreateView.as_view(), name="add"),
    path('delete/<int:id>', views.delete_expense, name="delete"),
    path('edit/<int:id>', views.edit_budget, name="edit_budget"),
    path('<slug:project_slug>', views.project_detail, name="detail"),  #to identity which project i want to currently vue

]
