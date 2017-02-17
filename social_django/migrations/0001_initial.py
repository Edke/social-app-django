# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import social_django.fields
import social_django.storage


class Migration(migrations.Migration):

    dependencies = [
        ('aquareina', '0146_pointcreditlinkatransaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_url', models.CharField(max_length=255)),
                ('handle', models.CharField(max_length=255)),
                ('secret', models.CharField(max_length=255)),
                ('issued', models.IntegerField()),
                ('lifetime', models.IntegerField()),
                ('assoc_type', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'social_auth_association',
            },
            bases=(models.Model, social_django.storage.DjangoAssociationMixin),
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('code', models.CharField(max_length=32, db_index=True)),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'social_auth_code',
            },
            bases=(models.Model, social_django.storage.DjangoCodeMixin),
        ),
        migrations.CreateModel(
            name='Nonce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_url', models.CharField(max_length=255)),
                ('timestamp', models.IntegerField()),
                ('salt', models.CharField(max_length=65)),
            ],
            options={
                'db_table': 'social_auth_nonce',
            },
            bases=(models.Model, social_django.storage.DjangoNonceMixin),
        ),
        migrations.CreateModel(
            name='Partial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=32, db_index=True)),
                ('next_step', models.PositiveSmallIntegerField(default=0)),
                ('backend', models.CharField(max_length=32)),
                ('data', social_django.fields.JSONField(default={})),
            ],
            options={
                'db_table': 'social_auth_partial',
            },
            bases=(models.Model, social_django.storage.DjangoPartialMixin),
        ),
        migrations.CreateModel(
            name='UserSocialAuth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider', models.CharField(max_length=32)),
                ('uid', models.CharField(max_length=255)),
                ('extra_data', social_django.fields.JSONField(default={})),
                ('user', models.ForeignKey(related_name='social_auth', to='aquareina.Client')),
            ],
            options={
                'db_table': 'social_auth_usersocialauth',
            },
            bases=(models.Model, social_django.storage.DjangoUserMixin),
        ),
        migrations.AlterUniqueTogether(
            name='nonce',
            unique_together=set([('server_url', 'timestamp', 'salt')]),
        ),
        migrations.AlterUniqueTogether(
            name='code',
            unique_together=set([('email', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='association',
            unique_together=set([('server_url', 'handle')]),
        ),
        migrations.AlterUniqueTogether(
            name='usersocialauth',
            unique_together=set([('provider', 'uid')]),
        ),
    ]
