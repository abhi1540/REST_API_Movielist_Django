# Generated by Django 2.0.2 on 2018-05-14 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movielist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie_Id', models.CharField(max_length=30)),
                ('Movie_Name', models.CharField(max_length=100)),
                ('Release_Date', models.DateField(max_length=100)),
                ('Rating', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['Release_Date'],
            },
        ),
        migrations.AddIndex(
            model_name='movielist',
            index=models.Index(fields=['Movie_Id'], name='moviesapp_m_Movie_I_2727a1_idx'),
        ),
    ]
