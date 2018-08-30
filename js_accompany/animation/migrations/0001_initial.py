# Generated by Django 2.1 on 2018-08-30 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criterion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('long_name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('name', 'training'),
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('advices', models.CharField(blank=True, max_length=1024)),
                ('fields', models.ManyToManyField(to='animation.Field')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='module',
            name='skills',
            field=models.ManyToManyField(to='animation.Skill'),
        ),
        migrations.AddField(
            model_name='module',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animation.Training'),
        ),
        migrations.AddField(
            model_name='criterion',
            name='skills',
            field=models.ManyToManyField(to='animation.Skill'),
        ),
    ]