from django.conf.urls import url, include
from . import views

app_name = 'network'

urlpatterns = [
    url('^castVote/(?P<candidateId>\w+)/$', views.castNewVote, name='castNewVote'),
    url('^api/', include('network.api.urls'), name='api'),

]