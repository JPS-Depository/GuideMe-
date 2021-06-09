from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import redirect, get_object_or_404
from .form import PesananForm
from .models import *
import pyrebase

config = {
    "apiKey": "AIzaSyC_HH8b6OjGzlQr4OfUnIyOq7Fjh9NnLxk",
    "authDomain": "visitnow-guideme.firebaseapp.com",
    "databaseURL": "https://visitnow-guideme-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "visitnow-guideme",
    "storageBucket": "visitnow-guideme.appspot.com",
    "messagingSenderId": "1044987250977",
    "appId": "1:1044987250977:web:9afcc18747ec6783fcd660"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

def Index(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('homepage')
        else:
            return render(request, 'index.html')

    if request.method == "POST":
        
        username_login = request.POST['username']
        password_login = request.POST['password']
        
        user = authenticate(request, username=username_login, password=password_login)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return redirect('index')

def HomePage(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user_profile = Profile.objects.get(id=user_id)
        user_name = request.user.get_full_name()
        context = {
            'ceklogin' : request.user.is_authenticated,
            'username' : request.user,
        }
        return render(request, 'homepage.html', context)
    else:
        return redirect('index')

def TourGuide(request):
    id_pengguna = request.user.id
    agensi_query = Agensi.objects.all()
    agensi_data =[]
    agensi = agensi_query
    for agensis in agensi_query:

            id_agensi = agensis.id
            nama_agensi = agensis.nama_agensi
            deskripsi = agensis.deskripsi
            detail={
                'id_agensi' : id_agensi,
                'nama_agensi' : nama_agensi,
                'deskripsi' : deskripsi
            }
            agensi_data.append(detail)
    if request.method == 'GET':
        return render(request, 'pilihtourguide.html', {'agensi_data' : agensi_data})
    elif request.method == 'POST':
        id_agensi = request.POST.get('id')
        request.session['id_agensi'] = id_agensi
        return redirect ('list_guide')
    

def ListGuide(request):
    lokasi = request.session.get('lokasi')
    id_agensi = request.session.get('id_agensi')
    guide_query = TourGuideProfile.objects.filter(id=id_agensi)
    guide_data = []
    guide = guide_query
    id_guide = ''
    if request.method == 'GET':
        for guides in guide:
            id_guide = guides.id
            nama    = guides.nama
            jangkauan_harga = guides.jangkauan_harga
            tempat_wisata = guides.tempat_wisata
            deskripsi = guides.deskripsi
            agensi = guides.agensi

        context = {
            'id_guide' : id_guide,
            'nama'  : nama,
            'jangkauan_harga' : jangkauan_harga,
            'tempat_wisata' : tempat_wisata,
            'deskripsi' :   deskripsi,
            'agensi' : agensi,
            'lokasi' : lokasi
        }
        guide_data.append(context)

        if request.user.is_authenticated:
            return render(request, 'listtourguide.html', {'guide_data' : guide_data})
        else:
            return redirect ('index')

    elif request.method == 'POST':
        lokasi = request.POST.get('lokasi')
        id_tourguide = request.POST.get('id')
        request.session['id_tourguide'] = id_tourguide
        request.session['lokasi'] = lokasi
        return redirect ('profile_guide')

def ProfileGuide(request):
    lokasi = request.session.get('lokasi')
    id_tourguide = request.session.get('id_tourguide')
    tourguide_query = TourGuideProfile.objects.filter(id=id_tourguide)
    tourguide_data = []
    tourguide = tourguide_query
    nama = ''

    if request.method == 'GET':
        pengguna = request.user.id
        for tourguides in tourguide:
            id_tourguide = tourguides.id
            nama    = tourguides.nama
            jangkauan_harga = tourguides.jangkauan_harga
            tempat_wisata = tourguides.tempat_wisata
            deskripsi = tourguides.deskripsi
            agensi = tourguides.agensi

        context = {
            'pengguna' : pengguna,
            'id_tourguide' : id_tourguide,
            'nama'  : nama,
            'jangkauan_harga' : jangkauan_harga,
            'tempat_wisata' : tempat_wisata,
            'deskripsi' :   deskripsi,
            'agensi' : agensi,
            'lokasi' : lokasi
        }
        tourguide_data.append(context)
        if request.user.is_authenticated:
            return render(request, 'profileguide.html', {'tourguide_data' : tourguide_data})
        else:
            return redirect ('index')

        return render(request, 'profileguide.html')

    elif request.method == 'POST':
        form = PesananForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('pesanan')
        else:
            return redirect ('index')

def LokasiTour(request):
    bali0img = db.child('area').child('bali').child('0').child('img').get().val()
    bali0price = db.child('area').child('bali').child('0').child('price').get().val()
    bali0spot = db.child('area').child('bali').child('0').child('spot').get().val()
    bali1img = db.child('area').child('bali').child('1').child('img').get().val()
    bali1price = db.child('area').child('bali').child('1').child('price').get().val()
    bali1spot = db.child('area').child('bali').child('1').child('spot').get().val()
    bali2img = db.child('area').child('bali').child('2').child('img').get().val()
    bali2price = db.child('area').child('bali').child('2').child('price').get().val()
    bali2spot = db.child('area').child('bali').child('2').child('spot').get().val()
    context={
        'bali0img': bali0img,
        'bali0price' : bali0price,
        'bali0spot' : bali0spot,
        'bali1img' : bali1img,
        'bali1price' : bali1price,
        'bali1spot' : bali1spot,
        'bali2img' : bali2img,
        'bali2price' : bali2price,
        'bali2spot' : bali2spot
    }
    if request.method == 'GET':
        return render(request, 'pilihlokasi.html', context)
    elif request.method == 'POST':
        lokasi = request.POST.get('lokasi')
        request.session['lokasi'] = lokasi
        return redirect ('list_guide')

def PesananList(request):
    pengguna = request.user.id
    pesanan_query = Pesanan.objects.filter(pelanggan_id=pengguna)
    pesanan_data = []
    pesanan_id = ''
    pelanggan = ''
    tour_guide = ''
    lokasi = ''
    if request.method == 'GET':
        for pesanans in pesanan_query:
            pesanan_id = pesanans.id
            pelanggan = pesanans.pelanggan
            tour_guide = pesanans.tour_guide
            lokasi = pesanans.lokasi
            context={
                'pesanan_id' : pesanan_id,
                'pelanggan' : pelanggan,
                'tour_guide' : tour_guide,
                'lokasi' : lokasi
            }
            pesanan_data.append(context)
            import pdb; pdb.set_trace()
    return render(request, 'pesanan.html', {'pesanan_data' : pesanan_data})