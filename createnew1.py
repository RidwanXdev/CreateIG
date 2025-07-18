import requests, time, random, string, re, os, sys, datetime, json
ig = requests.Session()

u = open('createnew1.json', 'r').read()
data = json.loads(u)
EMAIL_FILE = str(data['file_email'])
USERNAME_FILE = str(data['file_username'])
print(USERNAME_FILE)
day = random.randint(2,28)
month = random.randint(1,12)
year = random.randint(1990,1999)
set_pw = str(data['password'])
hari_indonesia = {
    "Monday": "Senin",
    "Tuesday": "Selasa",
    "Wednesday": "Rabu",
    "Thursday": "Kamis",
    "Friday": "Jumat",
    "Saturday": "Sabtu",
    "Sunday": "Minggu"
}
hari_inggris = datetime.datetime.now().strftime("%A")
hari_id = hari_indonesia[hari_inggris]

def set_bio():
  a = str(data['bio1'])
  b = str(data['bio2'])
  c = str(data['bio3'])
  d = str(data['bio4'])
  e = str(data['bio5'])
  f = str(data['bio6'])
  g = str(data['bio7'])
  h = str(data['bio8'])
  bio = random.choice([a,b,c,d,e,f,g,h])
  return bio

def set_picture():
  a  = str(data['picture1'])
  b  = str(data['picture2'])
  c  = str(data['picture3'])
  d  = str(data['picture4'])
  e  = str(data['picture5'])
  f  = str(data['picture6'])
  g  = str(data['picture7'])
  h  = str(data['picture8'])
  i  = str(data['picture9'])
  j  = str(data['picture10'])
  k  = str(data['picture11'])
  l  = str(data['picture12'])
  m  = str(data['picture13'])
  n  = str(data['picture14'])
  o  = str(data['picture15'])
  p  = str(data['picture16'])
  q  = str(data['picture17'])
  r  = str(data['picture18'])
  s  = str(data['picture19'])
  t  = str(data['picture20'])
  foto = random.choice([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t])
  return foto


def cek_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        print(f"🌐 IP Publik Kamu: {ip}")
    except (AttributeError,requests.exceptions.ConnectionError):
      print("Koneksi 404")
      time.sleep(23)

def delay15detik():
    delay = random.randint(12,20)
    for i in range(delay, 0, -1):
        print(f"⏳ Delay {i}s", end="\r")
        time.sleep(1)

