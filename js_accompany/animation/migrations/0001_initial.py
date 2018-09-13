# Generated by Django 2.1 on 2018-09-11 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criterion',
            fields=[
                ('tagable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tags.Tagable')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=('tags.tagable',),
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('tagable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tags.Tagable')),
                ('name', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('tags.tagable',),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('tagable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tags.Tagable')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('of_training', 'name'),
            },
            bases=('tags.tagable',),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('tagable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tags.Tagable')),
                ('name', models.CharField(max_length=255)),
                ('advices', models.TextField(blank=True, max_length=1024)),
                ('fields', models.ManyToManyField(to='animation.Field')),
            ],
            options={
                'abstract': False,
            },
            bases=('tags.tagable',),
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('tagable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tags.Tagable')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('tags.tagable',),
        ),
        migrations.AddField(
            model_name='module',
            name='of_training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animation.Training'),
        ),
        migrations.AddField(
            model_name='module',
            name='skills',
            field=models.ManyToManyField(to='animation.Skill'),
        ),
        migrations.AddField(
            model_name='criterion',
            name='skills',
            field=models.ManyToManyField(to='animation.Skill'),
        ),
    ]
