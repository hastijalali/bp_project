from django.db import models
from django.contrib.auth.models import Permission, User
import django
import datetime


class Course(models.Model):
	COURSE_CHOICE=(
		('bp','bp'),
	)
	name=models.CharField(choices=COURSE_CHOICE,max_length=100,default="")
	def __str__(self):
		return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	COURSE_CHOICE=('bp','bp')

	IDENTITY_CHOICE=(
		('teacher','teacher'),
		('student', 'student'),
		
	)
	identity=models.CharField(choices=IDENTITY_CHOICE,max_length=100,default="student")
	courses=models.CharField(COURSE_CHOICE,max_length=500,default="")
	full_name = models.CharField(max_length = 100)

	roll_no = models.CharField(max_length = 9, unique=True)
	created = models.DateField(editable=False, null=True)
	
	def __str__(self):
		return self.roll_no

	def save(self):
		if not self.id:
			self.roll_no = self.user.username
			self.created = datetime.date.today()
		super(UserProfile, self).save()

class Assignment(models.Model):

	course=models.ForeignKey(Course,on_delete=models.SET_NULL, null=True,default="")
	teacher=models.ForeignKey(UserProfile,on_delete=models.SET_NULL, null=True,default="")
	name = models.CharField(max_length = 200)
	questions = models.TextField(max_length = 1000)
	solutionfiles=models.FileField(upload_to="medias/solutions",default="")
	num=models.IntegerField(default=1)
	created = models.DateField(editable=False, null=True)
	updated = models.DateTimeField(editable=False, null=True)
	deadline = models.DateField()
	def __str__(self):
		return self.name

	def save(self):
		if not self.id:
			self.created = datetime.date.today()
		self.updated = datetime.datetime.today()
		super(Assignment, self).save()

class Solution(models.Model):
	assignment = models.ForeignKey(Assignment, on_delete=models.SET_NULL, null=True)
    
	student = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
	submission_date = models.DateField()
	title=models.CharField(max_length=100,default="")
	questionfiles=models.FileField(upload_to="medias/questions",default="")
	body=models.TextField(max_length=1000,default="")
	points=models.FloatField(default=0.)
	comments=models.CharField(max_length=200,default="")
	worked=models.BooleanField(default=False)
	def __str__(self):
		return self.title

	def save(self):
		self.submission_date = datetime.date.today()
		super(Solution, self).save()
class Videos(models.Model):
	caption = models.CharField(max_length=100)
	vids = models.FileField(upload_to="medias/video")
	def __str__(self):
	    return self.caption