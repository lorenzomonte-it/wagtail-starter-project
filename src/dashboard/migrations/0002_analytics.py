# Generated by Django 3.2.4 on 2021-06-30 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_tag_head', models.TextField(blank=True, help_text='Aggiungi lo script di Google Tag Manager per il tag <head></head>', null=True, verbose_name='Google Tag Manager <head>')),
                ('google_tag_body', models.TextField(blank=True, help_text='Aggiungi lo script di Google Tag Manager per il tag <body></body>', null=True, verbose_name='Google Tag Manager <body>')),
                ('google_analytics', models.CharField(blank=True, help_text='Il tuo Google Analytics tracking ID (inizia con "UA-")', max_length=20, null=True, verbose_name='Google Analytics Traking ID')),
                ('facebook_pixel', models.TextField(blank=True, help_text='Aggiungi lo script di Facebook Pixel', null=True, verbose_name='Facebook Pixel')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Analytics',
                'verbose_name_plural': 'Analytics',
            },
        ),
    ]
