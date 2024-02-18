from django.urls import path
from . import views

app_name = 'hostelmanagement'

urlpatterns = [
    #Home 
    path('', views.hostel_view, name="hostel_view"),
    path('/hello', views.hostel_view, name="hello"),

    #Notice Board
    path('notice_form/', views.notice_board, name="notice_board"),
    path('delete_notice/', views.delete_notice, name="delete_notice"),

    #Worker Schedule
    path('edit_schedule/', views.staff_edit_schedule, name='staff_edit_schedule'),
    path('delete_schedule/', views.staff_delete_schedule, name='staff_delete_schedule'),
    
    #Student Room
    path('edit_student/',views.edit_student_room,name="edit_student_room"),
    path('edit_student_rooms_sheet/', views.edit_student_rooms_sheet, name="edit_student_rooms_sheet"),

    #Attendance
    path('edit_attendance/', views.edit_attendance, name='edit_attendance'),

    #Attendance
    path('edit_attendance/', views.edit_attendance, name='edit_attendance'),

    #Worker Report
    path('worker_report/', views.generate_worker_report, name='workerreport'),
    path('pdf/', views.GeneratePDF.as_view(), name="pdf"),
    path('hostel-notices/', views.hostel_notice_board, name='hostel_notices_board'),
    # //caretaker and warden can see all leaves
    path('all_leave_data/', views.all_leave_data, name='all_leave_data'),
    # caretaker  or wardern can approve leave
    path('update_leave_status/', views.update_leave_status, name='update_leave_status'),
    # //apply for leave
    path('create_hostel_leave/', views.create_hostel_leave, name='create_hostel_leave'),
    
    # caretaker and warden can get all complaints
    path('hostel_complaints/', views.hostel_complaint_list, name='hostel_complaint_list'),

# // student register complaint
    path('register_complaint/', views.PostComplaint.as_view(), name='PostComplaint'),

#  Student can view his leave status
    path('my_leaves/', views.my_leaves.as_view(), name='my_leaves'),





]