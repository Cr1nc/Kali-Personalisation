import os
os.system("apt update")
os.system("apt upgrade")
os.system("apt-get dist-upgrade")
os.system("apt install terminator")
os.system("apt install tmux")
os.system("apt install git")
os.system("apt install python-pip")
os.system("apt install net-tools")
os.system("gzip -d /usr/share/wordlists/rockyou.txt.gz")
os.system("sh -c '$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)'")
os.system("chsh -s /bin/zsh")
###
os.system("clear")
raw_input("Please press enter to continue:")
print ("The Script will now install:")
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
###
print "And the following scripts/lists:"
###
print '''
/var/www/html/...
Linenum 
Linux Priv Checker

/usr/share/wordlists/....
SecLists Password Lists
'''
raw_input("Please press enter to continue:")
###
os.system("mkdir /Desktop/Tools")
os.system("git clone https://github.com/Mebus/cupp.git /root/Desktop/Tools/Cupp")
os.system("git clone https://github.com/sc0tfree/mentalist.git /root/Desktop/Tools/Mentalist")
os.system("git clone https://github.com/D35m0nd142/LFISuite.git /root/Desktop/Tools/LFISuite")
os.system("git clone https://github.com/leebaird/discover.git /root/Desktop/Tools/Discover")
os.system("git clone https://github.com/thewhiteh4t/pwnedOrNot.git /root/Desktop/Tools/pwnedOrNot")
os.system("git clone https://github.com/byt3bl33d3r/CrackMapExec /root/Desktop/Tools/CrackMapExec")
os.system("git clone https://github.com/threat9/routersploit.git /root/Desktop/Tools/RouterSploit")
os.system("git clone https://github.com/RUB-NDS/PRET.git /root/Desktop/Tools/PRET")
os.system("git clone https://github.com/ShawnDEvans/smbmap.git /root/Desktop/Tools/SmbMap")
os.system("git clone https://github.com/InteliSecureLabs/Linux_Exploit_Suggester.git /root/Desktop/Tools/Linux_Exploit_Suggester")
os.system("git clone https://github.com/trustedsec/unicorn.git /root/Desktop/Tools/Unicorn")
os.system("git clone https://github.com/EmpireProject/Empire.git /root/Desktop/Tools/Empire")
os.system("git clone https://github.com/PowerShellMafia/PowerSploit.git /root/Desktop/Tools/PowerSploit")
os.system("git clone https://github.com/s-rah/onionscan.git /root/Desktop/Tools/OnionScan")
os.system("git clone https://github.com/m4ll0k/SMBrute.git /root/Desktop/Tools/SMBrute")
os.system("git clone https://github.com/D35m0nd142/LFISuite.git /root/Desktop/Tools/LFISuite")
os.system("git clone https://github.com/v3n0m-Scanner/V3n0M-Scanner.git /root/Desktop/Tools/V3n0M-Scanner")
os.system("git clone https://github.com/nccgroup/redsnarf.git /root/Desktop/Tools/RedSnarf")
os.system("git clone https://github.com/SecureAuthCorp/impacket.git /root/Desktop/Tools/Impacket")
os.system("git clone https://github.com/m8r0wn/nullinux.git /root/Desktop/Tools/NullLinux")
os.system("git clone https://github.com/rebootuser/LinEnum.git /var/www/html/LinEnum")
os.system("git clone https://github.com/sleventyeleven/linuxprivchecker.git /var/www/html/linuxprivchecker")
os.system("git clone https://github.com/danielmiessler/SecLists.git /usr/share/wordlists/SecLists")
###

raw_input("FINISHED      \o/          ")





