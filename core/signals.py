from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from core.models import *
from posts.models import Post

# @receiver(post_save, sender=Answer)
# def post_point(sender, instance=None, created=False, **kwargs):
#     if created:
#         print('oiiiiiiiiiiiiiiiiiiii')
#         # points = StudentPoint.objects.filter(point=1)
#         # all_point = points.count()
#         instance.student.total += 1
#         instance.student.save()

# # post_save.connect(post_point, StudentPoint)
