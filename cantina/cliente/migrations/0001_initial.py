# Generated by Django 5.0.dev20230218152810 on 2023-02-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ItemDeMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(upload_to='imagens_menu/')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('categoria', models.ManyToManyField(related_name='item', to='cliente.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='ModeloPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('itens', models.ManyToManyField(blank=True, related_name='pedido', to='cliente.itemdemenu')),
            ],
        ),
    ]
