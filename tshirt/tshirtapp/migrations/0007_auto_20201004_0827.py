# Generated by Django 3.0.6 on 2020-10-04 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tshirtapp', '0006_shippingaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Brand', models.CharField(max_length=100)),
                ('Size', models.CharField(max_length=100)),
                ('Price', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='pics')),
                ('Gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='men_product',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='women_product',
        ),
        migrations.DeleteModel(
            name='Men',
        ),
        migrations.DeleteModel(
            name='Women',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tshirtapp.Product'),
        ),
    ]
