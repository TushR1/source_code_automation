# Selenium Automation Framework

A Python Selenium-based automation framework designed to automate web application testing.

The framework separates test logic from configuration by maintaining:

- XPath locators in a dedicated XPath file
- Application credentials in a separate credentials file
- Test scripts independently
- Logs and execution reports separately

This makes the framework easier to maintain and update when application locators or credentials change.

---

## Project Overview

The automation framework uses Selenium WebDriver to interact with the web application.

Instead of hardcoding XPath expressions and login credentials inside Python scripts:

- XPath values are maintained in `xpath.xlsx`
- Login credentials are maintained in `credentials.xlsx`
- Automation scripts read these values during execution
- Selenium performs the required UI actions
- Logs are generated during execution
- Execution results can be stored in reports

---

## Project Structure

```text
source_code_automation/
│
├── master.py
│
├── xpath.xlsx
├── credentials.xlsx
│
├── requirements.txt
│
├── logs/
│   └── automation.log
│
└── README.md
