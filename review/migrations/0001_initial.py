# Generated by Django 4.2.3 on 2023-08-23 16:47

from django.db import migrations, models
import django.db.models.deletion
import streams.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('BannerTitle', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('support', models.CharField(max_length=250, null=True)),
                ('email', models.CharField(max_length=550, null=True)),
                ('para_under_logo', models.CharField(max_length=550, null=True)),
                ('footer_column_two', models.CharField(blank=True, max_length=250, null=True)),
                ('footer_column_three', models.CharField(blank=True, max_length=250, null=True)),
                ('content', wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add title here', required=True)), ('text', wagtail.blocks.CharBlock(help_text='Add title here', required=True))])), ('Rich_text_editor', streams.blocks.Rich_Text_Block()), ('Info_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.blocks.CharBlock(help_text='Add title here', required=True)), ('text', wagtail.blocks.CharBlock(help_text='Add title here', required=True)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(required=False)), ('button_text', wagtail.blocks.CharBlock(default='Learn More', max_length=40, required=True))])), ('Cardblock', wagtail.blocks.StructBlock([('section_title', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=40, required=True)), ('button_text', wagtail.blocks.CharBlock(help_text='Enter button text here', required=False)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))])))])), ('About_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Best size 500 x 470 pixels ', required=False)), ('video', wagtail.blocks.URLBlock(help_text='Enter youtube video link here ', required=False)), ('title1_small', wagtail.blocks.CharBlock(help_text='Add title here', required=True)), ('title2_bold', wagtail.blocks.CharBlock(help_text='Add Big Bold title here', required=True)), ('text', wagtail.blocks.RichTextBlock(help_text='Add main para here', required=True)), ('icon1', wagtail.blocks.CharBlock(help_text='Add flaticon class here', required=False)), ('sub_title_1', wagtail.blocks.CharBlock(help_text='Add sub title 1 here', required=True)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(required=False)), ('sub_title_text_1', wagtail.blocks.RichTextBlock(help_text='Add text under sub title 1 here', required=True)), ('icon2', wagtail.blocks.CharBlock(help_text='Add flaticon class here', required=False)), ('sub_title_2', wagtail.blocks.CharBlock(help_text='Add sub title 2 here', required=True)), ('button_page_1', wagtail.blocks.PageChooserBlock(required=False)), ('button_url_1', wagtail.blocks.URLBlock(required=False)), ('sub_title_text_2', wagtail.blocks.RichTextBlock(help_text='Add text under sub title 2 here', required=True))])), ('About_block_2', wagtail.blocks.StructBlock([('title1_small', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('title2_bold', wagtail.blocks.CharBlock(help_text='Add gig title text here', required=True)), ('text', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False)), ('icon1', wagtail.blocks.CharBlock(help_text='Add flaticon class here', required=False)), ('sub_title_1', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(required=False)), ('sub_title_text_1', wagtail.blocks.RichTextBlock(help_text='Add pare here', required=False)), ('icon2', wagtail.blocks.CharBlock(help_text='Add flaticon class here', required=False)), ('sub_title_2', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('button_page_2', wagtail.blocks.PageChooserBlock(required=False)), ('button_url_2', wagtail.blocks.URLBlock(required=False)), ('sub_title_text_2', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False)), ('icon3', wagtail.blocks.CharBlock(help_text='Add flaticon class here', required=False)), ('sub_title_3', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('button_page_3', wagtail.blocks.PageChooserBlock(required=False)), ('button_url_3', wagtail.blocks.URLBlock(required=False)), ('sub_title_text_3', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False)), ('icon4', wagtail.blocks.CharBlock(help_text='Add flaticon class here', required=False)), ('sub_title_4', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('button_page_4', wagtail.blocks.PageChooserBlock(required=False)), ('button_url_4', wagtail.blocks.URLBlock(required=False)), ('sub_title_text_4', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False)), ('icon5', wagtail.blocks.CharBlock(help_text='Add flaticon class here', required=False)), ('imagebox_heading', wagtail.blocks.CharBlock(help_text='Add headign for box over image here', required=False)), ('imagebox_text', wagtail.blocks.CharBlock(help_text='Add text for box over image here', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Best size 460 x 455 pixels ', required=False))])), ('About_block_3', wagtail.blocks.StructBlock([('title1_small', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('title2_bold', wagtail.blocks.CharBlock(help_text='Add gig title text here', required=True)), ('text', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False)), ('sub_title_1', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('sub_title_1_text', wagtail.blocks.RichTextBlock(help_text='Add pare here', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Best size 460 x 455 pixels ', required=False)), ('iframe_youtube', wagtail.blocks.URLBlock(help_text='Add code here', required=False))])), ('About_block_4', wagtail.blocks.StructBlock([('title1_small', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('title2_bold', wagtail.blocks.CharBlock(help_text='Add gig title text here', required=False)), ('text', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False)), ('sub_title_1', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('percent1', wagtail.blocks.CharBlock(help_text='Add % here', required=False)), ('sub_title_2', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('percent2', wagtail.blocks.CharBlock(help_text='Add % here', required=False)), ('sub_title_3', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('percent3', wagtail.blocks.CharBlock(help_text='Add % here', required=False)), ('sub_title_4', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('percent4', wagtail.blocks.CharBlock(help_text='Add % here', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Best size 500 x 530 pixels ', required=False))])), ('Accordion_Block', wagtail.blocks.StructBlock([('Small_Heading', wagtail.blocks.CharBlock(help_text='Add your small heading here', required=False)), ('Bold_Heading', wagtail.blocks.CharBlock(help_text='Add bold heading under small heading here', required=False)), ('Paragraph', wagtail.blocks.RichTextBlock(help_text='Add para under bold heading here', required=False)), ('First_Section_Title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('First_Section_Content_Text', wagtail.blocks.RichTextBlock(help_text='Add your title', required=True)), ('Sections', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Section_ID', wagtail.blocks.CharBlock(help_text='Make sure you must enter a unique word or alphanumeric text as ID', max_length=40, required=True, unique=True)), ('Section_Title', wagtail.blocks.CharBlock(help_text='Enter Title for the sections text here', max_length=40, required=True)), ('Section_Content_Text', wagtail.blocks.RichTextBlock(help_text='Enter text for the sections here', required=False)), ('Button_Text', wagtail.blocks.CharBlock(help_text='Enter button text here, button will only appear if you either provide inner or external link', required=False)), ('Button_Page', wagtail.blocks.PageChooserBlock(required=False)), ('Button_Url', wagtail.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))])))])), ('Simple_Horizontal_Divider', wagtail.blocks.StructBlock([])), ('Tabs1Block', wagtail.blocks.StructBlock([('Block_Title', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('First_tab_Title', wagtail.blocks.CharBlock(help_text='Add Title for the first tab', required=True)), ('First_Section_Content_Heading', wagtail.blocks.CharBlock(help_text='Add Heading for the first tab', required=True)), ('First_Section_Content_Text', wagtail.blocks.CharBlock(help_text='Add Text for the first tab', required=True)), ('Button_Text', wagtail.blocks.CharBlock(help_text='Enter button text here, button will only appear if you either provide inner or external link', required=False)), ('Button_Page', wagtail.blocks.CharBlock(help_text='You can select a page to connect to the button', required=False)), ('Button_Url', wagtail.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False)), ('tabs', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Tab_ID', wagtail.blocks.CharBlock(help_text='Make sure you must enter a unique word or alphanumeric text as ID', max_length=40, required=True, unique=True)), ('Tab_Title', wagtail.blocks.CharBlock(help_text='Enter Title for the sections text here', max_length=40, required=True)), ('Section_Content_Heading', wagtail.blocks.CharBlock(help_text='Enter heading for the sections text here', required=False)), ('Section_Content_Text', wagtail.blocks.RichTextBlock(help_text='Enter text for the sections here', required=False)), ('Button_Text', wagtail.blocks.CharBlock(help_text='Enter button text here, button will only appear if you either provide inner or external link', required=False)), ('Button_Page', wagtail.blocks.PageChooserBlock(help_text='You can select a page to connect to the button', required=False)), ('Button_Url', wagtail.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))])))])), ('ImageSliderBlock', wagtail.blocks.StructBlock([('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text=' best size is 140 x 130 pixels', required=True)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))])))])), ('info_block1', wagtail.blocks.StructBlock([('title1_small', wagtail.blocks.CharBlock(help_text='Add title here', required=True)), ('title2_bold', wagtail.blocks.CharBlock(help_text='Add gig title text here', required=True)), ('paragraph', wagtail.blocks.RichTextBlock(help_text='Add paragraph here', required=True)), ('button_label', wagtail.blocks.CharBlock(help_text='Add button lable here', required=True)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Best size 570 x 350 pixels ', required=False))])), ('FeaturesElementBlock2', wagtail.blocks.StructBlock([('section_title', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=40, required=True)), ('button_text', wagtail.blocks.CharBlock(help_text='Enter button text here', required=False)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))])))])), ('FeaturesElementBlock3', wagtail.blocks.StructBlock([('section_title', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text=' best size is 260 x 270 pixels', required=True)), ('title', wagtail.blocks.CharBlock(max_length=40, required=True)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False)), ('text_on_hover', wagtail.blocks.CharBlock(help_text='Enter hover text here', required=False))])))])), ('news_1', wagtail.blocks.StructBlock([('section_title', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.blocks.CharBlock(max_length=400, required=True)), ('button_text', wagtail.blocks.CharBlock(help_text='Enter button text here', required=False)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))])))])), ('VideoGallery', wagtail.blocks.StructBlock([('Block_title', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('firstvideo', wagtail.blocks.URLBlock(help_text='Copy and Paste the Video URL here', required=True)), ('videos', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('video_url', wagtail.blocks.URLBlock(help_text='Copy and Paste the Video URL here', required=True)), ('imagecode', wagtail.blocks.CharBlock(help_text='Add image code from the youtube video url', required=False)), ('description', wagtail.blocks.CharBlock(help_text='Add video description here', required=False))])))])), ('ImageGallery', wagtail.blocks.StructBlock([('Block_title', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('description', wagtail.blocks.CharBlock(help_text='Add section description here', required=False)), ('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Upload_Image', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('Videosin2column', wagtail.blocks.StructBlock([('title1_bold', wagtail.blocks.CharBlock(help_text='Add  title text here', required=True)), ('video_url1', wagtail.blocks.URLBlock(help_text='Copy and Paste the Video URL here', required=True)), ('title2_bold', wagtail.blocks.CharBlock(help_text='Add title text here', required=True)), ('video_url2', wagtail.blocks.URLBlock(help_text='Copy and Paste the Video URL here', required=True))])), ('contact', wagtail.blocks.StructBlock([('custom_title', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('Main_Heading', wagtail.blocks.CharBlock(help_text='Add title text here', required=True)), ('Address1', wagtail.blocks.CharBlock(help_text='Building, Street, City', required=False)), ('Address2', wagtail.blocks.CharBlock(help_text='State, PIN, Country', required=False)), ('Phone1', wagtail.blocks.IntegerBlock(help_text='Any Phone number', required=False)), ('Phone2', wagtail.blocks.IntegerBlock(help_text='Any Phone number', required=False)), ('Email1', wagtail.blocks.EmailBlock(help_text='Any email id for contact', required=False)), ('Email2', wagtail.blocks.EmailBlock(help_text='Any email id for contact', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Best size 1900 x 500 pixels ', required=False))])), ('ImageGallery3', wagtail.blocks.StructBlock([('Block_title', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('title1', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('title2', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('title3', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('title4', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('title5', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('gallery', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('gallerytitle', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('Description', wagtail.blocks.CharBlock(help_text='Add image description here', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('page_url', wagtail.blocks.URLBlock(help_text='Copy and Paste the page URL here', required=False))])))])), ('textblock2', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('text', wagtail.blocks.RichTextBlock(help_text='Add title text here', required=True)), ('page_url', wagtail.blocks.URLBlock(help_text='Copy and Paste the page URL here', required=False))])), ('ImagesliderGallery', wagtail.blocks.StructBlock([('smallheading', wagtail.blocks.CharBlock(help_text='Add small section title here', required=False)), ('biglheading', wagtail.blocks.CharBlock(help_text='Add bold section title here', required=False)), ('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('Video_Intro', wagtail.blocks.StructBlock([('Tab1', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('Heading_tab1', wagtail.blocks.CharBlock(help_text='Add Heading for this tab here', required=True)), ('Paragraph_tab1', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False)), ('Bulletone_tab1', wagtail.blocks.CharBlock(help_text='Add bullet sentence here', required=True)), ('Bullettwo_tab1', wagtail.blocks.CharBlock(help_text='Add bullet sentence here', required=True)), ('Bulletthree_tab1', wagtail.blocks.CharBlock(help_text='Add bullet sentence here', required=True)), ('Bulletfour_tab1', wagtail.blocks.CharBlock(help_text='Add bullet sentence here', required=True)), ('Tab2', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('Heading_tab2', wagtail.blocks.CharBlock(help_text='Add Heading for this tab here', required=True)), ('Paragraph_tab2', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False)), ('Bulletone_tab2', wagtail.blocks.CharBlock(help_text='Add bullet sentence here', required=True)), ('Bullettwo_tab2', wagtail.blocks.CharBlock(help_text='Add bullet sentence here', required=True)), ('Bulletthree_tab2', wagtail.blocks.CharBlock(help_text='Add bullet sentence here', required=True)), ('Bulletfour_tab2', wagtail.blocks.CharBlock(help_text='Add bullet sentence here', required=True)), ('Tab3', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('Heading_tab3', wagtail.blocks.CharBlock(help_text='Add Heading for this tab here', required=True)), ('Paragraph_tab3', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False)), ('Bulletone_tab3', wagtail.blocks.CharBlock(help_text='Add bullet sentence here', required=True)), ('Bullettwo_tab3', wagtail.blocks.CharBlock(help_text='Add bullet sentence here', required=True)), ('Bulletthree_tab3', wagtail.blocks.CharBlock(help_text='Add bullet sentence here', required=True)), ('Bulletfour_tab3', wagtail.blocks.CharBlock(help_text='Add bullet sentence here', required=True)), ('video_url', wagtail.blocks.URLBlock(required=False)), ('image_left', wagtail.images.blocks.ImageChooserBlock(help_text='Best size 460 x 455 pixels ', required=False))])), ('map', wagtail.blocks.StructBlock([('Small_Heading', wagtail.blocks.CharBlock(help_text='Add small heading on top here', required=True)), ('Bold_Heading', wagtail.blocks.CharBlock(help_text='Add Bold Heading just below small heading here', required=True)), ('Locations', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('location_name', wagtail.blocks.CharBlock(max_length=150, required=False)), ('text', wagtail.blocks.CharBlock(max_length=400, required=False))])))])), ('funfact', wagtail.blocks.StructBlock([('Heading1', wagtail.blocks.CharBlock(help_text='Add heading on here', required=True)), ('Data_stop1', wagtail.blocks.IntegerBlock(help_text='Add the number on which the counter will stop', required=True)), ('Heading2', wagtail.blocks.CharBlock(help_text='Add heading on here', required=True)), ('Data_stop2', wagtail.blocks.IntegerBlock(help_text='Add the number on which the counter will stop', required=True)), ('Heading3', wagtail.blocks.CharBlock(help_text='Add heading on here', required=True)), ('Data_stop3', wagtail.blocks.IntegerBlock(help_text='Add the number on which the counter will stop', required=True)), ('Heading4', wagtail.blocks.CharBlock(help_text='Add heading on here', required=True)), ('Data_stop4', wagtail.blocks.IntegerBlock(help_text='Add the number on which the counter will stop', required=True))])), ('Team', wagtail.blocks.StructBlock([('Small_Heading', wagtail.blocks.CharBlock(help_text='Add small heading on top here', required=True)), ('Bold_Heading', wagtail.blocks.CharBlock(help_text='Add Bold Heading just below small heading here', required=True)), ('Paragraph', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False)), ('members', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Pic', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Name', wagtail.blocks.CharBlock(max_length=150, required=True)), ('Designation', wagtail.blocks.CharBlock(max_length=150, required=True)), ('FB_Profile', wagtail.blocks.URLBlock(help_text='Copy and Paste FB Profile link here', max_length=650, required=True)), ('Twitter_Profile', wagtail.blocks.URLBlock(help_text='Copy and Paste Twitter Profile link here', max_length=650, required=True)), ('Instagram_Profile', wagtail.blocks.URLBlock(help_text='Copy and Paste Instagram Profile link here', max_length=650, required=True)), ('LinkedIn_Profile', wagtail.blocks.URLBlock(help_text='Copy and Paste LinkedIn Profile link here', max_length=650, required=True))])))])), ('GetInTouch', wagtail.blocks.StructBlock([('MainHeading', wagtail.blocks.CharBlock(help_text='Add  title text here', required=False)), ('SubHeading', wagtail.blocks.RichTextBlock(help_text='Add text under manin heading here', required=False)), ('ButtonText', wagtail.blocks.CharBlock(help_text='Add  button text here', required=False))])), ('Pricing', wagtail.blocks.StructBlock([('Plan1', wagtail.blocks.CharBlock(help_text='Add plan name here', required=True)), ('Recommended_Plan1', wagtail.blocks.CharBlock(help_text="Optional: Type 'Recoomended' if this is a recommended plan", required=False)), ('Price_Plan1', wagtail.blocks.IntegerBlock(help_text='Enter Price here', required=True)), ('Detail_Plan1', wagtail.blocks.CharBlock(help_text='Enter unique plan feature in one line', required=False)), ('features_Plan1', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Feature', wagtail.blocks.CharBlock(max_length=250, required=True))]))), ('Plan2', wagtail.blocks.CharBlock(help_text='Add plan name here', required=True)), ('Recommended_Plan2', wagtail.blocks.CharBlock(help_text="Optional: Type 'Recoomended' if this is a recommended plan", required=False)), ('Price_Plan2', wagtail.blocks.IntegerBlock(help_text='Enter Price here', required=True)), ('Detail_Plan2', wagtail.blocks.CharBlock(help_text='Enter unique plan feature in one line', required=False)), ('features_Plan2', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Feature', wagtail.blocks.CharBlock(max_length=250, required=True))]))), ('Plan3', wagtail.blocks.CharBlock(help_text='Add plan name here', required=True)), ('Recommended_Plan3', wagtail.blocks.CharBlock(help_text="Optional: Type 'Recoomended' if this is a recommended plan", required=False)), ('Price_Plan3', wagtail.blocks.IntegerBlock(help_text='Enter Price here', required=True)), ('Detail_Plan3', wagtail.blocks.CharBlock(help_text='Enter unique plan feature in one line', required=False)), ('features_Plan3', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Feature', wagtail.blocks.CharBlock(max_length=250, required=True))])))])), ('HeadingPara', wagtail.blocks.StructBlock([('Small_Heading', wagtail.blocks.CharBlock(help_text='Add small heading on top here', required=False)), ('Bold_Heading', wagtail.blocks.CharBlock(help_text='Add Bold Heading just below small heading here', required=True)), ('Paragraph', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False))])), ('testimonials', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('Bold_Heading', wagtail.blocks.CharBlock(help_text='Add bold heading here', required=False)), ('testimonials', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('client_picture', wagtail.images.blocks.ImageChooserBlock(help_text=' best size is 80 x 80 pixels', required=False)), ('client_name', wagtail.blocks.CharBlock(help_text=' Enter client name ', max_length=150, required=False)), ('designation', wagtail.blocks.CharBlock(help_text=' Enter client designation ', max_length=150, required=False)), ('client_message', wagtail.blocks.CharBlock(help_text=" Enter client's message here (length=550 characters)", max_length=550, required=False))])))])), ('contactform', wagtail.blocks.StructBlock([('Small_Heading', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('Bold_Heading', wagtail.blocks.CharBlock(help_text='Add bold heading here', required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock(help_text=' 1920 x 870 px ', required=False)), ('Paragraph', wagtail.blocks.CharBlock(help_text='Add para under heading here', required=False)), ('Field1', wagtail.blocks.CharBlock(help_text='Add field name here', required=False)), ('Field2', wagtail.blocks.CharBlock(help_text='Add field name here', required=False)), ('Field3', wagtail.blocks.CharBlock(help_text='Add field name here', required=False)), ('Field4', wagtail.blocks.CharBlock(help_text='Add field name here', required=False)), ('Field5', wagtail.blocks.CharBlock(help_text='Add field name here', max_length=550, required=False)), ('DropDown', wagtail.blocks.CharBlock(help_text='Add field name here', max_length=150, required=False)), ('dropdown_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('item_name', wagtail.blocks.CharBlock(help_text=' Enter drop down items here ', max_length=150, required=False))])))])), ('LegalSection', wagtail.blocks.StructBlock([('Small_Heading', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('Bold_Heading', wagtail.blocks.CharBlock(help_text='Add bold heading here', required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('Paragraph', wagtail.blocks.CharBlock(help_text='Add para under heading here', max_length=150, required=False)), ('Heading1', wagtail.blocks.CharBlock(help_text='Add field name here', required=False)), ('Text_for_Heading1', wagtail.blocks.CharBlock(help_text='Add text for this heading here', max_length=150, required=False)), ('IconCode_for_Heading1', wagtail.blocks.CharBlock(help_text='Add icon code for this heading here', required=False)), ('Button_name', wagtail.blocks.CharBlock(help_text='Add button name here', required=False)), ('button_url_for_heading1', wagtail.blocks.URLBlock(required=False)), ('Heading2', wagtail.blocks.CharBlock(help_text='Add field name here', required=False)), ('Text_for_Heading2', wagtail.blocks.CharBlock(help_text='Add text for this heading here', max_length=150, required=False)), ('IconCode_for_Heading2', wagtail.blocks.CharBlock(help_text='Add icon code for this heading here', required=False)), ('button_url_for_heading2', wagtail.blocks.URLBlock(required=False)), ('Heading3', wagtail.blocks.CharBlock(help_text='Add field name here', required=False)), ('Text_for_Heading3', wagtail.blocks.CharBlock(help_text='Add text for this heading here', max_length=150, required=False)), ('IconCode_for_Heading3', wagtail.blocks.CharBlock(help_text='Add icon code for this heading here', required=False)), ('button_url_for_heading3', wagtail.blocks.URLBlock(required=False))])), ('whychooseus2', wagtail.blocks.StructBlock([('title1_small', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('title2_bold', wagtail.blocks.CharBlock(help_text='Add gig title text here', required=False)), ('title3', wagtail.blocks.CharBlock(help_text='Add gig title text here', required=False)), ('text', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False)), ('sub_title_1', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('percent1', wagtail.blocks.CharBlock(help_text='Add % here', required=False)), ('sub_title_2', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('percent2', wagtail.blocks.CharBlock(help_text='Add % here', required=False)), ('sub_title_3', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('percent3', wagtail.blocks.CharBlock(help_text='Add % here', required=False)), ('sub_title_4', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('percent4', wagtail.blocks.CharBlock(help_text='Add % here', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Best size 500 x 530 pixels ', required=False))])), ('whatweoffer', wagtail.blocks.StructBlock([('preview', wagtail.blocks.CharBlock(help_text='enter any text or number and leave the below fields blank to see the preview', required=False)), ('Small_Heading', wagtail.blocks.CharBlock(help_text='Add section title here', required=False)), ('Bold_Heading', wagtail.blocks.CharBlock(help_text='Add bold heading here', required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('Paragraph', wagtail.blocks.CharBlock(help_text='Add para under heading here', max_length=150, required=False)), ('Heading1', wagtail.blocks.CharBlock(help_text='Add field name here', required=False)), ('Text_for_Heading1', wagtail.blocks.CharBlock(help_text='Add text for this heading here', max_length=150, required=False)), ('IconCode_for_Heading1', wagtail.blocks.CharBlock(help_text='Add icon code for this heading here', required=False)), ('button_url_for_heading1', wagtail.blocks.URLBlock(required=False)), ('Heading2', wagtail.blocks.CharBlock(help_text='Add field name here', required=False)), ('Text_for_Heading2', wagtail.blocks.CharBlock(help_text='Add text for this heading here', max_length=150, required=False)), ('IconCode_for_Heading2', wagtail.blocks.CharBlock(help_text='Add icon code for this heading here', required=False)), ('button_url_for_heading2', wagtail.blocks.URLBlock(required=False)), ('Heading3', wagtail.blocks.CharBlock(help_text='Add field name here', required=False)), ('Text_for_Heading3', wagtail.blocks.CharBlock(help_text='Add text for this heading here', max_length=150, required=False)), ('IconCode_for_Heading3', wagtail.blocks.CharBlock(help_text='Add icon code for this heading here', required=False)), ('button_url_for_heading3', wagtail.blocks.URLBlock(required=False)), ('Heading4', wagtail.blocks.CharBlock(help_text='Add field name here', required=False)), ('Text_for_Heading4', wagtail.blocks.CharBlock(help_text='Add text for this heading here', max_length=150, required=False)), ('IconCode_for_Heading4', wagtail.blocks.CharBlock(help_text='Add icon code for this heading here', required=False)), ('button_url_for_heading4', wagtail.blocks.URLBlock(required=False)), ('Heading5', wagtail.blocks.CharBlock(help_text='Add field name here', required=False)), ('Text_for_Heading5', wagtail.blocks.CharBlock(help_text='Add text for this heading here', max_length=150, required=False)), ('IconCode_for_Heading5', wagtail.blocks.CharBlock(help_text='Add icon code for this heading here', required=False)), ('button_url_for_heading5', wagtail.blocks.URLBlock(required=False)), ('Heading6', wagtail.blocks.CharBlock(help_text='Add field name here', required=False)), ('Text_for_Heading6', wagtail.blocks.CharBlock(help_text='Add text for this heading here', max_length=150, required=False)), ('IconCode_for_Heading6', wagtail.blocks.CharBlock(help_text='Add icon code for this heading here', required=False)), ('button_url_for_heading6', wagtail.blocks.URLBlock(required=False))])), ('whatwebelieve', wagtail.blocks.StructBlock([('title1_small', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('title2_bold', wagtail.blocks.CharBlock(help_text='Add gig title text here', required=False)), ('text', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False)), ('LearMorePage', wagtail.blocks.URLBlock(help_text='Copy and Paste the page URL here', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Best size 500 x 530 pixels ', required=False))])), ('Whyshouldyouchooseus', wagtail.blocks.StructBlock([('title1_small', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('title2_bold', wagtail.blocks.CharBlock(help_text='Add  title text here', required=False)), ('text', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False)), ('tab_1', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('tab1_text', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False)), ('tab1_readmore_pagelink', wagtail.blocks.URLBlock(help_text='Add page link here', required=False)), ('tab_2', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('tab2_text', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False)), ('tab2_readmore_pagelink', wagtail.blocks.URLBlock(help_text='Add page link here', required=False)), ('tab_3', wagtail.blocks.CharBlock(help_text='Add title here', required=False)), ('tab3_text', wagtail.blocks.RichTextBlock(help_text='Add para here', required=False)), ('tab3_readmore_pagelink', wagtail.blocks.URLBlock(help_text='Add page link here', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Best size 500 x 530 pixels ', required=False))])), ('videosection', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add  title text here', required=False)), ('video_url', wagtail.blocks.URLBlock(help_text='Copy and Paste the Video URL here', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Add background image 1900 X 800 ', required=False))]))], blank=True, null=True, use_json_field=True)),
                ('bannerimage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Review Page',
                'verbose_name_plural': 'Review Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
