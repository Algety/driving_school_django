# Generated by Django 4.2.22 on 2025-06-12 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_contentblock_block_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contentblock',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='contentblock',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
