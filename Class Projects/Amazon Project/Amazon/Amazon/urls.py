"""
URL configuration for Amazon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from Electronics import views as v1
from Fashion import views as v2
from Groceries import views as v3
from Home_appliance import views as v4
from Sports import views as v5



urlpatterns = [
    path('admin/', admin.site.urls),
    path('mobile', v1.Mobile),
    path('laptop', v1.Laptop),
    path('tv', v1.TV),
    path('earbuds', v1.Earbuds),
    path('watches', v1.Watches),

    path('mens_cloths', v2.Mens_cloths),
    path('women_cloths', v2.Womens_cloths),
    path('kids_cloths', v2.Kids_cloths),
    path('footware', v2.Footware),
    path('accessories', v2.Accessories),

    path('fruits', v3.Fruits),
    path('vegetable', v3.Vegetable),
    path('dairy', v3.Dairy),
    path('dry-fruits', v3.Dry_fruits),
    path('snaks', v3.Snaks),

    path('grider', v4.Grinder),
    path('cooker', v4.Cooker),
    path('mixer', v4.Mixer),
    path('stove', v4.Stove),
    path('microwave', v4.Microwave),

    path('cricket', v5.Cricket),
    path('football', v5.Football),
    path('basketball', v5.Basketball),
    path('chess', v5.Chess),
    path('volleyball', v5.Volleyball),



]
