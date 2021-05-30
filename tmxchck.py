import os
import requests
import time

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
     888   T88b  "Y88888P"   "Y8888P"       d88P   Y88b                                                      
""")

      
 #HEADER                
text=cyan+"\t\tDeveloped By : Sanaur Asif"+green+"\n\n\t\t★★ ROC-X Auto Opening★★   \n" 
notice=""     
def header():
	print(logo)
	print(text)
	print(line)
	print(notice)
#SELECT_MAIN
def opt():
	print(cyan+"\n==> Select Your Option From Below")
	print(yellow+"\n\n [1] Turn On ROC-X Auto Opening\n\n [2] Turn Off ROC-X Auto Opening\n\n [3] Back to ROC-X")
	

#MAIN_TOOL
os.system('clear')
tt=1
header()	
opt()
while tt<2:
	opt2=str(input(blue+"\n\n [>] Enter the number of option : "+yellow))
	if opt2=="1":
		createtmx=open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
		createtmx.write("if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then\n	command_not_found_handle() {\n		/data/data/com.termux/files/usr/libexec/termux/command-not-found \"$1\"\n	}\nfi\nPS1=\'\\$ \'\nclear\ncd $HOME/roc-x\npython main.py")
		createtmx.close()
		os.system('clear')
		notice=green+"\n\t   [•] ROC-X Auto Opening Turned ON ! \n\n"
		header()
		opt()
	elif opt2=="2":
		createtmx=open("/data/data/com.termux/files/usr/etc/bash.bashrc","w")
		createtmx.write("if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then\n	command_not_found_handle() {\n		/data/data/com.termux/files/usr/libexec/termux/command-not-found \"$1\"\n	}\nfi\nPS1=\'\\$ \'")
		createtmx.close()
		os.system('clear')
		notice=red+"\n\t   [•] ROC-X Auto Opening Turned OFF ! \n\n"
		header()
		opt()
	elif opt2=="3":
		os.system("python3 main2.py")
	else:
		notice=red+"\n\t\t[×] Wrong Value Entered"
		os.system('clear')
		header()
		opt()
		continue