import subprocess
import optparse
import re


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="Change to interface!")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="New mac address!")
    return parse_object.parse_args()


def change_mac_address(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])


def new_mac_control(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None


def current_mac_address(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if current_mac:
        print("Current MAC:", current_mac.group(0))
        return current_mac.group(0)
    else:
        return None


(user_input, arguments) = get_user_input()
same_mac_control = current_mac_address(user_input.interface)


if len(user_input.mac_address) != 17:
    print("You tried:  ", user_input.mac_address, "\nIncorrect format: MAC length should be 'XX:XX:XX:XX:XX:XX'")
else:
    change_mac_address(user_input.interface, user_input.mac_address.lower())


finalized_mac = new_mac_control(user_input.interface)


if same_mac_control == user_input.mac_address.lower():
    print("New Mac:    ", user_input.mac_address.lower(), "\nIt's the same MAC!!")
elif finalized_mac == user_input.mac_address.lower():
    print("New Mac:    ", user_input.mac_address.lower(), "\nSuccess!!")
else:
    print("Error!")



# print(get_user_input())         = <Values at 0xffffbcd603d0: {'interface': 'eth0', 'mac_address': '00:02:a1:04:06:ff'}>, []
# print(type(get_user_input()))   = tuple

# print(user_input)               = {'interface': 'eth0', 'mac_address': '00:02:a1:04:06:ff'}
# print(type(user_input))         = 'optparse.Values'

# user_input.interface            = eth0, wlan vs...  str
# user_input.mac_address          = XX:XX:XX:XX:XX:XX ... str