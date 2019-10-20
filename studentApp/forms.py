from django import forms
from studentApp.models import *
from  django.contrib.auth.models import User

#login forms
class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields =  ['first_name', 'last_name', 'username', 'email','password']



#exam registration Form
class Exam_form_target(forms.ModelForm):
    class Meta:
        model = exam_registration_target
        fields = ('enrollment_no', 'name', 'phone')

        date_of_exam = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d/%m/%Y', )
        )

#exam registration Form
class Exam_form_12(forms.ModelForm):
    class Meta:
        model = exam_registration_class_12
        fields = ('enrollment_no', 'name', 'phone')

        date_of_exam = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d/%m/%Y', )
        )

#exam registration Form
class Exam_form_11(forms.ModelForm):
    class Meta:
        model = exam_registration_class_11
        fields = ('enrollment_no', 'name', 'phone')

        date_of_exam = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d/%m/%Y', )
        )

#exam registration Form
class Exam_form_10(forms.ModelForm):
    class Meta:
        model = exam_registration_class_10
        fields = ('enrollment_no', 'name', 'phone')

        date_of_exam = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d/%m/%Y', )
        )

#exam registration Form
class Exam_form_9(forms.ModelForm):
    class Meta:
        model = exam_registration_class_9
        fields = ('enrollment_no', 'name', 'phone')

        date_of_exam = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d/%m/%Y', )
        )
#exam registration Form
class Exam_form_8(forms.ModelForm):
    class Meta:
        model = exam_registration_class_8
        fields = ('enrollment_no', 'name', 'phone')

        date_of_exam = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d/%m/%Y', )
        )
#exam registration Form
class Exam_form_7(forms.ModelForm):
    class Meta:
        model = exam_registration_class_7
        fields = ('enrollment_no', 'name', 'phone')

        date_of_exam = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d/%m/%Y', )
        )

#exam registration Form
class Exam_form_6(forms.ModelForm):
    class Meta:
        model = exam_registration_class_6
        fields = ('enrollment_no', 'name', 'phone')

        date_of_exam = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%d/%m/%Y', )
        )
