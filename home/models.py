from django.db import models
from django import forms


from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index

from rest_framework import serializers
#from talk.models import Post

# Create your models here.

'''
#rest_framework start
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'created', 'updated')
#rest_framework end
'''

#wagtail start
class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]



class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]

#wagtail end


#Articles start
    
class Articles(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=250)
    writer = models.CharField(max_length=250)
    points = models.FloatField(null=True, blank=True, default=0.0)
    like = models.FloatField(null=True, blank=True, default=0.0)

class Comment(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    like = models.FloatField(null=True, blank=True, default=0.0)
    points = models.FloatField(null=True, blank=True, default=0.0)
    author = models.CharField(max_length=250)
    commentor = models.CharField(max_length=250)
    
class Bsell(models.Model):
    user_name = models.CharField(max_length=250)
    owner = models.CharField(max_length=250, default="admin")
    coins = models.FloatField(null=True, blank=True, default=0.0)
    price = models.FloatField(null=True, blank=True, default=1.0)

#articles end

#Members start
    
class Members(models.Model):
	user_name = models.CharField(max_length=250)
	age = models.IntegerField(null=True, blank=True, default=18)
	phone = models.CharField(max_length=250)
	upline = models.CharField(max_length=250)
	tin = models.CharField(max_length=250)
	points = models.FloatField(null=True, blank=True, default=0.0)
	money = models.FloatField(null=True, blank=True, default=0.0)
	photos1 = models.ImageField(null=True, blank=True, upload_to='images/member/')

#Members End


#Online Shop Start

class Product(models.Model):
	name = models.CharField(max_length = 250)
	type = models.CharField(max_length=250)
	category = models.CharField(max_length=250)
	desc = models.TextField(max_length=250)
	origprice = models.FloatField(null=True, blank=True, default=0.0)
	price = models.FloatField(null=True, blank=True, default=0.0)
	markup = models.FloatField(null=True, blank=True, default=0.0)
	owner = models.TextField(max_length=250)
	referal = models.FloatField(null=True, blank=True, default=0.0)
	pic1 = models.ImageField(null=True, blank=True, upload_to = 'images/product/')
	pic2 = models.ImageField(null=True, blank=True, upload_to = 'images/product/')
	pic3 = models.ImageField(null=True, blank=True, upload_to = 'images/product/')

	
	
#Online Shop End

#EMS Kaseong Start
class Students(models.Model):
	user_name = models.CharField(max_length = 250)
	first_name = models.CharField(max_length = 250)
	last_name = models.CharField(max_length = 250)
	age = models.IntegerField(null=True, blank=True, default=4)
	section = models.CharField(max_length = 250)
	guardian = models.CharField(max_length = 250)

class Guardian(models.Model):
	user_name = models.CharField(max_length = 250)
	first_name = models.CharField(max_length = 250)
	last_name = models.CharField(max_length = 250)
	age = models.IntegerField(null=True, blank=True, default=18)	
	
class Teacher(models.Model):
	user_name = models.CharField(max_length = 250)
	first_name = models.CharField(max_length = 250)
	last_name = models.CharField(max_length = 250)
	age = models.IntegerField(null=True, blank=True, default=18)	
	
class Subject(models.Model):
	name = models.CharField(max_length = 250)
	units = models.FloatField(null=True, blank=True, default=0.0)
	price = models.FloatField(null=True, blank=True, default=0.0)
	
class Section(models.Model):
	name = models.CharField(max_length = 250)
	teacher_name = models.CharField(max_length = 250)
	max_students = models.CharField(max_length = 250)

class Lesson(models.Model):
	subject_name = models.CharField(max_length = 250)
	teacher_name = models.CharField(max_length = 250)
	student_name = models.CharField(max_length = 250)
	student_score = models.CharField(max_length = 250)
	room = models.CharField(max_length = 250)
	date_sched = models.CharField(max_length = 250)
	time_sched = models.CharField(max_length = 250)

#EMS Kaseong End



	    