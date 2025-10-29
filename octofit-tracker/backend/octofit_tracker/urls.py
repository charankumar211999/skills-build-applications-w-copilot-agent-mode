"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from pymongo import MongoClient

def get_db():
    client = MongoClient(host='localhost', port=27017)
    return client['octofit_db']

def api_response(collection):
    db = get_db()
    docs = list(db[collection].find({}, {'_id': 0}))
    return JsonResponse(docs, safe=False)

codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
base_url = f'https://{codespace_name}-8000.app.github.dev/api/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/activities/', lambda request: api_response('activities')),
    path('api/users/', lambda request: api_response('users')),
    path('api/teams/', lambda request: api_response('teams')),
    path('api/leaderboard/', lambda request: api_response('leaderboard')),
    path('api/workouts/', lambda request: api_response('workouts')),
]
