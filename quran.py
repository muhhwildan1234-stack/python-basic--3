import requests

nomor = input("Masukan nomor surat : ")
if not nomor.isdigit():
    print("error")
    exit()

nama_latin = input("Masukan nama surat latin : ")
if not nama_latin.replace(" ", "").isalpha():
    print("error")
    exit()

nomor = int(nomor)

url = "https://equran.id/api/v2/surat"
response = requests.get(url)
data_json = response.json()

if 'data' not in data_json:
    print("error")
    exit()

surat = data_json['data'][nomor - 1]

print("=== DATA SURAT ===")
print(f"Nomor : {surat['nomor']}")
print(f"Nama Latin : {surat['namaLatin']}")
print(f"Nama Arab : {surat['nama']}")
print(f"Jumlah Ayat : {surat['jumlahAyat']}")
