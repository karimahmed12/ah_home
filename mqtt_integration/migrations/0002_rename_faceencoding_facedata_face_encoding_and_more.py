# Generated by Django 4.1.13 on 2024-04-30 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mqtt_integration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facedata',
            old_name='faceEncoding',
            new_name='face_encoding',
        ),
        migrations.RenameField(
            model_name='facedata',
            old_name='userId',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='numericaldata',
            old_name='gasLevel',
            new_name='gas_level',
        ),
        migrations.RenameField(
            model_name='numericaldata',
            old_name='userId',
            new_name='user_id',
        ),
        migrations.AlterField(
            model_name='facedata',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='numericaldata',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
