# Generated by Django 2.2.4 on 2019-09-16 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0004_auto_20190911_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_orcamento', models.IntegerField(max_length=10)),
                ('nome', models.CharField(max_length=30)),
                ('data', models.DateField()),
                ('valor_total', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
    ]