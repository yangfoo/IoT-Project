import time
import board
import adafruit_dht
import numpy as np
import requests

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

def send_temp_alert(temp, humid, msg):
     
    r = requests.post("https://maker.ifttt.com/trigger/temp_hum_abnormal/with/key/c3Qx7HZDqLDrcUOEH_kNR_",
                  params = {"value1": temp, "value2": humid, "value3": msg})
    if r.status_code == 200:
        print("Alert Sent")
    else:
        print("Error") 

def measure():

    temp_c_list = []
    humid_list = []
    k = 1
    while k==1:
        try:
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity

            print(
                "Temp: {:.1f} C    Humidity: {}% ".format(
                    temperature_c, humidity
                )
            )

        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error

        time.sleep(0.5)

        count += 1
        temp_c_list.append(temperature_c)
        humid_list.append(humidity)

        if count == 5:
            temp_c_ave = np.mean(temp_c_list)
            humid_ave = np.mean(humid_list)

            temp_std = np.std(temp_c_list)
            humid_std = np.std(humid_list)

            if temp_std < 5 and humid_std < 10:
                k = 0
                count = 0

                print(
                    "Average Temp: {:.1f} C    Average Humidity: {}% ".format(
                        temp_c_ave, humid_ave
                    )
                )
            else:
                print("Temperature sensor abnormal!")
                k = 1
                count = 0

    return temp_c_ave, humid_ave

def define_mode(temp, humid):

    abnormal_mode = 0
    msg = ""

    if (temp > 40 and humid < 60):
        abnormal_mode = 1
        msg = "Temperature Abnormal, Might cause fire."
    elif (humid > 80):
        abnormal_mode = 2
        msg = "Humidity High, raining"

    return abnormal_mode, msg
