from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PageChooserPanel
from streams import blocks



class HomePage(Page):
    templates = "home/home_page.html"
    

    logo = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Restaurants_Near_Me_front= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Restaurants_Near_Me_back= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    International_Cuisines_Icon_front= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    International_Cuisines_Icon_back= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Fine_dining_front= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Fine_dining_back= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Casual_dining_front= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Casual_dining_back= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Fast_Food_front= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Fast_Food_back= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Favourite_Food_front= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Favourite_Food_back= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Healthy_Food_front= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Healthy_Food_back= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Child_Friendly_front= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Child_Friendly_back= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Cafés_Coffee_front= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Cafés_Coffee_back= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Todays_Specials_front= models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name="+"
    )
    Todays_Specials_back= models.ForeignKey(
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
            ("testimonials", blocks.testimonials()),
            ("contactform", blocks.contactform()),
            ("LegalSection", blocks.LegalSection()),
            ("whychooseus2", blocks.whychooseus2()),
            ("whatwebelieve", blocks.whatwebelieve()),
            ("whatweoffer", blocks.whatweoffer()),
            ("Whyshouldyouchooseus", blocks.Whyshouldyouchooseus()),
            ("videosection", blocks.videosection()),

            
        ],
        null = True,
        blank= True,
        use_json_field=True
    )
  
    IntCuisines = StreamField(
        [
            ("Inttiles", blocks.Inttiles()),
           
            
        ],
        null = True,
        blank = True,
        use_json_field=True
        
    )
    FastFoods = StreamField(
        [
            ("Fastfoods", blocks.Fastfoods()),
            
        ],
        null = True,
        blank = True,
        use_json_field=True
        
    )
    Favfoods = StreamField(
        [           
            ("Favfoods", blocks.Favfoods()),
                      
        ],
        null = True,
        blank = True,
        use_json_field=True
        
    )
    
    Restaurants_Near_Me_text = models.CharField(max_length= 250, blank = False, null = True)
    International_Cuisines_Icon_text = models.CharField(max_length= 250, blank = False, null = True)
    Fine_dining_text = models.CharField(max_length= 250, blank = False, null = True)
    Casual_dining_text = models.CharField(max_length= 250, blank = False, null = True)
    Fast_Food_text = models.CharField(max_length= 250, blank = False, null = True)
    Favourite_Food_text = models.CharField(max_length= 250, blank = False, null = True)
    Healthy_Food_text = models.CharField(max_length= 250, blank = False, null = True)
    Child_Friendly_text = models.CharField(max_length= 250, blank = False, null = True)
    Cafés_Coffee_text = models.CharField(max_length= 250, blank = False, null = True)
    Todays_Specials_text = models.CharField(max_length= 250, blank = False, null = True)
    
    banner_tittle = models.CharField(max_length= 250, blank = False, null = True)
    banner_sub_tittle = models.CharField(max_length= 250, blank = False, null = True)
    header_address = models.CharField(max_length= 250, blank = False, null = True)
    support = models.CharField(max_length= 250, blank = False, null = True)

   
    
    

    content_panels = Page.content_panels +  [

        MultiFieldPanel(
            [
                FieldPanel('header_address'),
                FieldPanel('support'),
            ],
            heading="header optons",
        ),
        MultiFieldPanel(
            [
               FieldPanel('banner_tittle'),
               FieldPanel('banner_sub_tittle'),
               FieldPanel('banner_image'),
               FieldPanel('logo'),
               
            ],
            heading="Banner Options",
        ),     
        MultiFieldPanel(
            [
               FieldPanel('Restaurants_Near_Me_text'),
               FieldPanel('Restaurants_Near_Me_front'),
               FieldPanel('Restaurants_Near_Me_back'),
                              
            ],
            heading="Restaurants Near Me",
        ),     
        MultiFieldPanel(
            [
               FieldPanel('International_Cuisines_Icon_text'),
               FieldPanel('International_Cuisines_Icon_front'),
               FieldPanel('International_Cuisines_Icon_back'),
                              
            ],
            heading="International Cuisines",
        ),     
        MultiFieldPanel(
            [
               FieldPanel('Fine_dining_text'),
               FieldPanel('Fine_dining_front'),
               FieldPanel('Fine_dining_back'),
                              
            ],
            heading="Fine_dining",
        ),     
        MultiFieldPanel(
            [
               FieldPanel('Casual_dining_text'),
               FieldPanel('Casual_dining_front'),
               FieldPanel('Casual_dining_back'),
                              
            ],
            heading="Casual_dining",
        ),     
        MultiFieldPanel(
            [
               FieldPanel('Fast_Food_text'),
               FieldPanel('Fast_Food_front'),
               FieldPanel('Fast_Food_back'),
                              
            ],
            heading="Fast Food",
        ),     
        MultiFieldPanel(
            [
               FieldPanel('Favourite_Food_text'),
               FieldPanel('Favourite_Food_front'),
               FieldPanel('Favourite_Food_back'),
                              
            ],
            heading="Favourite Foods",
        ),     
        MultiFieldPanel(
            [
               FieldPanel('Healthy_Food_text'),
               FieldPanel('Healthy_Food_front'),
               FieldPanel('Healthy_Food_back'),
                              
            ],
            heading="Healthy Foods",
        ),     
        MultiFieldPanel(
            [
               FieldPanel('Child_Friendly_text'),
               FieldPanel('Child_Friendly_front'),
               FieldPanel('Child_Friendly_back'),
                              
            ],
            heading="Child Friendly",
        ),     
        MultiFieldPanel(
            [
               FieldPanel('Cafés_Coffee_text'),
               FieldPanel('Cafés_Coffee_front'),
               FieldPanel('Cafés_Coffee_back'),
                              
            ],
            heading="Cafés & Coffee",
        ),     
        MultiFieldPanel(
            [
               FieldPanel('Todays_Specials_text'),
               FieldPanel('Todays_Specials_front'),
               FieldPanel('Todays_Specials_back'),
                              
            ],
            heading="Todays Specials",
        ),     
           
        FieldPanel('content'),
        FieldPanel('IntCuisines'),
        FieldPanel('FastFoods'),
        FieldPanel('Favfoods'),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

