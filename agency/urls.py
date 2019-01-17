from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^accounts/signup/$',views.SignUpView, name='signup'),
    url(r'^model/',views.model, name='model'),
    url(r'^casting/',views.casting, name='casting'),
    url(r'^new/casting$', views.new_casting, name='new-casting'),
    url(r'^new/model$', views.new_model, name='new-model'),
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)