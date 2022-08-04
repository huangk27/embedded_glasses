from msilib import init_database
import board
import busio
import adafruit_vl53l0x
import RPi.GPIO as GPIO

import rospy

TOF_LEFT = 20
TOF_RIGHT = 16

class TofSensor:
    def __init__(self) -> None:
        # TODO: how to init sensor
        self.tof_left = self.init_sensor(TOF_LEFT)
        self.tof_right = self.init_sensor(TOF_RIGHT)

        rospy.init_node("tof_sensor")
        self.publisher_left = rospy.Publisher()



    # TODO: how to init sensor
    def init_sensor(pin):
        # TODO: maybe using pin?
        i2c = busio.I2C(board.SCL, board.SDA)
        sensor = adafruit_vl53l0x.VL53L0X(i2c)
        return sensor
