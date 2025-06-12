from django.db import models
from django_summernote.fields import SummernoteTextField
from cloudinary.models import CloudinaryField

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
    block_image = CloudinaryField('image', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)  # New field for sorting


    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} ({self.get_section_display()})"