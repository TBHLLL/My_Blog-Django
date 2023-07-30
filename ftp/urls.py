from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'ftp'

urlpatterns = [
    path('fileup/',views.file_update.as_view()),
    path('download/<int:id>/',views.file_download.as_view()),
]
