from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.views import View
from django.views.generic import ListView, DeleteView, CreateView, DetailView, UpdateView


def home(request):
    return HttpResponse('This is home page')

class PostListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        posts = Post.objects.all()
        context['posts'] = posts
        return context
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('posts')

class PostCreateView(CreateView):
    model = Post
    template_name = 'post.html'
    fields = ('title', 'short_desc', 'body')
    success_url = reverse_lazy('posts')
# class PostDetailView(View):
#     def get(self, request, pk):
#         post = get_object_or_404(Post, id=pk)
#         return render(request, 'post.html', {'post':post})
    
#     def put():
#         pass

    
#     def delete():
#         pass

# def posts(request):
#     posts = Post.objects.all()
#     return render(request, "posts.html", {'posts':posts})

# def post(request, pk):
#     post = get_object_or_404(Post, id=pk)
#     # respons = json.dumps(post.__dict__)
#     return JsonResponse(post)

# def postdelete(request, pk):
#     post = get_object_or_404(Post, id=pk)
#     post.delete()
#     return redirect('/posts')

# def updatepost(request, pk):
#     post = get_object_or_404(Post, id=pk)
#     form = PostForm(initial={"title":post.title, "short_desc":post.short_desc, "body":post.body})

#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('/posts')
#     return render(request, "update.html", context={'form':form})
    