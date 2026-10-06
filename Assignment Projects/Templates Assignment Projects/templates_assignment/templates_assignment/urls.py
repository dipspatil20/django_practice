"""
URL configuration for templates_assignment project.

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('app1.urls')),
    path('app2/',include('app2.urls')),
    path('app3/', include('app3.urls')),
    path('app4/', include('app4.urls')),
    path('app5/', include('app5.urls')),
]



    # path('', v1.home),
    # path('about', v1.about),
    # path('contact', v1.contact),

    # path('electronics', v2.Electronics),
    # path('fashion', v2.Fashion),
    # path('groceries', v2.Groceries),

    # path('add_items', v3.Add_item),
    # path('items',v3.Items),
    # path('remove_items',v3.Remove_item),

    # path('create_profile', v4.create_profile),
    # path('display_profile', v4.display_profile),
    # path('update_profile', v4.update_profile),

    # path('ai_help', v5.ai_help),
    # path('chat_help',v5.chat_help),
    # path('faq', v5.faq),

