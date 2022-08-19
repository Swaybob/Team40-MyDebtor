from django.contrib import admin
from .models import*

from .filters import DebtStatusFilter, ComplaintStatusFilter, DateFilter, ClassFilter
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'school', 'student_class']
    ordering = ['first_name','last_name','school']
    readonly_fields = ['date_created', 'date_updated']
    list_per_page = 10
    search_fields = ['first_name__istartswith','last_name__istartswith','school__istartswith']

    list_filter = [ClassFilter,]
    add_fieldsets = (
        ('Personal Details', {
            'fields': ('passport', 'reg_number', 'first_name', 'last_name', 'gender', 'nationality','date_of_birth')
            }
        ),
        ('School Details', {
            'fields': ('student_class', 'school',)
            }
        ),
        ('Address', {
            'fields': ('address', 'state',)
            }
        ),
    )
admin.site.register(Student, StudentAdmin)



@admin.action(description='Mark debt as resolved')
def mark_resolved(modeladmin, request, queryset=Debt.objects.all()):
    queryset.update(status='resolved')

@admin.action(description='Mark debt as pending')
def mark_pending(modeladmin, request, queryset=Debt.objects.all()):
    queryset.update(status='pending')

@admin.action(description='Mark debt as active')
def mark_active(modeladmin, request, queryset=Debt.objects.all()):
    queryset.update(status='active')

class DebtAdmin(admin.ModelAdmin):
    model = Debt
    list_display = ['student', 'total_fee', 'outstanding_fee', 'status']
    list_per_page = 10
    search_fields = ['student__istartswith']
    ordering = ['student']
    list_filter = (DebtStatusFilter,)
    actions = [mark_resolved, mark_active, mark_pending]

admin.site.register(Debt, DebtAdmin)



@admin.action(description='Mark Complaint as cleared')
def mark_cleared(modeladmin, request, queryset=Complaint.objects.all()):
    queryset.update(status='cleared')

@admin.action(description='Mark Complaint as pending')
def mark_pending(modeladmin, request, queryset=Complaint.objects.all()):
    queryset.update(status='pending')

class ComplaintAdmin(admin.ModelAdmin):
    model = Complaint
    list_display = ['description', 'school', 'status']
    list_per_page = 10
    search_fields = ['user__istartswith']
    # ordering = ['date_created']
    actions = [mark_cleared, mark_pending]
    readonly_fields = ['date_created',]
    list_filter = (ComplaintStatusFilter, DateFilter,)
    fieldsets = (
        
        (
            'Complaint', {
                'fields' : ('description', 'proof',)
            }
        ),
    )

    add_fieldsets = (
        (
            'User details', {
                'fields': ('user', 'school', 'debt',)
                }
        ),
        (
            'Complaint', {
                'fields' : ('description', 'proof',)
            }
        ),
    )
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Sponsor)



admin.site.register(Student, StudentAdmin)
admin.site.register(Sponsor)

admin.site.register(Debt)  

def hello():
    pass

