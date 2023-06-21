from djitellopy import tello 
from time import sleep


#The Definition of constants

THE_DEFAULT_SPEED = 60
DIRECTION_MOVING_FORWARD = "forward"
DIRECTION_MOVING_BACKWARD = "backward"
DIRECTION_MOVING_LEFT = "left"
DIRECTION_MOVING_RIGHT = "right"

class TelloController:
    def __init__(self):
        self.drone = Tello()
    
    def connect(self):
        self.drone.connect()
        
    def getting_battery_percentage(self):
        return self.drone.get_battery()
    
    def takeoff(self):
        self.drone.takeoff()
        
    def land(self):
        self.drone.land()
        
    def send_rc_control(self, left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity):
        self.drone.send_rc_control(left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity)
    
    def move(self, direction, distance):
        if direction == DIRECTION_MOVING_FORWARD:
            self.send_rc_control(0, THE_DEFAULT_SPEED, 0, 0)
        elif direction == DIRECTION_MOVING_BACKWARD:
            self.send_rc_control(0, -THE_DEFAULT_SPEED, 0, 0)
        elif direction == DIRECTION_MOVING_LEFT:
            self.send_rc_control(-THE_DEFAULT_SPEED, 0, 0, 0)
        elif direction == DIRECTION_MOVING_RIGHT:
            self.send_rc_control(-THE_DEFAULT_SPEED, 0, 0, 0)
            
        sleep(distance)
        self.send_rc_control(0, 0, 0, 0)

# Creating the instance of our Controller

controller = TelloController()

try:
    controller.connect()
    controller.takeoff()
    controller.move(DIRECTION_MOVING_FORWARD, 3)
    controller.move(DIRECTION_MOVING_BACKWARD, 3)
    controller.move(DIRECTION_MOVING_LEFT, 3)
    controller.move(DIRECTION_MOVING_RIGHT, 3)
    controller.land()
    
except Exception as e:
    print("The error is: ", str(e))
    
finally:
    if controller.drone.flying:
        controller.land()
    controller.drone.end() 