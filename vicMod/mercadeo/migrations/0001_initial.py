# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 03:37
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('c_nombre', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dueno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_nombre', models.CharField(max_length=200)),
                ('m_alias', models.CharField(max_length=30)),
                ('m_direccion', models.TextField()),
                ('m_correo', models.EmailField(blank=True, default='victrois@gmail.com', max_length=70)),
                ('m_razon_social', models.CharField(max_length=150)),
                ('m_doc_ident', models.CharField(max_length=30)),
                ('m_descripcion', models.TextField()),
                ('m_public', models.BooleanField(default=True)),
                ('m_moneda', models.CharField(choices=[('$  ', '$'), ('Bs.', 'Bs.'), ('€  ', '€')], default='Bs.', max_length=3)),
                ('m_boletin', models.BooleanField(default=True)),
                ('m_est_irrev', models.IntegerField(default=2)),
                ('m_est_rrev', models.IntegerField(default=4)),
                ('m_ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercadeo.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="El telefono debe estar en formato: '+999999999'.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_secondname', models.CharField(max_length=30)),
                ('u_secondlastname', models.CharField(max_length=30)),
                ('u_alias', models.CharField(max_length=100)),
                ('u_direccion', models.TextField()),
                ('u_fecha_nac', models.DateField(blank=True, default=datetime.datetime.now)),
                ('u_entrenador', models.BooleanField(default=False)),
                ('u_marca', models.BooleanField(default=False)),
                ('u_displinafav1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fav1', to='mercadeo.Disciplina')),
                ('u_displinafav2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fav2', to='mercadeo.Disciplina')),
                ('u_displinafav3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fav3', to='mercadeo.Disciplina')),
                ('u_telefono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercadeo.Phone')),
                ('u_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('z_municipio', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('z_ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercadeo.Ciudad')),
            ],
        ),
        migrations.AddField(
            model_name='marca',
            name='m_municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercadeo.Zona'),
        ),
        migrations.AddField(
            model_name='marca',
            name='m_telefono1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='principal', to='mercadeo.Phone'),
        ),
        migrations.AddField(
            model_name='marca',
            name='m_telefono2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercadeo.Phone'),
        ),
        migrations.AddField(
            model_name='dueno',
            name='d_marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercadeo.Marca'),
        ),
        migrations.AddField(
            model_name='dueno',
            name='d_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]