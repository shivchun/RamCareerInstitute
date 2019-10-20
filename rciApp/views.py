from django.shortcuts import render
from rciApp.forms import StudentEnquiryForm
from rciApp.models import StudentEnquiry,New_Batch,Notification
from django.http import HttpResponse
# Create your views here.


##view for complete site function
def index(request):
    form = StudentEnquiryForm()
    if request.method == 'POST':
        form = StudentEnquiryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanku(request)
    return render(request,"rciApp/index.html",{'form':form})

def contact(request):
    form = StudentEnquiryForm()
    if request.method == 'POST':
        form = StudentEnquiryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanku(request)
    return render(request,"rciApp/contact.html",{'form':form})

def program(request):
    form = StudentEnquiryForm()
    if request.method == 'POST':
        form = StudentEnquiryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanku(request)
    return render(request,"rciApp/foundation_extended.html",{'form':form})

def engineering(request):
    form = StudentEnquiryForm()
    if request.method == 'POST':
        form = StudentEnquiryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanku(request)
    return render(request,"rciApp/engineering.html",{'form':form})

def medical(request):
    form = StudentEnquiryForm()
    if request.method == 'POST':
        form = StudentEnquiryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanku(request)
    return render(request,"rciApp/medical.html",{'form':form})

def foundation(request):
    form = StudentEnquiryForm()
    if request.method == 'POST':
        form = StudentEnquiryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanku(request)
    return render(request,"rciApp/foundation.html",{'form':form})

def foundation_extended(request):
    form = StudentEnquiryForm()
    if request.method == 'POST':
        form = StudentEnquiryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanku(request)
    return render(request,"rciApp/foundation_extended.html",{'form':form})

#thanku views
def thanku(request):
    return render(request,"rciApp/thank.html")


#new batch views
def new_batch(request):
    batch = New_Batch.objects.all()
    return render(request,"rciApp/new_batch.html",{'batch':batch})

#about
def about(request):
    return render(request,"rciApp/about.html")

#notification
def notification(request):
    note = Notification.objects.all()
    return render(request,"rciApp/notification.html",{'note':note})
