# Indoor-Air-Quality-Monitor
This is an easy-to-build and fully functional indoor air quality monitor, with handy features like a calibration button and audio notifications
![IMG_6429](https://github.com/user-attachments/assets/ab55f016-cf25-4bc5-bb02-5ce5e62c1348)

## Components
This project is built using an Arduino Uno and MQ gas sensors. You can use any kinds of Arduino as long as you wire them correctly, and you can customize your own set of MQ sensors to match your need. Here is a brief description of the sensors I have available, hope it will give you some ideas about any potnetial use cases.
- **MQ-135:** ammonia, sulfide, bernze, smoke, and other harmful gas (good for generic air-quality monitoring)
- **MQ-2:** LPG, i-butane, propane, methane, alcohol, Hydrogen and smoke.
- **MQ-3:** alcohol, ethanol
- **MQ-4:** methane and natural gas
- **MQ-5:** combustible gases like LPG, natural gas, and propane, with low sensitivity to alcohol and smoke
- **MQ-6:** LPG, isobutane, and propane
- **MQ-7:** CO2
- **MQ-8:** hydrogen
- **MQ-9:** CO2, combustible gas

In my particular case I chose MQ-135, MQ-2 and MQ-9 to mostly detect harzardous gas in the air.



## Wiring
Here is the wriing diagram for Arduino Uno and the gas sensors.
<img width="1096" height="1308" alt="Screen Shot 2025-12-02 at 18 43 30 PM" src="https://github.com/user-attachments/assets/50e22066-defd-447e-b893-0ca5853ae1b4" />

There are a few things worth pointing out:
- Each MQ sensor draws about 150mA of current, and an Arduino Uno typically only provides around 500mA of current, so it's always a good idea to use an external 5v power source (as shown at the bottom of the wiring diagram), especially if you are using 3 or more MQ sensors together. I chose a 9v to 5v converter with a 9v battery attached, as you can see on the right side of the breadboard in the first picture.
- Make sure you connect the AO (analog out) pin on the MQ sensor to your Arduino. The DO (digital out) pin only outputs a binary digit (0/1), whereas AO outputs a value that correesponds to the gas concentration in the air.
- Ensure you connect MQ sensors to Arduino ports that accept analog input (A# ports)
- Make sure you connect the Arduino's GND to the GND (-) of your 5v power source. This is because the MQ sensor's AO pin outputs a voltage with respect to its GND (5v power source GND), and it's likely different from Arduino's own GND. Connecting these 2 pins ensures the entire system share the same GND.


## Code
The code should require little to no modification if you wire the sensors the same way as shown above. 

First, load ```air_quality_monitor.ino``` onto the arduino. You can verify by checking the serial monitor and see if data from the sensors are being printed out. Before running the python scripts, make sure you close the serial monitor window because otherwise python won't be able to open the serial port (```serial.Serial(...)``` will fail as the serial port is locked by Arduino IDE). 

Next, open ```read_data.py``` and ```start.py```, and make sure they are in the same folder becuase ```start.py``` depends on ```read_data.py``` for data reading. Inside ```read_data.py```, check that your ```BAUD_RATE``` is set to the same value as the baud rate in the ```setup()``` function in the arduino script (in this case 9600). Verify that your ```SERIAL_PORT``` is the same as the port on your computer connected to the Arduino. Lastly, ```pip install pyttsx3``` if you don't have the package installed. 

Now you should be able to run the python scripts and start monitoring air quality. The raw values you get from the MQ sensors correspond to the concentration of gases in the air. You can verify that it's working by breathing in front of the sensor. If any of your sensors detect CO2, you should see the value go up and slowly drop back down later. 

For the two buttons, one of them is the calibration button, and you can start a calibration process by long-pressing on it. While the button is pressed down, the script records a series of raw values from each sensor, and take the average as the baseline. Once you release the button, you will see the output value from each sensor to be around 0. This feature comes in handy when you want to monitor the trend in concentration of certain gases. For instance, I ran the calibration process in my room before going to bed at night, and in the morning I saw MQ-9 value raised from 0 to 7, indicating an increase in CO2 concentration in the room. 

The other button is the toggle for audio notification. You will hear "Audio enabled" or "Audio disabled" each time you press on it. When audio is enabled, you will get an audio notification of "Air quality warning!" if the value from any sensors exceeds ```threshold``` (preset to 5)

##
