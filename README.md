# Automated cookie clicker Playbot...

# Automated Cookie Clicker Play Bot (Python + Selenium)

This project features an **automated Cookie Clicker bot** created using **Python, Selenium**, and **undetected_chromedriver**.  
It automatically plays the Cookie Clicker game (https://orteil.dashnet.org/cookieclicker/) by clicking cookies, collecting golden cookies, purchasing upgrades, and keeping track of progress over time.

---

## Overview

The bot mimics user actions on the Cookie Clicker website.  
Here's what it does automatically:
1. Launches Cookie Clicker in a Chrome browser.
2. Chooses the English language if prompted.
3. Continuously clicks on the main cookie.
4. Instantly detects and clicks **Golden Cookies**.
5. Every few seconds, buys the **most expensive available product** or **upgrade**.
6. Records cookie counts over time into a CSV file to track progress.
7. Operates for a preset duration (default: 5 minutes) or until stopped manually.

---

## How the Bot Works (Step-by-Step)

### 1. Setup and Browser Initialization
The script utilizes `undetected_chromedriver` to open Chrome in stealth mode:
```python
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = uc.Chrome(options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
``` 
