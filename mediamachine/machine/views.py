# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list, object_detail


@login_required
def limited_direct_to_template(*args, **kwargs):
    return direct_to_template(*args, **kwargs)


@login_required
def limited_object_list(*args, **kwargs):
    return object_list(*args, **kwargs)


@login_required
def limited_object_detail(*args, **kwargs):
    return object_detail(*args, **kwargs)
