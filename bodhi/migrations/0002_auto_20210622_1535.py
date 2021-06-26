# Generated by Django 3.2.4 on 2021-06-22 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodhi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='content',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='img',
            field=models.ImageField(null=True, upload_to='img/about'),
        ),
        migrations.AddField(
            model_name='carousel',
            name='Img',
            field=models.ImageField(null=True, upload_to='img/carousel'),
        ),
        migrations.AddField(
            model_name='carousel',
            name='des',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='carousel',
            name='heading',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='carousel',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='content',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='gif',
            field=models.ImageField(null=True, upload_to='img/services'),
        ),
        migrations.AddField(
            model_name='services',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
