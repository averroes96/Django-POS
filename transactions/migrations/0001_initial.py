# Generated by Django 3.2.15 on 2022-09-15 17:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agents', '0002_init_agents_permissions'),
        ('sells', '0001_initial'),
        ('buys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierTransaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('value', models.IntegerField()),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='agents.agent')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='buys.supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('value', models.IntegerField()),
                ('type', models.IntegerField(choices=[(1, 'employees')])),
                ('note', models.TextField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agents.agent')),
            ],
            options={
                'ordering': ['-created_at'],
                'get_latest_by': ['created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClientTransaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('value', models.IntegerField()),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='agents.agent')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sells.client')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
