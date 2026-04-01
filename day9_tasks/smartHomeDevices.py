#Smart Home devices (Multiple Inheritance)
'''
A smart home device may have both WiFi connectivity and Voice control
features. Create classes WiFiDevice and VoiceAssistant, and a class
SmartSpeaker that inherits from both using multiple inheritance.

'''
class WifiDevice:
    def features(self):
        print("Wifi device connected")
        
class VoiceAssistant:
    def sound(self):
        print("Voice Assistant activated.")
        
class SmartSpeaker(WifiDevice, VoiceAssistant):
    def assist(self):
        print("Paired to Smart speaker via Wifi connectivity ")

#creating objects
speaker = SmartSpeaker()

#displaying content
speaker.features()
speaker.sound()
speaker.assist()
    
    
