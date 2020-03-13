import serial  
import socket
import time
import threading
import ast
import sys

def get_serial_data():
    while True:
        
        try:
            
            while ser.in_waiting:         
                data_raw = ser.readline()              
                data = str(data_raw)
                data = data[2:-5]  
                #data = data_raw.decode()   
                if(data[0:6] == '$GNGGA'):                
                    data = data.split(',')
                    msg["UTC"] = data[1]
                    msg["Status"] = data[6]
                    msg["Lat"] = conv_pos(data[2])
                    msg["Lon"] = conv_pos(data[4])

                    if msg["Status"] == '1':
                        msg["Status"] = '2D3D'

                    elif msg["Status"] == '2':
                        msg["Status"] = 'DGNSS'
                    
                    elif msg["Status"] == '4':
                        msg['Status'] = 'Fixed RTK'
                    
                    elif msg["Status"] == '5':
                        msg["Status"] = 'Float RTK'
                        
                    #print(msg)
                    
        except KeyboardInterrupt:
            ser.close()    # 清除序列通訊物件
    
def conv_pos(pos_):#conver 

    try:
        pos_ = float(pos_)
        pos_i = int(pos_/100)
        pos_p = (pos_/100) - pos_i
        pos_c = pos_i + (pos_p/60)*100 
        pos_c = format(pos_c,'.9f')      
        return pos_c

    except:
        print("Unexpected error:", sys.exc_info()[0])

def TCP_client(data):
    
    # Create a TCP/IP socket    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sock.settimeout(1)     
    #print('connecting to {} port {}'.format(*server_address))
    
    
    try:
        sock.connect(server_address)
        # Send data    
       
        message =bytes(data, 'utf-8')    
        #print('sending {!r}'.format(message))
        print('[+]sending position done!',time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()))
        sock.sendall(message)        
        

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            
            data = sock.recv(512)
            amount_received += len(data)            
            #print('send position to monitor!')
            #print('received {!r}'.format(data))
        
            monitor_msg = data.decode() 
            monitor_msg = ast.literal_eval(monitor_msg)#conver string to dict 
            print('[+]reciver work info!',time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()))
            return monitor_msg

    except TimeoutError:
        print('Time out!!')
        
    except OSError:
        print('[-]NO route to host:',time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()))

    finally:        
        sock.close()
        #GPIO.cleanup()

def serial_input_RTCM(data):
        try:
            ser1.write(data)

        except KeyboardInterrupt:
            ser1.close()    

        except:
            #self.ser1.close()
            print('再見！')
    
def TCP_client_RTCM():

    while True:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening     
        #print('connecting to {} port {}'.format(*self.base_station_server_address))
        print('[+] received RTCM3 data from base station!',time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()))
        
    
        try:        
            sock.connect(base_station_server_address)
            # Send data    
            message = 'require RTCM3'
            message =bytes(message, 'utf-8')    
            #print('sending {!r}'.format(message))
            sock.sendall(message)

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                #data = sock.recv(16)
                data = sock.recv(8192)
                amount_received += len(data)     
                serial_input_RTCM(data)
                #print('received {!r}'.format(data))

        except TimeoutError:
            print('Time out!!')

        finally:
            #print('closing socket')
            sock.close()

if __name__ == "__main__":
    #GNSS serial port  #get GNGGA data
    COM_PORT = '/dev/ttyACM0'   
    BAUD_RATES = 9600   
    ser = serial.Serial(COM_PORT, BAUD_RATES, timeout=1) 

    #GNSS serial port1  #insert RTCM3 data  
    COM_PORT1 = '/dev/ttyUSB0'   
    BAUD_RATES1 = 9600   
    ser1 = serial.Serial(COM_PORT1, BAUD_RATES1, timeout=1) 
    
    # Connect the socket to the port where the server is listening
    server_address = ('192.168.42.230', 10000)  #minitor's ipaddr and port   
    base_station_server_address = ('120.117.72.101', 2101)  #minitor's ipaddr and port         

    msg ={"UTC":'',"Status":'',"Lon":'0',"Lat":'0'}

    monitor_msg ={'marker1_lat':'0', 'marker1_lon':'0', 'marker2_lat':'0', 'marker2_lon':'0', 
    'marker3_lat':'0', 'marker3_lon':'0', 'marker4_lat':'0', 'marker4_lon':'0', 'cmd':'', 'speed':''}

    t1 = threading.Thread(target = get_serial_data)
    t1.start()  

    t2 = threading.Thread(target = TCP_client_RTCM)
    t2.start()  
    
    while True:
        try:
            
            send_msg = str(msg)
            monitor_msg = TCP_client(send_msg)  
            print(msg)
            print(monitor_msg)
            
        except:
            print("Unexpected error:", sys.exc_info()[0])
            

        