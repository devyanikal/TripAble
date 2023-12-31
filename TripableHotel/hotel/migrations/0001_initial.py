# Generated by Django 3.2.19 on 2023-11-06 19:45

from django.db import migrations, models
import django.utils.timezone
import hotel.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('hotel_name', models.CharField(max_length=240, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('username', models.CharField(max_length=20, null=True, unique=True)),
                ('prefix', models.CharField(max_length=4)),
                ('mobile', models.CharField(max_length=10)),
                ('hotel_profile_image', models.ImageField(upload_to='profile')),
                ('landmark', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('pincode', models.IntegerField(default=0)),
                ('visual_impaired', models.BooleanField(default=False)),
                ('wheelchair_user', models.BooleanField(default=False)),
                ('hearing_impaired', models.BooleanField(default=False)),
                ('speech_impaired', models.BooleanField(default=False)),
                ('roomtype1', models.CharField(default='', max_length=100)),
                ('roomtype2', models.CharField(default='', max_length=100)),
                ('roomtype3', models.CharField(default='', max_length=100)),
                ('pricetype1', models.IntegerField(default=0)),
                ('pricetype2', models.IntegerField(default=0)),
                ('pricetype3', models.IntegerField(default=0)),
                ('numOftype1', models.IntegerField(default=0)),
                ('numOftype2', models.IntegerField(default=0)),
                ('numOftype3', models.IntegerField(default=0)),
                ('facilityoftype1', models.CharField(default='', max_length=500)),
                ('facilityoftype2', models.CharField(default='', max_length=500)),
                ('facilityoftype3', models.CharField(default='', max_length=500)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', hotel.models.UserManager()),
            ],
        ),
    ]
