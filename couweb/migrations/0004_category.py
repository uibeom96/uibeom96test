# Generated by Django 3.2 on 2021-04-20 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couweb', '0003_alter_webs_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(blank=True, default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True)),
            ],
            options={
                'verbose_name': '카테고리들',
                'verbose_name_plural': '카테고리',
                'db_table': 'category',
                'ordering': ('-created',),
            },
        ),
    ]
