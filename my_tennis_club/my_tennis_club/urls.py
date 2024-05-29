
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from members import views as members_views
from django.views.generic import TemplateView # type: ignore
from members.views import contact_view
from members.views import contact_success_view

urlpatterns = [
    path('', TemplateView.as_view(template_name='homepage.html'), name='homepage.html'),
    path('members/allmembers', members_views.allmembers, name='allmembers.html'),
    path('members/details/<int:id>', members_views.details, name='details.html'),
    path('members/', members_views.members, name='members.html'),
    path('admin/', admin.site.urls),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success_view, name='contact_success'),
    
]
