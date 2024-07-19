#! usr/bin/env python3
import sys
import rospy
from pa1.srv import exponent_calc, exponent_calcResponse


def exp_calc_client(x, y):
    rospy.wait_for_service('exponent_calc_service_node')
    try:
        exponent_calc_service_node = rospy.ServiceProxy('exponent_calc_service_node', exponent_calc)
        response = exponent_calc_service_node(x,y)
        return response.x_to_the_power_y
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s to the power %s"%(x, y))
    print("%s to the power %s = %s"%(x, y, exp_calc_client(x, y)))
    