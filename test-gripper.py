import time
from combinewave.robot.drivers import rs485_connection
from combinewave.robot.drivers.rs485.gripper import gripper

connection = rs485_connection.RS485(port='com16', baudrate=115200)

my_gripper = gripper.Gripper(modbus_connection=connection, unit=1)

# input("press any key to continue")
my_gripper.initialization()
my_gripper.set_rotation_force(99)
# my_gripper.gripper_open(60)
time.sleep(4)
# input("press any key to continue")
my_gripper.rotate(300)

i = 1
while i<=100:
    ok = my_gripper.is_rotation_ok()
    print(ok)
    time.sleep(0.1)
    i = i+1


# time.sleep(2)

# my_gripper.gripper_close(10)
# time.sleep(0.1)

# d = my_gripper.get_rotation_position()
# print(d)
# time.sleep(5)
# d = my_gripper.get_rotation_position()
# print(d)

# my_gripper.rotate(-360)
# time.sleep(0.1)


# my_gripper.gripper_open(90)
# time.sleep(0.1)
# d = my_gripper.get_rotation_position()
# print(d)

# my_gripper.set_rotation_force(90)

# my_modbus.rotate(3600)
# time.sleep(2)
# my_modbus.gripper_open(90)
# time.sleep(1)
# my_modbus.gripper_open(10)
# time.sleep(1)
# my_modbus.gripper_open(90)
# time.sleep(1)
# my_modbus.get_rotation_degree()

# my_modbus.init()
# my_modbus.read(address=0x0101, count=2)
# my_modbus.gripper_open(10)
# # my_modbus.close()

# my_modbus.enable_motor()count
# my_modbus.move_to(10000)
# time.sleep(20)
# my_modbus.disable_motor()
# my_modbus.read(address=43, count=1)
#my_modbus.read_input(address=0, count=10)
