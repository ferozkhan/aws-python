
import os
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^ec2_state/$', 'aws.app.views.get_ec2_state'),
)
