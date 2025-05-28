from django.db import models

class Peer(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    email = models.EmailField("Электронная почта")
    phone = models.CharField("Телефон", max_length=20)
    photo = models.ImageField("Фото", upload_to='app2/peers_photos/')

    def __str__(self):
        return self.full_name