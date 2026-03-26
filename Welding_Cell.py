from robodk.robolink import Robolink, ITEM_TYPE_ROBOT

RDK = Robolink()
robot_abb = RDK.Item('ABB IRB 120-3/0.6', ITEM_TYPE_ROBOT)

if not robot_abb.Valid():
    raise Exception("Nie znaleziono robota!")

WELD_SPEED = 50
TRAVEL_SPEED = 150

weld_trajectory = [
    [ 20, -30, 30, 0, 80, 0],  #lewo prawo |przod  tyl | gora dol | przechyl na bok|kat nachylenia|krecenie
    [ 10, -30, 30, 0, 80, 0],
    [  0, -30, 30, 0, 80, 0], 
    [-10, -30, 30, 0, 80, 0],  
    [-14, -30, 30, 0, 80, 0],  
]

robot_abb.setSpeed(TRAVEL_SPEED)
robot_abb.MoveJ(robot_abb.JointsHome())

robot_abb.setSpeed(WELD_SPEED)
for joints in weld_trajectory:
    if RDK.Collisions()>0:
        RDK.ShowMessage("KOLIZJA!!! STOP")
        sys.exit()
    robot_abb.MoveJ(joints)

robot_abb.setSpeed(TRAVEL_SPEED)
robot_abb.MoveJ(robot_abb.JointsHome())
