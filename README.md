<<<<<<< HEAD
# 🚀 Cloud Nginx Reverse Proxy Project

## 📌 Description
This project demonstrates a real-world cloud web architecture using:

- Nginx as a reverse proxy
- Python Flask backend
- HTTPS (SSL configuration)
- Systemd service for production deployment

## 🏗️ Architecture
Client → Nginx → Flask Application

## ⚙️ Features
- Reverse proxy configuration
- Secure HTTPS setup (self-signed SSL)
- Backend API with Flask
- Persistent service using systemd
- Log monitoring and debugging

## 🛠️ Technologies Used
- Linux (Ubuntu)
- Nginx
- Python (Flask)
- Git & GitHub

## 🌐 How to Run

bash
# Install dependencies
sudo apt update
sudo apt install nginx python3-pip -y

# Install Flask
pip3 install flask

# Run app
python3 app.py

## Author 
OBED LEMBISSA MAGNAGNA
>>>>>>> 7529a2a (Initial commit - Nginx reverse proxy project)

## 💡 Project Goal
This project was built to demonstrate hands-on cloud engineering skills, including web server configuration, reverse proxy setup, HTTPS security, and Linux service management.

## System Monitoring Script

This script monitors CPU, memory, and disk usage.

### Sample Output

CPU: 25% | Memory: 40% | Disk: 60%  
CPU: 30% | Memory: 42% | Disk: 61%  

### Automation

Automated using cron:

* * * * * /usr/bin/python3 /home/ubuntu/monitor.py
