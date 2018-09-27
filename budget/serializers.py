from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Project, Expense


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        budget_left = serializers.DecimalField(source='budget_left', max_digits=8, decimal_places=2)
        total_expense = serializers.DecimalField(source='total_expense', max_digits=8, decimal_places=2)
        total_expense_dawid = serializers.DecimalField(source='total_expense_dawid', max_digits=8, decimal_places=2)
        total_expense_julita = serializers.DecimalField(source='total_expense_julita', max_digits=8, decimal_places=2)
        total_transactions = serializers.IntegerField(source='total_transactions')
        total_transactions_dawid = serializers.IntegerField(source='total_transactions_dawid')
        total_transactions_julita = serializers.IntegerField(source='total_transactions_julita')
        fields = ('id', 'name', 'budget', 'photo', 'total_expense', 'total_expense_dawid', 'total_expense_dawid',
                   'total_expense_julita', 'total_transactions', 'total_transactions_dawid','total_transactions_julita')

class ProjectCutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields  = ('id', 'name')

class ExpenseSerializer(serializers.ModelSerializer):
    project = ProjectCutSerializer(many=False)
    class Meta:
        model = Expense
        fields = ('id', 'project', 'expense_date', 'title', 'amount', 'category')



