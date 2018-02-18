#!/usr/bin/env python
 
import rospy
from robot_messages.msg import LandmarkDistance
from std_msgs.msg import String
from kobuki_msgs.msg import DockInfraRed
from kobuki_msgs.msg import SensorState


class RobotController(object):
      def __init__(self, publisher, core_pub):
	  self._publisher = publisher
	  self._core_pub = core_pub


      def distanceCallback(self, msg):
	  #extract message data
	  sensor_name = msg.name
	  sensor_distance = msg.distance
	  
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
	      self.rightSensorDetected(dock_ir_msg, sensor_distance, sensor_state_msg)
	  elif sensor_name == 'Left Sensor':
	      self.leftSensorDetected(dock_ir_msg, sensor_distance, sensor_state_msg)
	  else: #sensor_name == 'Center Sensor'
	      self.centerSensorDetected(dock_ir_msg, sensor_distance, sensor_state_msg)
      
      
      def rightSensorDetected(self, dock_ir_msg, sensor_distance, sensor_state_msg):
	  data = []
	  if sensor_distance <= 2 and sensor_distance > 0.8:
	      data.append((DockInfraRed.FAR_RIGHT))
	      dock_ir_msg.data = data
	      self._publisher.publish(dock_ir_msg)
	      self._core_pub.publish(sensor_state_msg)
	  elif sensor_distance <= 0.8:
	      data.append((DockInfraRed.NEAR_RIGHT))
	      dock_ir_msg.data = data
	      self._publisher.publish(dock_ir_msg)
	      self._core_pub.publish(sensor_state_msg)
      
      def leftSensorDetected(self, dock_ir_msg, sensor_distance, sensor_state_msg):
	  data = []
	  if sensor_distance <= 2 and sensor_distance > 0.8:
	      data.append((DockInfraRed.FAR_LEFT))
	      dock_ir_msg.data = data
	      self._publisher.publish(dock_ir_msg)
	      self._core_pub.publish(sensor_state_msg)
	  elif sensor_distance <= 0.8:
	      data.append((DockInfraRed.NEAR_LEFT))
	      dock_ir_msg.data = data
	      self._publisher.publish(dock_ir_msg)
	      self._core_pub.publish(sensor_state_msg)
      
      def centerSensorDetected(self, dock_ir_msg, sensor_distance, sensor_state_msg):
	  data = []
	  if sensor_distance <= 2 and sensor_distance > 0.8:
	      data.append((DockInfraRed.FAR_CENTER))
	      dock_ir_msg.data = data
	      self._publisher.publish(dock_ir_msg)
	      self._core_pub.publish(sensor_state_msg)
	  elif sensor_distance <= 0.8 and sensor_distance > 0.45:
	      data.append((DockInfraRed.NEAR_CENTER))
	      dock_ir_msg.data = data
	      self._publisher.publish(dock_ir_msg)
	      self._core_pub.publish(sensor_state_msg)
	  elif sensor_distance <= 0.45:
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
