# Generated by Django 4.0.5 on 2022-06-02 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
