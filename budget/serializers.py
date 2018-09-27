from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Project, Expense


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','url', 'username', 'email')

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id', 'expense_date', 'title', 'amount', 'category')

class ProjectSerializer(serializers.ModelSerializer):
    expense = ExpenseSerializer(many=False)
    class Meta:
        model = Project
        fields  = ('id', 'name', 'budget', 'photo','expense')

