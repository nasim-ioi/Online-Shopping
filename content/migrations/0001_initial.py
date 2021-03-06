# Generated by Django 2.2 on 2020-02-03 12:39

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('dateclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.DateClass')),
            ],
            bases=('content.dateclass',),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('dateclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.DateClass')),
                ('name', models.CharField(choices=[('laptop', 'laptops'), ('mobile', 'mobile'), ('electric_ferniture', 'electric_ferniture')], max_length=50)),
            ],
            bases=('content.dateclass',),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('dateclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.DateClass')),
                ('title', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=50)),
                ('made_in', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField()),
                ('exist', models.BooleanField()),
                ('price', models.PositiveIntegerField()),
                ('color', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None)),
                ('of_this_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', related_query_name='item', to='content.Category', verbose_name='category_relation')),
            ],
            bases=('content.dateclass',),
        ),
        migrations.CreateModel(
            name='laptop',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.Item')),
                ('ram', models.SmallIntegerField()),
                ('cpu', models.CharField(max_length=50)),
                ('graphic_card', models.CharField(max_length=50)),
            ],
            bases=('content.item',),
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.Item')),
                ('ram', models.SmallIntegerField()),
                ('touch', models.BooleanField()),
                ('camera', models.CharField(max_length=50)),
            ],
            bases=('content.item',),
        ),
        migrations.CreateModel(
            name='Refrigerator',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.Item')),
                ('side_by_side', models.BooleanField()),
                ('tavan_masrafy', models.CharField(max_length=50)),
            ],
            bases=('content.item',),
        ),
        migrations.CreateModel(
            name='WashingMachine',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.Item')),
                ('tavan_masrafy', models.CharField(max_length=50)),
            ],
            bases=('content.item',),
        ),
        migrations.CreateModel(
            name='CartDetailThrough',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('color', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartdetails', related_query_name='cartdetail', to='content.Cart')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartdetails2', related_query_name='cartdetail2', to='content.Item')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ManyToManyField(related_name='carts', related_query_name='cart', through='content.CartDetailThrough', to='content.Item'),
        ),
        migrations.AddField(
            model_name='cart',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profilecarts', related_query_name='profilecart', to='user.Profile'),
        ),
    ]
