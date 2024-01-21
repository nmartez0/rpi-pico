"""
Source: https://www.makeriot2020.com/index.php/2021/02/27/maker-pi-pico-with-esp01s-module/
"""

import os
from machine import UART, Pin
import time
import binascii

"""
ESPRESSIF AT Command Set
https://docs.espressif.com/projects/esp-at/en/latest/AT_Command_Set/
"""

TCP_SERVER_PORT = "80"
SSID = ""
PASSWORD = ""

#indicate program started visually
def led_start():
    led_onboard = Pin(25, Pin.OUT)
    led_onboard.value(0)     # onboard LED OFF/ON for 0.5/1.0 sec
    time.sleep(0.5)
    led_onboard.value(1)
    time.sleep(1.0)
    led_onboard.value(0)

uart0 = UART(0, rx=Pin(1), tx=Pin(0), baudrate=115200)
# NOTE that we explicitly set the Tx and Rx pins for use with the UART
# If we do not do this, they WILL default to Pin 0 and Pin 1
# Also note that Rx and Tx are swapped, meaning Pico Tx goes to ESP01 Rx 
# and vice versa.
print(uart0)


def recv_data(uart=uart0):
    recv=bytes()
    while uart.any()>0:
        recv+=uart.read(1)
    res= recv.decode('utf-8')
    return res

def send_at_cmd(cmd, sleep_seconds=0.0, uart=uart0, timeout=2000):
    print("CMD: " + cmd)
    uart.write(cmd)
    time.sleep(sleep_seconds)
    wait_resp(uart, timeout)
    print()
    
def wait_resp(uart=uart0, timeout=2000):
    prv_mills = time.ticks_ms()
    resp = b""
    while (time.ticks_ms()-prv_mills)<timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    print("resp:")
    try:
        print(resp.decode('utf-8'))
    except UnicodeError:
        print(resp)

# Set the Wi-Fi mode of ESP devices.
# mode
#     0: Null mode. Wi-Fi RF will be disabled.
#     1: Station mode.
#     2: SoftAP mode.
#     3: SoftAP+Station mode.
def initizalizate_module(mode="1"):
    print()
    print("Machine: \t" + os.uname()[4])
    print("MicroPython: \t" + os.uname()[3])
    send_at_cmd('AT\r\n')          #Test AT startup
    # send_at_cmd('AT+RST\r\n')      #Restart a Module
    send_at_cmd('AT+GMR\r\n')      #Check version information
    # send_at_cmd('AT+CWMODE?\r\n')  #Query the Wi-Fi mode
    # send_at_cmd('AT+CWMODE=' + mode + '\r\n') #Set the Wi-Fi mode = Station mode
    # send_at_cmd('AT+CWMODE?\r\n')  #Query the Wi-Fi mode again``
    # send_at_cmd('AT+CIPMUX=0')
    time.sleep(1.0)

# Connect to an AP
def connect_wifi(ssid='', password=''):
    send_at_cmd('AT+CWJAP="' + ssid + '","' + password + '"\r\n', sleep_seconds=7.0, timeout=5000) #Connect to AP
    send_at_cmd('AT+CIFSR\r\n')    #Obtain the Local IP Addres
    send_at_cmd('AT+CIPSTATUS\r\n')
    time.sleep(1.0)

def ap_provisioning():
    send_at_cmd('AT+CWSAP="pos_softap","",5,0,3')
    send_at_cmd('AT+CIPMUX=1')
    time.sleep(1.0)
   
def esp_restore():
    send_at_cmd('AT+RESTORE\r\n')  #Restore Factory Default Settings
    time.sleep(1.0)

# Create a TCP/SSL Server
# Notes:
#     A TCP/SSL server can only be created when multiple connections are activated (AT+CIPMUX=1).
    
def star_tcp_server(server_port=333):
    # 
    # Delete a TCP/SSL server.
    # send_at_cmd('AT+CIPSERVER=0')
    time.sleep(2.0)
    send_at_cmd('AT+CIPMUX=1')
    time.sleep(2.0)
    # Create a TCP/SSL server, port <server_port>
    # send_at_cmd('AT+CIPSERVER=1,333,TCP,0' + server_port + '\r\n')
    send_at_cmd('AT+CIPSERVER=1,333,TCP,0\r\n')
    time.sleep(1.0)
    print('WebServer is about to start on port ' + server_port  )
    time.sleep(1.0)

led_start()
# esp_restore()
# initizalizate_module("1")
# connect_wifi(SSID, PASSWORD)
star_tcp_server(333)

time.sleep(10.0)

send_at_cmd('AT+CIPSERVER=0')

# while True:
#     res = ""
#     res = recv_data()
#     time.sleep(2.0)
#     if '+IPD' in res: # if the buffer contains IPD(a connection), then respond with HTML handshake
#         id_index = res.find('+IPD')
#         print("resp:")
#         print(res)
#         connection_id =  res[id_index+5]
#         print("connectionId:" + connection_id)
#         print ('! Incoming connection - sending webpage')
#         uart0.write('AT+CIPSEND='+connection_id+',200'+'\r\n')  #Send a HTTP response then a webpage as bytes the 108 is the amount of bytes you are sending, change this if you change the data sent below
#         # led()
#         uart0.write('HTTP/1.1 200 OK'+'\r\n')
#         uart0.write('Content-Type: text/html'+'\r\n')
#         uart0.write('Connection: close'+'\r\n')
#         uart0.write(''+'\r\n')
#         uart0.write('<!DOCTYPE HTML>'+'\r\n')
#         uart0.write('<html>'+'\r\n')
#         uart0.write("<body><center><h1>Room's Ambient</h1></center"+'\r\n')
#         uart0.write('<h4>temperature</h4>\r\n')
#         # uart0.write(f"<h4>temperature {} </h4>"+'\r\n')
#         time.sleep(1.0)
#         uart0.write('<h4>humidity </h4>')
#         # uart0.write(f"<h4>humidity </h4>")
#         uart0.write('</body></html>')
#         time.sleep(4.0)
#         send_at_cmd('AT+CIPCLOSE='+ connection_id+'\r\n') # once file sent, close connection
#         time.sleep(2.0)
#         recv_buf="" #reset buffer
#         print ('Waiting For Connection...')
