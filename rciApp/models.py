from django.db import models

#Student Enquiry Models
stream_choice = [('Engineering','Engineering'),('Medical','Medical'),('6th,7th,8th,9th,10th','6th,7th,8th,9th,10th')]
class_choice = [tuple([x,x]) for x in range(6,13)]

class StudentEnquiry(models.Model):
    name = models.CharField('Name',max_length = 30, blank = False, null = False)
    mobileNo = models.IntegerField('mobile No', blank = False, null = False)
    presentClass = models.IntegerField('Present Class', choices=class_choice,default=6)
    stream = models.CharField('Stream', max_length = 20,choices=stream_choice,default = 'Engineering')


#new Batch models
new_class_choice = [('12th','12th'),('11th','11th'),('Target','Target'),('10th','10th'),('9th','9th'),('8th','8th'),('7th','7th'),('6th','6th')]

class New_Batch(models.Model):
    batch_class = models.CharField('Class', max_length = 10,blank = False, null = False,choices = new_class_choice, default = '12th')
    start_date = models.DateField('Starting Date of Batch', auto_now=False)
    time = models.TimeField('Batch Timing', blank = True, auto_now=False, auto_now_add=False)

#notification models
class Notification(models.Model):
    date = models.DateField('Date of Publish',auto_now=True)
    notice = models.TextField('Notification',blank=False)
