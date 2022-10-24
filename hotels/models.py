from django.db import models


class Hotels(models.Model):
    title = models.CharField(max_length=50, verbose_name="Отель")
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(verbose_name="Описание 1")
    description = models.TextField(verbose_name="Описание 2", blank=True)
    picture = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фотография")
    address = models.CharField(max_length=150, verbose_name="Адрес")
    telephone = models.CharField(max_length=50, verbose_name="Телефон")
    email = models.EmailField(max_length=50, verbose_name="Почта")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'


class BookingRooms(models.Model):
    date_booking = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey('Rooms', on_delete=models.PROTECT)
    QR = models.ImageField(upload_to="photos/%Y/%m/%d/")
    numbers = models.PositiveSmallIntegerField("Кол-во забронированных номеров", default=0)

    def __str__(self):
        return self.date_booking

    class Meta:
        verbose_name = 'Забронированный отель'
        verbose_name_plural = 'Забронированные отели'
        ordering = ['date_booking', 'room']


class StayRooms(models.Model):
    booking_room = models.ForeignKey('BookingRooms', on_delete=models.PROTECT)
    room = models.ForeignKey('Rooms', on_delete=models.PROTECT)
    stay = models.PositiveSmallIntegerField("Кол-во оставшихся номеров", default=0)

    def __str__(self):
        return self.booking_room

    class Meta:
        verbose_name = 'Свободный номер'
        verbose_name_plural = 'Свободные номера'


class Rooms(models.Model):
    hotel = models.ForeignKey('Hotels', on_delete=models.PROTECT)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    room_name = models.ForeignKey('RoomNames', on_delete=models.PROTECT)
    price = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="photos/%Y/%m/%d/", default=1)
    img = models.ImageField(upload_to="photos/%Y/%m/%d/", default=1)
    title = models.CharField(max_length=50, db_index=True)
    content = models.CharField(max_length=250)
    sub_content = models.CharField(max_length=250, verbose_name='Описание 2', blank=True)
    description = models.TextField(verbose_name="Описание 3", blank=True, default="Свободных номеров:")
    stock = models.PositiveSmallIntegerField("Количество номеров", default=0)

    def __str__(self):
        return f"{self.hotel.title} - {self.title}"

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'


class RoomNames(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='название номера')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Название номера'
        verbose_name_plural = 'Названия номеров'


class Services(models.Model):
    hotel = models.ForeignKey('Hotels', on_delete=models.PROTECT)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    services_name = models.ForeignKey('ServicesNames', on_delete=models.PROTECT)
    price = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="photos/%Y/%m/%d/")
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    title = models.CharField(max_length=50, db_index=True)
    content = models.CharField(max_length=250)
    sub_content = models.CharField(max_length=250, verbose_name='Описание 2', blank=True)

    def __str__(self):
        return f"{self.hotel.title} - {self.title}"

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class ServicesNames(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='название номера')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Название услуги'
        verbose_name_plural = 'Названия услуг'


class Contacts(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    picture = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='картинка')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Stock(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(verbose_name='описание')
    sub_content = models.TextField(verbose_name='доп. описание', blank=True)
    picture = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='картинка')
    additionally = models.TextField(verbose_name='дополнение')
    tel = models.CharField(max_length=255, verbose_name='телефон', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Акции'
        verbose_name_plural = 'Акции'
