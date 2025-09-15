# Billiard-Coppeliasim
<img width="1385" height="669" alt="Screenshot 2025-09-15 235325" src="https://github.com/user-attachments/assets/fa55f822-eeb1-4b45-9663-c1d3b0946cb4" />
This project implements a simple **virtual billiard game** using **CoppeliaSim** and **Python (ZMQ Remote API)**.  
The user can input a **shot angle** and **power** (like hitting a cue ball with a stick), and the program will translate it into a force applied to the white ball.  

---

## 🎯 Features
- Connects Python with CoppeliaSim via ZMQ Remote API.
- User input: **shot angle (degrees)** and **power (scalar)**.
- Input is converted into a global force vector applied to the cue ball.
- Prints updated ball positions after each shot.
- Educational purpose: understanding how to acquire data and send commands in CoppeliaSim.

## ⚙️ Installation
1. Make sure **Python 3.8+** is installed.  
2. Install the required libraries:  
   ```bash
   pip install coppeliasim-zmqremoteapi-client numpy

## 🛠️ Tantangan
- Perbedaan versi API (misalnya fungsi addForceAndTorque tidak selalu sama).
- Konversi input sederhana (sudut + power) menjadi vektor gaya global.
- Sinkronisasi antara Python dan simulasi di CoppeliaSim.

## ✨ Skill yang Dipelajari
- Integrasi Python–CoppeliaSim menggunakan ZMQ Remote API.
- Simulasi gaya impulsif dan torsi.
- Membuat program interaktif sederhana via terminal.

## 🚀 How to Run
- Open CoppeliaSim and load a scene containing:
  
  Green ball → /Sphere[0]
  
  White (cue) ball → /Sphere[6]
- Start the simulation in CoppeliaSim (or let the script start it automatically).
- Run the program in the terminal:testplay.py
- Follow the terminal instructions to enter the shot angle and power.

## ⌨️ Supported Input
- Shot Angle (deg) → in degrees (0° = +X axis direction).
- Power → positive real number (e.g., 10 = soft shot, 50 = strong shot).
- Exit the program → type q when asked for the angle.
- Example input:
   ```bash
   Angle (deg, 0=+X): 45
   Power (e.g. 10=soft, 50=strong): 30

## 📤 Example Output
- After the shot is applied and the simulation runs for ~3 seconds, the ball positions are printed in the terminal.
- Example result:
   ```bash
   {'green': (0.523, 1.240), 'white': (1.875, 0.664)}

---

<img width="500" height="206" alt="image" src="https://github.com/user-attachments/assets/61b7ee59-2dc5-4ffb-85f1-05710c14791c" /> 
