#!/usr/bin/env python3

import board
import busio
import adafruit_vl53l0x
import RPi.GPIO as GPIO

from std_msgs import Float32

import rospy

TOF_LEFT = 20
TOF_RIGHT = 16


class TofSensors:
    def __init__(self) -> None:
        # TODO: how to init sensor
        self.tof_left = self.init_sensor(TOF_LEFT)
        self.tof_right = self.init_sensor(TOF_RIGHT)

        rospy.init_node("tof_sensor")
        self.publisher_left = rospy.Publisher(
            "tof/left", Float32, queue_size=1)
        self.publisher_right = rospy.Publisher(
            "tof/right", Float32, queue_size=1)

        self.range = Float32()
        rate = rospy.Rate(10)  # 10hz

        while not rospy.is_shutdown():
            self.range = self.tof_left.range
            self.publisher_left(self.range)
            self.range = self.tof_right.range
            self.publisher_right(self.range)
            rate.sleep()

    # TODO: how to init sensor

    def init_sensor(pin, time_budget):
        # TODO: maybe using pin?
        i2c = busio.I2C(board.SCL, board.SDA)
        sensor = adafruit_vl53l0x.VL53L0X(i2c)

        # For example a higher speed but less accurate timing budget of 20ms:
        # sensor.measurement_timing_budget = 20000
        # Or a slower but more accurate timing budget of 200ms:
        # sensor.measurement_timing_budget = 200000

        return sensor


if __name__ == "__main__":
    TofSensors()
