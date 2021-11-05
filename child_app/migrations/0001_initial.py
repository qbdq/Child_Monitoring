# Generated by Django 3.2.9 on 2021-11-05 21:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emplacement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SiteName', models.CharField(max_length=50)),
                ('SiteAdresse', models.CharField(max_length=50)),
                ('Remark', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Enfant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30, verbose_name='Child Last Name')),
                ('LastName', models.CharField(max_length=30, verbose_name='Child Last Name')),
                ('DOB', models.DateField(default=django.utils.timezone.now)),
                ('Education', models.CharField(blank=True, choices=[('P1', '1 ére primaire'), ('P2', '2 éme primaire'), ('P3', '3 éme primaire'), ('P4', '4 éme primaire'), ('P5', '5 éme primaire'), ('P6', '6 éme primaire'), ('S1', '7 éme secondaire'), ('S2', '8 éme secondaire'), ('S3', '9 éme secondaire'), ('L1', '1 ére lycée'), ('L2', '2 éme lycée'), ('L3', '3 éme lycée'), ('L4', '4 éme lycée')], max_length=14, null=True)),
                ('Image', models.ImageField(height_field=500, upload_to='child_app/Storage', width_field=500)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30, verbose_name='Parent first Name')),
                ('LastName', models.CharField(max_length=30, verbose_name='Parent Last Name')),
                ('DOB', models.DateField(default=django.utils.timezone.now)),
                ('Image', models.ImageField(height_field=500, upload_to='child_app/Storage', width_field=500)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Place Name')),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=5)),
                ('attiude', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TaskName', models.CharField(max_length=50, verbose_name='Task name ')),
                ('Duration', models.DurationField()),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('TaskStatus', models.CharField(choices=[('F', 'Finished'), ('P', 'In Progress'), ('N', 'Not Started')], max_length=1)),
                ('TaskType', models.CharField(max_length=10)),
                ('Emplacement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='child_app.emplacement')),
                ('child_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='child_app.enfant')),
            ],
        ),
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RapportDate', models.DateField(default=django.utils.timezone.now)),
                ('TextDate', models.CharField(max_length=50)),
                ('Problems', models.CharField(blank=True, max_length=50)),
                ('id_Tache', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='child_app.tache')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contenu', models.CharField(max_length=256)),
                ('Date', models.DateField()),
                ('id_enfant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='child_app.enfant')),
            ],
        ),
        migrations.AddField(
            model_name='enfant',
            name='id_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='child_app.parent'),
        ),
        migrations.AddField(
            model_name='enfant',
            name='id_place',
            field=models.ManyToManyField(to='child_app.Place'),
        ),
    ]