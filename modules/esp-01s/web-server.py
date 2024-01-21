import uos
import machine
import utime

recv_buf="" # receive buffer global variable

print()
print("Machine: \t" + uos.uname()[4])
print("MicroPython: \t" + uos.uname()[3])

uart0 = machine.UART(0, baudrate=115200)
print(uart0)

def rx_esp_data():
    recv=bytes()
    while uart0.any()>0:
        recv+=uart0.read(1)
    res=recv.decode('utf-8')
    return res

def connect_wifi(cmd, uart=uart0, timeout=3000):
    print("CMD: " + cmd)
    uart.write(cmd)
    utime.sleep(7.0)
    wait_esp_rsp(uart, timeout)
    print()

def send_at_cmd(cmd, uart=uart0, timeout=3000):
    print("CMD: " + cmd)
    uart.write(cmd)
    wait_esp_rsp(uart, timeout)
    print()
    
def wait_esp_rsp(uart=uart0, timeout=3000):
    prv_mills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms()-prv_mills)<timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    print("resp:")
    try:
        print(resp.decode())
    except UnicodeError:
        print(resp)
    
send_at_cmd('AT\r\n')          #Test AT startup
send_at_cmd('AT+GMR\r\n')      #Check version information
send_at_cmd('AT+CIPSERVER=0\r\n')      #Destroy TCP/IP server
send_at_cmd('AT+RST\r\n')      #Reset ESP-01 module
send_at_cmd('AT+RESTORE\r\n')  #Restore Factory Default Settings
send_at_cmd('AT+CWMODE?\r\n')  #Query the WiFi mode
send_at_cmd('AT+CWMODE=1\r\n') #Set the WiFi mode = Station mode
send_at_cmd('AT+CWMODE?\r\n')  #Query the WiFi mode again
#send_at_cmd('AT+CWLAP\r\n', timeout=10000) #List available APs
connect_wifi('AT+CWJAP="",""\r\n', timeout=5000) #Connect to AP
send_at_cmd('AT+CIFSR\r\n')    #Obtain the Local IP Address
utime.sleep(3.0)
send_at_cmd('AT+CIPMUX=1\r\n')    #Obtain the Local IP Address
utime.sleep(1.0)
send_at_cmd('AT+CIPSERVER=1,80\r\n')    #Obtain the Local IP Address
utime.sleep(1.0)
print ('Starting connection to ESP8266...')
while True:
    res =""
    res=rx_esp_data()
    utime.sleep(2.0)
    if '+IPD' in res: # if the buffer contains IPD(a connection), then respond with HTML handshake
        id_index = res.find('+IPD')
        print("resp:")
        print(res)
        connection_id =  res[id_index+5]
        print("connectionId:" + connection_id)
        print ('! Incoming connection - sending webpage')
        uart0.write('AT+CIPSEND='+connection_id+',200'+'\r\n')  #Send a HTTP response then a webpage as bytes the 108 is the amount of bytes you are sending, change this if you change the data sent below
        utime.sleep(1.0)
        uart0.write('HTTP/1.1 200 OK'+'\r\n')
        uart0.write('Content-Type: text/html'+'\r\n')
        uart0.write('Connection: close'+'\r\n')
        uart0.write(''+'\r\n')
        uart0.write('<!DOCTYPE HTML>'+'\r\n')
        uart0.write('<html>'+'\r\n')
        uart0.write('<body><center><h1>Raspberry Pi Pico Web Server</h1></center>'+'\r\n')
        uart0.write('<center><h2>Microcontrollerslab.com</h2></center>'+'\r\n')
        uart0.write('</body></html>'+'\r\n')
        utime.sleep(4.0)
        send_at_cmd('AT+CIPCLOSE='+ connection_id+'\r\n') # once file sent, close connection
        utime.sleep(2.0)
        recv_buf="" #reset buffer
        print ('Waiting For connection...')