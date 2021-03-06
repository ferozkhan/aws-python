
from decorators import *
from django.http import HttpResponse
import simplejson
import boto
import os
ec2 = boto.connect_ec2()


def get_ec2_state(request):
    return ec2_state(request)

@json_response
def ec2_state(request):
    state = {
        'running': len(ec2.get_all_instances(filters={'instance-state-name': 'running'})),
        'pending': len(ec2.get_all_instances(filters={'instance-state-name': 'pending'})),
        'shutting-down': len(ec2.get_all_instances(filters={'instance-state-name': 'shutting-down'})),
        'terminated': len(ec2.get_all_instances(filters={'instance-state-name': 'terminated'})),
        'stopping': len(ec2.get_all_instances(filters={'instance-state-name': 'stopping'})),
        'stopped': len(ec2.get_all_instances(filters={'instance-state-name': 'stopped'}))
    }

    return state