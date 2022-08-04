#!/usr/bin/env python3

from std_msgs import Float32

import rospy

ALERT_DISTANCE = 5


class Vibrate:
    def __init__(self) -> None:
        rospy.init_node("vibrate")
        rospy.Subscriber("vibrator/left", Float32, self.vibrate_left)
        rospy.Subscriber("vibrator/right", Float32, self.vibrate_right)
        rospy.spin()

    def vibrate_left(data):
        if data.data < ALERT_DISTANCE:
            pass

    def vibrate_right(data):
        if data.data < ALERT_DISTANCE:
            pass


if __name__ == "__main__":
    Vibrate()
