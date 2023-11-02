"""Stream fields are created here"""

# from django.forms import Input
from wagtail import blocks
from wagtail.fields import RichTextField
from wagtail.images.blocks import ImageChooserBlock
from django.db import models
from wagtail.embeds.blocks import EmbedBlock

class titleandtext(blocks.StructBlock):
    title = blocks.CharBlock(required = True, help_text = "Add title here")
    text = blocks.CharBlock(required = True, help_text = "Add title here")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title&Text"

class info_block(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock(required = True, help_text = "Add title here")
    text = blocks.CharBlock(required = True, help_text = "Add title here")
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=40)

    class Meta:
        template = "streams/info_block.html"
        icon = "edit"
        label = "Info Block"

class about_block(blocks.StructBlock):
    image = ImageChooserBlock(required=False, help_text = "Best size 500 x 470 pixels ")
    video = blocks.URLBlock(required=False, help_text = "Enter youtube video link here ")    
    title1_small = blocks.CharBlock(required = True, help_text = "Add title here")
    title2_bold = blocks.CharBlock(required = True, help_text = "Add Big Bold title here")
    text = blocks.RichTextBlock(required = True, help_text = "Add main para here")
    icon1 = blocks.CharBlock(required = False, help_text = "Add flaticon class here")
    sub_title_1 = blocks.CharBlock(required = True, help_text = "Add sub title 1 here")
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    sub_title_text_1 = blocks.RichTextBlock(required = True, help_text = "Add text under sub title 1 here") 
    icon2 = blocks.CharBlock(required = False, help_text = "Add flaticon class here")  
    sub_title_2 = blocks.CharBlock(required = True, help_text = "Add sub title 2 here") 
    button_page_1= blocks.PageChooserBlock(required=False)
    button_url_1 = blocks.URLBlock(required=False)
    sub_title_text_2 = blocks.RichTextBlock(required = True, help_text = "Add text under sub title 2 here")
    
    class Meta:
        template = "streams/about_block.html"
        icon = "placeholder"
        label = "About Block1"
        
        
class contact(blocks.StructBlock):
    
    custom_title = blocks.CharBlock(required = False, help_text = "Add title here")
    Main_Heading = blocks.CharBlock(required = True, help_text = "Add title text here")
    Address1 = blocks.CharBlock(required = False, help_text = "Building, Street, City")   
    Address2 = blocks.CharBlock(required = False, help_text = "State, PIN, Country")   
    Phone1 = blocks.IntegerBlock(required = False, help_text = "Any Phone number")    
    Phone2 = blocks.IntegerBlock(required = False, help_text = "Any Phone number")    
    Email1 = blocks.EmailBlock(required = False, help_text = "Any email id for contact")     
    Email2 = blocks.EmailBlock(required = False, help_text = "Any email id for contact")     
    image = ImageChooserBlock(required=False, help_text = "Best size 1900 x 500 pixels ")
   
    
    
    
    class Meta:
        template = "streams/contactus.html"
        icon = "placeholder"
        label = "Contact"
        

class textblock2(blocks.StructBlock):
    
    title = blocks.CharBlock(required = False, help_text = "Add title here")
    text = blocks.RichTextBlock(required = True, help_text = "Add title text here")
    page_url= blocks.URLBlock(required=False, help_text="Copy and Paste the page URL here")
   
    class Meta:
        template = "streams/textblock2.html"
        icon = "placeholder"
        label = "textblock2"        
        
class ImageGallery3(blocks.StructBlock):   
    
    Block_title = blocks.CharBlock(required = False, help_text = "Add section title here")  
    title1 = blocks.CharBlock(required = False, help_text = "Add section title here")
    title2 = blocks.CharBlock(required = False, help_text = "Add section title here")
    title3 = blocks.CharBlock(required = False, help_text = "Add section title here")
    title4 = blocks.CharBlock(required = False, help_text = "Add section title here")
    title5 = blocks.CharBlock(required = False, help_text = "Add section title here")
    title5 = blocks.CharBlock(required = False, help_text = "Add section title here")
    
          
    gallery = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("gallerytitle", blocks.CharBlock(required=False, help_text="Add title here")),
                ("Description", blocks.CharBlock(required=False, help_text="Add image description here")),
                ("image",  ImageChooserBlock(required=True)),
                ("page_url", blocks.URLBlock(required=False, help_text="Copy and Paste the page URL here")),
                
                
                
            ]
        )
    )  
       
    
    class Meta:
        template = "streams/imagegallery3.html"
        icon = "placeholder"
        label = "ImageGallery3"
        
class ImagesliderGallery(blocks.StructBlock):   
    
    smallheading = blocks.CharBlock(required = False, help_text = "Add small section title here")  
    biglheading = blocks.CharBlock(required = False, help_text = "Add bold section title here")  
          
    images = blocks.ListBlock(
        blocks.StructBlock(
            [
                
                ("image",  ImageChooserBlock(required=True)),
               
                
                
            ]
        )
    )  
       
    
    class Meta:
        template = "streams/imagegallery2.html"
        icon = "placeholder"
        label = "ImagesliderGallery"


