from django.contrib import admin

from .models import *


class HotelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'picture', 'address', 'telephone', 'email')
    list_display_links = ('content',)
    search_fields = ('title', 'address')
    list_editable = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class BookingRoomsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_booking', 'room', 'QR', 'numbers')
    list_display_links = ('date_booking', 'room', 'QR', 'numbers')
    search_fields = ('date_booking', 'room')
    list_filter = ('date_booking', 'room')


class StayRoomsAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking_room', 'room', 'stay')
    list_display_links = ('booking_room', 'room', 'stay')
    search_fields = ('booking_room', 'room', 'stay')


class RoomsAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel', 'room_name', 'price', 'title', 'content', 'stock')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'hotel')
    prepopulated_fields = {"slug": ("title",)}


class RoomNamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel', 'services_name', 'price', 'title', 'content', 'sub_content')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'hotel')
    prepopulated_fields = {"slug": ("title",)}


class ServicesNamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'picture')
    list_display_links = ('full_name',)


class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'picture', 'additionally')
    list_display_links = ('title', 'content')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Hotels, HotelsAdmin)
admin.site.register(BookingRooms, BookingRoomsAdmin)
admin.site.register(StayRooms, StayRoomsAdmin)
admin.site.register(Rooms, RoomsAdmin)
admin.site.register(RoomNames, RoomNamesAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(ServicesNames, ServicesNamesAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Stock, StockAdmin)
