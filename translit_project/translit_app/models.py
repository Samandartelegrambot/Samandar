from django.db import models
from django.core.validators import RegexValidator

class TranslationHistory(models.Model):
    original_text = models.TextField(verbose_name="Asl matn")
    translated_text = models.TextField(verbose_name="Tarjima qilingan matn")
    direction = models.CharField(max_length=20, verbose_name="Yo‘nalish")
    file_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Fayl nomi")
    file_extension = models.CharField(max_length=10, null=True, blank=True, verbose_name="Fayl kengaytmasi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    class Meta:
        verbose_name = "Tarjima tarixi"
        verbose_name_plural = "Tarjima tarixlari"

    def __str__(self):
        return f"{self.direction}: {self.original_text[:50]}"

class Advertisement(models.Model):
    POSITION_CHOICES = (
        ('sidebar', 'Yon panel'),
        ('top', 'Tepa'),
        ('popup', 'Popup'),
        ('interstitial', 'Interstitial'),
    )
    title = models.CharField(max_length=100, verbose_name="Sarlavha")
    content = models.TextField(blank=True, verbose_name="Matn")  # Ixtiyoriy qilindi
    media_file = models.FileField(upload_to='ads/', null=True, blank=True, verbose_name="Media fayl")
    url = models.URLField(blank=True, verbose_name="Havola")
    active = models.BooleanField(default=True, verbose_name="Faol")
    position = models.CharField(max_length=15, choices=POSITION_CHOICES, default='sidebar', verbose_name="Joylashuv")
    views = models.PositiveIntegerField(default=0, verbose_name="Ko‘rishlar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    class Meta:
        verbose_name = "Reklama"
        verbose_name_plural = "Reklamalar"

    def __str__(self):
        return self.title

    @property
    def media_type(self):
        if not self.media_file:
            return None
        ext = self.media_file.name.lower().split('.')[-1]
        if ext in ['jpg', 'jpeg', 'png', 'gif']:
            return 'image'
        elif ext in ['mp4', 'webm', 'ogg']:
            return 'video'
        return 'unknown'

class ContactSubmission(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Ism")
    last_name = models.CharField(max_length=100, verbose_name="Familya/Taxallus")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(
        max_length=12,
        verbose_name="Raqam",
        validators=[RegexValidator(r'^\+998\d{9}$', 'Telefon raqami +998 bilan boshlanib, 9 ta raqamdan iborat bo‘lishi kerak')]
    )
    message = models.TextField(verbose_name="Xabar")
    file = models.FileField(upload_to='contact_files/', verbose_name="Fayl", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqt")

    class Meta:
        verbose_name = "Aloqa yuborilmasi"
        verbose_name_plural = "Aloqa yuborilmalari"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"