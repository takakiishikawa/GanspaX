from django.urls import path
from.import views
from django.contrib.auth import views as auth_views    # 追加


app_name="Ganspa"

urlpatterns=[
    path("top/",views.topView.as_view(),name="top"),
    path("guide/",views.guideView.as_view(),name="guide"),
    path("users/",views.usersView.as_view(),name="users"),
    path("register/",views.registerView.as_view(),name="register"),
]