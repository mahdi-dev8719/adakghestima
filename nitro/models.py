from django.db import models

class Nitro(models.Model):
    nitro = models.CharField("نیترو", max_length=20)
    zenon = models.CharField("زنون", max_length=20)
    showcase = models.CharField("ویترین", max_length=20)
    upgrade = models.CharField("ارتقا", max_length=20)


    class Meta:
        verbose_name = 'نیترو'
        verbose_name_plural = 'پلن ها'