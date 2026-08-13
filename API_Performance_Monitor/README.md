# 🚀 API Performance Monitor

A Python-based API Performance Monitoring system that collects API metrics, stores them in SQLite, and visualizes performance data using Grafana.

## 📌 Project Overview

The API Performance Monitor is designed to track and analyze API performance in real time.

It records important metrics such as:

- ⏱️ API response time
- 🟢 Successful requests
- 🔴 Failed requests
- 📊 Total API requests
- 📈 API performance trends
- 🎯 API error rate

The collected data is stored in an SQLite database and displayed through an interactive Grafana dashboard.

## 🛠️ Technologies Used

- 🐍 Python
- 🌐 Flask
- 📡 Requests
- 🗄️ SQLite
- 📊 Grafana

## ✨ Features

- Monitor API response times
- Track successful and failed API requests
- Calculate average response time
- Calculate API error rate
- Count total API errors
- Visualize API performance using Grafana
- Store monitoring data in SQLite
- Simple and beginner-friendly implementation

## 📊 Grafana Dashboard

The dashboard contains six monitoring panels:

1. **Total API Requests**
2. **API Success vs Errors**
3. **API Response Time Over Time**
4. **Average Response Time by API**
5. **API Error Rate**
6. **Total API Errors**

## 📁 Project Structure

```text
API_Performance_Monitor/
│
├── app.py
├── database.py
├── monitor.py
├── performance.db
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
