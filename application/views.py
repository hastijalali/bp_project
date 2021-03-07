from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404 ,redirect,reverse
from .forms import SolutionForm, UserProfileForm,AssignmentForm,SolCreditForm,CreateVideo
from .models import Assignment, Solution, UserProfile,Course,Videos
import datetime

def index(request):
	if  request.user.is_authenticated:
		return redirect('application:profile')
		
	else:
		return render(request, 'application/index.html')

def detail(request, assign_id):

		user = request.user
		assign = get_object_or_404(Assignment, pk=assign_id)
		return render(request, 'application/details.html', {'assignment': assign, 'user': user,'course':assign.course.name})

def detail_t(request, assign_id):

		user = request.user
		assign = get_object_or_404(Assignment, pk=assign_id)
		sol_set=Solution.objects.filter(assignment__id=assign_id)

		return render(request, 'application/details_t.html', {'assignment': assign,'sol_set':sol_set, 'user': user,'course':assign.course.name})
def sol_detail_t(request,sol_id):

		sol=get_object_or_404(Solution,pk=sol_id)
		if request.method=='POST':
			sol.comments=request.POST['comments']
			sol.points=request.POST['points']
			sol.save()
			return redirect('application:profile_t', course=sol.assignment.course)

		return render(request,'application/sol_details_t.html',{'sol':sol})
def profile(request,course):


		usr_profile = UserProfile.objects.get(user=request.user)
		usr_assign = Assignment.objects.filter(course__name=course)
		now=datetime.date.today()
		dead = []
		idx=[]
		asset = []
		cut = 1
		while True:
			usr_assign = Assignment.objects.filter(course__name=course,
												   num=cut)
			if len(usr_assign) == 0:
				break
			else:
				idx.append(cut)
				if usr_assign[0].deadline<now:
					dead.append(0)
				else:
					dead.append(1)

				asset.append(usr_assign)
				cut = cut + 1
		usr_soln = Solution.objects.filter(student=usr_profile)
		asset.reverse()
		dead.reverse()
		idx.reverse()

		return render(request, 'application/profile.html', {
			'asset': zip(asset,dead,idx),
			'solutions': usr_soln,
			'course':course,
		})

def profile_t(request,course):


		usr_profile = UserProfile.objects.get(user=request.user)
		now=datetime.date.today()
		idx=[]
		dead=[]
		asset=[]
		cut=1
		while True:

			usr_assign = Assignment.objects.filter(course__name=course, teacher=usr_profile, num=cut)
			if len(usr_assign)==0:
				break
			else:
				idx.append(cut)
				if usr_assign[0].deadline<now:
					dead.append(0)
				else:
					dead.append(1)
				asset.append(usr_assign)
				cut=cut+1
		asset.reverse()
		dead.reverse()
		idx.reverse()
		return render(request, 'application/profile_t.html', {
			'asset': zip(asset,dead,idx),
			'course':course,
		})



def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/application/')

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		identity=request.POST['identity']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				
				user_profile=UserProfile.objects.get(user=user,identity=identity)
				if user_profile is not None:
					if identity=='student':
						return redirect('application:s_courses')
					else:
						return redirect('application:t_courses')

			else:
				return render(request, 'application/index.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'application/index.html', {'error_message': 'Invalid login'})
	return render(request, 'application/index.html')

def s_courses(request):
	user_profile=UserProfile.objects.get(user=request.user)
	if user_profile is None:
		return render(request, 'application/index.html')
	else:
		courses=user_profile.courses
		course_list=courses.split('-')
		if course_list is not None:
			return render(request,'application/courses.html',{'course_list':course_list})


def t_courses(request):
	user_profile=UserProfile.objects.get(user=request.user)
	if user_profile is None:
		return render(request, 'application/index.html')
	else:
		courses=user_profile.courses
		course_list=courses.split('-')
		if course_list is not None:
			return render(request,'application/courses_t.html',{'course_list':course_list})

def submit(request,assignment_id):

		assignment=Assignment.objects.get(id=assignment_id)
		if request.method == 'POST':

			print(request.POST['title'])
			form = SolutionForm(user=request.user,course=assignment.course, data=request.POST)
			if form.is_valid():
				solution = form.save(commit=False)
				solution.student = UserProfile.objects.get(user=request.user)
				solution.assignment=assignment

				pre_sol=Solution.objects.filter(assignment__id=assignment_id,student=solution.student).all()
				pre_sol.delete()
				solution.save()
                

				return redirect('application:profile',course=assignment.course)

		else:
		
		    

			form = SolutionForm(user=request.user,course=assignment.course)
		return render(request, 'application/sol_submit.html', {'form': form,'course':assignment.course})

def add_t(request,course):

		if request.method == 'POST':
			form = AssignmentForm(data=request.POST)
			if form.is_valid():
				ass = form.save(commit=False)
				course=Course.objects.get(name=course)
				ass.teacher = UserProfile.objects.get(user=request.user)
				ass.course=course
				ass.save()

				return redirect('application:profile_t',course=course)

		else:
		
			

			form = AssignmentForm()
		return render(request, 'application/add_t.html', {'form': form,'course':course})
def teacherVideos(request):
	videos = Videos.objects.all()
	context={'videos':videos}
	return render(request,"application/teacher_videos.html",context)
def studentVideos(request):
	videos = Videos.objects.all()
	context={'videos':videos}
	return render(request,"application/student_videos.html",context)
def teacherUpload(request):
	
	if request.method=="POST":
		form = CreateVideo(request.POST , request.FILES)
		if form.is_valid():
			form.save()
			return  HttpResponseRedirect('/application/t_courses/')
	else:
	 form = CreateVideo()	
	 context={'form':form}
	 return render(request,"application/teacher_video_upload.html",context)

def videoDetail(request , video_id):
    vid = Videos.objects.get(id=video_id)
    context = {"video": vid}
    return render(request,"application/teacher_video_detail.html",context)
