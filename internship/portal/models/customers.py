from django.db import models
class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=8)
    phone=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    def register(self):
        self.save()
class add_course(models.Model):
    course_name=models.CharField(max_length=100)
    course_description=models.TextField(max_length=1000)

    def __str__(self):
        return self.course_name
class employee(models.Model):
    employee_name=models.CharField(max_length=100)
    email_id=models.EmailField()
    phone_number=models.CharField(max_length=10)
    designation=models.CharField(max_length=100)

    def __str__(self):
        return  self.employee_name
class course(models.Model):
    course_name = models.ForeignKey(add_course, on_delete=models.CASCADE, default=1)
    courser_name = models.ForeignKey(employee, on_delete=models.CASCADE, default=1)
    course_duration = models.CharField(max_length=500)
    course_fee = models.CharField(max_length=1000)

class company(models.Model):
    company_name=models.CharField(max_length=500)
    company_type=models.CharField(max_length=500)
    service=models.ForeignKey(add_course,on_delete=models.CASCADE,default=1)
    city=models.CharField(max_length=1000)
    interns_required=models.CharField(max_length=500)
    def __str__(self):
        return self.company_name

class Company_registration(models.Model):
    owner_name=models.CharField(max_length=100,unique=True)
    company_name=models.CharField(max_length=100,unique=True)
    type=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=8)
    phone=models.CharField(max_length=100)
    city=models.CharField(max_length=100)


class internshipform(models.Model):
    fname=models.CharField(max_length=100,unique=True)
    lname=models.CharField(max_length=100,unique=True)
    city=models.CharField(max_length=100)
    phone=models.CharField(max_length=10,unique=True)
    email=models.EmailField(max_length=1000)
    graduation=models.CharField(max_length=1000)
    highersecondary=models.CharField(max_length=1000)
    secondary=models.CharField(max_length=1000)
    skill=models.CharField(max_length=1000)
    link=models.CharField(max_length=1000)
    link2=models.CharField(max_length=100)
    job = models.CharField(max_length=1000)
    internship = models.CharField(max_length=1000)
    tranning = models.CharField(max_length=1000)
    details = models.CharField(max_length=1000)
    field = models.CharField(max_length=1000)
    myfile = models.FileField(null=True, blank=True)

class blog(models.Model):
    blog_title=models.CharField(max_length=1000)
    blog_subtitle=models.CharField(max_length=1000)
    blog_description=models.TextField(max_length=100000)
    image=models.ImageField(upload_to='pictures/',max_length=1000)

class contact(models.Model):
    user_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    subject=models.CharField(max_length=1000)
    message=models.TextField(max_length=100)

class addjob(models.Model):
    job_title=models.CharField(max_length=200)
    job_description=models.CharField(max_length=200)
