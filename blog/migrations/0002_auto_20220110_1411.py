# Generated by Django 3.2.11 on 2022-01-10 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]