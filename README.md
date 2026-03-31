# Robotic Welding Cell (RoboDK & Python)

![Nagranie działania symulacji](presentation1.gif) 

A simulation project of an automated welding station using an ABB industrial robot, developed in the RoboDK offline programming environment. The project combines kinematics simulation with advanced control logic written in Python.

## ⚙️ Main Features and Program Logic

This project is not just a simple path animation; it includes implemented control and safety algorithms:

* **Dynamic speed adjustment:** The robot automatically slows down its movement during the actual welding process of the workpiece (cube), and returns to travel speed once the weld is completed.
* **Active collision detection:** If a collision is detected, the program immediately generates an alert and stops the arm's movement, preventing potential damage.

## 🛠️ Technologies Used

* **Environment:** RoboDK
* **Programming Language:** Python (RoboDK API)
* **Target Hardware:** ABB Industrial Robot

## 📁 Repository Contents

* `Welding_Cell.rdk` - The RoboDK station file containing the 3D environment, ABB robot kinematics, welding tool, and the workpiece.
* `Welding_Cell.py` - The script controlling the robot's logic (handling welding process speeds and the collision detection/emergency stop algorithm).
