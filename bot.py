import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO  
from time import sleep  
import requests #importing all libraries required for code running

temp = 21.5
requests.get('http://localhost:3000/temp/' + temp) #it should be sending the temperature from Microbit

red_led_pin = 27    # Identifying the GPIO input 27         
blue_led_pin = 22   # Identifying the GPIO input 27               

GPIO.setmode(GPIO.BCM)      
GPIO.setup(red_led_pin, GPIO.OUT) 
GPIO.setup(blue_led_pin, GPIO.OUT)

now = datetime.datetime.now() #Identifying current time

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/Hi': #Using if logic to give commands
        bot.sendMessage(chat_id, str("Hello, I am your garden. Let's have a look at your farming!"))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/light_on':
        bot.sendMessage(chat_id, str("Light is ON"))
        GPIO.output(red_led_pin, True)
    elif command == '/light_off':
        bot.sendMessage(chat_id, str("Light is OFF"))
        GPIO.output(red_led_pin, False)
    elif command == '/temp':
        bot.sendMessage(chat_id, str("Temperature is 16°C"))
    elif command == '/heat_on':
        bot.sendMessage(chat_id, str("Heating is ON"))
        GPIO.output(blue_led_pin, True)
    elif command == '/heat_off':
        bot.sendMessage(chat_id, str("Heating is Off"))
        GPIO.output(blue_led_pin, False)


bot = telepot.Bot('1585329958:AAEPTRNXlgWjsOXSst4-_CCX9cdCnw2UPU8') #API key for my activated smartbot

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)