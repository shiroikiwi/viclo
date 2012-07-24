# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Poll'
        db.delete_table('vicloapp_poll')

        # Deleting model 'Choice'
        db.delete_table('vicloapp_choice')


    def backwards(self, orm):
        # Adding model 'Poll'
        db.create_table('vicloapp_poll', (
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('vicloapp', ['Poll'])

        # Adding model 'Choice'
        db.create_table('vicloapp_choice', (
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vicloapp.Poll'])),
            ('choice_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('votes', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('vicloapp', ['Choice'])


    models = {
        
    }

    complete_apps = ['vicloapp']