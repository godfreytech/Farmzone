# Generated by Django 3.0 on 2020-05-31 19:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('chat_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('message', models.TextField(max_length=1255)),
                ('message_post_time', models.DateTimeField(auto_now_add=True)),
                ('ads_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.ProductsAds')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.Category')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.Users')),
            ],
            options={
                'db_table': 'Chat',
            },
        ),
    ]
