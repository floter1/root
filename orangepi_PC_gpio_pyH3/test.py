#import the library / Import des librairies
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
#initialize the gpio module / initialise le GPIO
gpio.init()
#setup the port (same as raspberry pi's gpio.setup() function)
#Configure la broche PG7 (equivalent au GPIO21 du Raspberry) comme une sortie
gpio.setcfg(port.PG7, gpio.OUTPUT)
#now we do something (light up the LED)
#Maintenant, on allume la LED
gpio.output(port.PG7, gpio.HIGH)
#turn off the LED after 2 seconds
#Et on eteint après 2 secondes
sleep(2)
gpio.output(port.PG7, gpio.LOW)
