# billiard_game.py
# Simple billiard game in CoppeliaSim using ZMQ Remote API
# Player inputs angle (deg) and power, then the white ball is hit like in billiards.

from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import math
import numpy as np
import time

def shoot_ball(sim, white_handle, angle_deg, power):
    """
    Simulate a billiard cue strike:
    - angle_deg: direction of shot (0° = +X axis, counter-clockwise)
    - power: scalar magnitude of impulse
    """
    # Convert angle to radians
    angle_rad = math.radians(angle_deg)
    # Force vector in XY plane
    Fx = power * math.cos(angle_rad)
    Fy = power * math.sin(angle_rad)
    Fz = 0.0  # no vertical force
    force = [Fx, Fy, Fz]

    # Torque is ignored for simplicity (pure translation)
    torque = [0.0, 0.0, 0.0]

    try:
        if hasattr(sim, "addForceAndTorque"):
            sim.addForceAndTorque(white_handle, force, torque)
            print(f"Shot applied with force {force}")
        else:
            # fallback
            sim.setObjectForce(white_handle, force)
            sim.setObjectTorque(white_handle, torque)
            print(f"Shot applied with setObjectForce/setObjectTorque {force}")
    except Exception as e:
        print("Could not apply shot:", e)

def get_ball_positions(sim, ball_handles):
    positions = {}
    for name, h in ball_handles.items():
        try:
            pos = sim.getObjectPosition(h, -1)
            positions[name] = (pos[0], pos[1])
        except Exception:
            positions[name] = (None, None)
    return positions

def main():
    print("=== Billiard Game Simulation ===")
    client = RemoteAPIClient()
    sim = client.getObject("sim")

    # start simulation
    sim.setStepping(False)
    sim.startSimulation()

    # handles
    balls = {
        "green": sim.getObject("/Sphere[0]"),
        "white": sim.getObject("/Sphere[6]"),
    }

    # main loop
    while True:
        print("\nInput your shot (or type q to quit):")
        cmd = input("Angle (deg, 0=+X): ").strip().lower()
        if cmd == "q":
            break
        try:
            angle = float(cmd)
        except:
            print("Invalid angle, try again.")
            continue

        try:
            power = float(input("Power (e.g. 10 = soft, 50 = strong): "))
        except:
            print("Invalid power, try again.")
            continue

        # shoot
        shoot_ball(sim, balls["white"], angle, power)

        # let simulation run
        print("Simulating for 3 seconds...")
        time.sleep(3)

        # report ball positions
        pos = get_ball_positions(sim, balls)
        print("--- Ball positions (XY) ---")
        for name, p in pos.items():
            print(f"{name}: ({p[0]:.3f}, {p[1]:.3f})")

    print("Stopping simulation...")
    sim.stopSimulation()
    client.close()

if __name__ == "__main__":
    main()
