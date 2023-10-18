import odrive
from odrive.enums import *
import time,sys



odrv = odrive.find_any()
print(str(odrv.vbus_voltage))


odrv.config.dc_bus_overvoltage_trip_level = 50
odrv.config.dc_bus_undervoltage_trip_level = 45
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
odrv.axis0.controller.config.input_mode = InputMode.PASSTHROUGH
odrv.axis0.controller.config.control_mode = ControlMode.VELOCITY_CONTROL
odrv.axis0.config.torque_soft_min = -0.40271304347826087
odrv.axis0.config.torque_soft_max = 0.40271304347826087
odrv.axis0.config.encoder_bandwidth = 100
odrv.hall_encoder0.config.enabled = True
odrv.axis0.config.load_encoder = EncoderId.HALL_ENCODER0
odrv.axis0.config.commutation_encoder = EncoderId.HALL_ENCODER0


def connect():
    odrv.clear_errors
    odrv.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL
    return 1

def disconnect():
    odrv.axis0.requested_state = AxisState.IDLE
    return 1

def run(velocity = 0.5):
    odrv.axis0.controller.input_vel = velocity

def stop():
    odrv.axis0.controller.input_vel = 0







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