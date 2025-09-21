from django.contrib import admin

# Register your models here.
from .models import College, Program, Organization, Student, OrgMember





@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("college_name", "created_at", "updated_at",)
    search_fields = ("college_name",)
    list_filter = ("created_at",)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name","college",)
    search_fields = ("prog_name","college",)
    list_filter = ("college",)
    
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name","college","description",)
    search_fields = ("name","description",)
    

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "program")
    search_fields = ("lastname", "program",)


@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "get_member_program", "organization", "date_joined",)
    search_fields = ("student__lastname", "student__firstname",)

    def get_member_program(self, obj):
        try:
            member = Student.objects.get(id=obj.student_id)
            return member.program
        except Student.DoesNotExist:
            return None
