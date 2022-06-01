from django.urls import path
from.import views
from django.contrib.auth import views as auth_views    # 追加


app_name="Ganspa"

urlpatterns=[
    path("top/",views.topView.as_view(),name="top"),
    path("guide/",views.guideView.as_view(),name="guide"),
    path("users/",views.usersView.as_view(),name="users"),
    path("update/",views.GanspaUpdateView.as_view(),name="update"),
    path("register/",views.registerView.as_view(),name="register"),
    path("delete/<int:pk>",views.GanspaDeleteView.as_view(), name="delete"),
    #    path("sample/",views.LoginView.as_view(),name="sample"),
]