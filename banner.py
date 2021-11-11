import os ,shutil ,time
from time import sleep
os.system("clear")
logo = """\033[93m\033[40m
  █▀▄▀█ █▀▀█ ▀▀█▀▀ █  █ █▀▀ █▀▀ █▀▀ █  █ █▀▀█ 
  █ █ █ █▄▄█   █   █▀▀█ █▀▀ █▀▀ ▀▀█ █▀▀█ █▄▄█ 
  █   █ ▀  ▀   ▀   ▀  ▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀  ▀ ▀  ▀\033[0m"""
print (logo)
time.sleep(3.0)
os.system("clear")
logo1 = """\033[94m
              ▀▀█▀▀ █▀▀ █▀▀█ █▀▄▀█ █  █ █ █ 
                █   █▀▀ █▄▄▀ █ ▀ █ █  █ ▄▀▄ 
                █   ▀▀▀ ▀ ▀▀ ▀   ▀  ▀▀▀ ▀ ▀\033[0m"""
print (logo1)
logo2 = """
           █▀▀█  █▀▀█  █▄  █  █▄  █  █▀▀▀  █▀▀█ 
           █▀▀▄  █▄▄█  █ █ █  █ █ █  █▀▀▀  █▄▄▀ 
           █▄▄█  █  █  █  ▀█  █  ▀█  █▄▄▄  █  █"""
print (logo2)
print ("\033[01m\033[93m                                           \033[40mV1.0\033[0m")
print ("\033[01m\033[93m                \033[40m[+] Tool By Matheesha\033[0m")
print ("\033[01m\033[93m                \033[40m[+] Sl Cyber Warrior\033[0m")
print ()
print ("\033[01m\033[93m       \033[40m[01] Evil Eye Banner             \033[01m\033[32m[+] Animation\033[0m")
print ("\033[01m\033[93m       \033[40m[02] Neofetch Banner             \033[01m\033[32m[+] Animation\033[0m")
print ("\033[01m\033[93m       \033[40m[03] Your Name Asici             \033[01m\033[32m[+] Animation\033[0m")
print ("\033[01m\033[93m       \033[40m[04] Your Asici With Android logo\033[01m\033[32m[+] Animation\033[0m")
print ("\033[01m\033[93m       \033[40m[05] Asici With Android Color    \033[01m\033[32m[+] Animation\033[0m")
print ("\033[01m\033[93m       \033[40m[06] Letter Banner               \033[01m\033[32m[+] Normal\033[0m")
print ("\033[01m\033[93m       \033[40m[07] Letter Banner Colorful      \033[01m\033[32m[+] Animation\033[0m")
print ("\033[01m\033[93m       \033[40m[08] Only Neofetch               \033[01m\033[32m[+] Normal\033[0m")
print ("\033[01m\033[93m       \033[40m[09] Update Tool                 \033[01m\033[32m[+] Normal\033[0m")
print ("\033[01m\033[93m       \033[40m[10] Contact Me                  \033[01m\033[32m[+] Normal\033[0m")
print ("\033[01m\033[93m       \033[40m[00] Exit                        \033[01m\033[32m[+] Normal\033[0m")
def evil():
	name = str(input("\033[01m\033[93m   \033[40m[+] Enter Your Name :: \033[0m"))
	cs = str(input("\033[01m\033[93m   \033[40m[+] Enter Your Cowsay Name :: \033[0m"))
	speed = str(input("\033[01m\033[93m   \033[40m[+[ Enter Speed [50-150] :: \033[0m"))
	text = "cd /data/data/com.termux/files/usr/etc/"
	text1 = ("cowthink -f eyes "+cs+" |lolcat -a --speed="+speed)
	text2 = ("\nfiglet "+name+" |lolcat -a --speed="+speed)
	text3 = "\ncd"
	with open ("zshrc","w") as zsh :
		zsh.write(text1)
		zsh.write(text2)
def neo():
	name = str(input("\033[01m\033[93m   \033[40m[+] Enter Your Name :: \033[0m"))
	text = "cd /data/data/com.termux/files/usr/etc/"
	text1 = "\nneofetch"
	text2 = ("\nfiglet "+name+" |lolcat -a --speed=200")
	text3 = "\ncd"
	with open("zshrc","w") as zsh :
		zsh.write(text)
		zsh.write(text1)
		zsh.write(text2)
		zsh.write(text3)
def android():
	os.system("nano ban")
	text1 = "cd /data/data/com.termux/files/usr/etc/"
	text2 = "\ncat ban |lolcat -a --speed=200"
	text3 = "\nneofetch"
	text4 = "\ncd"
	with open("zshrc","w") as zsh :
		zsh.write(text1)
		zsh.write(text2)
		zsh.write(text3)
		zsh.write(text4)
