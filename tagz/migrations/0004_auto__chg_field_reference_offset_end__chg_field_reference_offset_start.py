# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Reference.offset_end'
        db.alter_column('tagz_reference', 'offset_end', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Reference.offset_start'
        db.alter_column('tagz_reference', 'offset_start', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Reference.offset_end'
        db.alter_column('tagz_reference', 'offset_end', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Reference.offset_start'
        db.alter_column('tagz_reference', 'offset_start', self.gf('django.db.models.fields.IntegerField')(default=0))

    models = {
        'tagz.reference': {
            'Meta': {'ordering': "['offset_start', 'offset_end', 'resource', 'reference', 'tag']", 'object_name': 'Reference'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offset_end': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'offset_start': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'resource': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tagz.Tag']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        'tagz.tag': {
            'Meta': {'ordering': "['tag']", 'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        }
    }

    complete_apps = ['tagz']