class about_block_2(blocks.StructBlock):
    
    title1_small = blocks.CharBlock(required = False, help_text = "Add title here")
    title2_bold = blocks.CharBlock(required = True, help_text = "Add gig title text here")
    text = blocks.RichTextBlock(required = False, help_text = "Add para here")
    icon1 = blocks.CharBlock(required = False, help_text = "Add flaticon class here")
    sub_title_1 = blocks.CharBlock(required = False, help_text = "Add title here")
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    sub_title_text_1 = blocks.RichTextBlock(required = False, help_text = "Add pare here")  
    icon2 = blocks.CharBlock(required = False, help_text = "Add flaticon class here") 
    sub_title_2 = blocks.CharBlock(required = False, help_text = "Add title here") 
    button_page_2= blocks.PageChooserBlock(required=False)
    button_url_2 = blocks.URLBlock(required=False)
    sub_title_text_2 = blocks.RichTextBlock(required = False, help_text = "Add para here")
    icon3 = blocks.CharBlock(required = False, help_text = "Add flaticon class here" )
    sub_title_3= blocks.CharBlock(required = False, help_text = "Add title here") 
    button_page_3= blocks.PageChooserBlock(required=False)
    button_url_3 = blocks.URLBlock(required=False)
    sub_title_text_3 = blocks.RichTextBlock(required = False, help_text = "Add para here")
    icon4 = blocks.CharBlock(required = False, help_text = "Add flaticon class here")
    sub_title_4 = blocks.CharBlock(required = False, help_text = "Add title here") 
    button_page_4= blocks.PageChooserBlock(required=False)
    button_url_4 = blocks.URLBlock(required=False)
    sub_title_text_4 = blocks.RichTextBlock(required = False, help_text = "Add para here")
    icon5 = blocks.CharBlock(required = False, help_text = "Add flaticon class here")
    imagebox_heading = blocks.CharBlock(required = False, help_text= "Add headign for box over image here")
    imagebox_text = blocks.CharBlock(required = False, help_text = "Add text for box over image here")
    image = ImageChooserBlock(required=False, help_text = "Best size 460 x 455 pixels ")
    
    class Meta:
        template = "streams/about-block-2.html"
        icon = "placeholder"
        label = "About Block2"
        
class about_block_3(blocks.StructBlock):
    
    title1_small = blocks.CharBlock(required = False, help_text = "Add title here")
    title2_bold = blocks.CharBlock(required = True, help_text = "Add gig title text here")
    text = blocks.RichTextBlock(required = False, help_text = "Add para here")   
    sub_title_1 = blocks.CharBlock(required = False, help_text = "Add title here")    
    sub_title_1_text = blocks.RichTextBlock(required = False, help_text = "Add pare here")     
    image = ImageChooserBlock(required=False, help_text = "Best size 460 x 455 pixels ")
    iframe_youtube = blocks.URLBlock(required = False, help_text = "Add code here")    
    
    
    
    class Meta:
        template = "streams/about-block-3.html"
        icon = "placeholder"
        label = "About Block3"
        
class Video_Intro(blocks.StructBlock):
    
    Tab1 = blocks.CharBlock(required = False, help_text = "Add title here")
    Heading_tab1 = blocks.CharBlock(required = True, help_text = "Add Heading for this tab here")
    Paragraph_tab1 = blocks.RichTextBlock(required = False, help_text = "Add para here")
    Bulletone_tab1 = blocks.CharBlock(required = True, help_text = "Add bullet sentence here")
    Bullettwo_tab1 = blocks.CharBlock(required = True, help_text = "Add bullet sentence here")
    Bulletthree_tab1 = blocks.CharBlock(required = True, help_text = "Add bullet sentence here")
    Bulletfour_tab1 = blocks.CharBlock(required = True, help_text = "Add bullet sentence here")
    
    Tab2 = blocks.CharBlock(required = False, help_text = "Add title here")
    Heading_tab2 = blocks.CharBlock(required = True, help_text = "Add Heading for this tab here")
    Paragraph_tab2 = blocks.RichTextBlock(required = False, help_text = "Add para here")
    Bulletone_tab2 = blocks.CharBlock(required = True, help_text = "Add bullet sentence here")
    Bullettwo_tab2 = blocks.CharBlock(required = True, help_text = "Add bullet sentence here")
    Bulletthree_tab2 = blocks.CharBlock(required = True, help_text = "Add bullet sentence here")
    Bulletfour_tab2 = blocks.CharBlock(required = True, help_text = "Add bullet sentence here")
    
    Tab3 = blocks.CharBlock(required = False, help_text = "Add title here")
    Heading_tab3 = blocks.CharBlock(required = True, help_text = "Add Heading for this tab here")
    Paragraph_tab3 = blocks.RichTextBlock(required = False, help_text = "Add para here")
    Bulletone_tab3 = blocks.CharBlock(required = True, help_text = "Add bullet sentence here")
    Bullettwo_tab3 = blocks.CharBlock(required = True, help_text = "Add bullet sentence here")
    Bulletthree_tab3 = blocks.CharBlock(required = True, help_text = "Add bullet sentence here")
    Bulletfour_tab3 = blocks.CharBlock(required = True, help_text = "Add bullet sentence here")
        
    video_url = blocks.URLBlock(required=False)
    
    image_left = ImageChooserBlock(required=False, help_text = "Best size 460 x 455 pixels ")
    
    class Meta:
        template = "streams/Video_Intro.html"
        icon = "placeholder"
        label = "VideoIntro"     

