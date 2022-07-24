from django.urls import include, path

'''
urls.py fires the respective view function whenever the a url
is accessed accordingly 

'''

from .views.views import StudentProject, StudentProjectUpload, \
    ViewMessages, StudentMessageSupervisor, PostDetailView, \
    StudentDefenceCall, StudentDefenceCallView, StudentMeetingCreate, StudentMeetingList, \
        MeetingDetailView, ReadTrue, StudentProjectContentUpdate, StudentProjectUploadContentDetailView, \
            StudentProjectTitleUpdate

from .views.supervisor import StudentList , PostDetailView as PDVSupervisor, \
    ViewMessages as VMSupervisor, SupervisorMessageStudent, StudentDefenceCall as SDcall, \
        StudentDefenceCallView as SDCallView, StudentProjectUpload as SProjectUpload, \
            SupervisorMeetingList, SupervisorMeetingDetailView, SupervisorMeetingUpdate, \
                ProjectUpdate, ReadTrueSupervisor, ProjectContentUpdate, ProjectUploadContentDetailview, \
                    ProjectTitleStatusUpdate

                
urlpatterns = [
    path('', StudentProject.as_view(), name='home'),  
    path('project/upload/', StudentProjectUpload.as_view(), name='project_upload'),
    path('project/titleupdate/<uuid:pk>/', StudentProjectTitleUpdate.as_view(), name='project_title_update'),
    path('project/upload/<pk>/', PostDetailView.as_view(), name='project_upload_detail'),
    path('project/uploadcontent/<pk>/', StudentProjectUploadContentDetailView.as_view(), name='project_upload_content_detail'),

    path('message/list/', ViewMessages.as_view(), name='view_messages'),
    path('message/create/', StudentMessageSupervisor.as_view(), name='create_message'),

    path('defence/call/create', StudentDefenceCall.as_view(), name='defence_call'),
    path('defence/call/', StudentDefenceCallView.as_view(), name='defence_call_list'),

    path('meeting/create/', StudentMeetingCreate.as_view(), name='meeting_create'),
    path('meeting/list/', StudentMeetingList.as_view(), name='meeting_list'),
    path('meeting/<pk>/', MeetingDetailView.as_view(), name='meeting_detail'),
    path('project/updatecontent/<pk>', StudentProjectContentUpdate.as_view(), name='update_project_content_student'),

    path('read/<pk>/', ReadTrue.as_view(), name='read_true'),



    #supervisor

    path('supervisor/', StudentList.as_view(), name='supervisor_home'),
    path('supervisor/project/titleupdate/<uuid:pk>/', ProjectTitleStatusUpdate.as_view(), name='project_title_update_supervisor'),
    path('supervisor/project/upload/<pk>/', PDVSupervisor.as_view(), name='project_upload_detail_supervisor'),
    path('supervisor/project/uploadcontent/<pk>/', ProjectUploadContentDetailview.as_view(), name='project_upload_content_detail_supervisor'),
    path('supervisor/projects/list/student_id=<student_id>/', SProjectUpload.as_view(), name='project_upload_list_supervisor'),
    path('supervisor/project/update/<pk>', ProjectUpdate.as_view(), name='project_update'),
    path('supervisor/project/updatecontent/<pk>', ProjectContentUpdate.as_view(), name='update_project_content'),

    path('supervisor/message/list/student_id=<student_id>/', VMSupervisor.as_view(), name='view_messages_supervisor'),
    path('supervisor/message/create/', SupervisorMessageStudent.as_view(), name='create_message_supervisor'),

    path('supervisor/defence/call/update/<pk>', SDcall.as_view(), name='defence_call_supervisor'),
    path('supervisor/defence/call/student_id=<student_id>/', SDCallView.as_view(), name='defence_call_list_supervisor'),

    # path('meeting/create/', StudentMeetingCreate.as_view(), name='meeting_create'),
    path('supervisor/meeting/list/student_id=<student_id>/', SupervisorMeetingList.as_view(), name='supervisor_meeting_list'),
    path('supervisor/meeting/<pk>/', SupervisorMeetingDetailView.as_view(), name='supervisor_meeting_detail'),
    path('supervisor/meetingcomment/update/<pk>', SupervisorMeetingUpdate.as_view(), name='meeting_update_supervisor'),

    path('supervisor/read/<pk>/', ReadTrueSupervisor.as_view(), name='read_true_supervisor'),




]

