from django.shortcuts import render
from blog.models import Post,About,Event,Membership,Contact
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)  #Anlagous to Index, Show, and Create on rails
from users.forms import AboutUsUpdateForm












# Create your views here.
def home(request):
    # context = {
    #     "posts": Post.objects.all()
    # }

    return render(request, 'blog/index.html')


class PostListView(ListView):
    model = Post 
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering=['-date_updated']


class PostDetailView(DetailView):
    model = Post 


class PostCreateView(LoginRequiredMixin, CreateView): #Order matters 
    model = Post 
    fields = ['title', 'content']

    # hur dur polymorpishm hurr
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # runs CreateView's version of from_valid


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False

        











def about(request):

    about_form = AboutUsUpdateForm(request.POST)


    return render(request, 'blog/about.html')



class AboutListView(ListView):
    model = About
    template_name = 'blog/about.html'
    context_object_name = 'abouts'
    ordering=['-date_updated']
    paginate_by = 1


class AboutDetailView(DetailView):
    model = About
 
class AboutCreateView(LoginRequiredMixin, CreateView): #Order matters 
    model = About
    fields = ['content']

    # hur dur polymorpishm hurr
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # runs CreateView's version of from_valid


class AboutUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = About 
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False


class AboutDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = About
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False







def membership(request):
    return render(request, 'blog/membership.html',)



class MembershipListView(ListView):
    model = Membership
    template_name = 'blog/membership.html'
    context_object_name = 'memberships'
    ordering=['-date_updated']
    paginate_by = 1


class MembershipDetailView(DetailView):
    model = Membership
 
class MembershipCreateView(LoginRequiredMixin, CreateView): #Order matters 
    model = Membership
    fields = ['title','content']

    # hur dur polymorpishm hurr
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # runs CreateView's version of from_valid


class MembershipUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Membership
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False


class MembershipDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Membership
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False





def events(request):
    #  context = {

    #     'events': Event.objects.all()
    # }
    return render(request, 'blog/events.html')


class EventListView(ListView):
    model = Event
    template_name = 'blog/events.html'
    context_object_name = 'events'
    ordering=['-date_updated']
    paginate_by = 1


class EventDetailView(DetailView):
    model = Event
 
class EventCreateView(LoginRequiredMixin, CreateView): #Order matters 
    model = Event
    fields = ['title','content']

    # hur dur polymorpishm hurr
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # runs CreateView's version of from_valid


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False








def portfolio(request):
    return render(request, 'blog/portfolio.html',)

def resources(request):
    return render(request, 'blog/resources.html',)

def mail(request):
    return render(request, 'blog/mail.html',)




def contact(request):
    return render(request, 'blog/contact-us.html',)



class ContactListView(ListView):
    model = Contact
    template_name = 'blog/contact-us.html'
    context_object_name = 'contacts'
    ordering=['-date_updated']
    paginate_by = 1


class ContactDetailView(DetailView):
    model = Contact
 
class ContactCreateView(LoginRequiredMixin, CreateView): #Order matters 
    model = Contact
    fields = ['title','content']

    # hur dur polymorpishm hurr
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # runs CreateView's version of from_valid


class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False


class ContactDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contact
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False







