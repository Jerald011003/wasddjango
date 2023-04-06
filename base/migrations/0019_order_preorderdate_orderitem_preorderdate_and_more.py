# Generated by Django 4.1.7 on 2023-04-01 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_friend_comment_friend_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='preorderdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='preorderdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='numofPreorder',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='preorderdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='watch',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='download',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='download',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='download',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]