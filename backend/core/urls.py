"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from apps.dashboard.views import dashboard
from apps.website.views import homepage, about

urlpatterns = [
    path('', homepage, name="homepage"),
    path('about', about, name="about"),
    path('dashboard/', dashboard, name="dashboard_root_path"),
    path('dashboard/campaigns/', include("apps.campaigns.urls")),
    path('dashboard/events/', include("apps.events_manager.urls")),
    path('dashboard/incidents/', include("apps.incidents_manager.urls")),
    path('dashboard/notes/', include("apps.notes.urls")),
    path('dashboard/tasks/', include("apps.project_manager.urls")),

    path('api/', include("apps.campaigns.urls")),

    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
