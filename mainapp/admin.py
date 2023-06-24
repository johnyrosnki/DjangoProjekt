from django.contrib import admin

from .models import *
# Register your models here.
from django.contrib import admin
admin.site.register(ExpenseCategories)
admin.site.register(Expenses)
admin.site.register(IncomeCategories)
admin.site.register(Incomes)


class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']


admin.site.register(Poll, PollAdmin)