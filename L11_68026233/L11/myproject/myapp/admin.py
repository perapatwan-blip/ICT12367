from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'date')  # 👈 เพิ่ม date

admin.site.register(Person, PersonAdmin)