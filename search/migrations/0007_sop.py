# Generated by Django 2.2.12 on 2021-07-27 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20210703_0809'),
    ]

    operations = [
        migrations.CreateModel(
            name='sop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('operator', models.CharField(max_length=100)),
                ('appt', models.CharField(max_length=100)),
                ('apname', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('ip', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='static/pdf')),
            ],
            options={
                'db_table': 'sop',
            },
        ),
    ]