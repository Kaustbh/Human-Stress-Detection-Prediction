# Generated by Django 5.1.3 on 2024-11-11 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict_risk', '0005_alter_predictions_sr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions',
            name='blood_ol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='bt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='em',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='hr',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='lm',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='rr',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='sh',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='sr',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
