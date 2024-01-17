"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include,path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("orm01/", include("orm01.urls")),
    path("users/",include("users.urls")),
    path('admin/', admin.site.urls)
]

''' 1.path() 함수를 통해 url 요청하는 방법
path(route , view, kwargs=None,name=None)

from django.urls import include, path
urlpatterns = [
    path("index/", views.index, name="main-view"), -> index/로 요청하면 view의 index라는 뷰함수로 라우팅해라
    path("bio/<username>/", views.bio, name="bio"),
    -> bio/<username> 요청하면 view의 bio라는 뷰 함수로 라우팅해라 
    -> <username>동적 url을 만드는 것 , username을 지정하게되면 bio(username)으로 전달된다.
    def bio(username):
        if username = 'insert' : insert.html~
        
    path("articles/<slug:title>/", views.article, name="article-detail"),
    -> <slug:title> : path convert 해주는 기능
    ex) My-First-Aticle 이런 제목을 가진 페이지에 요청하고 싶다.
    http://www.my.com/articles/my-first-aticle/
    
    path("articles/<slug:title>/<int:section>/", views.section, name="article-section"),
    -> url 문자열 패턴으로 path convert를 해주고 정수형으로 section값을 전달하겠다.
    ex) My-First-Aticle 이런 제목을 가진 페이지의 2번째 section 요청하고 싶다. 소문자,숫자,하이픈(-)
    http://www.my.com/articles/my-first-aticle/
    
    path("blog/", include("blog.urls")),
    ...,
    ]
    
    
    
################################## register converter()
class DateConverter:
    regex = "[0-9]{4}-[0-9]{2}-[0-9]{2}"

    def to_python(self, value):
        return datetime.strptime(value , '%y-%m-%d')

    def to_url(self, value):
        return value.strptime('%y-%m-%d')
        
2-2 변환기 등록
from django.urls import path, register_converter
from . import converters, views

register_converter(converters.DateConverter, "yyyy-mm-dd")

2-3 "yyyy-mm-dd"URL 패턴에 사용하자
urlpatterns = [
    path("event/<"yyyy-mm-dd":date>/", views.event , name = "my-event"),
]       
            
'''