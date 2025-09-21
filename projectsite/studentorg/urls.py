from django.urls import path
from . import views
from studentorg.views import (
    HomePageView, 
    OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView,
    StudentList, StudentCreateView, StudentUpdateView, StudentDeleteView,
    CollegeList, CollegeCreateView, CollegeUpdateView, CollegeDeleteView,
    ProgramList, ProgramCreateView, ProgramUpdateView, ProgramDeleteView,
    OrgMemberList, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView
)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    
    # Organization URLs
    path('organization_list/', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),
    
    # Student URLs
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/add', StudentCreateView.as_view(), name='student-add'),
    path('students/<pk>', StudentUpdateView.as_view(), name='student-update'),
    path('students/<pk>/delete', StudentDeleteView.as_view(), name='student-delete'),
    
    # College URLs
    path('colleges/', CollegeList.as_view(), name='college-list'),
    path('colleges/add', CollegeCreateView.as_view(), name='college-add'),
    path('colleges/<pk>', CollegeUpdateView.as_view(), name='college-update'),
    path('colleges/<pk>/delete', CollegeDeleteView.as_view(), name='college-delete'),
    
    # Program URLs
    path('programs/', ProgramList.as_view(), name='program-list'),
    path('programs/add', ProgramCreateView.as_view(), name='program-add'),
    path('programs/<pk>', ProgramUpdateView.as_view(), name='program-update'),
    path('programs/<pk>/delete', ProgramDeleteView.as_view(), name='program-delete'),
    
    # OrgMember URLs
    path('orgmembers/', OrgMemberList.as_view(), name='orgmember-list'),
    path('orgmembers/add', OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmembers/<pk>', OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmembers/<pk>/delete', OrgMemberDeleteView.as_view(), name='orgmember-delete'),
]
