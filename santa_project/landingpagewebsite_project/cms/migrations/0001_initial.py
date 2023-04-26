# Generated by Django 3.2 on 2022-01-03 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CMSSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cms_img', models.ImageField(upload_to='sliderimg/')),
                ('cms_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('cms_text', models.CharField(max_length=200, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]
