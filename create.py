import requests, time, random, string

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
  "email": "tontug576@exdonuts.com",
  "jazoest": "22628"
}
res = requests.post("https://www.instagram.com/api/v1/web/accounts/check_email/",headers = headermail, data = datamail).json()
print(f"Check Email: {str(res)}\n")

#verifikasi Email
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
  "email": "tontug576@exdonuts.com",
  "jazoest": "22628"
}
resverifikasi = requests.post(
        "https://www.instagram.com/api/v1/accounts/send_verify_email/",
        headers=headers_verifikasi,
        data=data_verifikasi
    ).json()
print(f"Send Email: {str(resverifikasi)}\n")

#konfirmasi email
res_code = input("Kode Email: ")
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
  "email": "tontug576@exdonuts.com",
  "jazoest": "22628"
}

res_konfirmasi = requests.post("https://www.instagram.com/api/v1/accounts/check_confirmation_code/", headers=headers_konfirmasi, data=data_konfirmasi).json()
signup_code = res_konfirmasi.get("signup_code")
print(f"Respon Konfirmasi Email: {str(res_konfirmasi)} | {signup_code}\n")

#Konfirmasi akun
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
  "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1752509089:ikanhiu8787",
  "email": "tontug576@exdonuts.com",
  "failed_birthday_year_count": "{}",
  "first_name": "ridwan developer",
  "username": "",
  "seamless_login_enabled": "1",
  "use_new_suggested_user_name": "true",
  "jazoest": "22628"
}
res_konfirmasi_akun = requests.post("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/", headers = headers_konfirmasi_akun, data = data_konfirmasi_akun).json()
print(f"Respon Konfirmasi Akun: {str(res_konfirmasi_akun)}\n")


#setting birthday
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
  "day": "25",
  "month": "7",
  "year": "1996",
  "jazoest": "22628"
}
res_birthday = requests.post("https://www.instagram.com/api/v1/web/consent/check_age_eligibility/", headers=headers_birthday, data = data_birthday).json()
print(f"Respon birthday: {str(res_birthday)}\n")

#username suggestion
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
  "email": "tontug576@exdonuts.com",
  "name": "ridwan developer",
  "jazoest": "22628"
}
res_suggestion = requests.post("https://www.instagram.com/api/v1/web/accounts/username_suggestions/", headers = headers_suggestion, data = data_suggestion).json()
username = res_suggestion.get("suggestions", [])[0]

print("Username dipilih:", username)
print(f"Respon Username Suggestion: {str(res_suggestion)}\n")

#create akun ig
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
  "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
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
  "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1752509089:ikanhiu8787",
  "day": "25",
  "email": "tontug576@exdonuts.com",
  "failed_birthday_year_count": "{}",
  "first_name": "ridwan developer",
  "month": "7",
  "username": username,
  "year": "1996",
  "client_id": "aHKHRwABAAHgLs5042cVjdRq9vfx",
  "seamless_login_enabled": "1",
  "tos_version": "row",
  "force_sign_up_code": signup_code,
  "extra_session_id": "dgkd1q:djd629:bi7f1n",
  "jazoest": "22628"
}
res_create = requests.post("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/",headers = headers_create, data = data_create).json()
print(f"Respon Create: {str(res_create)}\n")