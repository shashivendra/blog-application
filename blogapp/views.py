from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Category, Post, Author, Comment
from django.core.paginator import Paginator
from django.db.models import Q
  
  
def home(request):
    
    context = {
        'categories':Category.objects.all()
    }

    return render(request, 'blogapp/home.html', context)
   

def savequiry(request):
    context = {
        'categories': Category.objects.all()
    }

    if request.method == "POST":
        name = request.POST.get('name')
        en = Category.objects.create(name=name)
        
    return render(request, 'blogapp/home.html', context)
       

def addblog(request):

    
    if request.method == "POST":
        
        title = request.POST.get('title')
        blog_banner = request.FILES.get('blog_banner')
        content = request.POST.get('content')
        status = request.POST.get('status')
        category_id = request.POST.get('category')
        category_object = Category.objects.get(id=category_id)
        author_id =request.POST.get('author_name')
        author_object =Author.objects.get(id=author_id)
        
        post = Post.objects.create(title=title, blog_banner=blog_banner, content=content, category=category_object, author_name =author_object, status=status)
        return redirect('/post-list')
    
    context={
        'categories': Category.objects.all(),
        'authors': Author.objects.all()
    }
    return render(request, 'blogapp/addblog.html',  context)

        
def post_list(request):
    search_query = request.GET.get('q')
    all_posts = Post.objects.all()  
    if search_query:
        posts = all_posts.filter(
            Q(title=search_query) | 
            Q(content=search_query)
        )
    posts_per_page = 3

    # Paginator object
    paginator = Paginator(all_posts, posts_per_page)

    # Get the current page number from the URL query parameters
    page_number = request.GET.get('page')

    # Get the posts for the requested page
    page_obj = paginator.get_page(page_number)

    # Render the template with the paginated posts
    return render(request, 'blogapp/post_list.html', {'page_obj': page_obj})


def post_detail(request, post_detail_id):
    
    post =get_object_or_404(Post, id = post_detail_id)
    comments = Comment.objects.filter(post=post)
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Comment.objects.create(post=post, name=name, email=email, message=message)
        return redirect('post_detail', post_detail_id=post_detail_id)
      
    context = {
        
    'post':post, 
    'comments':comments
    
    }
    
    return render(request, 'blogapp/post_detail.html', context)


def author_name(request):
    
     if request.method == "POST":
        author_name =request.POST.get("author_name") 
        Author.objects.create(author_name =author_name)
        
     return render(request, 'blogapp/author.html') 
 
 
def blog_comment(request):
    
    context = {
        
        'comments':Comment.objects.all()
        
    }
       
    if request.method == "POST":
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        en =Comment.objects.create(name =name, email =email, message = message)
        
    return render(request, 'blogapp/comment.html', context)
        
        
        
        
        
    
    
    
    
      
         
    
    