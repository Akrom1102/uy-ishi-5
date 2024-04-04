

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('street', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.address')),
            ],
        ),
    ]
