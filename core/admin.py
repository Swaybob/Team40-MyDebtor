from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import School, Principal, CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.utils.translation import gettext_lazy as _

# Register your models here.
# admin.site.register(School)
# admin.site.register(CustomUser) 
# admin.site.register(School)
admin.site.register(Principal)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    ordering = ['date_joined']
    list_display = ['first_name', 'last_name', 'email']

    search_fields = ['first_name', 'last_name']
    # exclude = ('username',)

    # fieldsets = (
    #     (None, {
    #         'fields': ''
    #     })
    # )
class CategoryFilter(admin.SimpleListFilter):
    title = _('By category')

    parameter_name = 'category'

    def lookups(self, request, model_admin):
        return (
            ('primary', _('primary')),
            ('secondary', _('secondary')),
            # ('active', _('active')),
        )
    def queryset(self, request, queryset=School.objects.all()):
        if self.value() == 'primary':
            return queryset.filter(category='Primary')

        if self.value() == 'secondary':
            return queryset.filter(category='secondary')

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    model = School
    ordering = ['name']
    list_display = ['name', 'reg_number', 'category']
    # exclude = ['user']
    search_fields = ['name']
    readonly_fields = ['date_created', 'date_updated']
    list_filter = [CategoryFilter]

    fieldsets = (
        ('Details', {
            'fields': ('logo', 'reg_number', 'name', 'category',)
        }),
        (
            'User', {
                'fields': ('user',)
            }
        ),
        (
            'Address', {
                'fields': ('LGA', 'state', 'address',)
            }
        ),
        (
            'Important Dates', {
                'fields':('date_created', 'date_updated',)
            }
        )
    )