from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = [
    {'title': "Номера", 'url_name': 'rooms'},
    {'title': "Услуги", 'url_name': 'service'},
    {'title': "Акции", 'url_name': 'stock'},
    {'title': "Отзывы", 'url_name': 'reviews'}
]


def index(request):
    hotels = Hotels.objects.order_by("id")
    contacts = Contacts.objects.all()
    context = {
        'hotel': hotels,
        'contacts': contacts,
        'menu': menu,
        'title': 'Гостиничный комплекс'
    }
    return render(request, 'hotels/index.html', context=context)


def elem(request):
    hotels = Hotels.objects.order_by("id")
    context = {
        'hotels': hotels,
        'menu': menu,
        'title': 'О гостинице Элем'
    }
    return render(request, 'hotels/elem.html', context=context)


def selen(request):
    hotels = Hotels.objects.order_by("id")
    context = {
        'hotels': hotels,
        'menu': menu,
        'title': 'О гостинице Элем'
    }
    return render(request, 'hotels/selen.html', context=context)


def metallurg(request):
    hotels = Hotels.objects.order_by("id")
    context = {
        'hotels': hotels,
        'menu': menu,
        'title': 'О гостинице Элем'
    }
    return render(request, 'hotels/metallurg.html', context=context)


def rooms(request):
    room = Rooms.objects.all()
    rname = RoomNames.objects.all()
    hotel = Hotels.objects.all()
    context = {
        'room': room,
        'rname': rname,
        'hotel': hotel,
        'menu': menu,
        'title': 'Номера'
    }
    return render(request, 'hotels/rooms.html', context=context)


def service(request):
    services = Services.objects.all()
    sname = ServicesNames.objects.all()
    hotel = Hotels.objects.all()
    context = {
        'services': services,
        'sname': sname,
        'hotel': hotel,
        'menu': menu,
        'title': 'Номера'
    }
    return render(request, 'hotels/service.html', context=context)


def stock(request):
    stocks = Stock.objects.all()
    context = {
        'stocks': stocks,
        'menu': menu,
        'title': 'Акции'
    }
    return render(request, 'hotels/stock.html', context=context)


def reviews(request):
    hotel = Hotels.objects.all()
    context = {
        'hotel': hotel,
        'menu': menu,
        'title': 'Отзывы'
    }
    return render(request, 'hotels/reviews.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')
