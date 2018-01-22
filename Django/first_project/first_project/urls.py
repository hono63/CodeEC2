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

import manager.views as manager_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('worker_list/', manager_view.WorkerListView.as_view()),
    path('person_list/', manager_view.PersonListView.as_view()),
]

from django.conf.urls import url

urlpatterns += [
    url(r'^person/add/$', manager_view.person_edit, name='person_add'),  # 登録
    url(r'^person/mod/(?P<person_id>\d+)/$', manager_view.person_edit, name='person_mod'),  # 修正
    url(r'^person/del/(?P<person_id>\d+)/$', manager_view.person_delete, name='person_del'),  # 削除
]

from django.conf import settings
from django.conf.urls import include, url

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
