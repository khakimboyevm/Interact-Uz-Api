from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class Authors(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Authors, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Web_sites(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, blank=True)
    type_catg = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    about_item = models.TextField(max_length=4096)
    image = models.ImageField()
    screen1 = models.ImageField()
    screen2 = models.ImageField()
    screen3 = models.ImageField()
    UZ = "so'm"
    RU = "₽"
    ENG = "$"
    the_price = (
        (UZ, "so'm"),
        (RU, "₽"),
        (ENG, "$"),
    )
    price_type = models.CharField(max_length=10, choices=the_price, default="$")
    link = models.URLField(blank=True)
    price = models.IntegerField()
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Web_sites, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class telegram_bot(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, blank=True)
    type_catg = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    about_item = models.TextField(max_length=4096)
    image = models.ImageField()
    screen1 = models.ImageField()
    screen2 = models.ImageField()
    screen3 = models.ImageField()
    UZ = "so'm"
    RU = "₽"
    ENG = "$"
    the_price = (
        (UZ, "so'm"),
        (RU, "₽"),
        (ENG, "$"),
    )
    price_type = models.CharField(max_length=10, choices=the_price, default="$")
    link = models.URLField(blank=True)
    price = models.IntegerField()
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(telegram_bot, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class free_codes(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, blank=True)
    code = models.TextField()
    type_catg = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    about_item = models.TextField(max_length=4096)
    image = models.ImageField()
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(free_codes, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
