from django.urls import path
from . import views


urlpatterns = [
    path("", views.welcome.as_view(), name="welcom-page"),
    path("posts/", views.AllPosts.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.PostDetials.as_view(), name="post-detial-page"),
    path("read-later" ,views.readlater.as_view() , name ="read-later")
]
