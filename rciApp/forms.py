from django import forms
from rciApp.models import StudentEnquiry


#Student Enquiry Form
class StudentEnquiryForm(forms.ModelForm):
    class Meta:
        model = StudentEnquiry
        fields = ('name','mobileNo','presentClass','stream')
