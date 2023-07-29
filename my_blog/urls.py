"""
URL configuration for my_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from article.views import article_list
import notifications.urls
# 存放映射关系的列表
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',article_list,name='home'),
    # 新增代码，配置app的url
    path('article/', include('article.urls', namespace='article')),
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    path('inbox/notifications/', include('notifications.urls', namespace='notifications')),
    path('account/', include('allauth.urls')),
    #path('ftp/',include('ftp.urls')),
    #path('server/',include('server.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
