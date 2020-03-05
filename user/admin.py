from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    #припомощи какой формы добавляем пользователя в админки
    add_form = CustomUserCreationForm
    # форма с помощью которой редактируется
    form = CustomUserChangeForm
    list_display = ['username', 'year', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)
