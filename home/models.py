from django.db import models
from django_summernote.fields import SummernoteTextField

SECTION = [
        ("instructors", "Our Team"),
        ("services", "Services"),
        ("prices", "Prices"),
    ]
class ContentBlock(models.Model):
    title = models.CharField(max_length=255)
    # image = models.ImageField(upload_to="infoblocks/")
    content = models.TextField()
    # content = SummernoteTextField()
    section = models.CharField(max_length=20, choices=SECTION, default="services")
    publish = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.get_section_display()})"