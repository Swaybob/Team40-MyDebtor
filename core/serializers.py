from re import S
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from djoser.serializers import UserCreatePasswordRetypeSerializer as RegisterSerializer
    
from mydebtors.models import Debt, Sponsor, Student
from rest_framework import serializers 

from .models import *


class CustomUserCreateSerializer (RegisterSerializer):
    class Meta(RegisterSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name', 'NIN', 'password']

    def create(self, validated_data):
        try:
            if self.validated_data['NIN'] or self.validated_data['first_name']:
                if not Sponsor.objects.filter(email = self.validated_data['email']).exists():
                    self.fail("cannot_create_user")
                       
            user = self.perform_create(validated_data)

        except IntegrityError:
            self.fail("cannot_create_user")

        return user
        



class SchoolSerializer (serializers.ModelSerializer):
    debtors = serializers.SerializerMethodField()
    cleared_debtors = serializers.SerializerMethodField()
    contenders = serializers.SerializerMethodField()


    class Meta:
        model = School
        fields = ['id', 'reg_number', 'name',
                  'category', 'state', 'LGA', 'logo', 'address', 'debtors', 'cleared_debtors', 'contenders']

    def get_debtors(self, school):
        return school.students.count()

    def get_cleared_debtors(self, school):
        cleared = Student.objects.filter(debts__status = 'resolved', school = school)
        return cleared.count()
    
    def get_contenders(self, school):
        return school.complaints.count()


    


 
class PrincipalSerializer (serializers.ModelSerializer):
    #user = serializers.IntegerField(read_only =True)
    class Meta:
        model = Principal
        fields = ['id','name','gender','date_of_birth','address',
                    'id_type', 'id_number','CAC','letter','id_card']


    def save(self, **kwargs):

        user = self.context['user']

        self.instance = Principal.objects.create(user = user, **self.validated_data)

        return self.instance



