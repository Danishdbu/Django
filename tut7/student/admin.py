from django.contrib import admin
from student.models import Profile,Result
# Register your models here.
# without decorator showing data base on admin panel
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name','rollNo','city')

# Register the model on admin panel
admin.site.register(Profile,ProfileAdmin)

# with decorator
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id','stud_class','marks')

