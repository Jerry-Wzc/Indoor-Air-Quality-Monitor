import pyttsx3
from read_data import ArduinoReader


####################### Voice Engine Setup #######################
# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150) # speed, 200=normal

# Choose a voice
voices = engine.getProperty('voices')
# for i, voice in enumerate(voices): # see what voices are available
#     print(f"{i}: {voice.name} - {voice.id}")

engine.setProperty('voice', voices[105].id) # 105 = Reed Eng UK




#######################   Text to Speech   #######################

# Setup
arduino = ArduinoReader()
audio_enabled = True
audio_change_registered = False
calibrating_announced = False
air_quality_warning_announced = False
s1_history = []
s2_history = []
s3_history = []
s1_avg = 0
s2_avg = 0
s3_avg = 0
threshold = 5


# Speak the input
engine.say("Starting...")
engine.runAndWait()

if(audio_enabled==True):
    engine.say("Audio enabled")
    engine.runAndWait()


try:
    while True:
        data = arduino.read_line()
        s1, s2, s3, calibrate, audio = [int(x) for x in data.split()]

        if audio == 1: 
            if audio_change_registered == False:
                audio_change_registered = True
                audio_enabled = not audio_enabled
                if(audio_enabled):
                    engine.say("Audio enabled")
                else:
                    engine.say("Audio disabled")
                engine.runAndWait()
        else:
            audio_change_registered = False;


        if(calibrate == 0):
            s1_calibrated = round(s1-s1_avg)
            s2_calibrated = round(s2-s2_avg)
            s3_calibrated = round(s3-s3_avg)
            print(f"Sensors: {s1_calibrated, s2_calibrated, s3_calibrated}; Audio: {audio_enabled}")
            s1_history.clear()
            s2_history.clear()
            s3_history.clear()
            calibrating_announced = False
            if audio_enabled and (s1_calibrated > threshold or s2_calibrated > threshold or s3_calibrated > threshold) and not air_quality_warning_announced:
                print("Air quality warning!")
                engine.say("Air quality warning!")
                engine.runAndWait()
                air_quality_warning_announced = True

            
        else:
            print(f"Sensors: {s1, s2, s3}, Calibrating...")
            if(calibrating_announced==False):
                engine.say("Calibrating")
                engine.runAndWait()
                calibrating_announced = True
            s1_history.append(s1)
            s2_history.append(s2)
            s3_history.append(s3)
            s1_avg = sum(s1_history)/len(s1_history)
            s2_avg = sum(s2_history)/len(s2_history)
            s3_avg = sum(s3_history)/len(s3_history)
            air_quality_warning_announced = False
            
       



finally:
    arduino.close()

