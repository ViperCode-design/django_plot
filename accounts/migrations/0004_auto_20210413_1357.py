# Generated by Django 3.2 on 2021-04-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_owner_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
