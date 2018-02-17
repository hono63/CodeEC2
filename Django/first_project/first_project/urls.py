"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from manager.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.conf.urls import url

urlpatterns += [
    url(r'^person/$', PersonList.as_view(), name='person-list-page'),   # 一覧
    url(r'^person/detail/(?P<pk>\d+)/$', PersonDetail.as_view(), name='person-detail-page'),  # 修正
    url(r'^person/edit/(?P<pk>\d+)/$', PersonEdit.as_view(), name='person-edit-page'),  # 修正
    url(r'^person/add/$', PersonAdd.as_view(), name='person-add-page'),  # 登録
    url(r'^person/del/(?P<pk>\d+)/$', PersonDelete.as_view(), name='person-delete-page'),  # 削除
]

from django.conf import settings
from django.conf.urls import include, url

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
