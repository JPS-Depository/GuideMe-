from django.contrib import admin

from .models import Profile, Agensi, TourGuideProfile, Lokasi, Pesanan
# Register your models here.
admin.site.register(Profile),
admin.site.register(Agensi),
admin.site.register(TourGuideProfile),
admin.site.register(Lokasi),
admin.site.register(Pesanan)
