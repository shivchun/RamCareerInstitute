from django.contrib import admin
from studentApp.models import *


#exam_registration_target
class exam_registration_targetAdmin(admin.ModelAdmin):
    list_display = ['enrollment_no', 'name', 'phone', 'date']

admin.site.register(exam_registration_target,exam_registration_targetAdmin)

#exam_registration_12
class exam_registration_class_12Admin(admin.ModelAdmin):
    list_display = ['enrollment_no', 'name', 'phone', 'date']

admin.site.register(exam_registration_class_12,exam_registration_class_12Admin)


#exam_registration_11
class exam_registration_class_11Admin(admin.ModelAdmin):
    list_display = ['enrollment_no', 'name', 'phone', 'date']

admin.site.register(exam_registration_class_11,exam_registration_class_11Admin)

#exam_registration_10
class exam_registration_class_10Admin(admin.ModelAdmin):
    list_display = ['enrollment_no', 'name', 'phone', 'date']

admin.site.register(exam_registration_class_10,exam_registration_class_10Admin)

#exam_registration_9
class exam_registration_class_9Admin(admin.ModelAdmin):
    list_display = ['enrollment_no', 'name', 'phone', 'date']

admin.site.register(exam_registration_class_9,exam_registration_class_9Admin)

#exam_registration_8
class exam_registration_class_8Admin(admin.ModelAdmin):
    list_display = ['enrollment_no', 'name', 'phone', 'date']

admin.site.register(exam_registration_class_8,exam_registration_class_8Admin)

#exam_registration_7
class exam_registration_class_7Admin(admin.ModelAdmin):
    list_display = ['enrollment_no', 'name', 'phone', 'date']

admin.site.register(exam_registration_class_7,exam_registration_class_7Admin)

#exam_registration_6
class exam_registration_class_6Admin(admin.ModelAdmin):
    list_display = ['enrollment_no', 'name', 'phone', 'date']

admin.site.register(exam_registration_class_6,exam_registration_class_6Admin)

#result site register

class result_targetAdmin(admin.ModelAdmin):
    list_display = ['enrollment_no', 'name', 'physics_no', 'chemistry_no','math_no', 'bio_no']
admin.site.register(result_target,result_targetAdmin)

class result_12Admin(admin.ModelAdmin):
    list_display = ['enrollment_no', 'name', 'physics_no', 'chemistry_no','math_no', 'bio_no']
admin.site.register(result_12,result_12Admin)

class result_11Admin(admin.ModelAdmin):
    list_display = ['enrollment_no', 'name', 'physics_no', 'chemistry_no','math_no', 'bio_no']
admin.site.register(result_11,result_11Admin)

class result_10Admin(admin.ModelAdmin):
    list_display = ['enrollment_no', 'name', 'hindi', 'math', 'sanskrit', 'english', 'sst', 'english']
admin.site.register(result_10,result_10Admin)

class result_9Admin(admin.ModelAdmin):
    list_display = ['enrollment_no', 'name', 'hindi', 'math', 'sanskrit', 'english', 'sst', 'english']
admin.site.register(result_9,result_9Admin)

class result_8Admin(admin.ModelAdmin):
    list_display = ['enrollment_no', 'name', 'hindi', 'math', 'sanskrit', 'english', 'sst', 'english']
admin.site.register(result_8,result_8Admin)

class result_7Admin(admin.ModelAdmin):
    list_display = ['enrollment_no', 'name', 'hindi', 'math', 'sanskrit', 'english', 'sst', 'english']
admin.site.register(result_7,result_7Admin)

class result_6Admin(admin.ModelAdmin):
    list_display = ['enrollment_no', 'name', 'hindi', 'math', 'sanskrit', 'english', 'sst', 'english']
admin.site.register(result_6,result_6Admin)
