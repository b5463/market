# Generated by Django 4.1 on 2022-08-31 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_forumcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.CharField(choices=[('l', 'Like'), ('d', 'Dislike')], default='l', max_length=1)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='forum.forum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_rate', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]