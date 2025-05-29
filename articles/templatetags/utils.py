from django import template

register = template.Library()

# Кастомный тег для получения ключа из словаря
# Дело в том, что язык шаблонов Django не позволяет получать значения под динамическому ключу
@register.filter
def dict_key(d: dict, key):
    return d.get(key, "")
