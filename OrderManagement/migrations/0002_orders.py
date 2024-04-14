# Generated by Django 4.2.11 on 2024-03-31 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
        ('OrderManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_number', models.CharField(max_length=20, null=True)),
                ('o_date', models.DateField(null=True)),
                ('quantity', models.FloatField(default=0)),
                ('amount', models.FloatField(default=0)),
                ('gst_amt', models.FloatField(default=0)),
                ('bill_amt', models.FloatField(default=0)),
                ('c_reference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='OrderManagement.custumer')),
                ('p_reference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Inventory.product')),
            ],
        ),
    ]
