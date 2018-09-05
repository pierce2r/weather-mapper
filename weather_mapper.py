try:
	import json
	import requests
	import sys
	import datetime
	from playsound import playsound
	from gtts import gTTS

	
except:
	print('Package Missen. Now installing...')
	import os
	os.system('pip install playsound')
	os.system('pip install gTTS')
	sys.exit




city = raw_input('Please  enter city name:')
#banner design
print('*'*80)
print('Created by Pierce2r').center(80)
print('Version 2.0').center(80)
print('*'*80)
print('[*] Finding weather details for ' + city+ '...')

url= 'http://api.openweathermap.org/data/2.5/weather?q='+str(city)+'&appid=-------' #replace -------- with your own api key

json_data=requests.get(url).json()
try:
	
	main_data= json_data['main']['temp']
	weathercal = main_data - 273.15
		
		


	weather_data= json_data['weather'][0]['description']
	country_data= json_data['sys']['country']
	main1_data= json_data['main']['pressure']
	main2_data= json_data['main']['humidity']
	print('[+] Weather type: ' +weather_data)
	print ('[+] Temperature: ' +str(weathercal))
	print('[+] Pressure: ' +str(float(main1_data)))
	print('[+] Humidity: ' +str(float(main2_data)))
	print('[+] Country: ' +country_data)
	result= 'temperature is '+str(weathercal)+' degree celsius in'+str(city)+' and with a weather type' +weather_data

	#speech recognition
	tts = gTTS(text=result, lang='en')
	tts.save('/root/temp.mp3')
	playsound('/root/temp.mp3')	
	print (datetime.datetime.now())


except KeyboardInterrupt:
	print('exitting....')

