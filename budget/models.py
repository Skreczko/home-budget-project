from django.db import models
from django.utils.text import slugify
from datetime import date, datetime

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=124)
    slug = models.SlugField(max_length=124, unique=True, blank=True)
    budget = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(null=True, upload_to='months')

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs): #automaticly generate the slug field
        self.slug = slugify(self.name) #https://docs.djangoproject.com/en/2.1/ref/utils/ <- generate name of the project
        super(Project, self).save(*args,**kwargs)


    def budget_left(self):
        expense_list = Expense.objects.filter(project=self)
        total = 0
        for item in expense_list:
            total += item.amount
        return self.budget - total

    def total_expense(self):
        expense = Expense.objects.filter(project=self)
        total = 0
        for item in expense:
            total += item.amount
        return total

    def total_expense_dawid(self):
        expense_list = Expense.objects.filter(project=self, category='Dawid')
        total = 0
        for item in expense_list:
            total += item.amount
        return total

    def total_expense_julita(self):
        expense_list = Expense.objects.filter(project=self, category='Julita')
        total = 0
        for item in expense_list:
            total += item.amount
        return total

    def total_transactions(self):
        expense_list = Expense.objects.filter(project = self)
        return len(expense_list)

    def total_transactions_dawid(self):
        expense_list = Expense.objects.filter(project = self, category='Dawid')
        return len(expense_list)

    def total_transactions_julita(self):
        expense_list = Expense.objects.filter(project = self, category='Julita')
        return len(expense_list)

class Expense(models.Model):  #to store multiply expenses for one project
    user_category = (('Julita', 'Julita'),
                    ('Dawid', 'Dawid'))

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=124)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    expense_date = models.DateField(default=datetime.now, blank=True)
    category = models.CharField(max_length=50,choices=user_category)

