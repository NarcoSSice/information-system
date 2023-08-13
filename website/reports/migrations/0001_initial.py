# Generated by Django 4.2 on 2023-05-25 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
            ],
            options={
                'db_table': 'reports_category',
            },
        ),
        migrations.CreateModel(
            name='Two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.category')),
            ],
            options={
                'db_table': 'reports_2',
            },
        ),
        migrations.CreateModel(
            name='Three',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.category')),
            ],
            options={
                'db_table': 'reports_3',
            },
        ),
        migrations.CreateModel(
            name='Six',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.category')),
            ],
            options={
                'db_table': 'reports_6',
            },
        ),
        migrations.CreateModel(
            name='Seven',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.category')),
            ],
            options={
                'db_table': 'reports_7',
            },
        ),
        migrations.CreateModel(
            name='One',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.category')),
            ],
            options={
                'db_table': 'reports_1',
            },
        ),
        migrations.CreateModel(
            name='Four',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.category')),
            ],
            options={
                'db_table': 'reports_4',
            },
        ),
        migrations.CreateModel(
            name='FiveTwoTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.category')),
            ],
            options={
                'db_table': 'reports_5.2.2',
            },
        ),
        migrations.CreateModel(
            name='FiveTwoOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.category')),
            ],
            options={
                'db_table': 'reports_5.2.1',
            },
        ),
        migrations.CreateModel(
            name='FiveThreeTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.category')),
            ],
            options={
                'db_table': 'reports_5.3.2',
            },
        ),
        migrations.CreateModel(
            name='FiveThreeOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.category')),
            ],
            options={
                'db_table': 'reports_5.3.1',
            },
        ),
        migrations.CreateModel(
            name='FiveOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.category')),
            ],
            options={
                'db_table': 'reports_5.1',
            },
        ),
        migrations.CreateModel(
            name='FiveFourTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.category')),
            ],
            options={
                'db_table': 'reports_5.4.2',
            },
        ),
        migrations.CreateModel(
            name='FiveFourOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.category')),
            ],
            options={
                'db_table': 'reports_5.4.1',
            },
        ),
        migrations.CreateModel(
            name='AllReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.category')),
            ],
            options={
                'db_table': 'reports_all',
            },
        ),
    ]
