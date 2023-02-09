# Generated by Django 4.0 on 2023-02-09 19:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sancheck', '0003_parktag_num_upvotes_delete_upvotetag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parktag',
            name='num_upvotes',
            field=models.ManyToManyField(default=1, related_name='tag_upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
