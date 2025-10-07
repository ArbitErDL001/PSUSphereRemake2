from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, Student, College, Program, OrgMember
from studentorg.forms import (
    OrganizationForm, StudentForm, CollegeForm,
    ProgramForm, OrgMemberForm
)
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin, ListView):
    model = Organization
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_students"] = Student.objects.count()

        today = timezone.now().date()
        count = (
            OrgMember.objects.filter(date_joined__year=today.year)
            .values("student").distinct().count()
        )
        context["students_joined_this_year"] = count
        context["total_organizations"] = Organization.objects.count()
        context["total_programs"] = Program.objects.count()
        return context



class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organizations'
    template_name = 'org_list.html'
    paginate_by = 5
    ordering = ["college__college_name","name"]

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return qs



class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')


# Student Views
class StudentList(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'student/student_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(lastname__icontains=query) |
                Q(firstname__icontains=query) |
                Q(middlename__icontains=query)
            )
        return qs



class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_form.html'
    success_url = reverse_lazy('student-list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_form.html'
    success_url = reverse_lazy('student-list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/student_delete.html'
    success_url = reverse_lazy('student-list')


# College Views
class CollegeList(ListView):
    model = College
    context_object_name = 'colleges'
    template_name = 'college/college_list.html'
    paginate_by = 5
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(college_name__icontains=query) 
            )
        return qs




class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college/college_form.html'
    success_url = reverse_lazy('college-list')


class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college/college_form.html'
    success_url = reverse_lazy('college-list')


class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college/college_delete.html'
    success_url = reverse_lazy('college-list')


# Program Views
class ProgramList(ListView):
    model = Program
    template_name = 'program_list.html'
    paginate_by = 5

    def get_ordering(self):
        allowed = ["prog_name", "college__college_name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "prog_name"

    def get_ordering(self):
        allowed = ["prog_name", "college__college_name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "prog_name"



class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program/program_form.html'
    success_url = reverse_lazy('program-list')


class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program/program_form.html'
    success_url = reverse_lazy('program-list')


class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program/program_delete.html'
    success_url = reverse_lazy('program-list')


# OrgMember Views
class OrgMemberList(ListView):
    model = OrgMember
    template_name = 'orgmember_list.html'
    paginate_by = 5

    def get_ordering(self):
        allowed = ["student__name", "date_joined"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "student__name"


    def get_ordering(self):

        allowed = ["student__lastname", "organization__name", "date_joined"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "student__lastname"

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember/orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')


class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember/orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')


class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember/orgmember_delete.html'
    success_url = reverse_lazy('orgmember-list')
