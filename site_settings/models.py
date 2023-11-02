from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)

# Create your models here.
@register_setting

class Socialmediasettings(BaseSiteSetting):
    """Socila media settings are managed from here"""
    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    instagram = models.URLField(blank=True, null=True, help_text=" Instagram URL")
    youtube = models.URLField(blank=True, null=True, help_text="Youtube channel URL")
    linkedin = models.URLField(blank=True, null=True, help_text="Youtube channel URL")
    googleplus = models.URLField(blank=True, null=True, help_text="Youtube channel URL")
    

    panels = [ 
        
        MultiFieldPanel([

        FieldPanel("facebook"),
        FieldPanel("twitter"),
        FieldPanel("instagram"),
        FieldPanel("youtube"),
        FieldPanel("linkedin"),
        FieldPanel("googleplus"),

    ], heading = "Social Media Links")
    ]