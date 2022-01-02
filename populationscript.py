import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mydjangoproject.settings')

import django
django.setup()


import random
from mydjangoapp.models import Accesspage,Webpage,Topic
from faker import Faker

fak = Faker()

topc = ['sports', 'games', 'networking', 'social', 'news', 'food']

def addtopic():
    t = Topic.objects.get_or_create(top_name = random.choice(topc))[0]
    t.save()
    return t

def createntry(N=5):
    for i in range(N):
        top = addtopic()

        fake_name= fak.company()
        fake_url = fak.url()
        fake_date = fak.date()

        #creating the webpage
        webpg = Webpage.objects.get_or_create(topic=top, name = fake_name, url = fake_url)[0]

        #creating the acc_red
        acc_red = Accesspage.objects.get_or_create(name = webpg, date= fake_date)[0]

if __name__ == '__main__':
    print("starting to populate!")
    createntry(10)
    print("populated successfully!!")

