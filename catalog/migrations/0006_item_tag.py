# Generated by Django 3.0 on 2020-07-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tag',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
