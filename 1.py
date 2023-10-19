import odrive
from odrive.enums import *
import time,sys



odrv = odrive.find_any()
odrv.config.dc_bus_overvoltage_trip_level = 15
odrv.config.dc_bus_undervoltage_trip_level = 10.5
odrv.config.dc_max_positive_current = 10
odrv.config.dc_max_negative_current = -5
odrv.axis0.config.motor.motor_type = MotorType.HIGH_CURRENT
odrv.axis0.config.motor.torque_constant = 0.07191304347826087
odrv.axis0.config.motor.pole_pairs = 14
odrv.axis0.config.motor.current_soft_max = 28
odrv.axis0.config.motor.current_hard_max = 48
odrv.axis0.config.motor.calibration_current = 10
odrv.axis0.config.motor.resistance_calib_max_voltage = 2
odrv.axis0.config.calibration_lockin.current = 10
odrv.axis0.controller.config.control_mode = ControlMode.VELOCITY_CONTROL
odrv.axis0.controller.config.input_mode = InputMode.VEL_RAMP
odrv.axis0.controller.config.vel_ramp_rate = 1
odrv.axis0.config.torque_soft_min = -0.40271304347826087
odrv.axis0.config.torque_soft_max = 0.40271304347826087
odrv.axis0.config.encoder_bandwidth = 100
odrv.hall_encoder0.config.enabled = True
odrv.axis0.config.load_encoder = EncoderId.HALL_ENCODER0
odrv.axis0.config.commutation_encoder = EncoderId.HALL_ENCODER0

# setting PID gains
odrv.axis0.controller.config.vel_gain = 0.01
odrv.axis0.controller.config.vel_integrator_gain = 0.03


def connect():
    odrv.clear_errors
    odrv.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL
    if odrv.axis0.current_state == AxisState.CLOSED_LOOP_CONTROL:
        print("Connected")
    else:
        print("Error")
        exit()

def disconnect():
    odrv.axis0.requested_state = AxisState.IDLE
    if odrv.axis0.current_state == AxisState.IDLE:
        print("Disconnected")
    else:
        print("Error")
        exit()

def run(velocity = 0.7):
    odrv.axis0.controller.input_vel = velocity
    if odrv.axis0.current_state == AxisState.CLOSED_LOOP_CONTROL:
        print("Running")
    elif odrv.axis0.current_state == AxisState.IDLE:
        print("Error")
        exit()

def stop():
    odrv.axis0.controller.input_vel = 0
    if odrv.axis0.current_state == AxisState.CLOSED_LOOP_CONTROL:
        print("Stopped")
    else:
        print("Error")
        exit()

connect()
run()
time.sleep(30)
stop()





# odrv.axis0.requested_state = AxisState.MOTOR_CALIBRATION

# while odrv.axis0.current_state != AXIS_STATE_IDLE:
#         time.sleep(1)

# if odrv.axis0.disarm_reason != 0:
#         print("Disarmed: {}".format(odrv.axis0.disarm_reason))
#         print("Current state: {}".format(odrv.axis0.current_state))
#         sys.exit(1)
#         #odrv.clear_errors()

# # Wait for calibration to take place
# time.sleep(20)

# odrv.show_errors()