from django.db import models


class VkUsers(models.Model):
    vk_user_id = models.BigIntegerField(primary_key=True)
    count_clicks = models.IntegerField(default=0)
