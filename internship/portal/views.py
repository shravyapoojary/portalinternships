import uuid

from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .helper import  send_password_mail
from pyexpat.errors import messages




from django.shortcuts import render, redirect

from .models import Customer, company, course, Company_registration, internshipform, blog, contact
from django.contrib import messages

def homepage(request):
    return render(request, "index.html")
def blogpage(request):
    blogs=blog.objects.all()
    return render(request, "blog.html",{'Blog':blogs})
def applypage(request):
    return render(request,"apply.html")
@login_required(login_url="/login")

def userdashboardpage(request):
    return render(request,"userdashboard.html")
@login_required(login_url="/login")
def companypage(request):
    return render(request,"company.html")

def internpage(request):
    return render(request,"internship.html")
def coursepage(request):
    cou=course.objects.all()
    return render(request,"coursesoffered.html",{'Course':cou})

def student_data(request):


    student_list=Customer.objects.all()
    return render(request,'userprofile.html',{'student_list':student_list})

def signup(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phone']
        city=request.POST['city']
        if len(first_name) < 10:
            messages.warning(request,"Minimum 10 characters required")
        if len(password) < 8:
            messages.warning(request, "Minimum 8 characters required")

        Customer(first_name=first_name,
                 email=email,password=password,
                 phone=phone,city=city).save()
        messages.success(request,'The User '
                         +request.POST['first_name']+
                         " is registered Succesfully.")
        return  render(request,"signup.html")

    else:
        return  render(request,"signup.html")





def companysignup(request):
    if request.method=="POST":
        owner_name=request.POST['owner_name']
        company_name=request.POST['company_name']
        type=request.POST['type']
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phone']
        city=request.POST['city']
        Company_registration(owner_name=owner_name,company_name=company_name,type=type,email=email,password=password,phone=phone,city=city).save()
        messages.success(request,'The Company ' +request.POST['company_name']+ " is registered Succesfully.")
        return  render(request,"index.html")
    else:
        return  render(request,"companysignup.html")
def loginpage(request):
    redirect_to = request.POST.get('next')

    if request.method == "POST":
        try:
            email = request.POST['email']
            password = request.POST['password']

            Userdetails=Customer.objects.get(email=request.POST['email'],password = request.POST['password'])
            print("Username=",Userdetails)
            request.session['email']=Userdetails.email

            messages.success(request,"Login Successfull")
            return render(request, "userdashboard.html")


        except Customer.DoesNotExist as e:
            messages.success(request,"Email and Password Invalid..")

    return  render(request,"login.html")
def companyloginpage(request):
    if request.method == "POST":
        try:
            email = request.POST['email']
            password = request.POST['password']
            Userdetails=Company_registration.objects.get(email=request.POST['email'],password = request.POST['password'])
            print("Username=",Userdetails)
            request.session['email']=Userdetails.email
            messages.success(request,"Login Successfull")
            return render(request, "company.html")


        except Customer.DoesNotExist as e:
            messages.success(request,"Email and Password Invalid..")

    return  render(request,"companylogin.html")
def userlogout(request):
    try:
        del request.session['email']
    except:
        return render(request,"login.html")
    return render(request,"index.html")

def companylogout(request):
    try:
        del request.session['email']
    except:
        return render(request,"login.html")
    return render(request,"index.html")

def internship(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        city=request.POST['city']
        phone=request.POST['phone']
        email=request.POST['email']
        graduation=request.POST['graduation']
        highersecondary = request.POST['highersecondary']
        secondary = request.POST['secondary']
        skill = request.POST['skill']
        link = request.POST['link']
        link2 = request.POST['link2']
        job = request.POST['job']
        internship = request.POST['internship']
        tranning = request.POST['tranning']
        details = request.POST['details']
        field = request.POST['field']

        myfile = request.POST['myfile']



        internshipform(fname=fname,lname=lname,city=city,phone=phone,
                       email=email,graduation=graduation,
                       highersecondary=highersecondary,
                       secondary=secondary,skill=skill,link=link,
                       link2=link2,job=job,tranning=tranning,
                       internship=internship,details=details,
                       field=field,myfile=myfile).save()
        messages.success(request,'The Form '
                         +request.POST['fname']+
                         " is registered Succesfully.")
        return  render(request,"apply.html")
    else:
        return  render(request,"apply.html")

def blog_detail(request,id):
    blogs = blog.objects.get(id=id)
    context={'blogs': blogs}
    return render(request, "blog.html", context)

def contactinfo(request):
    if request.method=="POST":
        user_name=request.POST['user_name']
        email=request.POST['email']
        subject=request.POST['subject']
        message = request.POST['message']



        contact(user_name=user_name,
                       email=email,subject=subject,
                       message=message,
                       ).save()
        messages.success(request,"Your Form is added Succesfully.")
        return  render(request,"contact.html")
    else:
        return  render(request,"contact.html")

class blogDetailView(DetailView):
    model = blog
    template_name = 'blogdetail.html'

@login_required(login_url="/login")
def profilepage(request):
    context={
        'user':request.user
    }
    return render(request,"userprofile.html")
def forgetpassword(request):

    try:
        if request.method=="POST":
            username=request.POST('username')
            if not Customer.object.filter(username=username).first():
                 messages.success(request, "User Not Foound")
                 return redirect(request,"forget_password.html")

        userobj=Customer.objects.get(username=username)
        token = str(uuid.uuid4())
        send_password_mail(userobj,token)
        messages.success(request, "An email is sent")
        return redirect(request, "forget_password.html")


    except:
        return render(request,"forget_password.html")


