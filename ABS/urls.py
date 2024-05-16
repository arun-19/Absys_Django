"""
URL configuration for ABS project.

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
from django.urls import path,include
from django.http import HttpResponseNotFound
from .views import view



def notfound(request):
    return HttpResponseNotFound("<h1> 404 Page not found</h1>")
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",view.Home),
    
    path("Companymaster/<type>/",view.CompanyMaster,name="cm"),
   
    
    
    path("TableModification/<redir>/<modelTable>",view.TableModification,name="TableModification")
    ,
     path("ledger/<type>/",view.Ledger,name="led")
     , path("Unitmaster",view.Unitmaster ,name="um"),
    path("",include("Purchase.urls")),
   
]

handler404="ABS.views.view.page404"