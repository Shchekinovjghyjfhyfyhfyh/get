import RPi.GPIO as gpio

from time import sleep

import time

import matplotlib.pyplot as plt

gpio.setmode(gpio.BCM)

dac =  [26, 19, 13, 6, 5, 11, 9, 10]

comp = 4

troyka = 17

leds = [21, 20, 16, 12, 7, 8, 25, 24]

gpio.setup(dac, gpio.OUT)

gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)

gpio.setup(comp, gpio.IN)

gpio.setup(leds, gpio.OUT)

def ToBin(val:int) -> list:

   return [int (elem) for elem in bin(val)[2:].zfill(8)]

def adc():

   k = 0

   delay = 0.001

   for i in range(7, -1 , -1):

       k += 2**i

       gpio.output(dac, ToBin(k))

       sleep(delay)

       if gpio.input(comp) == 0:

           k -= 2**i

   return k



vallist = []

timestart = time.clock_gettime(0)

delay = 0.001

while True:

   volt = adc()

   vallist.append(volt)

   print(volt)

   if volt > 5:

       gpio.output(troyka, gpio.LOW)

   if volt > 250:

       break

   sleep(delay)

print('-----------------------------------')

q = 0

while True:

   # print(q, volt)

   vallist.append(volt)

   

   if q > 1:

       break

   q += 1

print('-----------------------------------')

gpio.output(troyka, gpio.HIGH)

sleep(0.01)

# gpio.output(troyka, gpio.LOW)

# sleep(0.01)

while True:

   volt = adc()

   vallist.append(volt)

   print(volt)

   if volt < 100:

       # gpio.output(troyka, gpio.HIGH)

       # print('******************************')

       # for q in range(10):

       #     a = 1 + 2

       # gpio.output(troyka, gpio.LOW)

       # break

       pass

   if volt < 10:

       break

   sleep(delay)

timeend = time.clock_gettime(0)

print('Experiment time:', timeend-timestart)

print('Period:', timeend-timestart)

print('mean frec:', len(vallist)/(timeend-timestart))

print('step:', 3.3/2**8)



plt.plot(list(range(len(vallist))), vallist)

plt.show()

file = open('data.txt', 'w+')

for q in vallist:

   file.write(str(q) + '\n')

file.close()

file = open('settings.txt', 'w+')

file.write(str(q) + ', ' + str(3.3/2**8))

file.close()



gpio.output(troyka, gpio.LOW)

gpio.output(dac, 0)

gpio.cleanup()

