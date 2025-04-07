# 🛠️ Log Monitoring & Alert Automation

A lightweight Python and Bash scripting project that automates log file monitoring, detects system errors, and outputs findings for manual or automated response workflows

---

## 📌 Project Overview

This project demonstrates how security teams or IT admins can proactively monitor log files for critical system errors using simple scripting techniques. It includes:

- Designed a Python script to parse log files and detect errors or anomalies based on defined patterns.
- Developed a complementary Bash script to scan multiple files and trigger alerts when specific error strings were found.
- Included robust logging and output tracking to assist in manual or automated incident response.

---

## ⚙️ Features

- 🔍 **Error Detection**: Scans `.log` files for keywords like `error`, `fail`, or custom regex patterns
- 📝 **Logging & Alert Prep**: Saves findings to file or console for integration with manual or automated alerting systems
- 🧩 **Modular & Customizable**: Easily expand to monitor more logs or hook into SIEM tools
- 🕒 **Automated Execution**: Cron-compatible for periodic scanning

---

## 📁 File Structure

```
Log-Monitoring-Alert-Automation/
├── scripts/
│   ├── python_sc.py        # Python script to parse logs and write output to file/console
│   └── Bash_sc.sh        # Bash script to call the Python script
├── README.md                 # Project overview and documentation
```

## 🐍 Technologies Used

- **Python 3**
- **Bash**
- **Cron (Linux Task Scheduler)**


## ✅ Features

- Scans logs for `ERROR` or `CRITICAL` entries
- Outputs detected issues to console or text file
- Configurable log path and error keyword settings
- Can be automated with cron for regular log scanning

## 📬 Contact

For suggestions, questions, or issues, feel free to [open an issue](https://github.com/your-username/log-monitoring/issues) or contact me on [LinkedIn](https://www.linkedin.com/in/your-link).
