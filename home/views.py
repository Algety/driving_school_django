from django.views.generic import ListView
from .models import ContentBlock

class ContentBlockList(ListView):
    queryset = ContentBlock.objects.filter(publish=True, section="services")
    template_name = "home/home.html"
    context_object_name  = "content_blocks_list"


class TeamBlockList(ListView):
    queryset = ContentBlock.objects.filter(publish=True, section="instructors")
    template_name = "home/team.html"
    context_object_name  = "content_blocks_list"
