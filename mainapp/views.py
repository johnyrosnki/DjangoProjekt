from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ExpenseCategoriesFORM, ExpensesFORM, IncomesFORM, IncomeCategoriesFORM
from .models import Expenses, ExpenseCategories, Todo, Incomes, IncomeCategories
from .filters import IncomesFilter, ExpensesFilter
from django.db.models import Sum

# Create your views here.
def home(request):
    return render(request, 'base.html')


def expenses(request):
    return render(request, 'expenses.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def planowanie(request):
    return render(request, 'planowanie.html')


def przychody(request):
    return render(request, 'przychody.html')


def categories(request):
    return render(request, 'categories.html')


def statement(request):
    return render(request, 'statement.html')

def enter_the_cost(request):
    form = ExpensesFORM(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        form = ExpensesFORM()

    context = {
        'form': form
    }
    return render(request, "wydatki.html", context)


def enter_the_income(request):
    form = IncomesFORM(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        form = IncomesFORM()
    context = {
        'form': form
    }
    return render(request, "przychody.html", context)





def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ExpenseCategoriesFORM(request.POST)
        # check whether it's valid:
        if form.is_valid():
            e = ExpenseCategories()
            e.category = form.cleaned_data['category_name']
            e.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/name')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ExpenseCategoriesFORM()

    return render(request, 'name.html', {'form': form})
def get_name1(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IncomeCategoriesFORM(request.POST)
        # check whether it's valid:
        if form.is_valid():
            e = IncomeCategories()
            e.category = form.cleaned_data['category_name']
            e.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/kategoria')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IncomeCategoriesFORM()

    return render(request, 'kategoria.html', {'form': form})


def get_amount(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ExpensesFORM(request.POST)
        # check whether it's valid:
        if form.is_valid():
            f = Expenses()
            f.amount = form.cleaned_data['amount']
            f.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ExpensesFORM()

    return render(request, 'kwota.html', {'form': form})

def display(request):
    inc = Incomes.objects.all()
    exp = Expenses.objects.all()

    myFilter = IncomesFilter(request.GET, queryset=inc)

    newFilter = ExpensesFilter(request.GET, queryset=exp)

    sum_of_incomes = Incomes.objects.all().aggregate(Sum('amount')).get('amount__sum')
    sum_of_expenses = Expenses.objects.all().aggregate(Sum('amount')).get('amount__sum')
    subtract = sum_of_incomes - sum_of_expenses

    inc = myFilter.qs
    exp = newFilter.qs
    context = {'inc': inc, 'exp': exp, 'myFilter': myFilter, 'newFilter': newFilter, 'sum_of_incomes': sum_of_incomes,
               'sum_of_expenses': sum_of_expenses, 'subtract': subtract}

    return render(request, 'statement.html', context)