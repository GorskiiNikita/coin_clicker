from django.db.models import F
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import VkUsers


@api_view(['GET'])
def click(request):
    vk_user_id = request.session.get('vk_user_id')
    if vk_user_id:
        user = VkUsers.objects.get(vk_user_id=vk_user_id)
        user.count_clicks = F('count_clicks') + 1
        user.save(update_fields=["count_clicks"])
        return Response(status=200)

    return Response(status=403)
