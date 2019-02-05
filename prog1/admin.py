from django.contrib import admin

# Register your models here.
from django.contrib import admin
from prog1.models import Person
from project1.admin import auchan_admin


# @admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # fields = (('name', 'age'), 'surname')

    list_display = ('id', 'surname', 'name',  'upper_case_name', 'age')

    list_display_links = ('name', 'surname')

    actions_selection_counter = True
    actions_on_top = False
    actions_on_bottom = True

    search_fields = ['name', 'surname', 'id']

    # list_editable = ('name')

    def upper_case_name(self, obj):
        return ("%s %s" % (obj.name, obj.surname)).upper()

    upper_case_name.short_description = 'Собранное имя'

    # fieldsets = [
    #     ('Ваше имя и фамилия:', {'fields': ['name']}),
    #     (None, {'fields': ['surname']}),
    #     # ('Ваш возраст', {'fields': ['age']}),
    #     ('Дополнительная информация', {'fields': ['age'], 'classes': ['collapse']}),
    # ]
    # pass


admin.site.register(Person, PersonAdmin)

auchan_admin.register(Person, PersonAdmin)

