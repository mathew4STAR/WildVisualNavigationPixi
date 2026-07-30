#!/usr/bin/python3
#
# Diffbot state converter for WVN.
# Converts the diff-drive Gazebo outputs into the RobotState and TwistStamped
# messages expected by the WVN learning node.
#
#   /odom (nav_msgs/Odometry)  -->  /wild_visual_navigation_node/robot_state (RobotState)
#   /cmd_vel (geometry_msgs/Twist) -->  /wild_visual_navigation_node/reference_twist (TwistStamped)
#
from geometry_msgs.msg import Twist, TwistStamped
from nav_msgs.msg import Odometry
from wild_visual_navigation_msgs.msg import RobotState, CustomState
import rospy


def odom_callback(odom_msg):
    robot_state_msg = RobotState()

    # Header
    robot_state_msg.header = odom_msg.header

    # Extract pose
    robot_state_msg.pose.header = odom_msg.header
    robot_state_msg.pose.pose = odom_msg.pose.pose

    # Extract twist
    robot_state_msg.twist.header = odom_msg.header
    robot_state_msg.twist.header.frame_id = odom_msg.child_frame_id
    robot_state_msg.twist.twist = odom_msg.twist.twist

    # Build the vector state expected by WVN
    vector_state = CustomState()
    vector_state.name = "vector_state"
    vector_state.dim = 7 + 6  # pose (7) + twist (6)
    vector_state.values = [0.0] * vector_state.dim
    vector_state.labels = [""] * vector_state.dim

    # Pose: tx, ty, tz, qx, qy, qz, qw
    vector_state.values[0] = robot_state_msg.pose.pose.position.x
    vector_state.values[1] = robot_state_msg.pose.pose.position.y
    vector_state.values[2] = robot_state_msg.pose.pose.position.z
    vector_state.values[3] = robot_state_msg.pose.pose.orientation.x
    vector_state.values[4] = robot_state_msg.pose.pose.orientation.y
    vector_state.values[5] = robot_state_msg.pose.pose.orientation.z
    vector_state.values[6] = robot_state_msg.pose.pose.orientation.w

    # Twist: vx, vy, vz, wx, wy, wz
    vector_state.values[7] = robot_state_msg.twist.twist.linear.x
    vector_state.values[8] = robot_state_msg.twist.twist.linear.y
    vector_state.values[9] = robot_state_msg.twist.twist.linear.z
    vector_state.values[10] = robot_state_msg.twist.twist.angular.x
    vector_state.values[11] = robot_state_msg.twist.twist.angular.y
    vector_state.values[12] = robot_state_msg.twist.twist.angular.z

    for i, label in enumerate(["tx", "ty", "tz", "qx", "qy", "qz", "qw",
                                "vx", "vy", "vz", "wx", "wy", "wz"]):
        vector_state.labels[i] = label

    robot_state_msg.states.append(vector_state)

    robot_state_pub.publish(robot_state_msg)


def twist_callback(msg):
    out_msg = TwistStamped()
    out_msg.header.stamp = rospy.Time.now()
    out_msg.header.frame_id = "base_link"
    out_msg.twist = msg
    ref_twist_pub.publish(out_msg)


if __name__ == "__main__":
    rospy.init_node("diffbot_state_converter_node")

    # Odometry -> RobotState
    odom_sub = rospy.Subscriber("/odom", Odometry, odom_callback, queue_size=20)
    robot_state_pub = rospy.Publisher(
        "/wild_visual_navigation_node/robot_state", RobotState, queue_size=20
    )

    # Twist cmd -> TwistStamped
    cmd_sub = rospy.Subscriber("/cmd_vel", Twist, twist_callback, queue_size=20)
    ref_twist_pub = rospy.Publisher(
        "/wild_visual_navigation_node/reference_twist", TwistStamped, queue_size=20
    )

    rospy.loginfo("[diffbot_state_converter_node] ready")
    rospy.spin()
