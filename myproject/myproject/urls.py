# 프로젝트의 URL 선언을 저장
"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from myapp import views

# router 선언
router = routers.DefaultRouter()
# router에 ViewSet등록. 이름으로 매핑
# ViewSet을 사용하면 router클래스에 등록만 해도 URLconf를 자동으로 생성할 수 있음
# 더 많은 제어가 필요할 경우 일반 클래스 기반 View를 사용하고 URL구성을 명시적으로 작성하면 됨
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)), # router 매핑
    # path('admin/', admin.site.urls), # admin 연결
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # 기본 로그인/로그아웃. 선택사항이지만 인증 편하게 가능
    # path('', include(router.urls)),
]