from django.contrib import admin
from .models import Specie
from .models import Category
from .models import Comment
from .models import Profile


# Register your models here.
admin.site.register(Specie)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Profile)


