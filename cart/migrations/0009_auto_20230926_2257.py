# Generated by Django 3.1.6 on 2023-09-26 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0010_auto_20230926_2028'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0008_auto_20230925_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='playtime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.playtime'),
        ),
    ]
