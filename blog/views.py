from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.views import View
from .models import Post


class welcome(ListView):
    template_name = "blog/welcome.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        data = super().get_queryset()
        data = data[:3]
        return data


class AllPosts(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


class PostDetials(View):
    
    def is_stored_post(self ,request , post_id):
        stored_post=request.session.get("stored_posts")
        if stored_post is not None:
            is_saved_for_later = post_id in stored_post 
        else :
            is_saved_for_later = False
        
        return is_saved_for_later 

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "tags": post.tag.all(),
            "comment":  CommentForm(),
            "comments" : post.comment.all().order_by('-id') ,
            "saved_for_later" : self.is_stored_post(request ,post.id)
        }
        return render(request, "blog/post-detail.html", context)

    def post(slef, request, slug):
        Comment_from = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if Comment_from.is_valid():
            comment = Comment_from.save(commit=False)
            comment.post = post
            Comment_from.save()
            return HttpResponseRedirect(reverse("post-detial-page", args=[slug]))

        context = {
            "post": post,
            "tags": post.tag.all(),
            "comment":  Comment_from,
            "comments" : post.comment.all().order_by('-id') ,
            "saved_for_later" : self.is_stored_post(request ,post.id) 
        }

        return render(request, "blog/post-detail.html", context)
    


class readlater(View) :
    def get(self, request) :
        stored_posts =request.session.get("stored_posts")

        context = {} 

        if stored_posts is None or len(stored_posts) == 0: 
            context["posts"] = [] 
            context["has_posts"] = False 
        else :
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        return render(request , "blog/stored_id.html" , context)

    def post(self , request):
        stored_posts =request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts =[] 
        
        stored_id = int(request.POST["post_id"])

        if stored_id not in stored_posts:
            stored_posts.append(stored_id) 
        else :
            stored_posts.remove(stored_id)    

        request.session["stored_posts"] = stored_posts 
        
        return HttpResponseRedirect("/")