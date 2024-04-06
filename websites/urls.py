from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'websites'

urlpatterns = [
    path('zhongkao', views.zhongkao, name='websites_zhongkao'),
]
