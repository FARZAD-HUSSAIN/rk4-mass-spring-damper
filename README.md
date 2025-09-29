# Mass-Spring-Damper Simulation with RK4

A Python simulation of a **mass-spring-damper system** using the **Runge-Kutta 4th Order (RK4) method**.
This project models the dynamics of mechanical vibrations and demonstrates the use of numerical methods to solve ordinary differential equations (ODEs).

---

## 📑 Table of Contents

1. [Introduction](#introduction)
2. [Mathematical Background](#mathematical-background)
3. [Features](#features)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Code Structure](#code-structure)
7. [Examples / Output](#examples--output)
8. [Customization](#customization)
9. [Comparison / Validation](#comparison--validation)
10. [Applications](#applications)
11. [Contributing](#contributing)
12. [Acknowledgements / References](#acknowledgements--references)

---

## 📘 Introduction

The mass-spring-damper system is a fundamental mechanical model used to study **vibrations, oscillations, and control systems**.
This project numerically simulates its motion by solving the governing differential equations using the **RK4 method**, which is known for its balance of accuracy and efficiency.

---

## 📐 Mathematical Background

The motion of a damped spring-mass system under external force is described by:

$$ m \ddot{x}(t) + c \dot{x}(t) + kx(t) = F(t) $$

Where:

* ( m ) = mass
* ( c ) = damping coefficient
* ( k ) = spring constant
* ( x(t) ) = displacement
* ( F(t) ) = external force

Rewritten as first-order ODEs:

[
\begin{aligned}
x_1 &= x \quad \text{(position)} \
x_2 &= \dot{x} \quad \text{(velocity)} \
\dot{x}_1 &= x_2 \
\dot{x}_2 &= \frac{F - c x_2 - k x_1}{m}
\end{aligned}
]

The system is solved with the **Runge-Kutta 4th Order Method (RK4):**

[
x_{n+1} = x_n + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)
]

---

## ✨ Features

* Simulation of displacement and velocity over time
* Implementation of the **RK4 method** for solving ODEs
* Configurable mass, damping, stiffness, and force
* Clean visualization with **Matplotlib**
* Beginner-friendly and modular code

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/rk4-mass-spring-damper.git
cd rk4-mass-spring-damper
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Dependencies:

* `numpy`
* `matplotlib`

---

## ▶️ Usage

Run the simulation:

```bash
python main.py
```

This will generate plots of position and velocity vs time.

---

## 📂 Code Structure

```
rk4-mass-spring-damper/
│── main.py              # Entry point, runs the simulation
│── README.md            # Documentation
│── requirements.txt     # Python dependencies
```

---

## 📊 Examples / Output

Simulation output plots:

![image alt](https://github.com/FARZAD-HUSSAIN/rk4-mass-spring-damper/blob/850690186db7ffc45b457d97c43c60179b74ef81/Figure_1.png)
*Figure: Position and velocity response of the mass-spring-damper system.*

---

## 🔧 Customization

Modify parameters inside `main.py`:

```python
c = 4   # damping coefficient
k = 2   # spring constant
m = 20  # mass
F = 5   # external force

x_init = [0.0, 0.0]  # [initial position, initial velocity]
start_time = 0.0
stop_time = 60.0
increment = 0.1
```

---

## 📈 Comparison / Validation

* **RK4** is more accurate and stable than **Euler’s method** for this problem.
* Euler tends to diverge for stiff systems, while RK4 remains stable.

---

## 🌍 Applications

Mass-spring-damper systems are widely applicable in:

* Mechanical vibration analysis
* Structural dynamics
* Vehicle suspension modeling
* Robotics and control systems
* Seismology and wave propagation studies

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push to branch (`git push origin feature-name`)
5. Open a Pull Request

---

## 📚 Acknowledgements / References

* Numerical Methods for Engineers – Chapra & Canale
* Ogata, K. *Modern Control Engineering*
* MIT OpenCourseWare – Differential Equations and Dynamical Systems

---
