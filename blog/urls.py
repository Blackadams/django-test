from django.urls import path
from .views import (PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,   AboutListView,AboutDetailView,AboutCreateView,AboutUpdateView,AboutDeleteView,   MembershipListView,MembershipDetailView,MembershipUpdateView,MembershipDeleteView,MembershipCreateView,   EventListView,EventDetailView,EventCreateView,EventUpdateView,EventDeleteView,    ContactListView,ContactDetailView,ContactCreateView,ContactUpdateView,ContactDeleteView,)

from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='blog-post'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='blog-post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='blog-post-delete'),
    path('post/new/', PostCreateView.as_view(), name='blog-post-create'),



    path('about/', AboutListView.as_view(), name='blog-about'),
    path('about/<int:pk>', AboutDetailView.as_view(), name='blog-about'),
    path('about/<int:pk>/update', AboutUpdateView.as_view(), name='blog-about-update'),
    path('about/<int:pk>/delete', AboutDeleteView.as_view(), name='blog-about-delete'),
    path('about/new/', AboutCreateView.as_view(), name='blog-about-create'),

    path('events/', EventListView.as_view(), name='blog-events'),
    path('events/<int:pk>', EventDetailView.as_view(), name='blog-events'),
    path('events/<int:pk>/update', EventUpdateView.as_view(), name='blog-events-update'),
    path('events/<int:pk>/delete', EventDeleteView.as_view(), name='blog-events-delete'),
    path('events/new/', EventCreateView.as_view(), name='blog-events-create'),


    path('contact/', ContactListView.as_view(), name='blog-contact'),
    path('contact/<int:pk>', ContactDetailView.as_view(), name='blog-contact'),
    path('contact/<int:pk>/update', ContactUpdateView.as_view(), name='blog-contact-update'),
    path('contact/<int:pk>/delete', ContactDeleteView.as_view(), name='blog-contact-delete'),
    path('contact/new/', ContactCreateView.as_view(), name='blog-contact-create'),



    path('membership/', MembershipListView.as_view(), name='blog-membership'),
    path('membership/<int:pk>', MembershipDetailView.as_view(), name='blog-membership'),
    path('membership/<int:pk>/update', MembershipUpdateView.as_view(), name='blog-membership-update'),
    path('membership/<int:pk>/delete', MembershipDeleteView.as_view(), name='blog-membership-delete'),
    path('membership/new/', MembershipCreateView.as_view(), name='blog-membership-create'),




    # path('membership/', views.membership, name='blog-membership'),
    path('mail/', views.mail, name='blog-mail'),
    # path('contact-us/', views.contact, name='blog-contact'),
    
] 

