# Generated by Django 2.1 on 2018-09-29 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0002_election'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='election_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='election.Election'),
            preserve_default=False,
        ),
    ]
