; Auto-generated. Do not edit!


(cl:in-package robot_messages-msg)


;//! \htmlinclude LandmarkDistance.msg.html

(cl:defclass <LandmarkDistance> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (distance
    :reader distance
    :initarg :distance
    :type cl:float
    :initform 0.0)
   (z_orientation
    :reader z_orientation
    :initarg :z_orientation
    :type cl:float
    :initform 0.0))
)

(cl:defclass LandmarkDistance (<LandmarkDistance>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LandmarkDistance>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LandmarkDistance)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_messages-msg:<LandmarkDistance> is deprecated: use robot_messages-msg:LandmarkDistance instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <LandmarkDistance>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_messages-msg:name-val is deprecated.  Use robot_messages-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <LandmarkDistance>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_messages-msg:distance-val is deprecated.  Use robot_messages-msg:distance instead.")
  (distance m))

(cl:ensure-generic-function 'z_orientation-val :lambda-list '(m))
(cl:defmethod z_orientation-val ((m <LandmarkDistance>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_messages-msg:z_orientation-val is deprecated.  Use robot_messages-msg:z_orientation instead.")
  (z_orientation m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LandmarkDistance>) ostream)
  "Serializes a message object of type '<LandmarkDistance>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'z_orientation))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LandmarkDistance>) istream)
  "Deserializes a message object of type '<LandmarkDistance>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distance) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'z_orientation) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LandmarkDistance>)))
  "Returns string type for a message object of type '<LandmarkDistance>"
  "robot_messages/LandmarkDistance")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LandmarkDistance)))
  "Returns string type for a message object of type 'LandmarkDistance"
  "robot_messages/LandmarkDistance")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LandmarkDistance>)))
  "Returns md5sum for a message object of type '<LandmarkDistance>"
  "435047e3d21c4581dc109651649042ee")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LandmarkDistance)))
  "Returns md5sum for a message object of type 'LandmarkDistance"
  "435047e3d21c4581dc109651649042ee")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LandmarkDistance>)))
  "Returns full string definition for message of type '<LandmarkDistance>"
  (cl:format cl:nil "string name 	# Name of the simulated docking station landmark~%float64 distance 	# Distance to the landmark, in meters~%float64 z_orientation	# Orientation of the robot, in radians~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LandmarkDistance)))
  "Returns full string definition for message of type 'LandmarkDistance"
  (cl:format cl:nil "string name 	# Name of the simulated docking station landmark~%float64 distance 	# Distance to the landmark, in meters~%float64 z_orientation	# Orientation of the robot, in radians~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LandmarkDistance>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LandmarkDistance>))
  "Converts a ROS message object to a list"
  (cl:list 'LandmarkDistance
    (cl:cons ':name (name msg))
    (cl:cons ':distance (distance msg))
    (cl:cons ':z_orientation (z_orientation msg))
))