class map(blocks.StructBlock):
    Small_Heading = blocks.CharBlock(required = True, help_text = "Add small heading on top here")
    Bold_Heading = blocks.CharBlock(required = True, help_text = "Add Bold Heading just below small heading here")
    
    Locations = blocks.ListBlock(
        blocks.StructBlock(

            [                
                ("location_name", blocks.CharBlock(required=False, max_length=150)),
                ("text", blocks.CharBlock(required=False, max_length=400)),
                                
            ]
        )
    )  

    class Meta:
        template = "streams/map.html"
        icon = "placeholder"
        label = "Map"  
        
class Team(blocks.StructBlock):
    Small_Heading = blocks.CharBlock(required = True, help_text = "Add small heading on top here")
    Bold_Heading = blocks.CharBlock(required = True, help_text = "Add Bold Heading just below small heading here")
    Paragraph = blocks.RichTextBlock(required = False, help_text = "Add para here")
    
    members = blocks.ListBlock(
        blocks.StructBlock(
            [                
                ("Pic", ImageChooserBlock(required=True)),
                ("Name", blocks.CharBlock(required=True, max_length=150)),
                ("Designation", blocks.CharBlock(required=True, max_length=150)),
                ("FB_Profile", blocks.URLBlock(required=True, max_length=650, help_text = "Copy and Paste FB Profile link here")),
                ("Twitter_Profile", blocks.URLBlock(required=True, max_length=650, help_text = "Copy and Paste Twitter Profile link here")),
                ("Instagram_Profile", blocks.URLBlock(required=True, max_length=650, help_text = "Copy and Paste Instagram Profile link here")),
                ("LinkedIn_Profile", blocks.URLBlock(required=True, max_length=650, help_text = "Copy and Paste LinkedIn Profile link here")),
                
                                
            ]
        )
    )  

    class Meta:
        template = "streams/team.html"
        icon = "placeholder"
        label = "Team"  
        
        
class HeadingPara(blocks.StructBlock):
    Small_Heading = blocks.CharBlock(required = False, help_text = "Add small heading on top here")
    Bold_Heading = blocks.CharBlock(required = True, help_text = "Add Bold Heading just below small heading here")
    Paragraph = blocks.RichTextBlock(required = False, help_text = "Add para here")
    
    

    class Meta:
        template = "streams/Heading&Para.html"
        icon = "edit"
        label = "Heading & Para Section"  
        
        
class Pricing(blocks.StructBlock):
    Plan1= blocks.CharBlock(required = True, help_text = "Add plan name here")
    Recommended_Plan1 = blocks.CharBlock(required = False, help_text = "Optional: Type 'Recoomended' if this is a recommended plan")
    Price_Plan1 = blocks.IntegerBlock(required = True, help_text = "Enter Price here")
    Detail_Plan1= blocks.CharBlock(required =False, help_text="Enter unique plan feature in one line") 
      
    features_Plan1 = blocks.ListBlock(
        blocks.StructBlock(
            [                
                
                ("Feature", blocks.CharBlock(required=True, max_length=250)),
               
                                
            ]
        )
    )  
    
    Plan2= blocks.CharBlock(required = True, help_text = "Add plan name here")
    Recommended_Plan2 = blocks.CharBlock(required = False, help_text = "Optional: Type 'Recoomended' if this is a recommended plan")
    Price_Plan2 = blocks.IntegerBlock(required = True, help_text = "Enter Price here")
    Detail_Plan2 = blocks.CharBlock(required =False, help_text="Enter unique plan feature in one line") 
      
    features_Plan2 = blocks.ListBlock(
        blocks.StructBlock(
            [                
                
                ("Feature", blocks.CharBlock(required=True, max_length=250)),
               
                                
            ]
        )
    )  
    Plan3= blocks.CharBlock(required = True, help_text = "Add plan name here")
    Recommended_Plan3= blocks.CharBlock(required = False, help_text = "Optional: Type 'Recoomended' if this is a recommended plan")
    Price_Plan3 = blocks.IntegerBlock(required = True, help_text = "Enter Price here")
    Detail_Plan3 = blocks.CharBlock(required =False, help_text="Enter unique plan feature in one line") 
      
    features_Plan3 = blocks.ListBlock(
        blocks.StructBlock(
            [                
                
                ("Feature", blocks.CharBlock(required=True, max_length=250)),
               
                                
            ]
        )
    )  

    class Meta:
        template = "streams/Pricing.html"
        icon = "edit"
        label = "Pricing Plans"  
        