def ambil_username_pertama():
    with open(USERNAME_FILE, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines:
        return None 
    user = lines[0]
    with open(USERNAME_FILE, "w") as f:
        f.write('\n'.join(lines[1:]) + '\n')
    return user

def hapus_email_dipakai(email):
    with open(EMAIL_FILE, "r") as f:
        lines = f.readlines()
    with open(EMAIL_FILE, "w") as f:
        for line in lines:
            if line.strip() != email:
                f.write(line)


def kirim_ke_telegram(email, username, set_pw, cookie):
    CHAT_ID = str(data['chat_id'])
    if 'Minggu' in hari_id:
      TOKEN = '8074833119:AAG3ejANNF8ONrFaLnsAzSdhkRFMOiE_R5Q'
    elif 'Senin' in hari_id:
      TOKEN = '7778289640:AAHrJDWA2r6HwLwiOWFjBBtZmIzQL2LHLZg'
    elif 'Selasa' in hari_id:
      TOKEN = '7969612241:AAEjcy7O7AymYVRVf4ULwXi38C6xnJh-At0'
    elif 'Rabu' in hari_id:
      TOKEN = '7778612273:AAFuvM404hpH9feUp559KgUccYeM6wxmkwM'
    elif 'Kamis' in hari_id:
      TOKEN = '8009206407:AAFXSlV_OX1Ztl-2wBteHPVhKW1NlY8lrKs'
    elif 'Jumat' in hari_id:
      TOKEN = '7236845732:AAE4wCDRWkgSGcCDeO6XlCGfUvsePwssjvY'
    elif 'Sabtu' in hari_id:
      TOKEN = '7709587820:AAGmCJsq3i3TChUFUZLVWdSgXyAxhmyD_Gw'
    else:
      TOKEN = '7740073731:AAEycTU97pT3fO9PDJZfdI0EEeuw3s3JBaQ'
    message = f"""
📧 *Email     :* `{email}`
👤 *Username:* `{username}`
🔑 *Password:* `{set_pw}`
🍪 *Cookie    :* `{cookie}`
    `{username}|{set_pw}`
"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)                

def update_bio(email, set_pw, cookie):
  with open(USERNAME_FILE, "r") as f:
    daftar_username = [x.strip() for x in f if x.strip()]
  csrftoken = re.search(r'csrftoken=([^;]+)', str(cookie)).group(1)
  username = ambil_username_pertama()
  headers_bio = {
  "method": "POST",
  "authority": "www.instagram.com",
  "path": "/api/v1/web/accounts/edit/",
  "scheme": "https",
  "content-length": "163",
  "sec-ch-ua": "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
  "x-ig-www-claim": "hmac.AR1esP69srM9JeHlJU5txXgZvjPUlZD-zki2pXSDzQWLrnyp",
  "x-web-session-id": "4tqfzp:rkaw3b:eb1yby",
  "sec-ch-ua-platform-version": "\"15.0.0\"",
  "x-requested-with": "XMLHttpRequest",
  "sec-ch-ua-full-version-list": "\"Chromium\";v=\"137.0.7337.0\", \"Not/A)Brand\";v=\"24.0.0.0\"",
  "sec-ch-prefers-color-scheme": "light",
  "x-csrftoken": csrftoken,
  "sec-ch-ua-platform": "\"Android\"",
  "x-ig-app-id": "1217981644879628",
  "sec-ch-ua-model": "\"V2237\"",
  "sec-ch-ua-mobile": "?1",
  "x-instagram-ajax": "1024758508",
  "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
  "content-type": "application/x-www-form-urlencoded",
  "accept": "*/*",
  "x-asbd-id": "359341",
  "origin": "https://www.instagram.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://www.instagram.com/accounts/edit/",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
  "cookie": cookie 
    
  }
  data_bio = {
  "biography": set_bio(),
  "chaining_enabled": "on",
  "email": email,
  "external_url": "https://hoo.be/hotgirlcontent",
  "first_name": "",
  "phone_number": "",
  "username": username,
  "jazoest": "22677"
    
  }
  headers_pp = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'x-ig-www-claim': 'hmac.AR0qv4ff17iSTAOowBvLr1419GjWTtJ3P33Xzx5tyMIzbhsx',
    'x-web-session-id': '5efa4l:k4mu57:iisext',
    'sec-ch-ua-platform-version': '""',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
    'sec-ch-prefers-color-scheme': 'light',
    'x-csrftoken': csrftoken,
    'sec-ch-ua-platform': '"Linux"',
    'x-ig-app-id': '936619743392459',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-mobile': '?0',
    'x-instagram-ajax': '1024803561',
    'x-asbd-id': '359341',
    'origin': 'https://www.instagram.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': f'https://www.instagram.com/{username}/',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
     'Cookie': cookie,
    
  }
  files = {
    'profile_pic': ('c56d3fb0-0d35-429e-bb64-4f6b22723601', open(set_picture(), 'rb'), None, {'Content-Type': 'image/jpeg'}),
    
  }
  try:
    res_bio = requests.post('https://www.instagram.com/api/v1/web/accounts/edit/', headers = headers_bio, data = data_bio).text
    res_change = requests.post('https://www.instagram.com/api/v1/web/accounts/web_change_profile_picture/',headers=headers_pp,files=files,).text
  except (AttributeError,requests.exceptions.ConnectionError):
    time.sleep(3)
    res_bio = requests.post('https://www.instagram.com/api/v1/web/accounts/edit/', headers = headers_bio, data = data_bio).text
    res_change = requests.post(
    'https://www.instagram.com/api/v1/web/accounts/web_change_profile_picture/',headers=headers_bio,files=files,).text
  if 'ok' in str(res_bio):
    print("==== DATA AKUN ====")
    print(f"📧 Email     : {email}")
    print(f"👤 Username  : {username}")
    print(f"🔑 Password  : {set_pw}")
    print(f"🍪 Cookie IG : {cookie}")
    print("====================\n")
    kirim_ke_telegram(email, username, set_pw, cookie)
  elif 'checkpoint_required' in str(res_bio):
    print('Spam IP: Mode Pesawat Yang Lama')
    exit()
  else:
    print(f'Error: {str(res_bio)}')
     

def check_email(email):
  cek_ip()
  headermail = {
  "method": "POST",
  "authority": "www.instagram.com",
  "path": "/api/v1/web/accounts/check_email/",
  "scheme": "https",
  "content-length": "47",
  "sec-ch-ua": "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
  "x-ig-www-claim": "0",
  "x-web-session-id": "dgkd1q:djd629:bi7f1n",
  "sec-ch-ua-platform-version": "\"15.0.0\"",
  "x-requested-with": "XMLHttpRequest",
  "sec-ch-ua-full-version-list": "\"Chromium\";v=\"137.0.7337.0\", \"Not/A)Brand\";v=\"24.0.0.0\"",
  "sec-ch-prefers-color-scheme": "light",
  "x-csrftoken": "DLpvscgRZTuQiCSE83NWWccO7H1F7Di1",
  "sec-ch-ua-platform": "\"Android\"",
  "x-ig-app-id": "1217981644879628",
  "sec-ch-ua-model": "\"V2237\"",
  "sec-ch-ua-mobile": "?1",
  "x-instagram-ajax": "1024710423",
  "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
  "content-type": "application/x-www-form-urlencoded",
  "accept": "*/*",
  "x-asbd-id": "359341",
  "origin": "https://www.instagram.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://www.instagram.com/accounts/signup/email/",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
  "cookie": "wd=513x510"
    
  }
  datamail ={
  "email": email,
  "jazoest": "22628"
    
  }
  try:
    res = requests.post("https://www.instagram.com/api/v1/web/accounts/check_email/",headers = headermail, data = datamail).json()
    verifikasi_email(email)
  except (AttributeError,requests.exceptions.ConnectionError):
    print('Koneksi 404')
    time.sleep(20)

def verifikasi_email(email):
  headers_verifikasi = {
  "method": "POST",
  "authority": "www.instagram.com",
  "path": "/api/v1/accounts/send_verify_email/",
  "scheme": "https",
  "content-length": "86",
  "sec-ch-ua": "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
  "x-ig-www-claim": "0",
  "x-web-session-id": "dgkd1q:djd629:bi7f1n",
  "sec-ch-ua-platform-version": "\"15.0.0\"",
  "x-requested-with": "XMLHttpRequest",
  "sec-ch-ua-full-version-list": "\"Chromium\";v=\"137.0.7337.0\", \"Not/A)Brand\";v=\"24.0.0.0\"",
  "sec-ch-prefers-color-scheme": "light",
  "x-csrftoken": "DLpvscgRZTuQiCSE83NWWccO7H1F7Di1",
  "sec-ch-ua-platform": "\"Android\"",
  "x-ig-app-id": "1217981644879628",
  "sec-ch-ua-model": "\"V2237\"",
  "sec-ch-ua-mobile": "?1",
  "x-instagram-ajax": "1024710423",
  "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
  "content-type": "application/x-www-form-urlencoded",
  "accept": "*/*",
  "x-asbd-id": "359341",
  "origin": "https://www.instagram.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://www.instagram.com/accounts/signup/email/",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
  "cookie": "wd=513x510"
    
  }
  data_verifikasi = {
  "device_id": "aHKHRwABAAHgLs5042cVjdRq9vfx",
  "email": email,
  "jazoest": "22628"
    
  }
  resverifikasi = requests.post(
        "https://www.instagram.com/api/v1/accounts/send_verify_email/",headers=headers_verifikasi,data=data_verifikasi).json()
  if 'email_sent' in resverifikasi:
    pass
  else:
    print('Rate Limit Error: ganti email anda dengan yang lain!')
    exit()
    

def konfirmasi_email(res_code, email):
  headers_konfirmasi = {
  "method": "POST",
  "authority": "www.instagram.com",
  "path": "/api/v1/accounts/check_confirmation_code/",
  "scheme": "https",
  "content-length": "98",
  "sec-ch-ua": "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
  "x-ig-www-claim": "0",
  "x-web-session-id": "dgkd1q:djd629:bi7f1n",
  "sec-ch-ua-platform-version": "\"15.0.0\"",
  "x-requested-with": "XMLHttpRequest",
  "sec-ch-ua-full-version-list": "\"Chromium\";v=\"137.0.7337.0\", \"Not/A)Brand\";v=\"24.0.0.0\"",
  "sec-ch-prefers-color-scheme": "light",
  "x-csrftoken": "DLpvscgRZTuQiCSE83NWWccO7H1F7Di1",
  "sec-ch-ua-platform": "\"Android\"",
  "x-ig-app-id": "1217981644879628",
  "sec-ch-ua-model": "\"V2237\"",
  "sec-ch-ua-mobile": "?1",
  "x-instagram-ajax": "1024710423",
  "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
  "content-type": "application/x-www-form-urlencoded",
  "accept": "*/*",
  "x-asbd-id": "359341",
  "origin": "https://www.instagram.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://www.instagram.com/accounts/signup/emailConfirmation/",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
  "cookie": "wd=513x510"
    
  }
  data_konfirmasi = {
  "code": res_code,
  "device_id": "aHKHRwABAAHgLs5042cVjdRq9vfx",
  "email": email,
  "jazoest": "22628"
    
  }
  res_konfirmasi = requests.post("https://www.instagram.com/api/v1/accounts/check_confirmation_code/", headers=headers_konfirmasi, data=data_konfirmasi).json()
  if 'signup_code' in res_konfirmasi:
    signup_code = res_konfirmasi.get("signup_code")
  else:
    print(f'Kode Salah: {str(res_konfirmasi)}')
    exit()
  return signup_code

def konfirmasi_akun(email, pw):
  headers_konfirmasi_akun = {
  "method": "POST",
  "authority": "www.instagram.com",
  "path": "/api/v1/web/accounts/web_create_ajax/attempt/",
  "scheme": "https",
  "content-length": "398",
  "sec-ch-ua": "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
  "x-ig-www-claim": "0",
  "x-web-session-id": "dgkd1q:djd629:bi7f1n",
  "sec-ch-ua-platform-version": "\"15.0.0\"",
  "x-requested-with": "XMLHttpRequest",
  "sec-ch-ua-full-version-list": "\"Chromium\";v=\"137.0.7337.0\", \"Not/A)Brand\";v=\"24.0.0.0\"",
  "sec-ch-prefers-color-scheme": "light",
  "x-csrftoken": "DLpvscgRZTuQiCSE83NWWccO7H1F7Di1",
  "sec-ch-ua-platform": "\"Android\"",
  "x-ig-app-id": "1217981644879628",
  "sec-ch-ua-model": "\"V2237\"",
  "sec-ch-ua-mobile": "?1",
  "x-instagram-ajax": "1024710423",
  "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
  "content-type": "application/x-www-form-urlencoded",
  "accept": "*/*",
  "x-asbd-id": "359341",
  "origin": "https://www.instagram.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://www.instagram.com/accounts/signup/name/",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
  "cookie": "wd=513x510"
    
  }
  data_konfirmasi_akun = {
  "enc_password": pw,
  "email": email,
  "failed_birthday_year_count": "{}",
  "first_name": "Hot Girl",
  "username": "",
  "seamless_login_enabled": "1",
  "use_new_suggested_user_name": "true",
  "jazoest": "22628"
    
  }
  res_konfirmasi_akun = requests.post("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/", headers = headers_konfirmasi_akun, data = data_konfirmasi_akun).json()
  if 'account_created' in res_konfirmasi_akun:
    setting_birthday()
  else:
    print(f"Error: {str(res_konfirmasi_akun)}")


def setting_birthday():
  headers_birthday = {
  "method": "POST",
  "authority": "www.instagram.com",
  "path": "/api/v1/web/consent/check_age_eligibility/",
  "scheme": "https",
  "content-length": "38",
  "sec-ch-ua": "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
  "x-ig-www-claim": "0",
  "x-web-session-id": "dgkd1q:djd629:bi7f1n",
  "sec-ch-ua-platform-version": "\"15.0.0\"",
  "x-requested-with": "XMLHttpRequest",
  "sec-ch-ua-full-version-list": "\"Chromium\";v=\"137.0.7337.0\", \"Not/A)Brand\";v=\"24.0.0.0\"",
  "sec-ch-prefers-color-scheme": "light",
  "x-csrftoken": "DLpvscgRZTuQiCSE83NWWccO7H1F7Di1",
  "sec-ch-ua-platform": "\"Android\"",
  "x-ig-app-id": "1217981644879628",
  "sec-ch-ua-model": "\"V2237\"",
  "sec-ch-ua-mobile": "?1",
  "x-instagram-ajax": "1024710423",
  "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
  "content-type": "application/x-www-form-urlencoded",
  "accept": "*/*",
  "x-asbd-id": "359341",
  "origin": "https://www.instagram.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://www.instagram.com/accounts/signup/birthday/",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
  "cookie": "wd=513x984"
    
  }
  data_birthday = {
  "day": day,
  "month": month,
  "year": year,
  "jazoest": "22628"
    
  }
  res_birthday = requests.post("https://www.instagram.com/api/v1/web/consent/check_age_eligibility/", headers=headers_birthday, data = data_birthday).json()

def username_suggestion(email):
  headers_suggestion = {
  "method": "POST",
  "authority": "www.instagram.com",
  "path": "/api/v1/web/accounts/username_suggestions/",
  "scheme": "https",
  "content-length": "65",
  "sec-ch-ua": "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
  "x-ig-www-claim": "0",
  "x-web-session-id": "dgkd1q:djd629:bi7f1n",
  "sec-ch-ua-platform-version": "\"15.0.0\"",
  "x-requested-with": "XMLHttpRequest",
  "sec-ch-ua-full-version-list": "\"Chromium\";v=\"137.0.7337.0\", \"Not/A)Brand\";v=\"24.0.0.0\"",
  "sec-ch-prefers-color-scheme": "light",
  "x-csrftoken": "DLpvscgRZTuQiCSE83NWWccO7H1F7Di1",
  "sec-ch-ua-platform": "\"Android\"",
  "x-ig-app-id": "1217981644879628",
  "sec-ch-ua-model": "\"V2237\"",
  "sec-ch-ua-mobile": "?1",
  "x-instagram-ajax": "1024710423",
  "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
  "content-type": "application/x-www-form-urlencoded",
  "accept": "*/*",
  "x-asbd-id": "359341",
  "origin": "https://www.instagram.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://www.instagram.com/accounts/signup/birthday/",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
  "cookie": "wd=513x984"
    
  }
  data_suggestion = {
  "email": email,
  "name": "Hot Girl",
  "jazoest": "22628"
    
  }
  res_suggestion = requests.post("https://www.instagram.com/api/v1/web/accounts/username_suggestions/", headers = headers_suggestion, data = data_suggestion).json()
  username = res_suggestion.get("suggestions", [])[0]
  return username

def create_akun_ig(pw, email, usn, signup_code, set_pw):
  headers_create = {
  "method": "POST",
  "authority": "www.instagram.com",
  "path": "/api/v1/web/accounts/web_create_ajax/",
  "scheme": "https",
  "content-length": "522",
  "sec-ch-ua": "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
  "x-ig-www-claim": "0",
  "x-web-session-id": "dgkd1q:djd629:bi7f1n",
  "sec-ch-ua-platform-version": "\"15.0.0\"",
  "x-requested-with": "XMLHttpRequest",
  "sec-ch-ua-full-version-list": "\"Chromium\";v=\"137.0.7337.0\", \"Not/A)Brand\";v=\"24.0.0.0\"",
  "sec-ch-prefers-color-scheme": "light",
  "x-csrftoken": "DLpvscgRZTuQiCSE83NWWccO7H1F7Di1",
  "sec-ch-ua-platform": "\"Android\"",
  "x-ig-app-id": "1217981644879628",
  "sec-ch-ua-model": "\"V2237\"",
  "sec-ch-ua-mobile": "?1",
  "x-instagram-ajax": "1024710423",
  "user-agent": "Mozilla/5.0 (Linux; Android 11; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
  "content-type": "application/x-www-form-urlencoded",
  "accept": "*/*",
  "x-asbd-id": "359341",
  "origin": "https://www.instagram.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://www.instagram.com/accounts/signup/username/",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
  "cookie": "wd=513x984"
    
  }
  data_create = {
  "enc_password": pw,
  "day": day,
  "email": email,
  "failed_birthday_year_count": "{}",
  "first_name": "Hot Girl",
  "month": month,
  "username": usn,
  "year": year,
  "client_id": "aHKHRwABAAHgLs5042cVjdRq9vfx",
  "seamless_login_enabled": "1",
  "tos_version": "row",
  "force_sign_up_code": signup_code,
  "extra_session_id": "dgkd1q:djd629:bi7f1n",
  "jazoest": "22628"
    
  }
  ig = requests.Session()
  res_create = ig.post("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/",headers = headers_create, data = data_create).text
  print(str(res_create))
  if 'user_id' in str(res_create):
    ig.get("https://www.instagram.com/")
    all_cookies = ig.cookies.get_dict()
    cookie = '; '.join([f"{k}={v}" for k, v in all_cookies.items()])
    print(cookie)
    print("\n✅ Akun berhasil dibuat!")
    #update_bio(email, set_pw, cookie)
    #hapus_email_dipakai(email)
  else:
    print(f"Gagal membuat akun: {str(res_create)}")
    
with open(EMAIL_FILE, "r") as f:
    daftar_email = [x.strip() for x in f if x.strip()]

def clear_terminal():
  os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

def banner_create_ig():
    clear_terminal()
    print("======================================")
    print("        Instagram Auto Create")
    print("     Created by: ODP Dev | © 2025")
    print("======================================\n")
banner_create_ig()
for email in daftar_email:
  pw = f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{set_pw}'
  check_email(email)
  res_code = input('kode email: ')
  signup_code = konfirmasi_email(res_code, email)
  konfirmasi_akun(email, pw)
  usn = username_suggestion(email)
  create_akun_ig(pw, email, usn, signup_code, set_pw)
  delay15detik()
  