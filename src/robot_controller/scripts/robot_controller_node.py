#!/usr/bin/env python
 
import rospy
import math
from robot_messages.msg import LandmarkDistance
from std_msgs.msg import String
from kobuki_msgs.msg import DockInfraRed
from kobuki_msgs.msg import SensorState
from tf.transformations import euler_from_quaternion


class RobotController(object):
      def __init__(self, publisher, core_pub):
	  self._publisher = publisher
	  self._core_pub = core_pub


      def distanceCallback(self, msg):
	  #extract message data
	  sensor_name = msg.name
	  sensor_distance = msg.distance
	  roll = None
	  pitch = None
	  yaw = None
	  orientation_list = [msg.quat_orientation_x, msg.quat_orientation_y, msg.quat_orientation_z, msg.quat_orientation_w]
	  (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
	  
	  #create publishing dock_ir message and populate header
	  dock_ir_msg = DockInfraRed()
	  dock_ir_msg.header.frame_id = 'base_link'
	  dock_ir_msg.header.stamp = rospy.Time.now()
	  sensor_state_msg = SensorState()
	  sensor_state_msg.header.frame_id = 'base_link'
	  sensor_state_msg.header.stamp = rospy.Time.now()
	  sensor_state_msg.charger = SensorState.DISCHARGING
	  
	  #populate pub msg data based on sensor and distance
	  if sensor_name == 'Right Sensor':
	      self.rightSensorDetected(dock_ir_msg, sensor_distance, sensor_state_msg, math.degrees(yaw))
	  elif sensor_name == 'Left Sensor':
	      self.leftSensorDetected(dock_ir_msg, sensor_distance, sensor_state_msg, math.degrees(yaw))
	  else: #sensor_name == 'Center Sensor'
	      self.centerSensorDetected(dock_ir_msg, sensor_distance, sensor_state_msg, math.degrees(yaw))
      
      
      def rightSensorDetected(self, dock_ir_msg, sensor_distance, sensor_state_msg, robot_orientation):
	  data = []
	  if sensor_distance <= 2.5 and sensor_distance > 0.8:
	      if robot_orientation >= -95 and robot_orientation <= -65:
		 data.append(50)
		 data.append(50)
		 data.append((DockInfraRed.FAR_RIGHT)) 
		 dock_ir_msg.data = data
		 self._publisher.publish(dock_ir_msg)
	         self._core_pub.publish(sensor_state_msg)
	      else:
		 data.append((DockInfraRed.FAR_RIGHT))
		 data.append((DockInfraRed.FAR_RIGHT))
		 data.append((DockInfraRed.FAR_RIGHT)) 
		 dock_ir_msg.data = data
		 self._publisher.publish(dock_ir_msg)
	         self._core_pub.publish(sensor_state_msg)
	  elif sensor_distance <= 0.8:
	      if robot_orientation >= -95 and robot_orientation <= -80:
		 data.append(50)
		 data.append(50)
	         data.append((DockInfraRed.NEAR_RIGHT))
	         dock_ir_msg.data = data
	         self._publisher.publish(dock_ir_msg)
	         self._core_pub.publish(sensor_state_msg)
	      else:
		 data.append((DockInfraRed.NEAR_RIGHT))
	         data.append((DockInfraRed.NEAR_RIGHT))
	         data.append((DockInfraRed.NEAR_RIGHT))
	         dock_ir_msg.data = data
	         self._publisher.publish(dock_ir_msg)
	         self._core_pub.publish(sensor_state_msg)
      
      def leftSensorDetected(self, dock_ir_msg, sensor_distance, sensor_state_msg, robot_orientation):
	  data = []
	  if sensor_distance <= 2.5 and sensor_distance > 0.8:
	      if robot_orientation >= 65 and robot_orientation <= 95:
		 data.append((DockInfraRed.FAR_LEFT)) 
	         data.append(50)
	         data.append(50)
	         dock_ir_msg.data = data
	         self._publisher.publish(dock_ir_msg)
	         self._core_pub.publish(sensor_state_msg)
	      else:
		 data.append((DockInfraRed.FAR_LEFT)) 
	         data.append((DockInfraRed.FAR_LEFT))
	         data.append((DockInfraRed.FAR_LEFT))
	         dock_ir_msg.data = data
	         self._publisher.publish(dock_ir_msg)
	         self._core_pub.publish(sensor_state_msg)
	  elif sensor_distance <= 0.8:
	      if robot_orientation >= 80 and robot_orientation <= 95:
		 data.append((DockInfraRed.NEAR_LEFT))
		 data.append(50)
	         data.append(50)
		 dock_ir_msg.data = data
	         self._publisher.publish(dock_ir_msg)
		 self._core_pub.publish(sensor_state_msg)
	      else:
		 data.append((DockInfraRed.NEAR_LEFT))
	         data.append((DockInfraRed.NEAR_LEFT))
	         data.append((DockInfraRed.NEAR_LEFT))
	         dock_ir_msg.data = data
	         self._publisher.publish(dock_ir_msg)
	         self._core_pub.publish(sensor_state_msg)
		
      
      def centerSensorDetected(self, dock_ir_msg, sensor_distance, sensor_state_msg, robot_orientation):
	  data = []
	  if sensor_distance <= 4 and sensor_distance > 0.8:
	     if robot_orientation >= -10 and robot_orientation <= 10:
		data.append((DockInfraRed.FAR_CENTER)) 
		data.append((DockInfraRed.FAR_CENTER)) 
		data.append((DockInfraRed.FAR_CENTER))
		dock_ir_msg.data = data
		self._publisher.publish(dock_ir_msg)
		self._core_pub.publish(sensor_state_msg)
	     else:
	        data.append((DockInfraRed.NEAR_RIGHT)) 
		data.append((DockInfraRed.NEAR_RIGHT)) 
		data.append((DockInfraRed.NEAR_RIGHT))
		dock_ir_msg.data = data
		self._publisher.publish(dock_ir_msg)
		self._core_pub.publish(sensor_state_msg)
	  elif sensor_distance <= 1.0 and sensor_distance > 0.5:
		if robot_orientation >= -5 and robot_orientation <= 5:
		   data.append((DockInfraRed.NEAR_CENTER))
		   data.append((DockInfraRed.NEAR_CENTER))
		   data.append((DockInfraRed.NEAR_CENTER))
		   dock_ir_msg.data = data
		   self._publisher.publish(dock_ir_msg)
		   self._core_pub.publish(sensor_state_msg)
		else:
		   data.append((DockInfraRed.NEAR_CENTER))
		   data.append((DockInfraRed.NEAR_CENTER))
		   data.append((DockInfraRed.NEAR_CENTER))
		   dock_ir_msg.data = data
		   self._publisher.publish(dock_ir_msg)
		   self._core_pub.publish(sensor_state_msg)
	  elif sensor_distance <= 0.5:
	      sensor_state_msg.charger = SensorState.DOCKING_CHARGING
	      self._core_pub.publish(sensor_state_msg)
	      

      
def main():
    rospy.init_node('robot_dock_controller') 
    
    #publish DockInfraRed msgs based on sensor and distance
    publisher = rospy.Publisher("/mobile_base/sensors/dock_ir", DockInfraRed, queue_size = 10)
    core = rospy.Publisher("/mobile_base/sensors/core", SensorState, queue_size = 10)
    
    #create RobotController object
    controller = RobotController(publisher, core)
    
    #subscribe to /closest_landmark topic and get distance to the closest sensor
    rospy.Subscriber("/closest_landmark", LandmarkDistance, controller.distanceCallback)
    
    rospy.spin()
  

if __name__ == '__main__':
    main() 
