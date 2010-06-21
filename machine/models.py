from django.db import models
from django.contrib import databrowse

class Resource(models.Model):
    resource = models.CharField(max_length=200,default="",blank=True,null=True)
    description = models.TextField(default="",blank=True,null=True)

    def __unicode__(self):
        return self.resource

    def get_absolute_url(self):
        return "/resource/%d/" % self.id


class Theme(models.Model):
    theme = models.CharField(max_length=200,default="",blank=True,null=True)

    class Meta:
        ordering = ('theme',)
    
    def __unicode__(self):
        return self.theme

    def get_absolute_url(self):
        return "/theme/%d/" % self.id


class Keyword(models.Model):
    keyword = models.CharField(max_length=200,default="",blank=True,null=True)

    class Meta:
        ordering = ('keyword',)

    def __unicode__(self):
        return self.keyword

    def get_absolute_url(self):
        return "/keyword/%d/" % self.id


class Video(models.Model):
    title = models.CharField(max_length=200,default="",blank=True,null=True)
    scene = models.CharField(max_length=200,default="",blank=True,null=True)
    author = models.CharField(max_length=100,default="",blank=True,null=True)
    copyrightholder = models.CharField(max_length=300,default="",blank=True,null=True)
    copyrightdate = models.IntegerField(default=0,blank=True,null=True)
    created = models.DateField(blank=True,null=True,auto_now_add=True)
    modified = models.DateField(blank=True,null=True,auto_now=True)
    full_text = models.TextField(default="",blank=True,null=True)
    questions = models.TextField(default="",blank=True,null=True)
    commentary = models.TextField(default="",blank=True,null=True)
    plot = models.TextField(default="",blank=True,null=True)
    screenplay = models.TextField(default="",blank=True,null=True)
    image_url = models.URLField(default='http://www.columbia.edu/itc/tc/cstudies/imagesequence/',blank=True,null=True)
    real_video_url = models.URLField(default='http://kola.cc.columbia.edu:8080/ramgen/itcmedia/tc/culturalstudies/',blank=True,null=True)
    sequence_url = models.URLField(default='http://www.columbia.edu/itc/tc/cstudies/imagesequence/',blank=True,null=True)
    local_video = models.BooleanField(default=False)
    real_video_filename = models.CharField(max_length=200,default="",blank=True,null=True)
    local_image = models.BooleanField(default=False)
    image_filename = models.CharField(max_length=200,default="",blank=True,null=True)
    sequence_prefix = models.CharField(max_length=200,default="",blank=True,null=True)
    sequence_count = models.IntegerField(default=1,blank=True,null=True)

    resources = models.ManyToManyField(Resource)
    themes = models.ManyToManyField(Theme)
    keywords = models.ManyToManyField(Keyword)

    class Meta:
        ordering = ('title','scene')

    def __unicode__(self):
        if self.scene:
            return "%s: %s" % (self.title,self.scene)
        else:
            return self.title

    def images(self):
        for i in range(1,self.sequence_count):
            yield self.sequence_url + self.sequence_prefix + str(i) + ".jpg"

    def get_absolute_url(self):
        return "/video/%d/" % self.id


databrowse.site.register(Video)
databrowse.site.register(Keyword)
databrowse.site.register(Theme)
databrowse.site.register(Resource)

