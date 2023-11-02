"""Flexible page."""
from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PageChooserPanel
from streams import blocks


class FlexPage(Page):
    """Flexibile page class."""

    template = "flex/flex.html"


    logo = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    
   

    BannerTitle = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length= 250, blank = False, null = True)
    support = models.CharField(max_length= 250, blank = False, null = True)
    email = models.CharField(max_length= 550, blank = False, null = True)
    para_under_logo = models.CharField(max_length= 550, blank = False, null = True)
    footer_column_two = models.CharField(max_length=250, blank = True, null = True)
    footer_column_three = models.CharField(max_length=250, blank = True, null = True)
    
    bannerimage = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    
    content = StreamField(
        [
            ("title_and_text", blocks.titleandtext()),
            ("Rich_text_editor", blocks.Rich_Text_Block()),
            ("Info_block", blocks.info_block()),
            ("Cardblock", blocks.CardBlock()),
            ("About_block", blocks.about_block()),
            ("About_block_2", blocks.about_block_2()),
            ("About_block_3", blocks.about_block_3()),
            ("About_block_4", blocks.about_block_4()),
            ("Accordion_Block", blocks.AccordionBlock()),
            ("Simple_Horizontal_Divider", blocks.Simple_Horizontal_Divider()),
            ("Tabs1Block", blocks.Tabs1Block()),
            ("ImageSliderBlock", blocks.ImageSliderBlock()),
            ("info_block1", blocks.info_block1()),
            ("FeaturesElementBlock2", blocks.FeaturesElementBlock2()),
            ("FeaturesElementBlock3", blocks.FeaturesElementBlock3()),
            ("news_1", blocks.news_1()),
            ("VideoGallery", blocks.VideoGallery()),
            ("ImageGallery", blocks.ImageGallery()),
            ("Videosin2column", blocks.Videosin2column()),
            ("contact", blocks.contact()),
            ("ImageGallery3", blocks.ImageGallery3()),
             ("textblock2", blocks.textblock2()),
            ("ImagesliderGallery", blocks.ImagesliderGallery()),
            ("Video_Intro", blocks.Video_Intro()),
            ("map", blocks.map()),
            ("funfact", blocks.funfact()),
            ("Team", blocks.Team()),
            ("GetInTouch", blocks.GetInTouch()),
            ("Pricing", blocks.Pricing()),
            ("HeadingPara", blocks.HeadingPara()),
            ("testimonials", blocks.testimonials()),
            ("contactform", blocks.contactform()),
            ("LegalSection", blocks.LegalSection()),
            ("whychooseus2", blocks.whychooseus2()),
            ("whatweoffer", blocks.whatweoffer()),
            ("whatwebelieve", blocks.whatwebelieve()),
            ("Whyshouldyouchooseus", blocks.Whyshouldyouchooseus()),
            ("videosection", blocks.videosection()),
            
             
            
        ],
        null = True,
        blank= True,
        use_json_field=True
    )
    
    

    content_panels = Page.content_panels + [
      
           
        MultiFieldPanel(
            [
               FieldPanel('BannerTitle'),
               FieldPanel('address'),
               FieldPanel('support'),
               FieldPanel('email'),
               FieldPanel('bannerimage'),
               FieldPanel('logo'),
               
            ],
            heading="Page Headings and Info",
        ), 
        MultiFieldPanel(
            [
               FieldPanel('para_under_logo'),
               FieldPanel('footer_column_two'),
               FieldPanel('footer_column_three'),
               
            ],
            heading="Footer",
               
        ), 
    
        FieldPanel('content'),
    
     ] 

    class Meta:  # noqa 
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"

