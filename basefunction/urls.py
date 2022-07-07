from django.urls import path
from.import views
from django.contrib.auth import views as auth_views    # 追加


app_name="Ganspa"

urlpatterns=[
    path("top/",views.topView.as_view(),name="top"),
    path("guide/",views.guideView.as_view(),name="guide"),
    path("users/",views.usersView.as_view(),name="users"),
    path("register/",views.registerView.as_view(),name="register"),
<<<<<<< HEAD
=======
    path("delete/<int:pk>",views.GanDeleteView.as_view(), name="delete"),
    path("update/<int:pk>",views.GanUpdateView.as_view(),name="update"),
    #    path("sample/",views.LoginView.as_view(),name="sample"),
>>>>>>> 7fdf035ef125271469b0698aecb130cea40be012
]