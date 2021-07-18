from urllib import request

from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.forms import forms, ModelForm
from .models import Customer, Company_registration
from .models.customers import internshipform, contact


class registerforms(ModelForm):
    class Meta:
        model=Customer
        fields=["first_name","email","password","phone","city"]
    def clean(self):
        email = self.cleaned_data.get('email')
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError("Email exists")
        return self.cleaned_data
class userregisterforms(ModelForm):
    class Meta:
        model=Company_registration
        fields=["owner_name","company_name","type",
                "email","password","phone","city"]

class applyinternshipform(ModelForm):
            class Meta:
                model = internshipform
                fields = ["fname", "lname", "city",
                          "phone", "email", "graduation",
                          "highersecondary","secondary",
                          "skill","link",
                          "link2","job","internship","tranning","details","field","myfile"]


class conatctforms(ModelForm):
    class Meta:
        model=contact
        fields=["user_name",
                "email","subject","message"]