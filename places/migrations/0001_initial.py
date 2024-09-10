# Generated by Django 5.0.1 on 2024-09-09 07:25

import django.db.models.deletion
import modelcluster.fields
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0092_formsubmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacesPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('description', wagtail.fields.RichTextField(blank=True, help_text='Description of the places', null=True)),
            ],
            options={
                'verbose_name': 'Places Page',
                'verbose_name_plural': 'Places Pages',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('place_name', models.CharField(help_text='Name of the place', max_length=255)),
                ('place_id', models.CharField(blank=True, help_text='Google Place ID', max_length=255, null=True)),
                ('address', models.CharField(blank=True, help_text='Address of the place', max_length=255, null=True)),
                ('description', wagtail.fields.RichTextField(blank=True, help_text='Description of the place', null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='places.placespage')),
            ],
            options={
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
                'ordering': ['sort_order'],
            },
        ),
    ]
