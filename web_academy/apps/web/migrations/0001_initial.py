# Generated by Django 3.1.7 on 2021-04-22 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True)),
                ('create_to', models.DateTimeField(auto_now_add=True)),
                ('update_to', models.DateTimeField(auto_now=True)),
                ('company', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/about/')),
                ('about_us', models.TextField()),
                ('name2', models.CharField(blank=True, max_length=100, null=True)),
                ('detail', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('title_resume', models.CharField(blank=True, max_length=200, null=True)),
                ('resume', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'AboutUs',
                'verbose_name_plural': 'AboutsUs',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True)),
                ('create_to', models.DateTimeField(auto_now_add=True)),
                ('update_to', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='ExternalServices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True)),
                ('create_to', models.DateTimeField(auto_now_add=True)),
                ('update_to', models.DateTimeField(auto_now=True)),
                ('name_test', models.CharField(max_length=200)),
                ('test', models.URLField(blank=True, null=True)),
                ('name_theoretical', models.CharField(max_length=200)),
                ('theoretical', models.URLField(blank=True, null=True)),
                ('name_reservation', models.CharField(max_length=200)),
                ('reservation', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'ExternalService',
                'verbose_name_plural': 'ExternalServices',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True)),
                ('create_to', models.DateTimeField(auto_now_add=True)),
                ('update_to', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=254, unique=True)),
                ('price', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(upload_to='images/lesson/')),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('quantity_lesson', models.PositiveIntegerField(default=0)),
                ('description', models.TextField()),
                ('resume', models.TextField()),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True)),
                ('create_to', models.DateTimeField(auto_now_add=True)),
                ('update_to', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/offer')),
                ('resume', models.TextField()),
                ('description', models.TextField()),
                ('period', models.CharField(max_length=200)),
                ('published', models.BooleanField(default=False)),
                ('published_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Offer',
                'verbose_name_plural': 'Offers',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True)),
                ('create_to', models.DateTimeField(auto_now_add=True)),
                ('update_to', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('name2', models.CharField(max_length=50)),
                ('resume', models.TextField()),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/post')),
                ('published', models.BooleanField(default=False)),
                ('published_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True)),
                ('create_to', models.DateTimeField(auto_now_add=True)),
                ('update_to', models.DateTimeField(auto_now=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Socials',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True)),
                ('create_to', models.DateTimeField(auto_now_add=True)),
                ('update_to', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=200)),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True)),
                ('create_to', models.DateTimeField(auto_now_add=True)),
                ('update_to', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/teacher/')),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True)),
                ('create_to', models.DateTimeField(auto_now_add=True)),
                ('update_to', models.DateTimeField(auto_now=True)),
                ('detail', models.TextField()),
                ('image', models.ImageField(upload_to='images/testimonial/')),
                ('author', models.CharField(max_length=200)),
                ('published', models.BooleanField(default=False)),
                ('published_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]
