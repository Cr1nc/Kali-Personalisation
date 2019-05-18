import os
import colored

#sets the stage
os.system("clear")
print("\033[1;31;40m \n")
#updates and distribution upgrades system.
wait_1 = raw_input("Press enter to begin:")
os.system("clear")
print "Would you like to perform an update and dist upgrade to the system?"
update_upgrade = raw_input(":").lower()
if update_upgrade.startswith('y'):
        result = os.system("apt update && apt dist-upgrade")
        print result
if update_upgrade.startswith('n'):
        print "Skipping to next step:"
else:
        print "Not recognised"
        
print("\033[1;31;40m \n")        
#this will install multiple applications
wait_2 = raw_input("Press enter to continue:")
os.system("clear")
print "Would you like to install the following applications:"
print("\033[1;34;40m \n")
print '''
Tmux
Git
Pip
Zsh
Terminator
Net-Tools
'''
print("\033[1;31;40m \n") 
application_install = raw_input(":").lower()
if application_install.startswith('y'):
        result2 = os.system("apt install tmux git terminator python-pip net-tools zsh")
        print result2
if application_install.startswith('n'):
        print "Skipping to next step:"
else:
        print "Not recognised"

wait_3 = raw_input("Press enter to continue:")
os.system("clear")
print '''
Would you like to install the following github scripts:
They will be located at /root/Desktop/Tools
'''
print("\033[1;34;40m \n")
print '''
Cupp
Mentalist
LFISuite
Discover
PwnedOrNot
CrackMapExec
Router Sploit
PRET
Smbmap
Linux Exploit Suggestor
Unicorn
EmpireProject
PowerSploit
OnionScan
SMBrute
LFISuite
Venom Scanner
Red Snarf
Impacket
Null Linux
'''
print("\033[1;31;40m \n") 
print "And the following scripts/lists:"
###
print("\033[1;34;40m \n") 
print '''
/var/www/html/...
Linenum 
Linux Priv Checker

/usr/share/wordlists/....
SecLists Password Lists
'''
gitscript_install = raw_input(":").lower()
if gitscript_install.startswith('y'):
        result3 = ["git clone https://github.com/Mebus/cupp.git /root/Desktop/Test/Cupp", "git clone https://github.com/sc0tfree/mentalist.git /root/Desktop/Test/Mentalist", "git clone https://github.com/D35m0nd142/LFISuite.git /root/Desktop/Test/LFISuite", "git clone https://github.com/leebaird/discover.git /root/Desktop/Tools/Discover", "git clone https://github.com/thewhiteh4t/pwnedOrNot.git /root/Desktop/Tools/pwnedOrNot", "git clone https://github.com/byt3bl33d3r/CrackMapExec /root/Desktop/Tools/CrackMapExec", "git clone https://github.com/threat9/routersploit.git /root/Desktop/Tools/RouterSploit", "git clone https://github.com/RUB-NDS/PRET.git /root/Desktop/Tools/PRET", "git clone https://github.com/ShawnDEvans/smbmap.git /root/Desktop/Tools/SmbMap", "git clone https://github.com/InteliSecureLabs/Linux_Exploit_Suggester.git /root/Desktop/Tools/Linux_Exploit_Suggester", "git clone https://github.com/trustedsec/unicorn.git /root/Desktop/Tools/Unicorn", "git clone https://github.com/EmpireProject/Empire.git /root/Desktop/Tools/Empire", "git clone https://github.com/PowerShellMafia/PowerSploit.git /root/Desktop/Tools/PowerSploit", "git clone https://github.com/s-rah/onionscan.git /root/Desktop/Tools/OnionScan", "git clone https://github.com/m4ll0k/SMBrute.git /root/Desktop/Tools/SMBrute", "git clone https://github.com/D35m0nd142/LFISuite.git /root/Desktop/Tools/LFISuite", "git clone https://github.com/v3n0m-Scanner/V3n0M-Scanner.git /root/Desktop/Tools/V3n0M-Scanner", "git clone https://github.com/nccgroup/redsnarf.git /root/Desktop/Tools/RedSnarf", "git clone https://github.com/SecureAuthCorp/impacket.git /root/Desktop/Tools/Impacket", "git clone https://github.com/m8r0wn/nullinux.git /root/Desktop/Tools/NullLinux", "git clone https://github.com/rebootuser/LinEnum.git /var/www/html/LinEnum", "git clone https://github.com/sleventyeleven/linuxprivchecker.git /var/www/html/linuxprivchecker", "git clone https://github.com/danielmiessler/SecLists.git /usr/share/wordlists/SecLists"]
        for cmd in result3:
            os.system(cmd)
if gitscript_install.startswith('n'):
        print "Skipping to next step:"
else:
        print "Not recognised"
print("\033[1;31;40m \n") 

os.system("clear")
print "FIN"
