# Generated by Django 4.1.1 on 2022-12-11 17:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartas',
            fields=[
                ('idbiblioteca', models.IntegerField(primary_key=True, serialize=False, verbose_name='IDBIBLIOTECA')),
                ('juego', models.TextField(default='Juego', max_length=50, verbose_name='JUEGO')),
                ('sets', models.TextField(default='Sets', max_length=50, verbose_name='SETS')),
                ('idcarta', models.IntegerField(default=0, verbose_name='IDCARTA')),
                ('nombrecarta', models.TextField(default='Nombre Carta', max_length=50, verbose_name='NOMBRECARTA')),
                ('habilidad', models.TextField(default='Habilidad', max_length=250, verbose_name='HABILIDAD')),
                ('keyword', models.TextField(default='Keyword', max_length=50, verbose_name='KEYWORD')),
                ('costomana', models.IntegerField(default=0, verbose_name='COSTOMANA')),
                ('fuerza', models.IntegerField(default=0, verbose_name='FUERZA')),
                ('salud', models.IntegerField(default=0, verbose_name='SALUD')),
                ('rareza', models.TextField(default='Rareza', max_length=50, verbose_name='RAREZA')),
                ('tipocarta', models.TextField(default='Tipo carta', max_length=50, verbose_name='TIPOCARTA')),
                ('region', models.TextField(default='Region', max_length=50, verbose_name='REGION')),
                ('tipohechizo', models.TextField(default='Tipo hechizo', max_length=50, verbose_name='TIPOHECHIZO')),
            ],
            options={
                'db_table': 'home_cartas',
            },
        ),
        migrations.CreateModel(
            name='Observaciones',
            fields=[
                ('idobservacion', models.IntegerField(primary_key=True, serialize=False, verbose_name='IDOBSERVACION')),
                ('nombrejugador', models.TextField(default='Juego', max_length=50, verbose_name='NOMBREJUGADOR')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('actividad', models.TextField(default=0, verbose_name='ACTIVIDAD')),
                ('observacion', models.TextField(default='Nombre Carta', max_length=50, verbose_name='OBSERVACION')),
            ],
            options={
                'db_table': 'home_observaciones',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('clave', models.CharField(default='', max_length=50)),
            ],
            options={
                'db_table': 'home_usuarios',
            },
        ),
    ]
