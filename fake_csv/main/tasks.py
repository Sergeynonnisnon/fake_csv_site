from celery import shared_task
from .models import Schema, Sets
from .generate_fakecsv import gen_csv



@shared_task
def create_csv(params):

    return params