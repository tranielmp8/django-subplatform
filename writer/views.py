from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from . forms import ArticleForm, UpdateUserForm
from . models import Article
from account.models import CustomUser

# CRUD

# Create your views here.
@login_required(login_url='my-login')
def writer_dashboard(request):
  
  return render(request, 'writer/writer-dashboard.html')

@login_required(login_url='my-login')
def create_article(request):
  form = ArticleForm()
  
  if request.method == 'POST':
    form = ArticleForm(request.POST)
    
    if form.is_valid():
      article = form.save(commit=False) # don't save it in the db just yet
      article.user = request.user # make sure the user is connected to the article
      article.save()
      return redirect('my-articles')
    
  context = {'CreateArticleForm': form}
  
  return render(request, 'writer/create-article.html', context)

@login_required(login_url='my-login')
def my_articles(request):
  current_user = request.user.id #id of logged in user
  # all articles that pertain to logged in user
  article = Article.objects.all().filter(user=current_user) 
  
  context = { 'AllArticles': article }
  
  return render(request, 'writer/my-articles.html', context)


@login_required(login_url='my-login')
def update_article(request, pk):
  
  try: 
    # user=request.user makes sure only user who created the article can update/delete that article
    article = Article.objects.get(id=pk, user=request.user)
  except:
    return redirect('my-articles')

# form will have article details we want to update
  form = ArticleForm(instance=article) 
  
  if request.method == 'POST':
    form = ArticleForm(request.POST, instance=article)
    
    if form.is_valid():
      form.save()
      return redirect('my-articles')
    
  context = {'UpdateArticleForm':form}
  return render(request, 'writer/update-article.html', context)


@login_required(login_url='my-login')
def delete_article(request, pk):
  
  try: 
    # user=request.user makes sure only user who created the article can update/delete that article
    article = Article.objects.get(id=pk, user=request.user)
  except:
    return redirect('my-articles')
  
  if request.method == 'POST':
    article.delete()
    return redirect('my-articles')
  
  return render(request, 'writer/delete-article.html')


# ACCOUNT MANAGEMENT

@login_required(login_url='my-login')
def account_management(request):
  form = UpdateUserForm(instance=request.user)
  
  if request.method == 'POST':
    form = UpdateUserForm(request.POST, instance=request.user)
    
    if form.is_valid():
      form.save()
      return redirect('writer-dashboard')
    
  context = {'UpdateUserForm':form}
  
  return render(request, 'writer/account-management.html', context)


# DELETE ACCOUNT:
@login_required(login_url='my-login')
def delete_account(request):
  
  if request.method == 'POST': 
    #grab email of user who is signed in in order to delete it
    deleteUser = CustomUser.objects.get(email=request.user)
    deleteUser.delete()
    return redirect('my-login')
  
  return render(request, 'writer/delete-account.html')