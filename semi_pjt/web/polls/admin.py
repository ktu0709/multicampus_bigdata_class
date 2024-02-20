from django.contrib import admin
from .forms import MyForm
from .models import YourModel
from django.contrib.auth.models import Group
# Register your models here.
from django.contrib.auth.models import Group

class YourModelAdmin(admin.ModelAdmin):
    form = MyForm

    list_display = ('sector_option', 'apply_option', 'university_option', 'size_option', 'grade', 'license', 'abroad', 'intern', 'eng')

admin.site.unregister(Group)
admin.site.register(YourModel, YourModelAdmin)