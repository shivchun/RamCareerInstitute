from django.shortcuts import render
from studentApp.forms import *
from  django.contrib.auth.decorators import login_required
from studentApp.forms import SignUpForm


# Create your views here.
@login_required
def student_index(request):
    return render(request,"studentApp/student_page.html")

@login_required
def time_table(request):
    return render(request,"studentApp/time_table.html")

@login_required
def exam(request):
    return render(request,"studentApp/exam.html")

@login_required
def exam_registration_target(request):
    form = Exam_form_target()
    if request.method == 'POST':
        form = Exam_form_target(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanku(request)
    return render(request,"studentApp/exam_form.html",{'form':form})

@login_required
def exam_registration_12(request):
    form = Exam_form_12()
    if request.method == 'POST':
        form = Exam_form_12(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanku(request)
    return render(request,"studentApp/exam_form.html",{'form':form})

@login_required
def exam_registration_11(request):
    form = Exam_form_11()
    if request.method == 'POST':
        form = Exam_form_11(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanku(request)
    return render(request,"studentApp/exam_form.html",{'form':form})

@login_required
def exam_registration_10(request):
    form = Exam_form_10()
    if request.method == 'POST':
        form = Exam_form_10(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanku(request)
    return render(request,"studentApp/exam_form.html",{'form':form})

@login_required
def exam_registration_9(request):
    form = Exam_form_9()
    if request.method == 'POST':
        form = Exam_form_9(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanku(request)
    return render(request,"studentApp/exam_form.html",{'form':form})

@login_required
def exam_registration_8(request):
    form = Exam_form_8()
    if request.method == 'POST':
        form = Exam_form_8(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanku(request)
    return render(request,"studentApp/exam_form.html",{'form':form})

@login_required
def exam_registration_7(request):
    form = Exam_form_7()
    if request.method == 'POST':
        form = Exam_form_7(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanku(request)
    return render(request,"studentApp/exam_form.html",{'form':form})

@login_required
def exam_registration_6(request):
    form = Exam_form_6()
    if request.method == 'POST':
        form = Exam_form_6(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanku(request)
    return render(request,"studentApp/exam_form.html",{'form':form})


def thanku(request):
    return render(request,"studentApp/thanku.html")


#sign up views
def sign_up_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return  HttpResponseRedirect('/accounts/login')
    return  render(request,"registration/signup.html",{'form':form})

#exam RESULT
def result_page(request):
    return render(request,"studentApp/result_page.html")

def r_target(request):
    result = result_target.objects.all()
    return render(request,"studentApp/result1.html",{'result':result})

def r_12(request):
    result = result_12.objects.all()
    return render(request,"studentApp/result1.html",{'result':result})

def r_11(request):
    result = result_11.objects.all()
    return render(request,"studentApp/result1.html",{'result':result})

def r_10(request):
    result = result_10.objects.all()
    return render(request,"studentApp/result2.html",{'result':result})

def r_9(request):
    result = result_9.objects.all()
    return render(request,"studentApp/result2.html",{'result':result})

def r_8(request):
    result = result_8.objects.all()
    return render(request,"studentApp/result2.html",{'result':result})

def r_7(request):
    result = result_7.objects.all()
    return render(request,"studentApp/result2.html",{'result':result})

def r_6(request):
    result = result_6.objects.all()
    return render(request,"studentApp/result2.html",{'result':result})
