# Generated by Django 4.1.6 on 2023-02-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('P', 'Patient'), ('D', 'Doctor')], default='P', max_length=2, verbose_name='Type'),
        ),
    ]