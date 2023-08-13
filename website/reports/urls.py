from django.urls import path

from .views import ReportsIndex, Addpub, LoginUser, logout_user, RegisterUser, about, ShowTable

urlpatterns = [
    path('', ReportsIndex.as_view(), name='home'),
    path('add/', Addpub.as_view(), name='addpublication'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('about/', about, name='about'),
    path('table/<slug:name>/', ShowTable.as_view(), name='table')
]
