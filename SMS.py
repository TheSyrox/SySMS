import requests

# Kullanıcıdan proxy listesini al
proxy_file = input("Proxy listesini içeren txt dosyasının adını giriniz: ")
with open(proxy_file, 'r') as f:
    proxy_list = f.read().splitlines()

# Kullanıcıdan telefon numarasını ve mesajı al
phone_number = input("Telefon numarasını giriniz: ")
message = input("Mesajınızı giriniz: ")

for proxy in proxy_list:
    try:
        # Textbelt API'sini kullanarak SMS gönder
        response = requests.post('https://textbelt.com/text', {
            'phone': phone_number,
            'message': message,
            'key': 'textbelt',
        }, proxies={'http': proxy, 'https': proxy})

        # SMS gönderme sonucunu kontrol et
        if response.json()['success']:
            print(f'SMS {proxy} ile başarıyla gönderildi.')
        else:
            print(f'SMS {proxy} ile gönderme başarısız oldu.')
    except:
        print(f'{proxy} ile bağlantı kurulamadı.')
