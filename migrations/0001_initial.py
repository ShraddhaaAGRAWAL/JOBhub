# Generated by Django 4.0.3 on 2022-05-04 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=500)),
                ('review', models.TextField(blank=True, max_length=500)),
                ('rating', models.FloatField(default=5)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='jobseeker',
            fields=[
                ('J_email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('J_fname', models.CharField(max_length=20)),
                ('J_lname', models.CharField(max_length=20, null=True)),
                ('J_address', models.CharField(max_length=50)),
                ('J_city', models.CharField(max_length=15)),
                ('J_experience', models.CharField(max_length=15)),
                ('J_state', models.CharField(max_length=15)),
                ('J_dob', models.CharField(max_length=10)),
                ('J_gender', models.CharField(max_length=10)),
                ('J_contact', models.CharField(max_length=10)),
                ('J_password', models.CharField(max_length=50)),
                ('J_education', models.CharField(max_length=20)),
                ('J_skill', models.TextField(max_length=100, null=True)),
                ('forget_password_token', models.CharField(max_length=100)),
                ('auth_token', models.CharField(default='', editable=False, max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='jobprovider',
            fields=[
                ('U_email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('U_name', models.CharField(max_length=20)),
                ('U_address', models.CharField(max_length=50)),
                ('U_contact', models.CharField(max_length=10)),
                ('U_password', models.CharField(max_length=50)),
                ('U_website', models.CharField(max_length=20, null=True)),
                ('U_about', models.TextField(max_length=100, null=True)),
                ('forget_password_token', models.CharField(max_length=100)),
                ('auth_token', models.CharField(default='', editable=False, max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('title', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('contact', models.TextField(max_length=10)),
                ('experience', models.CharField(max_length=100)),
                ('salary', models.FloatField(max_length=20)),
                ('filter1', models.CharField(default='Interested Field', max_length=20)),
                ('filter2', models.CharField(default='Location', max_length=20)),
                ('skills', models.TextField(max_length=100)),
                ('role', models.TextField(max_length=100)),
                ('about', models.TextField(max_length=100, null=True)),
                ('creationdate', models.DateField()),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobhub.jobprovider')),
            ],
        ),
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='')),
                ('applydate', models.DateField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobhub.job')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobhub.jobseeker')),
            ],
        ),
    ]
