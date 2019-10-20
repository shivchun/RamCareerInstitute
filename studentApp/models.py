from django.db import models

#class target
class exam_registration_target(models.Model):
    enrollment_no =models.IntegerField('Enrollment Number', primary_key=True)
    name = models.CharField('Name', max_length = 30, blank = False, null = False)
    phone = models.IntegerField('Phone',blank = False, null = False )
    date = models.DateField('Date', auto_now=True)
#class 12
class exam_registration_class_12(models.Model):
    enrollment_no =models.IntegerField('Enrollment Number', primary_key=True)
    name = models.CharField('Name', max_length = 30, blank = False, null = False)
    phone = models.IntegerField('Phone',blank = False, null = False )
    date = models.DateField('Date', auto_now=True)

#class 11
class exam_registration_class_11(models.Model):
    enrollment_no =models.IntegerField('Enrollment Number', primary_key=True)
    name = models.CharField('Name', max_length = 30, blank = False, null = False)
    phone = models.IntegerField('Phone',blank = False, null = False )
    date = models.DateField('Date', auto_now=True)

#class 10
class exam_registration_class_10(models.Model):
    enrollment_no =models.IntegerField('Enrollment Number', primary_key=True)
    name = models.CharField('Name', max_length = 30, blank = False, null = False)
    phone = models.IntegerField('Phone',blank = False, null = False )
    date = models.DateField('Date', auto_now=True)

#class 9
class exam_registration_class_9(models.Model):
    enrollment_no =models.IntegerField('Enrollment Number', primary_key=True)
    name = models.CharField('Name', max_length = 30, blank = False, null = False)
    phone = models.IntegerField('Phone',blank = False, null = False )
    date = models.DateField('Date', auto_now=True)

#class 8
class exam_registration_class_8(models.Model):
    enrollment_no =models.IntegerField('Enrollment Number', primary_key=True)
    name = models.CharField('Name', max_length = 30, blank = False, null = False)
    phone = models.IntegerField('Phone',blank = False, null = False )
    date = models.DateField('Date', auto_now=True)

#class 7
class exam_registration_class_7(models.Model):
    enrollment_no =models.IntegerField('Enrollment Number', primary_key=True)
    name = models.CharField('Name', max_length = 30, blank = False, null = False)
    phone = models.IntegerField('Phone',blank = False, null = False )
    date = models.DateField('Date', auto_now=True)

#class 6
class exam_registration_class_6(models.Model):
    enrollment_no =models.IntegerField('Enrollment Number', primary_key=True)
    name = models.CharField('Name', max_length = 30, blank = False, null = False)
    phone = models.IntegerField('Phone',blank = False, null = False )
    date = models.DateField('Date', auto_now=True)

#result_page

#class 11
class result_target(models.Model):
    enrollment_no = models.IntegerField('Enrollment Number')
    name = models.CharField('Name',max_length = 30)
    physics_no = models.IntegerField('Physics',default=0)
    chemistry_no = models.IntegerField('Chemistry',default=0)
    math_no = models.IntegerField('Math', default=0)
    bio_no = models.IntegerField('Biology', default=0)

#class 11
class result_12(models.Model):
    enrollment_no = models.IntegerField('Enrollment Number')
    name = models.CharField('Name',max_length = 30)
    physics_no = models.IntegerField('Physics', default=0)
    chemistry_no = models.IntegerField('Chemistry', default=0)
    math_no = models.IntegerField('Math', default=0)
    bio_no = models.IntegerField('Biology', default=0)

#class 11
class result_11(models.Model):
    enrollment_no = models.IntegerField('Enrollment Number')
    name = models.CharField('Name',max_length = 30)
    physics_no = models.IntegerField('Physics', default=0)
    chemistry_no = models.IntegerField('Chemistry', default=0)
    math_no = models.IntegerField('Math', default=0)
    bio_no = models.IntegerField('Biology', default=0)

#class 10
class result_10(models.Model):
    enrollment_no = models.IntegerField('Enrollment Number')
    name = models.CharField('Name',max_length = 30)
    science = models.IntegerField('Science', default=0)
    math = models.IntegerField('Math', default=0)
    hindi = models.IntegerField('Hindi', default=0)
    sst = models.IntegerField('Social Science', default=0)
    sanskrit = models.IntegerField('Sanskrit', default=0)
    english = models.IntegerField('English', default=0)

#class 9
class result_9(models.Model):
    enrollment_no = models.IntegerField('Enrollment Number')
    name = models.CharField('Name',max_length = 30)
    science = models.IntegerField('Science', default=0)
    math = models.IntegerField('Math', default=0)
    hindi = models.IntegerField('Hindi', default=0)
    sst = models.IntegerField('Social Science', default=0)
    sanskrit = models.IntegerField('Sanskrit', default=0)
    english = models.IntegerField('English', default=0)

#class 8
class result_8(models.Model):
    enrollment_no = models.IntegerField('Enrollment Number')
    name = models.CharField('Name',max_length = 30)
    science = models.IntegerField('Science', default=0)
    math = models.IntegerField('Math', default=0)
    hindi = models.IntegerField('Hindi', default=0)
    sst = models.IntegerField('Social Science', default=0)
    sanskrit = models.IntegerField('Sanskrit', default=0)
    english = models.IntegerField('English', default=0)

#class 7
class result_7(models.Model):
    enrollment_no = models.IntegerField('Enrollment Number')
    name = models.CharField('Name',max_length = 30)
    science = models.IntegerField('Science', default=0)
    math = models.IntegerField('Math', default=0)
    hindi = models.IntegerField('Hindi', default=0)
    sst = models.IntegerField('Social Science', default=0)
    sanskrit = models.IntegerField('Sanskrit', default=0)
    english = models.IntegerField('English', default=0)

#class 6
class result_6(models.Model):
    enrollment_no = models.IntegerField('Enrollment Number')
    name = models.CharField('Name',max_length = 30)
    science = models.IntegerField('Science', default = 0)
    math = models.IntegerField('Math', default = 0)
    hindi = models.IntegerField('Hindi', default = 0)
    sst = models.IntegerField('Social Science', default = 0)
    sanskrit = models.IntegerField('Sanskrit', default = 0)
    english = models.IntegerField('English', default = 0)
