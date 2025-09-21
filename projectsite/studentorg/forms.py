from django import forms
from .models import Organization, Student, College, Program, OrgMember


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'college', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'lastname', 'firstname', 'middlename', 'program']


class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['college_name']


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['prog_name', 'college']


class OrgMemberForm(forms.ModelForm):
    class Meta:
        model = OrgMember
        fields = ['student', 'organization', 'date_joined']
        widgets = {
            'date_joined': forms.DateInput(attrs={'type': 'date'}),
        }

