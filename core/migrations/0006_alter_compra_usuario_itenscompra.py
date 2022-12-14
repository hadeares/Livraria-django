# Generated by Django 4.1 on 2022-08-30 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='compras', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ItensCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='core.compra')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.livros')),
            ],
        ),
    ]
