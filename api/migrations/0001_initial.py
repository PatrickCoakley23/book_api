# Generated by Django 5.0.4 on 2024-05-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Unread', 'Unread'), ('In Progress', 'In Progress'), ('Finished', 'Finished')], default='Unread', max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Books',
            },
        ),
    ]