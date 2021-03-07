from django import forms
from django.contrib.auth.models import User
from .models import Assignment, Solution, UserProfile,Videos
import datetime

class SolutionForm(forms.ModelForm):
	class Meta:
		model = Solution
		fields = ['title','body']

	def __init__(self, *args, **kwargs):
		
		user = kwargs.pop('user')

		course=kwargs.pop('course')

		super(SolutionForm, self).__init__(*args, **kwargs)


class AssignmentForm(forms.ModelForm):
	class Meta:
		model=Assignment
		fields=['num','name','questions','deadline']

class SolCreditForm(forms.ModelForm):
	class Meta:
		model=Solution
		fields=['points','comments']

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['full_name']
class CreateVideo(forms.ModelForm):
	class Meta :
		model = Videos
		fields = ['caption', 'vids']