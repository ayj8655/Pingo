# Generated by Django 3.2.7 on 2021-10-01 13:56

from django.db import migrations, models
import django.db.models.deletion
import paint_game.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('word_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=50)),
                ('room_password', models.CharField(max_length=50, null=True)),
                ('problems', models.IntegerField()),
                ('max_head_counts', models.IntegerField()),
                ('is_locked', models.BooleanField()),
                ('is_started', models.BooleanField()),
                ('room_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.accounts')),
            ],
        ),
        migrations.CreateModel(
            name='UserInRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paint_game.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.accounts')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paint_game.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.accounts')),
            ],
        ),
        migrations.CreateModel(
            name='Paint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(storage=paint_game.models.OverwriteStorage(), upload_to=paint_game.models.get_name)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paint_game.categories')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paint_game.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.accounts')),
            ],
        ),
    ]
