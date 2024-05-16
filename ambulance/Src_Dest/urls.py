from django.urls import path
from . import views

urlpatterns=[

    #path("store/",views.store),
    #path("ambulance/",views.ambulance_fetch),
    path("storepage/",views.members),
    #server side html page .
    path('store/', views.store_data, name='store_data'),
    path('server/', views.ambulance_page, name='ambulance_page'),
    path('display/',views.display),

    path('server/', views.server_page, name='server_page')
   
]