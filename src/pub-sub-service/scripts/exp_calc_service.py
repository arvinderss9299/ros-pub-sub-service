#! usr/bin/env python3
import rospy
from pa1.srv import exponent_calc, exponent_calcResponse

def callback(request):
    print("%s to the power %s = %s"%(request.x, request.y, (pow(request.x,request.y))))
    return exponent_calcResponse(pow(request.x,request.y))

def exp():
    rospy.init_node("exp_calc_service")
    service=rospy.Service("exponent_calc_service_node", exponent_calc, callback)
    print("Ready to calculate x to the power y")
    rospy.spin()

if __name__ == '__main__':
    exp()