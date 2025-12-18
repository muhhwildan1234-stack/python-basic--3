import requests

# =========================
# INPUT & VALIDASI KOTA
# =========================
kota = input("Masukan nama kota : ")

if not kota.replace(" ", "").isalpha():
    print("error")
    exit()

# =========================
# INPUT & VALIDASI TANGGAL
# =========================
tanggal = input("Masukan Tanggal (1-31) : ")
if not tanggal.isdigit():
    print("error")
    exit()

bulan = input("Masukan bulan (1-12) : ")
if not bulan.isdigit():
    print("error")
    exit()

tahun = input("Masukan Tahun (contoh 2025) : ")
if not tahun.isdigit():
    print("error")
    exit()

# =========================
# KONVERSI KE INTEGER
# =========================
tanggal = int(tanggal)
bulan = int(bulan)
tahun = int(tahun)

# =========================
# FORMAT TANGGAL
# =========================
tanggal_lengkap = f"{str(tanggal).zfill(2)}-{str(bulan).zfill(2)}-{tahun}"

# =========================
# REQUEST API
# =========================
target_url = (
    f"https://api.aladhan.com/v1/timingsByCity/{tanggal_lengkap}"
    f"?city={kota}&country=Indonesia&method=20"
)

response = requests.get(target_url)
data_json = response.json()

if data_json['code'] != 200:
    print("error")
    exit()

# =========================
# OUTPUT
# =========================
print("===== JADWAL SHOLAT =====")

jadwal = data_json['data']['timings']

print(f"- Imsak     : {jadwal['Imsak']}")
print(f"- Shubuh    : {jadwal['Fajr']}")
print(f"- Terbit    : {jadwal['Sunrise']}")
print(f"- Dzuhur    : {jadwal['Dhuhr']}")
print(f"- Ashar     : {jadwal['Asr']}")
print(f"- Terbenam  : {jadwal['Sunset']}")
print(f"- Maghrib   : {jadwal['Maghrib']}")
print(f"- Isya      : {jadwal['Isha']}")
