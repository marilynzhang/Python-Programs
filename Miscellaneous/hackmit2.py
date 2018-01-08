import requests
r = requests.get("https://store.delorean.codes/u/marilynzhang/login", data = {'username' : 'marty_mcfly',
          'password' : 'tG6NCPMFZI'}

headers = {"Set-Cookie": "eyJnaCI6Im1hcmlseW56aGFuZyIsInVzZXJuYW1lIjoibWFydHlfbWNmbHkifQ.DElQGA.2gwH19v4OYZuedQ1yatstc5qdgk"}

r = requests.get("https://store.delorean.codes/u/marilynzhang", headers=headers)
print r.text
