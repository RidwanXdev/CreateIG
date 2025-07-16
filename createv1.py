import requests, random, string, time, uuid, json, re

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
            "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36",
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
        res = self.session.post("https://www.instagram.com/api/v1/web/accounts/check_email/", headers=self.headers, data={"email": self.email, "jazoest": self.jazoest})
        return res.json()

    def send_verification(self):
        res = self.session.post("https://www.instagram.com/api/v1/accounts/send_verify_email/", headers=self.headers, data={"email": self.email, "device_id": self.device_id, "jazoest": self.jazoest})
        return res.json()

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
        res = self.session.post("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/", headers=self.headers, data=data)
        
        return res

# ▶️ Jalankan
email = input("Masukkan email: ").strip()
name = input("Masukkan nama lengkap: ").strip()
pw = input("Masukkan password: ").strip()

ig = InstagramCreator(email, name, pw)
print("[1] Cek Email:", ig.check_email())
print("[2] Kirim OTP:", ig.send_verification())
code = input("Masukkan kode OTP: ").strip()
signup_code = ig.confirm_code(code)
if not signup_code:
    print("❌ OTP Salah atau kadaluarsa.")
    exit()
ig.set_birthday()
print("[4] Username dipilih:", ig.suggest_username())
res = ig.create_account(signup_code)
print("[5] Buat Akun:", res.status_code, res.text)



if 'account_created' in res.text:
    ig.session.get("https://www.instagram.com/")
    all_cookies = ig.session.cookies.get_dict()
    cookie = '; '.join([f"{k}={v}" for k, v in all_cookies.items()])
    print("\n✅ Akun berhasil dibuat!")
    print("\n==== DATA AKUN ====")
    print(f"📧 Email     : {ig.email}")
    print(f"🔑 Password  : {ig.password}")
    print(f"👤 Username  : {ig.username}")
    print(f"🆔 Device ID : {ig.device_id}")
    print(f"🍪 Cookie IG : {cookie}")
    print(f"🕒 Enc Pass  : {ig.enc_password}")
    print("====================\n")
else:
    print("❌ Gagal membuat akun.")
