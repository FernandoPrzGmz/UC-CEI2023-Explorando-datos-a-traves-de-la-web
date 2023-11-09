from django.contrib import admin
from src.apps.account.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_joined', 'is_active', 'username', 'email']
    search_fields = ('username', 'email')
    list_filter = ('is_active',)


    list_display += ['full_name']
    def full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'
    full_name.short_description = 'Nombre completo'   


    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = "Marcar seleccionados como activos"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = "Marcar seleccionados como inactivos"
