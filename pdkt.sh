function updat(){
clear
cd /usr/local/
rm -rf sbin
rm -rf /usr/bin/enc
cd
mkdir /usr/local/sbin
dateFromServer=$(curl -v --insecure --silent https://google.com/ 2>&1 | grep Date | sed -e 's/< Date: //')
biji=`date +"%Y-%m-%d" -d "$dateFromServer"`
red() { echo -e "\\033[32;1m${*}\\033[0m"; }
clear
fun_bar() {
    CMD[0]="$1"
    CMD[1]="$2"
    (
        [[ -e $HOME/fim ]] && rm $HOME/fim
        ${CMD[0]} -y >/dev/null 2>&1
        ${CMD[1]} -y >/dev/null 2>&1
        touch $HOME/fim
    ) >/dev/null 2>&1 &
    tput civis
    echo -ne "  \033[0;33mPlease Wait Loading \033[1;37m- \033[0;33m["
    while true; do
        for ((i = 0; i < 18; i++)); do
            echo -ne "\033[0;32m# "
            sleep 0.1s
        done
        [[ -e $HOME/fim ]] && rm $HOME/fim && break
        echo -e "\033[0;33m]"
        sleep 1s
        tput cuu1
        tput dl1
        echo -ne "  \033[0;33mPlease Wait Loading \033[1;37m- \033[0;33m["
    done
    echo -e "\033[0;33m]\033[1;37m -\033[1;32m OK !\033[1;37m"
    tput cnorm
}
res1() {
    rm -rf /usr/local/sbin/WELTX
    rm -rf /usr/local/sbin/LTX
    rm -rf /usr/local/sbin/FT
    rm -rf /usr/local/sbin/FEATUR
    rm -rf /usr/local/sbin/menu-default
    rm -rf /usr/local/sbin/wel-default
    rm -rf /usr/local/sbin/ftr-default
    wget https://raw.githubusercontent.com/scriswan/v1/main/Cdy/LT
    wget -q -O /usr/bin/enc "https://raw.githubusercontent.com/scriswan/v1/main/Enc/encrypt" ; chmod +x /usr/bin/enc
    7z e -paskykenza123 LT
    unzip LT
    chmod +x menu/*
    enc menu/*
    mv menu/* /usr/local/sbin
    rm -rf menu
    rm -rf LT
    rm -rf menu.zip
    rm -rf update.sh
    rm -rf update
    rm -rf /root/menu
    rm -rf /root/menu.zip
    rm -rf /root/update.sh
    rm -rf /root/welcome
    rm -rf /root/change-limit-xray
    rm -rf /root/change-ip-limit
    rm -rf /root/change-domain
    rm -rf /root/fixhap
    rm -rf /root/fixcert
    rm -rf /root/xtra-menu
    rm -rf /root/others
    rm -rf /root/manager
    rm -rf /root/m-ftr
    rm -rf /root/m-bkp
    rm -rf /root/m-bot
    rm -rf /root/m-ssh
    rm -rf /root/m-ssr
    rm -rf /root/m-vme
    rm -rf /root/m-vle
    rm -rf /root/m-tro
    rm -rf /root/mbot
    rm -rf /root/m-panel
    rm -rf /root/add-bot-notif
    rm -rf /root/add-ip
    rm -rf /root/add-ssh
    rm -rf /root/add-vme
    rm -rf /root/add-vle
    rm -rf /root/add-ssr    
    rm -rf /root/auto-kill
    rm -rf /root/autobackup
    rm -rf /root/autoreboot
    rm -rf /root/clearcache
    rm -rf /root/clearlog
    rm -rf /root/backup
    rm -rf /root/restore
    rm -rf /root/cek-ssh
    rm -rf /root/cek-ssr
    rm -rf /root/cek-vle
    rm -rf /root/cek-vme
    rm -rf /root/cek-tro
    rm -rf /root/member-ssh
    rm -rf /root/member-vme
    rm -rf /root/member-vle
    rm -rf /root/member-tro
    rm -rf /root/membee-ssr
    rm -rf /root/user-ssh
    rm -rf /root/user-ssr
    rm -rf /root/user-vme
    rm -rf /root/user-vle
    rm -rf /root/user-tro
    rm -rf /root/renew-ssh
    rm -rf /root/renew-ssr
    rm -rf /root/renew-vme
    rm -rf /root/renew-vle
    rm -rf /root/renew-tro
    rm -rf /root/trial-ssh
    rm -rf /root/trial-vle
    rm -rf /root/trial-ssr
    rm -rf /root/trial-vme
    rm -rf /root/trial-tro
    rm -rf /root/delexp
    rm -rf /root/xp
    rm -rf /root/member
    rm -rf /root/tendang
    rm -rf /root/speedtest
    rm -rf /root/run
    rm -rf /root/reset
    rm -rf /root/gotop
    rm -rf /root/prot
    rm -rf /root/mullog
    rm -rf /root/Lt-on-off
    rm -rf /root/limitspeed
    rm -rf /root/limitssh-ip
    rm -rf /root/lock-vmess
    rm -rf /root/lock-xray-ip
    rm -rf /root/lock
    rm -rf /root/unlock
    rm -rf /root/ganti-ip-ssh
    rm -rf /root/ganti-ip-vmess
    rm -rf /root/ganti-ip-vless
    rm -rf /root/ganti-ip-trojan
    rm -rf /root/del-ssh
    rm -rf /root/del-vme
    rm -rf /root/del-vle
    rm -rf /root/del-ssr
    rm -rf /root/del-tro
    rm -rf /root/create-bot-notif
    rm -rf /root/hapus-bot-notif
    rm -rf /root/ceklim
    rm -rf /root/about
    rm -rf /root/limit-on-off
    rm -rf /root/killtrial
    rm -rf /root/hapus-bot
    rm -rf /root/delet-cache-file
    rm -rf /root/del-bot-notif
    rm -rf /root/change-vmess-qouta
    rm -rf /root/change-vless-qouta
    rm -rf /root/change-trojan-qouta
    rm -rf /root/cf
    rm -rf /root/bot
    rm -rf /root/add-tro
    rm -rf /root/add-ip-bot
    rm -rf /root/about
    rm -rf /root/UDEPE
    rm -rf /root/Bot-Domain
    rm -rf /root/menu-noobzvpns
    rm -rf /root/welcome.bak
    rm -rf /root/scdomain
    rm -rf /root/menu-tai
    rm -rf /root/menu-mentahan
    rm -rf /root/Neo
    rm -rf /root/m-xray
    rm -rf /root/menu.bak
    rm -rf /root/del-bot-notif
    rm -rf /root/delet-cache-file
    rm -rf /root/bot
    rm -rf /root/backup
    rm -rf /root/auto-kill
    rm -rf /root/autoreboot
    rm -rf /root/auto-backup
    rm -rf /root/add-ip-bot
    rm -rf /root/ipbot
    rm -rf /root/cf
    rm -rf /root/change-trojan-qouta
    rm -rf /root/clearcache
    rm -rf /root/clearlog
    rm -rf /root/del-bot-notif
    rm -rf /root/gz13051
    rm -rf /root/gz22349
    rm -rf /root/izinsc
    rm -rf /root/Lt-on-off
    rm -rf /root/udp
}
netfilter-persistent
clear
echo -e "\033[96;1m┌───────────────────────────────────────────┐\033[0m "
echo -e " \e[1;97;104m               UPDATE SCRIPT         \e[0m"
echo -e "\033[96;1m└───────────────────────────────────────────┘\033[0m "
echo -e ""
echo -e "  \033[1;91m Ipdate version Script\033[1;37m"
fun_bar 'res1'
echo -e "\033[96;1m└───────────────────────────────────────────┘\033[0m "
echo -e ""
echo -e "\033[92mWait in  3 sec..\033[0m"
sleep 3
menu
}

updat
