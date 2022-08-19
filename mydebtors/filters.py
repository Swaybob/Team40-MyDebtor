from .models import *

import datetime

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

new_time = timezone.now() - datetime.timedelta(minutes=20)


class DebtStatusFilter(admin.SimpleListFilter):
    title = _('Status')

    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            ('pending', _('pending')),
            ('resolved', _('resolved')),
            ('active', _('active')),
        )
    def queryset(self, request, queryset=Debt.objects.all()):
        if self.value() == 'pending':
            return queryset.filter(status='pending')

        if self.value() == 'resolved':
            return queryset.filter(status='resolved')

        if self.value() == 'active':
            return queryset.filter(status='active')


class ComplaintStatusFilter(admin.SimpleListFilter):
    title = _('Status')

    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            ('pending', _('pending')),
            ('cleared', _('cleared')),
        )
    def queryset(self, request, queryset=Complaint.objects.all()):
        if self.value() == 'pending':
            return queryset.filter(status='pending')

        if self.value() == 'cleared':
            return queryset.filter(status='cleared')

class DateFilter(admin.SimpleListFilter):
    title = 'Time' 
    parameter_name = 'Time'

    

    def lookups(self, request, model_admin): #recent means within the last 7 days
        return (
            ('old-new', _('old-new')),
            ('new-old', _('new-old')),
        )
    def queryset(self, request, queryset=Complaint.objects.all()):
        if self.value() == 'new-old':
            return queryset.order_by('date_created')[:]

        if self.value() == 'old-new':
            return queryset.order_by('-date_created')[:]


class ClassFilter(admin.SimpleListFilter):
    title = _('By class')

    parameter_name = 'class'

    def lookups(self, request, model_admin):
        return (
            ('primary', _('primary')),
            ('secondary', _('secondary')),
            # ('active', _('active')),
        )
    def queryset(self, request, queryset=Student.objects.all()):
        if self.value() == 'primary':
            return queryset.filter(student_class__startswith='Primary')

        if self.value() == 'secondary':
            return queryset.exclude(student_class__startswith='Primary')
