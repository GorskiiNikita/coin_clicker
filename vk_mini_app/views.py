from django.http import HttpResponse
from django.shortcuts import render

from coin_clicker import settings
from vk_mini_app.utils import is_valid_sign

from api.models import VkUsers


def index(request):
    status = is_valid_sign(query=request.GET, secret=settings.CLIENT_SECRET)
    if status:
        request.session['vk_user_id'] = request.GET['vk_user_id']
        user, created = VkUsers.objects.get_or_create(vk_user_id=request.session.get('vk_user_id'))
        return render(request, 'vk_mini_app/index.html', {'count_clicks': user.count_clicks})

    return HttpResponse(status=403)

