# 🤖 Vision-Based Robotic Hand Teleoperation System

> Real-time AI-powered robotic hand control using Computer Vision, Embedded Systems, IoT Communication, and Human-Machine Interaction.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)
![ESP8266](https://img.shields.io/badge/ESP8266-IoT-red)
![ESP32](https://img.shields.io/badge/ESP32-Embedded%20Systems-red)
![PyQt5](https://img.shields.io/badge/PyQt5-GUI-purple)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📌 Overview

This project presents a **Vision-Based Robotic Hand Teleoperation Platform** capable of replicating real-time human hand movements on a robotic hand using Artificial Intelligence, Computer Vision, and Embedded Systems.

Unlike conventional glove-based systems that depend on flex sensors, this solution utilizes a camera-based hand tracking pipeline powered by **MediaPipe's 21-landmark hand pose estimation model**, enabling contactless and intuitive control.

The system captures human hand motion through a webcam, extracts skeletal landmarks, computes finger articulation angles, converts them into servo commands, and transmits control packets to a remote robotic hand via a TCP/IP communication channel.

---

## 🚀 Key Features

### ✅ Real-Time Hand Tracking
- MediaPipe Hands 21-landmark model
- Multi-finger articulation detection
- Contactless operation
- Robust landmark estimation

### ✅ Teleoperation
- Remote robotic hand control
- Network-based communication
- Real-time command transmission

### ✅ Human-Robot Interaction
- Natural gesture-based control
- Intuitive hand motion replication
- Vision-driven actuation

### ✅ Interactive Dashboard
- Live camera feed
- Hand skeleton visualization
- Servo telemetry monitoring
- Connection status monitoring

### ✅ Embedded Integration
- ESP8266 / ESP32 support
- Multi-servo control
- JSON packet processing
- TCP socket communication

---

# 🏗 System Architecture

```text
Human Hand
     │
     ▼
Laptop Camera
     │
     ▼
MediaPipe Hand Tracking
(21 Landmark Detection)
     │
     ▼
Finger Angle Estimation
     │
     ▼
Servo Mapping Algorithm
     │
     ▼
PyQt Control Dashboard
     │
     ▼
TCP/IP Communication
     │
     ▼
ESP8266 / ESP32
     │
     ▼
Robotic Hand Actuation
```

---

# 🧠 AI & Computer Vision Pipeline

The vision subsystem is built using:

### MediaPipe Hands

The model performs:

1. Palm Detection
2. Hand Landmark Regression
3. Temporal Tracking

Detected Landmarks:

```text
21 Keypoints
```

Including:

```text
Wrist
Thumb
Index Finger
Middle Finger
Ring Finger
Pinky Finger
```

The landmark data is processed using geometric vector operations to compute finger articulation angles.

---

# ⚙️ Kinematic Processing

Finger movement estimation is performed using:

```python
cos(θ) = (A·B)/(|A||B|)
```

Where:

- A = Joint Vector 1
- B = Joint Vector 2

Computed joint angles are mapped to:

```text
Servo Range:
0° → 180°
```

This enables direct robotic finger replication.

---

# 🌐 Communication Layer

The project implements a custom TCP/IP communication framework.

### Packet Format

```json
{
  "id": "laptop",
  "to": "espB",
  "msg": {
    "type": "servos",
    "thumb": 90,
    "index": 45,
    "middle": 120,
    "ring": 30,
    "pinky": 10
  }
}
```

### Features

- JSON-based messaging
- Low-latency communication
- Extensible protocol design
- Real-time robotic control

---

# 🔌 Embedded System

### Microcontroller

- ESP8266
- ESP32

### Responsibilities

- Receive JSON packets
- Parse servo commands
- Generate PWM outputs
- Control robotic hand actuators

### Libraries

```cpp
ArduinoJson
ESP8266WiFi
Servo
```

---

# 🖥 Dashboard

A desktop dashboard was developed using PyQt5.

Features include:

- Live camera stream
- Hand landmark visualization
- Servo angle monitoring
- Communication status
- Real-time system feedback

---

# 📊 Performance Metrics

| Metric | Value |
|----------|----------|
| Landmark Points | 21 |
| FPS | 25–35 |
| Servo Channels | 5 |
| Communication | TCP/IP |
| Control Method | Vision-Based |
| Tracking Type | Contactless |
| Inference | CPU-Based |
| Latency | ~30–80 ms |

---

# 🛠 Technologies Used

## Software

- Python
- OpenCV
- MediaPipe
- NumPy
- PyQt5
- Socket Programming

## Embedded

- ESP8266
- ESP32
- Arduino Framework

## Computer Vision

- MediaPipe Hands
- Hand Pose Estimation
- Landmark Tracking

## Networking

- TCP/IP
- JSON Serialization

---

# 🔬 Engineering Domains Involved

This project integrates multiple engineering disciplines:

- Computer Vision
- Artificial Intelligence
- Embedded Systems
- Internet of Things (IoT)
- Robotics
- Human Machine Interaction (HMI)
- Real-Time Systems
- Mechatronics

---

# 🏭 Hardware Development Experience

During development, hands-on experience was gained in:

- PCB Designing (KiCad)
- CNC PCB Milling
- Embedded Hardware Prototyping
- Laser Cutting
- 3D Printing
- Mechanical Assembly
- Servo Actuation Systems
- Hardware-Software Co-Design

---

# 🎯 Applications

- Robotic Teleoperation
- Assistive Robotics
- Prosthetic Research
- Human-Machine Interfaces
- Industrial Manipulators
- Remote Control Systems
- Educational Robotics

---

# 👨‍💻 Team

Developed by a team of 4 members.

### Leadership & Contributions

- Team Lead
- System Architecture Design
- Computer Vision Pipeline Development
- Communication Framework Design
- Embedded System Integration
- Dashboard Development

---

# 📈 Future Improvements

- 3D Robotic Hand Visualization
- Gesture Recognition
- ROS2 Integration
- Web-Based Dashboard
- Multi-Hand Tracking
- Cloud Teleoperation
- Digital Twin Implementation

---

## ⭐ If you find this project interesting, consider giving the repository a star.
