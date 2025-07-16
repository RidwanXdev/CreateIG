import requests, random, string, time, uuid, json, re, os

TOKEN = "7740073731:AAEycTU97pT3fO9PDJZfdI0EEeuw3s3JBaQ"
CHAT_ID = "7603492657"
EMAIL_FILE = "list_email.txt"
HASIL_FILE = "hasil_akun.txt"

class InstagramCreator:
    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
        self.username = None
        self.device_id = self.rand_string(32)
        self.jazoest = str(random.randint(20000, 29999))
        self.enc_password = self.get_enc_password()
        self.extra_session_id = self.generate_session_id()
        self.headers = self.get_headers()
        self.session = requests.Session()

    def rand_string(self, length):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def get_enc_password(self):
        return f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{self.password}"

    def generate_session_id(self):
        return f"{self.rand_string(6)}:{self.rand_string(6)}:{self.rand_string(6)}"

    def get_headers(self):
        return {
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
            "x-ig-app-id": "1217981644879628",
            "x-requested-with": "XMLHttpRequest",
            "content-type": "application/x-www-form-urlencoded",
            "accept": "*/*",
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/accounts/signup/email/",
            "x-csrftoken": "missing",
            "cookie": "wd=512x948"
        }

    def check_email(self):
        return self.session.post("https://www.instagram.com/api/v1/web/accounts/check_email/", headers=self.headers, data={"email": self.email, "jazoest": self.jazoest}).json()

    def send_verification(self):
        return self.session.post("https://www.instagram.com/api/v1/accounts/send_verify_email/", headers=self.headers, data={"email": self.email, "device_id": self.device_id, "jazoest": self.jazoest}).json()

    def confirm_code(self, otp):
        res = self.session.post("https://www.instagram.com/api/v1/accounts/check_confirmation_code/", headers=self.headers, data={"code": otp, "email": self.email, "device_id": self.device_id, "jazoest": self.jazoest})
        return res.json().get("signup_code")

    def set_birthday(self):
        self.session.post("https://www.instagram.com/api/v1/web/consent/check_age_eligibility/", headers=self.headers, data={"day": "25", "month": "7", "year": "1996", "jazoest": self.jazoest})

    def suggest_username(self):
        res = self.session.post("https://www.instagram.com/api/v1/web/accounts/username_suggestions/", headers=self.headers, data={"email": self.email, "name": self.name, "jazoest": self.jazoest})
        self.username = res.json().get("suggestions", [])[0]
        return self.username

    def create_account(self, signup_code):
        data = {
            "enc_password": self.enc_password,
            "email": self.email,
            "day": "25",
            "month": "7",
            "year": "1996",
            "first_name": self.name,
            "username": self.username,
            "client_id": self.device_id,
            "seamless_login_enabled": "1",
            "tos_version": "row",
            "jazoest": self.jazoest,
            "extra_session_id": self.extra_session_id,
            "force_sign_up_code": signup_code,
            "failed_birthday_year_count": "{}"
        }
        return self.session.post("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/", headers=self.headers, data=data)

    def get_cookie(self):
        self.session.get("https://www.instagram.com/")
        all_cookies = self.session.cookies.get_dict()
        return '; '.join([f"{k}={v}" for k, v in all_cookies.items()])
        
def kirim_ke_telegram(email, username, password, cookie):
    message = f"""
✅ *Akun IG Berhasil Dibuat!*

📧 *Email:* `{email}`
👤 *Username:* `{username}`
🔑 *Password:* `{password}`
🍪 *Cookie:* `{cookie}`
"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"⚠️ Gagal kirim ke Telegram: {e}")


def hapus_email_dipakai(email):
    with open(EMAIL_FILE, "r") as f:
        lines = f.readlines()
    with open(EMAIL_FILE, "w") as f:
        for line in lines:
            if line.strip() != email:
                f.write(line)

def simpan_hasil(data):
    with open(HASIL_FILE, "a") as f:
        f.write(data + "\n")

# ▶️ Jalankan otomatis berdasarkan file email
if not os.path.exists(EMAIL_FILE):
    print(f"❌ File {EMAIL_FILE} tidak ditemukan.")
    exit()

with open(EMAIL_FILE, "r") as f:
    daftar_email = [x.strip() for x in f if x.strip()]

for email in daftar_email:
    pw = 'podokabeh@123'
    ig = InstagramCreator(email, "Tytyd Goyeng", pw)

    print(f"\n[🚀] Cek: {email}")
    print("[1] Cek Email:", ig.check_email())
    print("[2] Kirim OTP:", ig.send_verification())
    otp = input("🧾 Masukkan OTP dari email: ").strip()
    signup_code = ig.confirm_code(otp)
    if not signup_code:
        print("❌ OTP Salah/kadaluarsa.")
        continue

    ig.set_birthday()
    print("[3] Username:", ig.suggest_username())
    res = ig.create_account(signup_code)
    print("[4] Status:", res.status_code)

    if 'account_created' in res.text:
        ig.session.get("https://www.instagram.com/")
        all_cookies = ig.session.cookies.get_dict()
        cookie = '; '.join([f"{k}={v}" for k, v in all_cookies.items()])
        hasil = (
            f"✅ BERHASIL ✅\n"
            f"📧 Email     : {ig.email}\n"
            f"🔑 Password  : {ig.password}\n"
            f"👤 Username  : {ig.username}\n"
            f"🆔 Device ID : {ig.device_id}\n"
            f"🍪 Cookie IG : {cookie}"
        )
        print(hasil)
        kirim_ke_telegram(ig.email, ig.username, ig.password, cookie)
        simpan_hasil(hasil)
        hapus_email_dipakai(email)
    else:
        print("❌ Gagal membuat akun.")
