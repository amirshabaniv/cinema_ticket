# Generated by Django 3.1.6 on 2023-09-26 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0006_auto_20230926_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinema',
            old_name='card_khan',
            new_name='cart_reader',
        ),
    ]