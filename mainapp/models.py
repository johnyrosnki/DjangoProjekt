from django.db import models

from django.db import models
#from django.utils.translation import ugettext_lazy as trans
import datetime
class ExpenseCategories(models.Model):
    category = models.CharField(max_length=25, null=False)
    objects = models.Manager()

    def __str__(self):
        return self.category


class Expenses(models.Model):
    amount = models.FloatField(null=False, verbose_name=('Kwota:'))
    expense_category = models.ForeignKey(ExpenseCategories, null=False, on_delete=models.PROTECT,
                                         verbose_name=('Kategoria wydatku:'))
    objects = models.Manager()

    class Meta:
        db_table = "expenses"
        verbose_name_plural = "Wydatki"


#    def __str__(self):
#        return self.expense_category.name


class IncomeCategories(models.Model):
    category = models.CharField(max_length=25, null=False)

    def __str__(self):
        return self.category


class Incomes(models.Model):
    amount = models.FloatField(null=False, verbose_name=('Kwota:'))
    income_category = models.ForeignKey(IncomeCategories, null=False, on_delete=models.PROTECT,
                                        verbose_name=('Kategoria przychodu:'))
    objects = models.Manager()

    class Meta:
        db_table = "incomes"


#    def __str__(self):
#        return self.income_category.name


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.PROTECT)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text




