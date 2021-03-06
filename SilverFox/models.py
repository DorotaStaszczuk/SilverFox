from django.db import models
from django.contrib.auth.models import AbstractUser


CAMERA_NAME_CHOICES = (
    (0, 'nie pamiętam'),
    (1, 'Fuji GW690III'),
    (2, 'Yashica T4'),
    (3, 'Konica Hexar AF'),
    (4, 'Nikon F2'),
    (5, 'Nikon FE'),
    (6, 'Zenit 12xp'),
    (7, 'Mamiya/Sekor DTL 100'),
    (8, 'Olympus miu'),
    (9, 'Pentax K1000'),
    (10, 'Canon AE-1'),
    (11, 'Plaubel Makina W67'),
    (12, 'Rollei 35 S'),
    (13, 'Contax G1/G2'),
    (14, 'Leica M6'),
    (15, 'Mamiya RZ67'),
    (16, 'Yashica Mat 124G'),
    (17, 'Zenza Bronica ETRS'),
    (18, 'Kiev 88'),
    (19, 'Pentacon Six TL'),
    (20, 'Pentax 67'),
    (21, 'Hasselblad 500C/M'),
    (22, 'Polaroid SX-70'),
    (23, 'Graflex Speed Graphic 4×5'),
    (24, 'Camera obscura'),
    (25, 'inny'),
)

FILM_TYPE_CHOICES = {
    (0, 'nie pamiętam'),
    (1, '110'),
    (2, 'APS/IX240'),
    (3, '126'),
    (4, '135'),
    (5, '127'),
    (6, '120'),
    (7, '220'),
    (8, 'błona cięta'),
    (9, 'taśma filmowa'),
    (10, 'inny'),
}

FILM_NAME_CHOICES = {
    (0, 'nie pamiętam'),
    (1, 'Adox CHS'),
    (2, 'Adox CMS'),
    (3, 'Adox Silvermax'),
    (4, 'Film Washi W'),
    (5, 'FOMA FOMAPAN Classic'),
    (6, 'FOMA FOMAPAN Creative'),
    (7, 'FOMA FOMAPAN Action'),
    (8, 'FOMA FOMAPAN R'),
    (9, 'FOMA RETROPAN soft'),
    (10, 'FujiFilm Neopan Acros'),
    (11, 'Ilford Pan F Plus'),
    (12, 'Ilford HP5 Plus'),
    (13, 'Ilford FP4 Plus'),
    (14, 'Ilford Delta'),
    (15, 'Ilford XP2 Super'),
    (16, 'Ilford SFX '),
    (17, 'Kentmere'),
    (18, 'Kodak TMX'),
    (19, 'Kodak TMY'),
    (20, 'Kodak TRX'),
    (21, 'ORWO UN'),
    (22, 'ORWO N plus'),
    (23, 'inny')
}

FILM_ISO_CHOICES = {
    (0, 'nie pamiętam'),
    (1, 'inny'),
    (2, '25'),
    (3, '50'),
    (4, '64'),
    (5, '100'),
    (6, '160'),
    (7, '200'),
    (8, '400'),
    (9, '800'),
    (10, '1600'),
    (11, '3200'),
    (12, '6400'),
}


# Create your models here.
class User(AbstractUser):
    description = models.TextField(null=True, verbose_name="Opis")
    profile_image = models.ImageField(null=True, verbose_name="Zdjęcie profilowe")
    # photo_set


class Photo(models.Model):
    title = models.CharField(max_length=64, verbose_name="Tytuł")
    file = models.ImageField(null=True, verbose_name="Dodaj plik")
    date_added = models.DateTimeField(auto_now_add=True)
    camera_name = models.IntegerField(choices=CAMERA_NAME_CHOICES, default=0, verbose_name="Aparat")
    film_type = models.IntegerField(choices=FILM_TYPE_CHOICES, default=0, verbose_name="Typ filmu")
    film_name = models.IntegerField(choices=FILM_NAME_CHOICES, default=0, verbose_name="Nazwa filmu")
    film_iso = models.IntegerField(choices=FILM_ISO_CHOICES, default=0, verbose_name="Czułość filmu")
    film_option1 = models.BooleanField(blank=True, default=False, verbose_name="przeterminowany")
    film_option2 = models.BooleanField(blank=True, default=False, verbose_name="podczerwień")
    description = models.TextField(blank=True, null=True, verbose_name="Opis")
    photo_option1 = models.BooleanField(blank=True, default=False, verbose_name="Skan z negatywu")
    photo_option2 = models.BooleanField(blank=True, default=False, verbose_name="Odbitka ciemniowa")
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date_added',)
