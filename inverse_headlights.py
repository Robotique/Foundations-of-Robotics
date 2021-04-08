import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import RvrStreamingServices
from sphero_sdk import RvrLedGroups

rvr = SpheroRvrObserver()
def ambient_light_handler(ambient_light_data):
    s = int(ambient_light_data['AmbientLight']['Light'])
    print('ambient only: ', s)
    brightness = [max(255-s,0)]*6
    rvr.set_all_leds(
        led_group=RvrLedGroups.headlight_left.value | RvrLedGroups.headlight_right.value,
        led_brightness_values = brightness
    )

def accelerometer_light_handler(ambint_light_data):
    print('Aceelerometer data response: ', accelerometer_data)

def main():
    """ This program demonstrates how to enable multiple sensors to stream.
    """

    try:
        rvr.wake()

        # Give RVR time to wake up
        time.sleep(2)
        
        rvr.sensor_control.add_sensor_data_handler(
            service=RvrStreamingServices.ambient_light,
            handler=ambient_light_handler
        )

        rvr.sensor_control.start(interval=250)

        while True:
            # Delay to allow RVR to stream sensor data
            time.sleep(1)

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.sensor_control.clear()

        # Delay to allow RVR issue command before closing
        time.sleep(.5)
        
        rvr.close()


if __name__ == '__main__':
    main()
