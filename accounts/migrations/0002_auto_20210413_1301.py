# Generated by Django 3.1.7 on 2021-04-13 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='date_created',
            field=models.DateTimeField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='profile_picture',
            field=models.ImageField(default='profile.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='owner',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
