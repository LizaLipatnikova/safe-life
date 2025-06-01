from django.db import models
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToCover
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Модель расширяющая стандартного пользователя, позволяя добавить допоплнительную информацию
class Profile(models.Model):
    # Связыаем профиль с пользователем с помощью связи "Один ко одному"
    user = models.OneToOneField(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="profile"
    )

    avatar = models.ImageField(
        "Аватар",
        upload_to="users_avatars/",
        help_text="Выбирайте изображения квадтратного формата, иначе аватар может быть некорректно обрезан",
        blank=True,
        null=True,
    )
    avatar_format = ImageSpecField([ResizeToCover(width=300, height=300), ], source="avatar", format="PNG")

    def __str__(self):
        return f"Профиль {self.user.username}"
    
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


# Настраиваем сигналы
# Если был создан новый пользователь
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Сохрание текущего пользователя
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
