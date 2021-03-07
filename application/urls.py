from django.conf.urls import url
from application import views
from django.urls import path, re_path
app_name='application'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    re_path(r'profile/(?P<course>[a-zA-Z]+)$', views.profile, name='profile'),
    re_path(r'profile_t/(?P<course>[a-zA-Z]+)$', views.profile_t, name='profile_t'),
    path(r'logout/', views.logout_user, name='logout'),
    re_path(r'assignment/(?P<assign_id>[0-9]+)$', views.detail, name='detail'),
    re_path(r'assignment_t/(?P<assign_id>[0-9]+)$', views.detail_t, name='detail_t'),
    re_path(r'sol_detail_t/(?P<sol_id>[0-9]+)$', views.sol_detail_t, name='sol_detail_t'),
    re_path(r'sol_submit/(?P<assignment_id>[0-9]+)$', views.submit, name='submit'),
    re_path(r'add_t/(?P<course>[a-zA-Z]+)$', views.add_t, name='add_t'),
    path('t_courses/',views.t_courses,name="t_courses"),
    path('s_courses/',views.s_courses,name="s_courses"),
    path('t_videos/',views.teacherVideos,name="hasti"),
    path('videos/upload/',views.teacherUpload, name = "teacher_video_upload"),
    path('videos/<int:video_id>',views.videoDetail, name="teacher_video_detail"),
    path('s_videos/',views.studentVideos,name="student_videos")]
