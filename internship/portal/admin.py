from django.contrib import admin
from .models import  addjob,blog,Customer,contact,add_course,internshipform,employee,course,company,Company_registration

# Register your models here.
#add courses
class blogadmin(admin.ModelAdmin):
    search_fields = ['blog_title']
    list_filter = ['blog_title','blog_subtitle']
    list_display = ('id','blog_title','blog_subtitle','blog_description','image')
class customeradmin(admin.ModelAdmin):
    list_display =('id','first_name')
    search_fields = ['first_name','email','phone','password','city']
    list_filter = ['first_name']
#add courses
class course_name_admin(admin.ModelAdmin):
    list_display = ('id','course_name','course_description')
    search_fields = ['course_name']
    list_filter = ['course_name']
#add emplyoee
class employeeadmin(admin.ModelAdmin):

    list_display = ('id','employee_name','email_id','phone_number','designation')
    search_fields = ['employee_name']
    list_filter = ['employee_name']
#add courses with prices details//all

class course_admin(admin.ModelAdmin):
    list_display = ('id','course_name','courser_name','course_duration','course_fee')
    search_fields = ['course_name']
    list_filter = ['course_name']

class companyadmin(admin.ModelAdmin):
    list_display = ('id','company_name','company_type','service','city','interns_required')
    search_fields = ['company_name']
    list_filter = ['company_type']
class companyregadmin(admin.ModelAdmin):
    list_display =("id","owner_name","company_name","type","email","password","phone","city")
    search_fields = ['company_name']
    list_filter = ['company_name']
class internadmin(admin.ModelAdmin):
    list_display = ("fname","lname","city","phone",
                       "email","graduation",
                       "highersecondary",
                       "secondary","skill","link",
                       "link2","job","tranning",
                       "internship","details",
                       "field","myfile")
    search_fields = ['fname']
    list_filter = ['fname']

class contactadmin(admin.ModelAdmin):
    list_display = ("user_name","email","subject","message")
    search_fields = ['user_name']
    list_filter = ['user_name']
class addjobadmin(admin.ModelAdmin):
    list_display = ['job_title','job_description']
admin.site.register(Customer,customeradmin)
admin.site.register(add_course,course_name_admin)
admin.site.register(employee,employeeadmin)
admin.site.register(course,course_admin)
admin.site.register(company,companyadmin)
admin.site.register(Company_registration,companyregadmin)
admin.site.register(internshipform,internadmin)
admin.site.register(blog,blogadmin)
admin.site.register(contact,contactadmin)
admin.site.register(addjob,addjobadmin)
