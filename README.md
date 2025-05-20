# Selenium Python UI Automation - SauceDemo

This is an automated UI testing project using Selenium with Python and pytest for the [Sauce Demo](https://www.saucedemo.com/) web application. It includes tests for login functionality, product interaction, and checkout processes, complete with screenshots.

---

# Project Structure

selenium_python_projects/
│
├── pages/ # Page Object Model (POM) classes
│ └── login_page.py
│
├── tests/ # Test cases
│ └── test_login.py
│
├── utils/ # Driver factory or helper utilities
│ └── driver_factory.py
│
├── screenshots/ # Screenshots captured on test failure
│
├── conftest.py # pytest fixtures & hooks
├── requirements.txt # Python dependencies
├── README.md # Project documentation


---

## 🛠 Setup Instructions

# 1. Clone this repo

```bash
git clone https://github.com/your-username/selenium_python_projects.git
cd selenium_python_projects

# 2. Set up and activate a virtual environment (recommended)

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux

# 3. Install dependencies

pip install -r requirements.txt

# 4. Running Tests

pytest -s

On test failure, a screenshot will be saved to the screenshots/ folder.

# 5. Screenshot Naming 
Filenames include test name and timestamp, e.g., test_valid_login_2025-05-20_153012.png

Screenshot logic is handled in conftest.py

screenshots are generated automatically after test execution

# 6. Key Features
Selenium WebDriver for UI interactions

Pytest framework

Screenshot capture on test failure

Modular POM structure

