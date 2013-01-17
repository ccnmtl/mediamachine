# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resource'
        db.create_table('machine_resource', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('resource', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
        ))
        db.send_create_signal('machine', ['Resource'])

        # Adding model 'Theme'
        db.create_table('machine_theme', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('theme', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('machine', ['Theme'])

        # Adding model 'Keyword'
        db.create_table('machine_keyword', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keyword', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('machine', ['Keyword'])

        # Adding model 'Video'
        db.create_table('machine_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('scene', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('copyrightholder', self.gf('django.db.models.fields.CharField')(default='', max_length=300, null=True, blank=True)),
            ('copyrightdate', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateField')(auto_now=True, null=True, blank=True)),
            ('full_text', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('questions', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('commentary', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('plot', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('screenplay', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('image_url', self.gf('django.db.models.fields.URLField')(default='http://www.columbia.edu/itc/tc/cstudies/imagesequence/', max_length=200, null=True, blank=True)),
            ('real_video_url', self.gf('django.db.models.fields.URLField')(default='http://kola.cc.columbia.edu:8080/ramgen/itcmedia/tc/culturalstudies/', max_length=200, null=True, blank=True)),
            ('sequence_url', self.gf('django.db.models.fields.URLField')(default='http://www.columbia.edu/itc/tc/cstudies/imagesequence/', max_length=200, null=True, blank=True)),
            ('local_video', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('real_video_filename', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('local_image', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image_filename', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('sequence_prefix', self.gf('django.db.models.fields.CharField')(default='', max_length=200, null=True, blank=True)),
            ('sequence_count', self.gf('django.db.models.fields.IntegerField')(default=1, null=True, blank=True)),
        ))
        db.send_create_signal('machine', ['Video'])

        # Adding M2M table for field resources on 'Video'
        db.create_table('machine_video_resources', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['machine.video'], null=False)),
            ('resource', models.ForeignKey(orm['machine.resource'], null=False))
        ))
        db.create_unique('machine_video_resources', ['video_id', 'resource_id'])

        # Adding M2M table for field themes on 'Video'
        db.create_table('machine_video_themes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['machine.video'], null=False)),
            ('theme', models.ForeignKey(orm['machine.theme'], null=False))
        ))
        db.create_unique('machine_video_themes', ['video_id', 'theme_id'])

        # Adding M2M table for field keywords on 'Video'
        db.create_table('machine_video_keywords', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['machine.video'], null=False)),
            ('keyword', models.ForeignKey(orm['machine.keyword'], null=False))
        ))
        db.create_unique('machine_video_keywords', ['video_id', 'keyword_id'])


    def backwards(self, orm):
        # Deleting model 'Resource'
        db.delete_table('machine_resource')

        # Deleting model 'Theme'
        db.delete_table('machine_theme')

        # Deleting model 'Keyword'
        db.delete_table('machine_keyword')

        # Deleting model 'Video'
        db.delete_table('machine_video')

        # Removing M2M table for field resources on 'Video'
        db.delete_table('machine_video_resources')

        # Removing M2M table for field themes on 'Video'
        db.delete_table('machine_video_themes')

        # Removing M2M table for field keywords on 'Video'
        db.delete_table('machine_video_keywords')


    models = {
        'machine.keyword': {
            'Meta': {'ordering': "('keyword',)", 'object_name': 'Keyword'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'machine.resource': {
            'Meta': {'object_name': 'Resource'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resource': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'machine.theme': {
            'Meta': {'ordering': "('theme',)", 'object_name': 'Theme'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'theme': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'machine.video': {
            'Meta': {'ordering': "('title', 'scene')", 'object_name': 'Video'},
            'author': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'commentary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'copyrightdate': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'copyrightholder': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'full_text': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_filename': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'default': "'http://www.columbia.edu/itc/tc/cstudies/imagesequence/'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['machine.Keyword']", 'symmetrical': 'False'}),
            'local_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'local_video': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'plot': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'questions': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'real_video_filename': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'real_video_url': ('django.db.models.fields.URLField', [], {'default': "'http://kola.cc.columbia.edu:8080/ramgen/itcmedia/tc/culturalstudies/'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'resources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['machine.Resource']", 'symmetrical': 'False'}),
            'scene': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'screenplay': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'sequence_count': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'sequence_prefix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sequence_url': ('django.db.models.fields.URLField', [], {'default': "'http://www.columbia.edu/itc/tc/cstudies/imagesequence/'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'themes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['machine.Theme']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['machine']
