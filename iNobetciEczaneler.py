#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import datetime
import base64

print('\033[32m'+"""
*********************************************
* #iNobetciEczaneler                        *
* @IhsanSencan                              *
* github.com/ihsansencan/iNobetciEczaneler  *
*********************************************
"""+'\x1b[0m')

ap = "YUhSMGNEb3ZMMkZ3YVM1cmIyUnNZVzFoTG01bGRBPT0="
b64mm = ap
base64_bytes = b64mm.encode('ascii')
b_bytes = base64.b64decode(base64.b64decode(base64_bytes))
api = b_bytes.decode('ascii')

ver = datetime.datetime.now()
bugun = datetime.datetime.strftime(ver, '%d %B %Y')

sehirler = {
    "Adana": "01",
    "Adıyaman": "02",
    "Afyonkarahisar": "03",
    "Ağrı": "04",
    "Amasya": "05",
    "Ankara": "06",
    "Antalya": "07",
    "Artvin": "08",
    "Aydın": "09",
    "Balıkesir": "10",
    "Bilecik": "11",
    "Bingöl": "12",
    "Bitlis": "13",
    "Bolu": "14",
    "Burdur": "15",
    "Bursa": "16",
    "Çanakkale": "17",
    "Çankırı": "18",
    "Çorum": "19",
    "Denizli": "20",
    "Diyarbakır": "21",
    "Edirne": "22",
    "Elazığ": "23",
    "Erzincan": "24",
    "Erzurum": "25",
    "Eskişehir": "26",
    "Gaziantep": "27",
    "Giresun": "28",
    "Gümüşhane": "29",
    "Hakkâri": "30",
    "Hatay": "31",
    "Isparta": "32",
    "Mersin": "33",
    "İstanbul": "34",
    "İzmir": "35",
    "Kars": "36",
    "Kastamonu": "37",
    "Kayseri": "38",
    "Kırklareli": "39",
    "Kırşehir": "40",
    "Kocaeli": "41",
    "Konya": "42",
    "Kütahya": "43",
    "Malatya": "44",
    "Manisa": "45",
    "Kahramanmaraş": "46",
    "Mardin": "47",
    "Muğla": "48",
    "Muş": "49",
    "Nevşehir": "50",
    "Niğde": "51",
    "Ordu": "52",
    "Rize": "53",
    "Sakarya": "54",
    "Samsun": "55",
    "Siirt": "56",
    "Sinop": "57",
    "Sivas": "58",
    "Tekirdağ": "59",
    "Tokat": "60",
    "Trabzon": "61",
    "Tunceli": "62",
    "Şanlıurfa": "63",
    "Uşak": "64",
    "Van": "65",
    "Yozgat": "66",
    "Zonguldak": "67",
    "Aksaray": "68",
    "Bayburt": "69",
    "Karaman": "70",
    "Kırıkkale": "71",
    "Batman": "72",
    "Şırnak": "73",
    "Bartın": "74",
    "Ardahan": "75",
    "Iğdır": "76",
    "Yalova": "77",
    "Karabük": "78",
    "Kilis": "79",
    "Osmaniye": "80",
    "Düzce": "81"
}

sehirAra = input("Şehir Adını Yazınız: ")

sonuc = requests.get(f"{api}/eczane/il/{sehirler.get(sehirAra.title())}").json()

print("\033[33m\033[1m***** "+str(sehirAra.title())+" İlimiz için Nöbetçi Eczaneler... *****\x1b[0m")
try:
    for i in sonuc["data"]:
        print(25*"*")
        print("Tarih: "+bugun)
        print("Eczane Adı: "+i["eczane_adi"])
        print("İlçe: "+i["eczane_ilce"])
        print("Adres: "+i["eczane_adres"])
        print("Telefon: "+i["eczane_telefon"])
except KeyError:
    print("Hatalı İsim..")
print("\033[33m\033[1m***** "+str(sehirAra.title())+" İlimiz için Nöbetçi Eczaneler... *****\x1b[0m")