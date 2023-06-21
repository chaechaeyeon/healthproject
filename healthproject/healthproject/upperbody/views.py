from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import Paginator
from .forms import PostModelForm , CommentForm
from .models import Post, Comment


def upperhome(request):
    return render(request,"upperbody.html")

def create(request):
    if request.method == 'POST'or request.method== 'FILES':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save() 
            return redirect('upperbodyHome') 
    else:
        form = PostModelForm() 
    return render(request, 'upperbody_form.html', {'form':form})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts,5)
    pagnum = request.GET.get('page')
    posts = paginator.get_page(pagnum)
    return render(request, 'upperbody_list.html', {'posts':posts})

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    comment_form = CommentForm()
    context={
        'post':post,
        'comment_form': comment_form
    }
    return render(request,'upperbody_detail.html', context)

def post_update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method =='POST'or request.method== 'FILES':
        form = PostModelForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('upperbodyHome')
    else:
        form = PostModelForm(instance=post)
        return render(request,'upperbody_form.html',{'form':form, 'id':id})
    

def post_delete(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'GET':
        context = {'post' : post}
        return render(request, 'upperbody_confirm_delete.html',context)
    else:
        post.delete()
        return redirect('upperbodyHome')
    
def create_comment(request, id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():        
        finished_form = filled_form.save(commit=False)      
        finished_form.article = get_object_or_404(Post, pk=id)        
        finished_form.save()   
    return redirect('upperbodyDetail', id)


def update_comment(request, post_id, com_id):
    my_com = Comment.objects.get(id=com_id)
    comment_form = CommentForm(instance=my_com)
    if request.method == "POST":
        update_form = CommentForm(request.POST, instance=my_com)
        if update_form.is_valid():
            update_form.save()
            return redirect('upperbodyDetail', post_id)
    else:
        return render(request, 'upperbodyComment_update.html', {'comment_form' : comment_form})
    
def delete_comment(request,post_id,com_id):
    my_com = Comment.objects.get(id=com_id)
    my_com.delete()

    return redirect('upperbodyDetail' ,post_id)
    