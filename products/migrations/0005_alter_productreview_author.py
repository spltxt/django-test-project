# Generated by Django 4.0 on 2022-10-19 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('products', '0004_alter_productreview_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
