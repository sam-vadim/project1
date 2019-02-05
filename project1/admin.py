from django.contrib import admin
from django.contrib.auth import models
from django.contrib.auth.admin import UserAdmin

__all__ = ['auchan_admin', 'AuchanModelAdmin', ]


class AuchanModelAdmin(admin.ModelAdmin):
    list_per_page = 25



class AuchanAdminSite(admin.AdminSite):
    site_header = 'Админ панель Ашана'
    site_title = 'Сайт администрирования Ашан'
    site_url = None
    index_title = 'Админ панель'


auchan_admin = AuchanAdminSite(name='auchan_admin')
# auchan_admin.register(models.Group)
# auchan_admin.register(models.User, UserAdmin)
