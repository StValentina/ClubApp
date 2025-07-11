from django.db.models.enums import TextChoices

class CategoryChoices(TextChoices):
    FISHING = 'Fishing', 'Fishing'
    DANCING = 'Dancing', 'Dancing'
    CHESS = 'Chess', 'Chess'
    SINGING = 'Singing', 'Singing'
    HIKING = 'Hiking', 'Hiking'
    COOKING = 'Cooking', 'Cooking'
    PHOTOGRAPHY = 'Photography', 'Photography'
