from django.contrib import admin
from .models import Assignment, Solution, UserProfile ,Videos
# Register your models here.


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student')
    list_filter = ('assignment', 'submission_date', 'student')

class SolutionInline(admin.TabularInline):
    model = Solution

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name','updated', 'deadline')
    list_filter = ('deadline', 'updated')
    inlines = [SolutionInline]

class UserProfileAdmin(admin.ModelAdmin):
	pass

#Register the admin class with the associated model
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Videos)