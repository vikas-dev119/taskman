from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from activities.models import Activity


class Index(TemplateView):
    def get(self, request):
        user_id = request.session.get('userauth', {}).get('user_id')
        activities = Activity.objects.filter(user_id=user_id).order_by('-created_on')
        return render(request, 'activities/index.html', {'activities': activities} )
