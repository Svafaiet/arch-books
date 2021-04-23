from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_roles(**kwargs):
    from .models import Tag
    for tag in Tag.DEFAULT_TAGS:
        if not Tag.objects.filter(name=tag).exists():
            tag = Tag.objects.create(name=tag)
            tag.save()
