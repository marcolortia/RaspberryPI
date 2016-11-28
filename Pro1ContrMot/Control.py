import socket
import sys
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#declaracion de motor derecho 
in4=37
in3=32
enb=40
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
pulso=GPIO.PWM(enb,255)
# declaracion de motor izquierdo
in2=36
in1=38
ena=7
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
pulso1=GPIO.PWM(ena,255)
GPIO.output(in4,GPIO.LOW)

try:
    accion='n'
    pulso.start(0)
    pulso1.start(0)
    while True:
      
        
        s=socket.socket()
        s.connect(("192.168.5.176",9999))
        accion=s.recv(20)
        if accion.find('A')>0:
            print "Avanza"
            GPIO.output(in4,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in1,GPIO.LOW)
            pulso.start(80)
            pulso1.start(80)
        
        if accion.find('D')>0:
            print "Derecha"
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in1,GPIO.LOW)
            pulso.start(0)
            pulso1.start(30)
            
        if accion.find("I")>0:
            print "Izquierda"
            GPIO.output(in4,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            pulso.start(30)
            pulso1.start(0)
        if accion.find("R")>0:
            print "Reversa"
            GPIO.output(in4,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in1,GPIO.HIGH)
            pulso.start(80)
            pulso1.start(80)
        if accion.find("S")>0:
            print "Detente"
            pulso.start(0)
            pulso1.start(0)
        if accion.find("O")>0:
            print "Apaga"
            pulso.start(0)
            pulso1.start(0)
            GPIO.cleanup()
            
        s.close()    
except KeyboardInterrupt:
    pulso.start(0)
    pulso1.start(0)
    GPIO.cleanup()
        
