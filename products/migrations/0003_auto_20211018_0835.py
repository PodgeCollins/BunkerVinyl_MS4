# Generated by Django 3.2.8 on 2021-10-18 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211018_0829'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genre',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='genre',
            new_name='category',
        ),
    ]