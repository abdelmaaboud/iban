# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import messages

# Register your models here.
from models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fields = ["first_name","last_name","iban"]
    list_display = ["first_name","last_name","iban",'created_by']
    list_filter = ['created_by']
    readonly_fields = ('created_by', )

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


admin.site.register(User,UserAdmin)