def only():
	text = "cd /data/data/com.termux/files/usr/etc/"
	text1 = "\nneofetch"
	text3 = "\ncd"
	with open("zshrc","w") as zsh :
		zsh.write(text)
		zsh.write(text1)
		zsh.write(text3)
def color():
	os.system("nano ban")
	text1 = "cd /data/data/com.termux/files/usr/etc/"
	text2 = "\ncat ban |lolcat -a --speed=200"
	text3 = "\nneofetch |lolcat -a --speed=200"
	text4 = "\ncd"
	with open("zshrc","w") as zsh :
		zsh.write(text1)
		zsh.write(text2)
		zsh.write(text3)
		zsh.write(text4)
def letter():
	name = str(input("\033[01m\033[93m   \033[40m[+] Enter Your Name :: \033[0m"))
	text1 = "cd /data/data/com.termux/files/usr/etc/"
	text2 = ("\ntoilet "+name+" |lolcat -a --speed=200")
	text3 = "\ncd"
	with open("zshrc","w") as zsh :
		zsh.write(text1)
		zsh.write(text2)
		zsh.write(text3)
def letter_f():
	name = str(input("\033[01m\033[93m   \033[40m[+] Enter Your Name :: \033[0m"))
	text1 = "cd /data/data/com.termux/files/usr/etc/"
	text2 = ("\ntoilet -f mono12 -F gay "+name+" ")
	text3 = "\ncd"
	with open("zshrc","w") as zsh :
		zsh.write(text1)
		zsh.write(text2)
		zsh.write(text3)
def asici():
	os.system("nano asici")
	text1 = "cd /data/data/com.termux/files/usr/etc/"
	text2 = "\ncat asici |lolcat -a --speed=200"
	text3 = "\ncd"
	with open("zshrc","w") as zsh :
		zsh.write(text1)
		zsh.write(text2)
		zsh.write(text3)
def move_x():
	if os.path.exists("/data/data/com.termux/files/usr/etc/ban"):
		os.remove("/data/data/com.termux/files/usr/etc/ban")
	shutil.move("ban" ,"/data/data/com.termux/files/usr/etc")
	print ("\033[01m\033[93m   \033[40m[+] Done\033[0m")
def move_a():
	if os.path.exists("/data/data/com.termux/files/usr/etc/asici"):
		os.remove("/data/data/com.termux/files/usr/etc/asici")
	shutil.move("asici" ,"/data/data/com.termux/files/usr/etc")
	print ("\033[01m\033[93m   \033[40m[+] Done\033[0m")
def move_f():
	if os.path.exists("/data/data/com.termux/files/usr/etc/zshrc"):
		os.remove("/data/data/com.termux/files/usr/etc/zshrc")
	shutil.move("zshrc" ,"/data/data/com.termux/files/usr/etc")
	print ("\033[01m\033[93m   \033[40m[+] Done\033[0m")
def move_z():
	if os.path.exists("/data/data/com.termux/files/usr/etc/zshrc"):
		os.remove("/data/data/com.termux/files/usr/etc/zshrc")
	shutil.move("zshrc" ,"/data/data/com.termux/files/usr/etc")
print ()
cho = int(input("\033[01m\033[93m   \033[40m[+] Enter Your Choice :: \033[0m"))
print ()
if cho == 1 :
	evil()
	move_f()
elif cho == 2 :
	neo()
	move_f()
elif cho == 3 :
	asici()
	move_a()
	move_z()
elif cho == 4 :
	android()
	move_x()
	move_z()
elif cho == 5 :
	color()
	move_x()
	move_z()
elif cho == 6 :
	letter()
	move_f()
elif cho == 7 :
	letter_f()
	move_f()
elif cho == 8 :
	only()
	move_f()
elif cho == 9 :
	print ("\033[01m\033[93m   \033[40m[+] Updating\033[0m")
	time.sleep(3.0)
	os.system("clear")
	os.system("python banner.py")
elif cho == 10 :
	os.system("xdg -open http://wa.me/+94766628462")
	os.system("clear")
	os.system("python banner.py")
elif cho == 00 :
	print ("\033[01m\033[93m   \033[40m[+] Thank For Using\033[0m")
	time.sleep(3.0)
	os.system("clear")
	exit()
else :
	print ("\033[01m\033[93m   [+] Your Choice Is Wrong\033[0m")
	os.system("clear")
	os.system("python banner.py")
