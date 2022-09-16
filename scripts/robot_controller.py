#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

class RobotController:

    def __init__(self):
        self.topic = "/robot0/cmd_vel"
        self.publisher = rospy.Publisher(self.topic, Twist, queue_size=10)
        self.seconds_passed = 0
        self.rate = rospy.Rate(1)
    def move_forward(self):
        twistCmd = Twist()
        twistCmd.linear.x = .2
        self.publisher.publish(twistCmd)
    def move_backward(self):
        twistCmd = Twist()
        twistCmd.linear.x = -.2
        self.publisher.publish(twistCmd)
    def turn_right(self):
        twistCmd = Twist()
        twistCmd.angular.z = -.2
        self.publisher.publish(twistCmd)
    def stop(self):
        twistCmd = Twist()
        self.publisher.publish(twistCmd)
    def run_robot(self):
        while not rospy.is_shutdown():
            if (self.seconds_passed < 5):
                self.move_forward()
            elif (self.seconds_passed < 10):
                self.turn_right()
            elif (self.seconds_passed < 13):
                self.move_backward()
            else:
                self.stop()
            self.seconds_passed+=1
            self.rate.sleep()

def main(args=None):
    rospy.init_node("Controller",anonymous=True)
    robot_controller = RobotController()
    robot_controller.run_robot()

if __name__ == '__main__':
    main()