# Generated by Django 3.1.3 on 2020-12-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_administrator_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='upload',
            field=models.FileField(default='Unnamed File', upload_to='files/certificates'),
        ),
    ]