class funfact(blocks.StructBlock):
    Heading1 = blocks.CharBlock(required = True, help_text = "Add heading on here")
    Data_stop1 = blocks.IntegerBlock(required = True, help_text = "Add the number on which the counter will stop")
    Heading2 = blocks.CharBlock(required = True, help_text = "Add heading on here")
    Data_stop2 = blocks.IntegerBlock(required = True, help_text = "Add the number on which the counter will stop")
    Heading3 = blocks.CharBlock(required = True, help_text = "Add heading on here")
    Data_stop3 = blocks.IntegerBlock(required = True, help_text = "Add the number on which the counter will stop")
    Heading4 = blocks.CharBlock(required = True, help_text = "Add heading on here")
    Data_stop4 = blocks.IntegerBlock(required = True, help_text = "Add the number on which the counter will stop")
    
    class Meta:
        template = "streams/fun-fact.html"
        icon = "placeholder"
        label = "FunFact"  
        
class Videosin2column(blocks.StructBlock):    
    
    title1_bold = blocks.CharBlock(required = True, help_text = "Add  title text here")
    video_url1 = blocks.URLBlock(required=True, help_text="Copy and Paste the Video URL here")
    title2_bold = blocks.CharBlock(required = True, help_text = "Add title text here")
    video_url2 = blocks.URLBlock(required=True, help_text="Copy and Paste the Video URL here")
    
    
    
    class Meta:
        template = "streams/Videosin2column.html"
        icon = "placeholder"
        label = "Videosin2column"
        
class videosection(blocks.StructBlock):    
    
    title = blocks.CharBlock(required = False, help_text = "Add  title text here")
    video_url = blocks.URLBlock(required=False, help_text="Copy and Paste the Video URL here")
    image = ImageChooserBlock(required=False, help_text = "Add background image 1900 X 800 ")
    
    
    
    class Meta:
        template = "streams/videosection.html"
        icon = "placeholder"
        label = "Video Section"
        
class GetInTouch(blocks.StructBlock):    
    
    MainHeading = blocks.CharBlock(required = False, help_text = "Add  title text here")
    SubHeading = blocks.RichTextBlock(required = False, help_text = "Add text under manin heading here")
    ButtonText = blocks.CharBlock(required = False, help_text = "Add  button text here")
     
    
    class Meta:
        template = "streams/Getintouch.html"
        icon = "placeholder"
        label = "GetInTouch"
        
class news_1(blocks.StructBlock):   
    
    section_title = blocks.CharBlock(required = False, help_text = "Add section title here") 
          
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.CharBlock(required=True, max_length=400)),
                ("button_text", blocks.CharBlock(required=False, help_text="Enter button text here")),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
                
            ]
        )
    )  
       
    
    class Meta:
        template = "streams/news-element-2.html"
        icon = "placeholder"
        label = "News"
        
class VideoGallery(blocks.StructBlock):   
    
    Block_title = blocks.CharBlock(required = False, help_text = "Add section title here")     
    firstvideo  = blocks.URLBlock(required=True, help_text="Copy and Paste the Video URL here")
          
    videos = blocks.ListBlock(
        blocks.StructBlock(
            [
                
                ("video_url", blocks.URLBlock(required=True, help_text="Copy and Paste the Video URL here")),
                ("imagecode", blocks.CharBlock(required=False, help_text="Add image code from the youtube video url")),
                ("description", blocks.CharBlock(required=False, help_text="Add video description here")),
                
            ]
        )
    )  
       
    
    class Meta:
        template = "streams/VideoGallery.html"
        icon = "placeholder"
        label = "VideoGallery"
        
class ImageGallery(blocks.StructBlock):   
    
    Block_title = blocks.CharBlock(required = False, help_text = "Add section title here") 
    description = blocks.CharBlock(required = False, help_text = "Add section description here") 
          
    images = blocks.ListBlock(
        blocks.StructBlock(
            [
                
                ("Upload_Image",ImageChooserBlock(required=True)),
                
            ]
        )
    )  
       
    
    class Meta:
        template = "streams/ImageGallery.html"
        icon = "placeholder"
        label = "ImageGallery"
        
    
        
