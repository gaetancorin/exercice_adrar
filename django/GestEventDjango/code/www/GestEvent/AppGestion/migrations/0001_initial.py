# Generated by Django 3.2.12 on 2022-03-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=127)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('info', models.TextField(blank=True, null=True)),
                ('illustration', models.ImageField(blank=True, null=True, upload_to='AppGestion\\static\\AppGestion\\images\\evenement')),
                ('place_restante', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Intervenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=127)),
                ('niveau', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=127)),
                ('jauge_max_assise', models.IntegerField(default=0)),
                ('jauge_max_debout', models.IntegerField(default=0)),
                ('equipement_audio', models.BooleanField()),
                ('equipement_lumiere', models.BooleanField()),
                ('equipement_stand', models.BooleanField()),
                ('equipement_rideau', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=127)),
                ('prenom', models.CharField(max_length=127)),
                ('username', models.CharField(max_length=127)),
                ('pwd', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=127)),
            ],
        ),
    ]