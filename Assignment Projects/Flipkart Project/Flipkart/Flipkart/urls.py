"""
URL configuration for Flipkart project.

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
from Elecrtonics import views as v1
from Fashion import views as v2
from Grocery import views as v3
from Home_appliences import views as v4
from Sports import views as v5

urlpatterns = [
    path('admin/', admin.site.urls),

    path('camera', v1.Cameras),
    path('tablet', v1.Tablets),
    path('speaker', v1.Speakers),
    path('printer', v1.Printers),
    path('power_bank', v1.Power_Banks),

    path('saree', v2.Sarees),
    path('kurta', v2.Kurtas),
    path('jeans', v2.Jeans),
    path('shirt', v2.Shirts),
    path('handbag', v2.Handbags),

    path('rice', v3.Rice_Grains),
    path('pulse', v3.Pulses),
    path('oil', v3.Oil),
    path('beverages', v3.Beverages),
    path('spices', v3.Spices),

    path('ac', v4.ACs),
    path('fan', v4.Fans),
    path('iron', v4.Irons),
    path('fridge', v4.Fridge),
    path('washing_machine', v4.Washing_Machines),

    path('cycling', v5.Cycling),
    path('swimming', v5.Swimming),
    path('yoga', v5.Yoga),
    path('fitness', v5.Fitness_Equipment),
    path('badminton', v5.Badminton),

]