class about_block_4(blocks.StructBlock):
    
    title1_small = blocks.CharBlock(required = False, help_text = "Add title here")
    title2_bold = blocks.CharBlock(required = False, help_text = "Add gig title text here")
    text = blocks.RichTextBlock(required = False, help_text = "Add para here")   
    sub_title_1 = blocks.CharBlock(required = False, help_text = "Add title here")    
    percent1 = blocks.CharBlock(required = False, help_text = "Add % here")     
    sub_title_2 = blocks.CharBlock(required = False, help_text = "Add title here")    
    percent2 = blocks.CharBlock(required = False, help_text = "Add % here")     
    sub_title_3 = blocks.CharBlock(required = False, help_text = "Add title here")    
    percent3 = blocks.CharBlock(required = False, help_text = "Add % here")     
    sub_title_4 = blocks.CharBlock(required = False, help_text = "Add title here")    
    percent4 = blocks.CharBlock(required = False, help_text = "Add % here")     
    image = ImageChooserBlock(required=False, help_text = "Best size 500 x 530 pixels ")
    
    class Meta:
        template = "streams/about-block-4.html"
        icon = "placeholder"
        label = "Why Choose Us 1"
        
class Whyshouldyouchooseus(blocks.StructBlock):
        
    title1_small = blocks.CharBlock(required = False, help_text = "Add title here")
    title2_bold = blocks.CharBlock(required = False, help_text = "Add  title text here")
    text = blocks.RichTextBlock(required = False, help_text = "Add para here")   
    
    tab_1 = blocks.CharBlock(required = False, help_text = "Add title here")    
    tab1_text = blocks.RichTextBlock(required = False, help_text = "Add para here")   
    tab1_readmore_pagelink= blocks.URLBlock(required = False, help_text = "Add page link here")     
    
    tab_2 = blocks.CharBlock(required = False, help_text = "Add title here")    
    tab2_text = blocks.RichTextBlock(required = False, help_text = "Add para here")   
    tab2_readmore_pagelink= blocks.URLBlock(required = False, help_text = "Add page link here")     
    
    tab_3 = blocks.CharBlock(required = False, help_text = "Add title here")    
    tab3_text = blocks.RichTextBlock(required = False, help_text = "Add para here")   
    tab3_readmore_pagelink= blocks.URLBlock(required = False, help_text = "Add page link here")     
    
    image = ImageChooserBlock(required=False, help_text = "Best size 500 x 530 pixels ")
    
    class Meta:
        template = "streams/WhyYouShdChsUs.html"
        icon = "placeholder"
        label = "Why You Should Choose Us"
        
class whatwebelieve(blocks.StructBlock):
    
       
    title1_small = blocks.CharBlock(required = False, help_text = "Add title here")
    title2_bold = blocks.CharBlock(required = False, help_text = "Add gig title text here")
    text = blocks.RichTextBlock(required = False, help_text = "Add para here") 
    LearMorePage= blocks.URLBlock(required=False, help_text="Copy and Paste the page URL here")  
    image = ImageChooserBlock(required=False, help_text = "Best size 500 x 530 pixels ")
    
    class Meta:
        template = "streams/whatwebelieve.html"
        icon = "placeholder"
        label = "What We Believe"
        
class whychooseus2(blocks.StructBlock):
    
    title1_small = blocks.CharBlock(required = False, help_text = "Add title here")
    title2_bold = blocks.CharBlock(required = False, help_text = "Add gig title text here")
    title3 = blocks.CharBlock(required = False, help_text = "Add gig title text here")
    text = blocks.RichTextBlock(required = False, help_text = "Add para here")   
    sub_title_1 = blocks.CharBlock(required = False, help_text = "Add title here")    
    percent1 = blocks.CharBlock(required = False, help_text = "Add % here")     
    sub_title_2 = blocks.CharBlock(required = False, help_text = "Add title here")    
    percent2 = blocks.CharBlock(required = False, help_text = "Add % here")     
    sub_title_3 = blocks.CharBlock(required = False, help_text = "Add title here")    
    percent3 = blocks.CharBlock(required = False, help_text = "Add % here")     
    sub_title_4 = blocks.CharBlock(required = False, help_text = "Add title here")    
    percent4 = blocks.CharBlock(required = False, help_text = "Add % here")     
    image = ImageChooserBlock(required=False, help_text = "Best size 500 x 530 pixels ")
    
    class Meta:
        template = "streams/whychooseus1.html"
        icon = "placeholder"
        label = "Why Choose Us 2"
        
class info_block1(blocks.StructBlock):
    
    title1_small = blocks.CharBlock(required = True, help_text = "Add title here")
    title2_bold = blocks.CharBlock(required = True, help_text = "Add gig title text here")      
    paragraph = blocks.RichTextBlock(required = True, help_text = "Add paragraph here")  
    button_label = blocks.CharBlock(required = True, help_text = "Add button lable here") 
    button_page= blocks.PageChooserBlock(required=False)
    button_url= blocks.URLBlock(required=False)           
    image = ImageChooserBlock(required=False, help_text = "Best size 570 x 350 pixels ")
    
    class Meta:
        template = "streams/about-block-4.html"
        icon = "placeholder"
        label = "Chart-Element"

