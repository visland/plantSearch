# Generated by Django 3.0.dev20190216065628 on 2019-03-12 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hzTree', '0008_auto_20190312_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='months',
            name='name',
            field=models.CharField(choices=[('Jan', '1月'), ('Feb', '2月'), ('Mar', '3月'), ('Apr', '4月'), ('May', '5月'), ('Jun', '6月'), ('Jul', '7月'), ('Aug', '8月'), ('Sep', '9月'), ('Oct', '10月'), ('Nov', '11月'), ('Dec', '12月')], max_length=12),
        ),
    ]