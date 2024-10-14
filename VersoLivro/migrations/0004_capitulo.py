# Generated by Django 5.1.1 on 2024-10-09 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VersoLivro', '0003_alter_livro_capa_delete_capa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('titulo', models.CharField(help_text='nome', max_length=30)),
                ('texto', models.TextField(default='Texto..')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VersoLivro.livro')),
            ],
        ),
    ]
