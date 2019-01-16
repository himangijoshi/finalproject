from django.contrib import admin,messages
# Register your models here.
class User_register(admin.ModelAdmin):
    messages.add_message(request, messages.INFO, '=====New User request=====')