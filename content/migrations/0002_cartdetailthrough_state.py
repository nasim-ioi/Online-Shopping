# Generated by Django 2.2 on 2020-02-04 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdetailthrough',
            name='state',
            field=models.CharField(choices=[('bought', 'bought'), ('selected', 'selected')], default='selected', max_length=20),
            preserve_default=False,
        ),
    ]