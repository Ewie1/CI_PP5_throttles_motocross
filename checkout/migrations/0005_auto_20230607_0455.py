# Generated by Django 3.2.18 on 2023-06-07 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('checkout', '0004_alter_order_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.userprofile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address1',
            field=models.CharField(default='', max_length=85),
        ),
        migrations.AlterField(
            model_name='order',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=85, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, default='', max_length=85, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(default='', max_length=55),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='', editable=False, max_length=35),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, default='', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(default='', max_length=45),
        ),
    ]
