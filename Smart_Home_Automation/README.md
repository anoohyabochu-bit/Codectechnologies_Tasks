# 🏠 Smart Home Automation System

A Python-based Smart Home Automation System that provides a web interface for monitoring and controlling smart home devices. The project integrates Flask, MQTT communication, SQLite database management, scheduled automation, and a virtual Raspberry Pi environment to simulate an IoT-based smart home without requiring physical hardware.

---

## 📌 Overview

The Smart Home Automation System demonstrates how software and IoT technologies can be combined to create a centralized platform for managing smart devices.

The application provides a web-based interface through which users can interact with connected devices. Device commands are processed by the Flask backend and can be communicated through MQTT to simulated devices running in a virtual Raspberry Pi environment.

The system also maintains device information using SQLite and supports scheduled automation for performing predefined actions automatically.

---

## 🎯 Objectives

- Develop a web-based smart home control system.
- Implement device communication using MQTT.
- Store and manage device information using SQLite.
- Provide scheduled automation capabilities.
- Simulate Raspberry Pi-based devices without physical hardware.
- Build a modular architecture using Python and Flask.
- Provide an interactive frontend for device management.

---

## ✨ Key Features

- 🌐 **Web-Based Control Panel**  
  Provides an interface for interacting with smart home devices.

- 💡 **Device Control**  
  Allows users to control the state of supported simulated devices.

- 📡 **MQTT Communication**  
  Enables lightweight communication between the application and smart devices.

- 🗄️ **SQLite Database**  
  Stores smart home device information and application data.

- ⏰ **Scheduled Automation**  
  Supports predefined device actions based on scheduled times.

- 🍓 **Virtual Raspberry Pi**  
  Simulates Raspberry Pi and device behavior without requiring physical hardware.

- 🔄 **Device Status Management**  
  Maintains and displays the current state of smart devices.

- 💻 **Hardware-Free Development**  
  Can be developed and demonstrated on a standard computer.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application and automation logic |
| Flask | Web application and backend |
| MQTT | IoT device communication |
| SQLite | Data storage |
| HTML | Web interface structure |
| CSS | User interface styling |
| JavaScript | Frontend interaction |
| Scheduler | Automated device actions |

---

## 📁 Project Structure

```text
Smart_Home_Automation/
│
├── app.py
├── database.py
├── mqtt_client.py
├── requirements.txt
├── scheduler.py
├── smart_home.db
├── virtual_raspberry_pi.py
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   └── index.html
│
└── README.md