# Generated by Django 3.2.15 on 2022-09-23 18:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleBrand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ['-created_at'],
                'get_latest_by': ['created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleFamily',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Article families',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ['-created_at'],
                'get_latest_by': ['created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('reference', models.CharField(max_length=128, unique=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('quantity_minimum', models.IntegerField(default=0)),
                ('stock_negative', models.BooleanField(default=False)),
                ('margin', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
                ('buy_price', models.PositiveIntegerField()),
                ('sell_price', models.PositiveIntegerField()),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.articlebrand')),
                ('family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.articlefamily')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.unit')),
            ],
        ),
        migrations.AddConstraint(
            model_name='article',
            constraint=models.CheckConstraint(check=models.Q(('quantity__gte', 0), ('stock_negative', False), ('quantity_minimum__gte', 0)), name='check_stock'),
        ),
    ]
