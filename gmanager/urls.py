"""gmanager URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from ceo import views

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include("ceo.urls")),
        path("employee/", include("employee.urls")),
        path("crm/", include("crm.urls")),
        path("hrm/", include("hrm.urls")),
        path("accounts/", include("accounts.urls")),
        path("clients/", include("clients.urls")),
        path("gm/", include("gm.urls")),
        path("pm/", include("pm.urls")),
        path("common/", include("common.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

admin.site.site_header = "G-mananger Administration"
admin.site.site_title = "g-manager  Admin Portal"
admin.site.index_title = "Welcome to Gedexo g-manager Admin Portal"


handler404 = views.handler404

handler500 = views.handler500
