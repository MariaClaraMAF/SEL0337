import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

led_pin =12

gpio.setup(led_pin, gpio.OUT)

def contador(segundos):
	while (segundos>=0):
		mins, segs = divmod(segundos,60)
		print("{:02d}:{:02d}".format(mins,segs),end='\r')
		time.sleep(1)
		segundos-=1
	print("Ascende Led")
	gpio.output(led_pin, gpio.HIGH)
	time.sleep(5)
	gpio.output(led_pin, gpio.LOW)
	
def ascender():
	while True:
		inp = input()
		try:
			tempo = int(inp)
			if tempo <0:
				print("valor negativo")
			else:
				return tempo
		except ValueError:
			print ("Valor invalido")

def main():
	try:
		temp = ascender()
		contador(temp)
	except KeyboardInterrupt:
		print("apagou")
		gpio.output(led_pin, gpio.LOW)
		
if __name__=="__main__":
	main()
		 
