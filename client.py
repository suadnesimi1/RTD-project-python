import argparse
import RDT
import time

if __name__ == '__main__':
    parser =  argparse.ArgumentParser(description='client talking to server.')
    parser.add_argument('server', help='Server.')
    parser.add_argument('port', help='Port.', type=int)
    args = parser.parse_args()
    
    msg_L = ['Istanbul Ticaret Universitesi',
            'Muhendislik Fakultesi',
            'Bilgisayar Muhendisligi']
    
     
    timeout = 2 #send the next message if no response
    time_of_last_data = time.time()
     
    rdt = RDT.RDT('client', args.server, args.port)
    for msg_S in msg_L:
        print('Converting: '+msg_S)
        rdt.rdt_2_1_send(msg_S)
       
        # try to receive message before timeout 
        msg_S = None
        while msg_S == None:
            msg_S = rdt.rdt_2_1_receive()
            if msg_S is None:
                if time_of_last_data + timeout < time.time():
                    break
                else:
                    continue
        time_of_last_data = time.time()
        
        #print the result
        if msg_S:
            print('to: '+msg_S+'\n')
        
    rdt.disconnect()
    print("Transimission completed")