class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""
    section_title = blocks.CharBlock(required = False, help_text = "Add section title here")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("button_text", blocks.CharBlock(required=False, help_text="Enter button text here")),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
                
            ]
        )
    )
          
    class Meta:  # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "3CardsBlock"

class FeaturesElementBlock2(blocks.StructBlock):
    """Cards with image and text and button(s)."""
    
    section_title = blocks.CharBlock(required = False, help_text = "Add section title here")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("button_text", blocks.CharBlock(required=False, help_text="Enter button text here")),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
                
            ]
        )
    )
          
    class Meta:  # noqa
        template = "streams/feature-element-2.html"
        icon = "placeholder"
        label = "Feature-Element-2"

class FeaturesElementBlock3(blocks.StructBlock):
    """Cards with image and text and button(s)."""
    
    section_title = blocks.CharBlock(required = False, help_text = "Add section title here")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True, help_text=" best size is 260 x 270 pixels")),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
                ("text_on_hover", blocks.CharBlock(required=False, help_text="Enter hover text here")),
            ]
        )
    )
          
    class Meta:  # noqa
        template = "streams/feature-element-3.html"
        icon = "placeholder"
        label = "Feature-Element-3"
        
class testimonials(blocks.StructBlock):
    """Cards with image and text and button(s)."""
    
    title = blocks.CharBlock(required = False, help_text = "Add section title here")
    Bold_Heading = blocks.CharBlock(required = False, help_text = "Add bold heading here")

    testimonials = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("client_picture", ImageChooserBlock(required=False, help_text=" best size is 80 x 80 pixels")),
                ("client_name", blocks.CharBlock(required=False, max_length=150, help_text=" Enter client name ")),
                ("designation", blocks.CharBlock(required=False, max_length=150, help_text=" Enter client designation ")),
                ("client_message", blocks.CharBlock(required=False, max_length=550, help_text=" Enter client's message here (length=550 characters)")),
                
            ]     
            
            )
    )
          
    class Meta:  # noqa
        template = "streams/testimonials.html"
        icon = "placeholder"
        label = "Testimonials"
        
class Inttiles(blocks.StructBlock):
    
    row1 = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("front_icon", ImageChooserBlock(required=False, help_text=" Upload front picture")),
                ("back_icon", ImageChooserBlock(required=False, help_text=" Upload back picture")),
                ("title", blocks.CharBlock(required=False, max_length=150, help_text=" Enter title ")),
                
            ]     
            
            )
    )
    row2 = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("front_icon", ImageChooserBlock(required=False, help_text=" Upload front picture")),
                ("back_icon", ImageChooserBlock(required=False, help_text=" Upload back picture")),
                ("title", blocks.CharBlock(required=False, max_length=150, help_text=" Enter title ")),
                
            ]     
            
            )
    )
    row3 = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("front_icon", ImageChooserBlock(required=False, help_text=" Upload front picture")),
                ("back_icon", ImageChooserBlock(required=False, help_text=" Upload back picture")),
                ("title", blocks.CharBlock(required=False, max_length=150, help_text=" Enter title ")),
                
            ]     
            
            )
    )
          
    class Meta:  # noqa
        template = "streams/Intcuisines.html"
        icon = "placeholder"
        label = "International Cuisines"
        
class Favfoods(blocks.StructBlock):
    
    row1 = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("front_icon", ImageChooserBlock(required=False, help_text=" Upload front picture")),
                ("back_icon", ImageChooserBlock(required=False, help_text=" Upload back picture")),
                ("title", blocks.CharBlock(required=False, max_length=150, help_text=" Enter title ")),
                
            ]     
            
            )
    )
    row2 = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("front_icon", ImageChooserBlock(required=False, help_text=" Upload front picture")),
                ("back_icon", ImageChooserBlock(required=False, help_text=" Upload back picture")),
                ("title", blocks.CharBlock(required=False, max_length=150, help_text=" Enter title ")),
                
            ]     
            
            )
    )
   
          
    class Meta:  # noqa
        template = "streams/favfood.html"
        icon = "placeholder"
        label = "Favourite Foods"
        
class Fastfoods(blocks.StructBlock):
    
    row1 = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("front_icon", ImageChooserBlock(required=False, help_text=" Upload front picture")),
               
                ("title", blocks.CharBlock(required=False, max_length=150, help_text=" Enter title ")),
                
            ]     
            
            )
    )
    row2 = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("front_icon", ImageChooserBlock(required=False, help_text=" Upload front picture")),
                
                ("title", blocks.CharBlock(required=False, max_length=150, help_text=" Enter title ")),
                
            ]     
            
            )
    )
   
          
    class Meta:  # noqa
        template = "streams/fastfood.html"
        icon = "placeholder"
        label = "Fast Foods"
        
