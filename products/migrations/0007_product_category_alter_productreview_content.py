# Generated by Django 4.0 on 2022-10-24 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_productreview_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('pizza', 'Пицца'), ('drinks and snacks', 'Напитки и закуски')], default='pizza', max_length=50),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name=''),
        ),
    ]
