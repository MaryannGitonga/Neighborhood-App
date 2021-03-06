# Generated by Django 2.0 on 2018-11-22 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('business_neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.Neighborhood')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.User')),
            ],
        ),
    ]
