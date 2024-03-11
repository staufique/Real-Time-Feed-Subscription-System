# Generated by Django 5.0.3 on 2024-03-11 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_user_delete_distributeddata'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
