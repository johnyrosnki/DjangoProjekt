from django import forms
from .models import Todo, Expenses, Incomes
from django.db.models import Sum
from django.utils.translation import gettext_lazy as trans

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ExpenseCategoriesFORM(forms.Form):
    category_name = forms.CharField(label='Kategoria wydatków ', max_length=100)

class IncomeCategoriesFORM(forms.Form):
    category_name = forms.CharField(label='Kategoria przychodów ', max_length=100)


class ExpensesFORM(forms.ModelForm):
    def clean_amount(self):
        amount = self.cleaned_data['amount']

        przychody = Incomes.objects.all().aggregate(Sum('amount')).get('amount__sum')

        if amount < 0.01:
            raise forms.ValidationError("Kwota nie może być mniejsza niż: 1")
        if amount > przychody:
            raise forms.ValidationError("Przekroczono budżet")
        return amount

    amount = forms.FloatField(required=True, label=trans(u'Kwota:'))

    class Meta:
        model = Expenses
        fields = [
            'amount',
            'expense_category'
        ]


class IncomesFORM(forms.ModelForm):
    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 0.01:
            raise forms.ValidationError("Kwota nie może być mniejsza niż: 1")
        return amount

    amount = forms.FloatField(required=True, label=trans(u'Kwota:'))

    class Meta:
        model = Incomes
        fields = [
            'amount',
            'income_category'
        ]


