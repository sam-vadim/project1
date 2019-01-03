from django.contrib import admin

# Register your models here.
from django.contrib import admin
from prog1.models import Person


# @admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # fields = (('name', 'age'), 'surname')

    list_display = ('id', 'name', 'age', 'surname')

    # fieldsets = [
    #     ('Ваше имя и фамилия:', {'fields': ['name']}),
    #     (None, {'fields': ['surname']}),
    #     # ('Ваш возраст', {'fields': ['age']}),
    #     ('Дополнительная информация', {'fields': ['age'], 'classes': ['collapse']}),
    # ]
    # pass


admin.site.register(Person, PersonAdmin)