class contactform(blocks.StructBlock):
    """Cards with image and text and button(s)."""
    
    Small_Heading = blocks.CharBlock(required = False, help_text = "Add section title here")
    Bold_Heading = blocks.CharBlock(required = False, help_text = "Add bold heading here")
    background_image = ImageChooserBlock(required=False, help_text = " 1920 x 870 px ")
    Paragraph = blocks.CharBlock(required = False, help_text = "Add para under heading here")
    Field1 = blocks.CharBlock(required = False, help_text = "Add field name here")
    Field2 = blocks.CharBlock(required = False, help_text = "Add field name here")
    Field3   = blocks.CharBlock(required = False, help_text = "Add field name here")
    Field4   = blocks.CharBlock(required = False, help_text = "Add field name here")
    Field5   = blocks.CharBlock(required = False, max_length= 550, help_text = "Add field name here")
    DropDown   = blocks.CharBlock(required = False, max_length= 150, help_text = "Add field name here")
    
    dropdown_items = blocks.ListBlock(
        blocks.StructBlock(
            [
                
                ("item_name", blocks.CharBlock(required=False, max_length=150, help_text=" Enter drop down items here ")),
               
                
            ]     
            
            )
    )
          
    class Meta:  # noqa
        template = "streams/contact_form.html"
        icon = "placeholder"
        label = "Contact Form"
        
class LegalSection(blocks.StructBlock):
    """Cards with image and text and button(s)."""
    
    Small_Heading = blocks.CharBlock(required = False, help_text = "Add section title here")
    Bold_Heading = blocks.CharBlock(required = False, help_text = "Add bold heading here")
    background_image = ImageChooserBlock(required=False )
    Paragraph = blocks.CharBlock(required = False, max_length=150, help_text = "Add para under heading here")
    Heading1 = blocks.CharBlock(required = False, help_text = "Add field name here")
    Text_for_Heading1 = blocks.CharBlock(required = False, max_length=150, help_text = "Add text for this heading here")
    IconCode_for_Heading1   = blocks.CharBlock(required = False, help_text = "Add icon code for this heading here")
    Button_name   = blocks.CharBlock(required = False, help_text = "Add button name here")
    button_url_for_heading1= blocks.URLBlock(required=False)
   
    Heading2 = blocks.CharBlock(required = False, help_text = "Add field name here")
    Text_for_Heading2 = blocks.CharBlock(required = False, max_length=150, help_text = "Add text for this heading here")
    IconCode_for_Heading2   = blocks.CharBlock(required = False, help_text = "Add icon code for this heading here")
    button_url_for_heading2= blocks.URLBlock(required=False)
    
    Heading3 = blocks.CharBlock(required = False, help_text = "Add field name here")
    Text_for_Heading3 = blocks.CharBlock(required = False, max_length=150, help_text = "Add text for this heading here")
    IconCode_for_Heading3   = blocks.CharBlock(required = False, help_text = "Add icon code for this heading here")
    button_url_for_heading3= blocks.URLBlock(required=False)
    
          
    class Meta:  # noqa
        template = "streams/LegalSection.html"
        icon = "placeholder"
        label = "Legal Section"
        
class whatweoffer(blocks.StructBlock):
    """Cards with image and text and button(s)."""
    preview = blocks.CharBlock(required = False, help_text = "enter any text or number and leave the below fields blank to see the preview")
    Small_Heading = blocks.CharBlock(required = False, help_text = "Add section title here")
    Bold_Heading = blocks.CharBlock(required = False, help_text = "Add bold heading here")
    background_image = ImageChooserBlock(required=False )
    Paragraph = blocks.CharBlock(required = False, max_length=150, help_text = "Add para under heading here")
    
    Heading1 = blocks.CharBlock(required = False, help_text = "Add field name here")
    Text_for_Heading1 = blocks.CharBlock(required = False, max_length=150, help_text = "Add text for this heading here")
    IconCode_for_Heading1   = blocks.CharBlock(required = False, help_text = "Add icon code for this heading here")
    button_url_for_heading1= blocks.URLBlock(required=False)
   
    Heading2 = blocks.CharBlock(required = False, help_text = "Add field name here")
    Text_for_Heading2 = blocks.CharBlock(required = False, max_length=150, help_text = "Add text for this heading here")
    IconCode_for_Heading2   = blocks.CharBlock(required = False, help_text = "Add icon code for this heading here")
    button_url_for_heading2= blocks.URLBlock(required=False)
    
    Heading3 = blocks.CharBlock(required = False, help_text = "Add field name here")
    Text_for_Heading3 = blocks.CharBlock(required = False, max_length=150, help_text = "Add text for this heading here")
    IconCode_for_Heading3   = blocks.CharBlock(required = False, help_text = "Add icon code for this heading here")
    button_url_for_heading3= blocks.URLBlock(required=False)
    
    Heading4 = blocks.CharBlock(required = False, help_text = "Add field name here")
    Text_for_Heading4 = blocks.CharBlock(required = False, max_length=150, help_text = "Add text for this heading here")
    IconCode_for_Heading4 = blocks.CharBlock(required = False, help_text = "Add icon code for this heading here")
    button_url_for_heading4= blocks.URLBlock(required=False)
    
    Heading5 = blocks.CharBlock(required = False, help_text = "Add field name here")
    Text_for_Heading5 = blocks.CharBlock(required = False, max_length=150, help_text = "Add text for this heading here")
    IconCode_for_Heading5   = blocks.CharBlock(required = False, help_text = "Add icon code for this heading here")
    button_url_for_heading5= blocks.URLBlock(required=False)
    
    Heading6 = blocks.CharBlock(required = False, help_text = "Add field name here")
    Text_for_Heading6 = blocks.CharBlock(required = False, max_length=150, help_text = "Add text for this heading here")
    IconCode_for_Heading6   = blocks.CharBlock(required = False, help_text = "Add icon code for this heading here")
    button_url_for_heading6= blocks.URLBlock(required=False)
    
          
    class Meta:  # noqa
        template = "streams/whatweoffer.html"
        icon = "placeholder"
        label = "What We Offer"
        
