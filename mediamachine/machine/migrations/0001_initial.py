# flake8: noqa
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(default=b'', max_length=200, null=True, blank=True)),
            ],
            options={
                'ordering': ('keyword',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resource', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('description', models.TextField(default=b'', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theme', models.CharField(default=b'', max_length=200, null=True, blank=True)),
            ],
            options={
                'ordering': ('theme',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('scene', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('author', models.CharField(default=b'', max_length=100, null=True, blank=True)),
                ('copyrightholder', models.CharField(default=b'', max_length=300, null=True, blank=True)),
                ('copyrightdate', models.IntegerField(default=0, null=True, blank=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('modified', models.DateField(auto_now=True, null=True)),
                ('full_text', models.TextField(default=b'', null=True, blank=True)),
                ('questions', models.TextField(default=b'', null=True, blank=True)),
                ('commentary', models.TextField(default=b'', null=True, blank=True)),
                ('plot', models.TextField(default=b'', null=True, blank=True)),
                ('screenplay', models.TextField(default=b'', null=True, blank=True)),
                ('image_url', models.URLField(default=b'http://www.columbia.edu/itc/tc/cstudies/imagesequence/', null=True, blank=True)),
                ('real_video_url', models.URLField(default=b'http://kola.cc.columbia.edu:8080/ramgen/itcmedia/tc/culturalstudies/', null=True, blank=True)),
                ('sequence_url', models.URLField(default=b'http://www.columbia.edu/itc/tc/cstudies/imagesequence/', null=True, blank=True)),
                ('local_video', models.BooleanField(default=False)),
                ('real_video_filename', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('local_image', models.BooleanField(default=False)),
                ('image_filename', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('sequence_prefix', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('sequence_count', models.IntegerField(default=1, null=True, blank=True)),
                ('keywords', models.ManyToManyField(to='machine.Keyword')),
                ('resources', models.ManyToManyField(to='machine.Resource')),
                ('themes', models.ManyToManyField(to='machine.Theme')),
            ],
            options={
                'ordering': ('title', 'scene'),
            },
            bases=(models.Model,),
        ),
    ]
