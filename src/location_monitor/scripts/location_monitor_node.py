#!/usr/bin/env python
 
import rospy
import math
from robot_messages.msg import LandmarkDistance
from std_msgs.msg import String
from nav_msgs.msg import Odometry


def distance(tr_x, tr_y, obj_x, obj_y):
    xd = tr_x - obj_x
    yd = tr_y - obj_y
    return math.sqrt(xd*xd + yd*yd)


class LandmarkMonitor(object):
    def __init__(self, publisher, landmarks):
	self._publisher = publisher
	self._landmarks = landmarks
    
    def odomCallback(self, msg):
	x = msg.pose.pose.position.x
	y = msg.pose.pose.position.y
	z_orient = msg.pose.pose.orientation.z
	closest_name = None
	closest_distance = None
	for l_name, l_x, l_y in self._landmarks:
	    dist = distance(x, y, l_x, l_y)
	    if closest_distance is None or dist < closest_distance:
		closest_distance = dist
		closest_name = l_name
	landmark_msg = LandmarkDistance()
	landmark_msg.name = closest_name
	landmark_msg.distance = closest_distance
	landmark_msg.z_orientation = z_orient
	self._publisher.publish(landmark_msg)
    
    
def main():
    rospy.init_node('location_monitor') 
    landmarks = []
    landmarks.append(("Right Sensor", 6.00, 1.54));
    landmarks.append(("Center Sensor", 7.00, -0.51));
    landmarks.append(("Left Sensor", 6.00, -2.50));

    
    publisher = rospy.Publisher('closest_landmark', LandmarkDistance, queue_size = 10)
    monitor = LandmarkMonitor(publisher, landmarks)
    rospy.Subscriber("/odom", Odometry, monitor.odomCallback)
    
    rospy.spin()
  

if __name__ == '__main__':
    main()