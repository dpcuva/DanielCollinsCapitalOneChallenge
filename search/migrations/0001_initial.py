# Generated by Django 2.1.7 on 2019-03-17 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lower_Year_Bound', models.IntegerField(help_text='(YYYY)')),
                ('Upper_Year_Bound', models.IntegerField(help_text='(YYYY)')),
                ('Keywords', models.CharField(max_length=400)),
            ],
        ),
    ]
