# Generated by Django 3.0.2 on 2020-09-04 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LdapUser',
            fields=[
                ('uid', models.SlugField(primary_key=True, serialize=False)),
                ('supann_alias_login', models.CharField(max_length=16)),
                ('mail', models.EmailField(max_length=254)),
                ('given_name', models.CharField(max_length=128)),
                ('sn', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Utilisateur importé depuis le LDAP',
                'verbose_name_plural': 'Utilisateurs importés depuis le LDAP',
            },
        ),
        migrations.CreateModel(
            name='ScheduledRemoteShift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(verbose_name='Jour flottant de télétravail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remoteshifts.LdapUser')),
            ],
            options={
                'verbose_name': 'Jour flottant de télétravail',
                'verbose_name_plural': 'Jours flottants de télétravail',
            },
        ),
        migrations.CreateModel(
            name='ScheduledHalfDayOff',
            fields=[
                ('scheduledremoteshift_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='remoteshifts.ScheduledRemoteShift')),
                ('year_in_school', models.CharField(choices=[('am', 'Matin'), ('pm', 'Après-midi')], default='pm', max_length=2)),
            ],
            options={
                'verbose_name': 'Demi-journée de congés',
                'verbose_name_plural': 'Demi-journées de congés',
            },
            bases=('remoteshifts.scheduledremoteshift',),
        ),
        migrations.CreateModel(
            name='PartTimeWorkDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.PositiveSmallIntegerField(choices=[(1, 'Lundi'), (2, 'Mardi'), (3, 'Mercredi'), (4, 'Jeudi'), (5, 'Vendredi')], default=3, help_text='Spécifier un jour où vous serez en temps partiel', verbose_name='Jour de temps partiel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remoteshifts.LdapUser')),
            ],
            options={
                'verbose_name': 'Jour de temps partiel',
                'verbose_name_plural': 'Jours de temps partiel',
            },
        ),
        migrations.CreateModel(
            name='FixedRemoteShift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixed_day', models.PositiveSmallIntegerField(choices=[(1, 'Lundi'), (2, 'Mardi'), (3, 'Mercredi'), (4, 'Jeudi'), (5, 'Vendredi')], default=5, help_text='Spécifier un jour fixe où vous serez en télétravail toutes les semaines', verbose_name='Jour fixe de télétravail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remoteshifts.LdapUser')),
            ],
            options={
                'verbose_name': 'Jour fixe de télétravail',
                'verbose_name_plural': 'Jours fixes de télétravail',
            },
        ),
    ]
