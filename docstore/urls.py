from django.conf.urls import url
from . import views


app_name = 'docstore'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    url(r'docstore/(?P<pk>[0-9]+)/$',views.ArtifactUpdate.as_view(),name='artifact-update'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'docstore/add/$',views.ArtifactCreate.as_view(),name='artifact-add'),
    url(r'docstore/(?P<pk>[0-9]+)/delete/$',views.ArtifactDelete.as_view(),name='artifact-delete'),
]