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
    actions = ['delete_selected']

    def save_model(self, request, obj, form, change):
        try:
            if obj.created_by :
                if obj.created_by != request.user:
                    messages.set_level(request, messages.ERROR)
                    messages.error(request, 'No changes are permitted ..Not allowed To Edit This User')
                    return False
        except:
            pass
        obj.created_by = request.user
        obj.save()

    def delete_model(self, request, obj):
        if obj.created_by != request.user:
            messages.set_level(request, messages.ERROR)
            messages.error(request, 'No changes are permitted ..Not allowed To Edit This User')
        else :
            obj.delete()

    def delete_selected(self, request, obj):
        for o in obj.all():
            self.delete_model(request,o)



admin.site.register(User,UserAdmin)