class ImageSliderBlock(blocks.StructBlock):
    """Cards with image only """

    images = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True, help_text=" best size is 140 x 130 pixels")),                
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
                
            ]
        )
    )
          
    class Meta:  # noqa
        template = "streams/clients-element.html"
        icon = "placeholder"
        label = "ImageSlideBlock"

class AccordionBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""
    
    Small_Heading  = blocks.CharBlock(required=False, help_text="Add your small heading here")
    Bold_Heading  = blocks.CharBlock(required=False, help_text="Add bold heading under small heading here")
    Paragraph = blocks.RichTextBlock(required =False, help_text = "Add para under bold heading here")
    
    First_Section_Title = blocks.CharBlock(required=True, help_text="Add your title")
    
    First_Section_Content_Text = blocks.RichTextBlock(required=True, help_text="Add your title")  

    Sections = blocks.ListBlock(
        blocks.StructBlock(
            [    
                ("Section_ID", blocks.CharBlock(required=True, max_length=40, unique=True,  help_text="Make sure you must enter a unique word or alphanumeric text as ID")),
                ("Section_Title", blocks.CharBlock(required=True, max_length=40,  help_text="Enter Title for the sections text here")),
                
                ("Section_Content_Text", blocks.RichTextBlock(required=False, help_text="Enter text for the sections here")),               
                ("Button_Text", blocks.CharBlock(required=False, help_text="Enter button text here, button will only appear if you either provide inner or external link")),
                ("Button_Page", blocks.PageChooserBlock(required=False)),
                ("Button_Url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
                
            ]   )   )
    
    class Meta:  # noqa
        template = "streams/Accordion.html"
        icon = "placeholder"
        label = "Accordion:TypeOne"
    
class Tabs1Block(blocks.StructBlock):
    """Tabs with text and button(s)."""
    
    Block_Title = blocks.CharBlock(required=False, help_text="Add section title here")
    First_tab_Title = blocks.CharBlock(required=True, help_text="Add Title for the first tab")
    First_Section_Content_Heading = blocks.CharBlock(required=True, help_text="Add Heading for the first tab")
    First_Section_Content_Text = blocks.CharBlock(required=True, help_text="Add Text for the first tab")
    Button_Text = blocks.CharBlock(required=False, help_text="Enter button text here, button will only appear if you either provide inner or external link")  
    Button_Page = blocks.CharBlock(required = False, help_text="You can select a page to connect to the button")
    Button_Url = blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")

    tabs = blocks.ListBlock(
        blocks.StructBlock(
            [    
                ("Tab_ID", blocks.CharBlock(required=True, max_length=40, unique=True,  help_text="Make sure you must enter a unique word or alphanumeric text as ID")),
                ("Tab_Title", blocks.CharBlock(required=True, max_length=40,  help_text="Enter Title for the sections text here")),
                ("Section_Content_Heading", blocks.CharBlock(required=False, help_text="Enter heading for the sections text here")),
                ("Section_Content_Text", blocks.RichTextBlock(required=False, help_text="Enter text for the sections here")),               
                ("Button_Text", blocks.CharBlock(required=False, help_text="Enter button text here, button will only appear if you either provide inner or external link")),
                ("Button_Page", blocks.PageChooserBlock(required=False, help_text="You can select a page to connect to the button" )),
                ("Button_Url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
                
            ]   )   )
          
    class Meta:  # noqa
        template = "streams/tab_1.html"
        icon = "placeholder"
        label = "Tabs:TypeOne"

class Rich_Text_Block(blocks.RichTextBlock):

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "edit"
        label = "RichTextBlock"
        
class Simple_Horizontal_Divider(blocks.StructBlock):

    class Meta:
        template = "streams/Simple_Horizontal_Divider.html"
        icon = "placeholder"
        label = "SimpleHorizontalDivider"