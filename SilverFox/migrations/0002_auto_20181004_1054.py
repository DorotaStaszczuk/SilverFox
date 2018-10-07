# Generated by Django 2.1.2 on 2018-10-04 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SilverFox', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='favourite',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='film_options',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='photo_options',
        ),
        migrations.AddField(
            model_name='photo',
            name='film_option1',
            field=models.BooleanField(default=False, verbose_name='przeterminowany'),
        ),
        migrations.AddField(
            model_name='photo',
            name='film_option2',
            field=models.BooleanField(default=False, verbose_name='podczerwień'),
        ),
        migrations.AddField(
            model_name='photo',
            name='photo_option1',
            field=models.BooleanField(default=False, verbose_name='Skan z negatywu'),
        ),
        migrations.AddField(
            model_name='photo',
            name='photo_option2',
            field=models.BooleanField(default=False, verbose_name='Odbitka ciemniowa'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='camera_name',
            field=models.IntegerField(choices=[(0, 'nie pamiętam'), (1, 'Fuji GW690III'), (2, 'Yashica T4'), (3, 'Konica Hexar AF'), (4, 'Nikon F2'), (5, 'Nikon FE'), (6, 'Zenit 12xp'), (7, 'Mamiya/Sekor DTL 100'), (8, 'Olympus miu'), (9, 'Pentax K1000'), (10, 'Canon AE-1'), (11, 'Plaubel Makina W67'), (12, 'Rollei 35 S'), (13, 'Contax G1/G2'), (14, 'Leica M6'), (15, 'Mamiya RZ67'), (16, 'Yashica Mat 124G'), (17, 'Zenza Bronica ETRS'), (18, 'Kiev 88'), (19, 'Pentacon Six TL'), (20, 'Pentax 67'), (21, 'Hasselblad 500C/M'), (22, 'Polaroid SX-70'), (23, 'Graflex Speed Graphic 4×5'), (24, 'inny')], default=0, verbose_name='Aparat'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(null=True, verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(null=True, upload_to='', verbose_name='Dodaj plik'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='film_iso',
            field=models.IntegerField(choices=[(3, '50'), (5, '100'), (0, 'nie pamiętam'), (10, '1600'), (2, '25'), (6, '160'), (12, '6400'), (11, '3200'), (4, '64'), (1, 'inny'), (8, '400'), (9, '800'), (7, '200')], default=0, verbose_name='Czułość filmu'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='film_name',
            field=models.IntegerField(choices=[(15, 'Ilford XP2 Super'), (17, 'Kentmere'), (13, 'Ilford FP4 Plus'), (1, 'Adox CHS'), (5, 'FOMA FOMAPAN Classic'), (4, 'Film Washi W'), (8, 'FOMA FOMAPAN R'), (3, 'Adox Silvermax'), (11, 'Ilford Pan F Plus'), (16, 'Ilford SFX '), (0, 'nie pamiętam'), (23, 'inny'), (21, 'ORWO UN'), (10, 'FujiFilm Neopan Acros'), (12, 'Ilford HP5 Plus'), (22, 'ORWO N plus'), (20, 'Kodak TRX'), (9, 'FOMA RETROPAN soft'), (6, 'FOMA FOMAPAN Creative'), (14, 'Ilford Delta'), (18, 'Kodak TMX'), (19, 'Kodak TMY'), (2, 'Adox CMS'), (7, 'FOMA FOMAPAN Action')], default=0, verbose_name='Nazwa filmu'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='film_type',
            field=models.IntegerField(choices=[(3, '126'), (1, '110'), (5, '127'), (6, '120'), (2, 'APS/IX240'), (0, 'nie pamiętam'), (10, 'inny'), (7, '220'), (9, 'taśma filmowa'), (4, '135'), (8, 'błona cięta')], default=0, verbose_name='Typ filmu'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Tytuł'),
        ),
    ]
