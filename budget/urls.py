from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'expenses', views.ExpenseViewSet)

urlpatterns = [
    path('', views.project_list, name="list"),
    path('add', views.ProjectCreateView.as_view(), name="add"),
    path('delete/<int:id>', views.delete_expense, name="delete"),
    path('edit/<int:id>', views.edit_budget, name="edit_budget"),
    path('<slug:project_slug>', views.project_detail, name="detail"),
    url(r'^', include(router.urls))
]
