from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Project, Expense
from django.views.generic import CreateView
from django.utils.text import slugify
from .forms import ExpenseForm, CategoryForm, ProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, ProjectSerializer, ExpenseSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


@login_required
def project_list(request): #its in urls ->  path('<slug:project_slug>', fetching the correct project
    project_list = Project.objects.all()
    return render(request, 'project-list.html', {'project_list': project_list})


@login_required
def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug) #identify by the slug
    category = CategoryForm(request.POST)
    if request.method == "GET":

        return render(request, 'project-detail.html', {'project': project,
                                                   'expense_list': project.expenses.all().order_by('-expense_date'),
                                                       'category': category} )

    elif request.method == "POST":

        form = ExpenseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            amount = form.cleaned_data['amount']
            category = form.cleaned_data['category'] #label is taken from forms (CategoryForm) <- in models for Expense its exacly the same name

            Expense.objects.create(project=project,
                                   title=title,
                                   amount=amount,
                                   category=category,
                                   ).save()

    return HttpResponseRedirect(project_slug)

def delete_expense(request, id):
    expense = get_object_or_404(Expense, pk=id)
    if request.method == "POST":
        expense.delete()
        return redirect(project_detail, expense.project.slug)


    return render(request, 'delete.html',
                      {'expense': expense})


def edit_budget(request, id):
    project = get_object_or_404(Project, pk = id)
    form = ProjectForm(request.POST)
    if form.is_valid():
        new_budget = form.cleaned_data['budget']
        project.budget = new_budget
        project.save()

        return redirect(project_detail, project.slug)
    return render(request, 'edit_project.html', {'form': form})


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'add-project.html'
    fields = ['name', 'budget', 'photo']

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return slugify(self.request.POST['name'])
