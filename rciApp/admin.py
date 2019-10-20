from django.contrib import admin
from rciApp.models import StudentEnquiry,New_Batch,Notification
# Register your models here.

#Student Enquiry model registration
class StudentEnquiryAdmin(admin.ModelAdmin):
    list_display = ['name','mobileNo','presentClass','stream']

admin.site.register(StudentEnquiry,StudentEnquiryAdmin)

#new batch model registration
class New_BatchAdmin(admin.ModelAdmin):
    list_display = ['batch_class','start_date']

admin.site.register(New_Batch,New_BatchAdmin)

#notification models
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['date', 'notice']

admin.site.register(Notification, NotificationAdmin)
