# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, null=True, verbose_name='Title')),
                ('image', models.ImageField(upload_to=b'jssor', null=True, verbose_name='Image')),
                ('thumbnail', models.ImageField(upload_to=b'jssor/thumbnails', null=True, verbose_name='Thumbnail', blank=True)),
                ('order', models.PositiveSmallIntegerField(null=True, verbose_name='Order')),
                ('link', models.CharField(max_length=255, null=True, verbose_name='Link', blank=True)),
                ('link_is_blank', models.BooleanField(default=False, verbose_name='Open link in a new tab')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slides',
            },
        ),
        migrations.CreateModel(
            name='Slideshow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, null=True, verbose_name='Title')),
                ('slug', models.SlugField(default=b'', max_length=150, help_text='This field must not contain any spaces, special characters or capital letter', unique=True, verbose_name='Id')),
                ('template_name', models.CharField(default=b'jssor/full_width_slider.html', max_length=150, null=True, verbose_name='Slideshow type', choices=[(b'jssor/full_width_slider.html', 'Full width slider'), (b'jssor/thumbnails_navigator_with_arrows.html', 'Thumbnails navigator with arrows'), (b'jssor/banner_slider.html', 'Banner slider'), (b'jssor/bootstrap_slider.html', 'Bootstrap slider')])),
                ('autoplay', models.BooleanField(default=False, verbose_name='Autoplay')),
                ('width', models.PositiveSmallIntegerField(null=True, verbose_name='Width', blank=True)),
                ('height', models.PositiveSmallIntegerField(null=True, verbose_name='Height', blank=True)),
            ],
            options={
                'verbose_name': 'Slideshow',
                'verbose_name_plural': 'Slideshows',
            },
        ),
        migrations.AddField(
            model_name='slide',
            name='slideshow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Slideshow', to='jssor.Slideshow', null=True),
        ),
    ]
