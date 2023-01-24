from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView
from .form import WriteForm,TopicForm,LoginForm,SignupForm
from .models import Items,Topics
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User



# Create your views here.

class writeview(TemplateView):
    def get(self,request,param,*args, **kwargs):
        queryset = Items.objects.filter(topictitle=param).order_by('-created_at')
        return render(request, 'items/post.html',{'form':WriteForm,'items':queryset,'param':param})
    
    def post(self,request,param,*args,**kwargs):
        form = WriteForm(request.POST)
        post = form.save(commit=False)
        post.save()
        que = Items.objects.last()
        username = self.request.user
        username = str(username)
        que.user = username
        que.save()
        que.topictitle = param
        que.save()
        return redirect('items:write',param)

write = writeview.as_view()




class IndexView(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    def get(self,request, *args, **kwargs):
        queryset = Topics.objects.all().order_by('-created')
        return render(request, 'items/topicpost.html',{'topics':queryset})
    
index = IndexView.as_view()




class Topicmake(TemplateView):
    def get(self,request,*args,**kwargs):
        return render(request,'items/topicwrite.html',{'form':TopicForm})
    
    def post(self,request,*args,**kwargs):
        form = TopicForm(request.POST)
        post = form.save(commit=False)
        post.save()
        return redirect(to='items:index')
    
topicwrite = Topicmake.as_view()





class Login(LoginView):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'items/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'items/login.html', {'form': form,})

account_login = Login.as_view()





class Signup(CreateView):
    template_name = 'items/login.html'
    def post(self, request, *args, **kwargs):
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            name = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            passw = form.cleaned_data.get('password1')
            user = authenticate(username=name, password=passw)
            login(request, user)
            return redirect('items:login')
        return render(request, 'items/create.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        return  render(request, 'items/create.html', {'form': form,})
    
sign = Signup.as_view()





class Logout(LogoutView):
    template_name = 'items/login.html'
    
out = Logout.as_view()





class Search(TemplateView):
    def get(self,request,*args,**kwargs):
        return render(request,'items/search.html',{'form':TopicForm})
    
    def post(self,request,*args,**kwargs):
        form = TopicForm(request.POST)
        post = form.save(commit=False)
        param = str(post.title)
        return redirect('items:searchpost',param)
    
search = Search.as_view()





class Searchpost(TemplateView):
    def get(self,request,param,*args,**kwargs):
        param = str(param)
        queue = Topics.objects.filter(title__contains=param).order_by('-created')
        return render(request,'items/searchpost.html',{'topics':queue})
    
searchpost = Searchpost.as_view()