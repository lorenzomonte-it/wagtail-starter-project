# Generated by Django 3.2.4 on 2021-06-30 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('dashboard', '0002_analytics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='favicon', to='wagtailimages.image', verbose_name='Favicon')),
                ('logo', models.ForeignKey(blank=True, help_text='Brand logo per tutto il sito', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logo', to='wagtailimages.image', verbose_name='Logo')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Branding',
                'verbose_name_plural': 'Branding',
            },
        ),
    ]