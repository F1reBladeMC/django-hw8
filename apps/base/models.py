from django.db import models

# Create your models here.
class MyBaseInfo(models.Model):
    company_name = models.CharField(max_length=100, verbose_name="Название компании")
    description = models.TextField(verbose_name="Описание компании")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    address = models.TextField(verbose_name="Адрес")
    working_hours = models.CharField(max_length=100, verbose_name="Время работы")
    about_text = models.TextField(verbose_name="Текст о компании")
    services_title = models.CharField(max_length=100, verbose_name="Заголовок услуг")
    
    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name = "2) Информация о компании"
        verbose_name_plural = "2) Информация о компании"

class Settings(models.Model):
    title = models.CharField(max_length=50,verbose_name="Название сайта")
    logo = models.ImageField(upload_to="logo",verbose_name="Логотип")
    icon = models.ImageField(upload_to="icon",verbose_name="Иконка")
    description = models.TextField(verbose_name="Описание")
    phone_number = models.CharField(max_length=50,verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Email")
    address = models.CharField(max_length=100,verbose_name="Адрес")
    locate = models.URLField(verbose_name="Ссылка на карту")
    instagram = models.URLField(verbose_name="Ссылка на инстаграм")
    facebook = models.URLField(verbose_name="Ссылка на фейсбук")
    youtube = models.URLField(verbose_name="Ссылка на ютуб")
    whatsapp = models.URLField(verbose_name="Ссылка на ватсап")
    telegram = models.URLField(verbose_name="Ссылка на телеграм")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "1) Настройка сайта"
        verbose_name_plural = "1) Настройки сайта"
