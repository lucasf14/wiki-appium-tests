# Wikipedia Mobile App Tests

## Description
This project automates the Android Wikipedia mobile application using Python, Pytest and Appium.
It was developed and tested on macOS, using an Android emulator as the execution environment.
The designed test cases validate the search functionality, article navigation, and content verification.

---
## Project Structure
```
├── apk                     # Applications to test
│   └── wikipedia.apk
├── data                    # Test data
│   ├── __init__.py
│   └── search_data.py      # Search terms and expected values
├── pages                   # Page Object Models
│   ├── __init__.py
│   ├── article_page.py     # Article page locators and methods
│   ├── explore_page.py     # Explore page locators and methods
│   └── page.py             # Base page shared locators and methods
└── tests                   # Test files
    ├── __init__.py
    ├── conftest.py         # Pytest fixtures
    ├── test_history.py     # History validation tests
    └── test_search.py      # Search validation tests
```
---
## Assumptions
The application always starts in a fresh state, and therefore some button actions were implemented in order to support the app's fresh start:
* The Skip button, when launching the app
* The Close button, when opening an article for the first time
  
---
## Test Scenarios

### 1. Invalid Search Flow Validation
Validate that an invalid (or non-existing) search term returns no results.

### 2. Valid Search and Article Content Validation
Validate that a valid search term returns matching results, open the corresponding article and verify some Quick Facts content.

### 3. Search History Validation
Validate that previously opened articles are correctly stored in the search history after opening multiple articles.

---
## Used Emulator
- **Device**: Pixel 8
- **API**: 34
  
---
## Setup

### 1. Install Android Studio
Download and install Android Studio from: https://developer.android.com/studio

### 2. Create Emulator  
1. Open Android Studio
2. Go to **More Actions**
3. Select **Virtual Device Manager**
4. Click **Create Virtual Device** button
5. Select:
    * **Device**: Pixel 8
    * **API**: 34
6. Click **Next**
7. Enter **AppiumTest** in the **Name** field
8. Click **Finish**

### 3. Set environment variables
1. Add to `.zshrc` or `.bashrc`
```bash
export ANDROID_HOME=$HOME/Library/Android/sdk

export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
```
2. Reload shell 
```bash
source ~/.zshrc
```

### 4. Install Node.js
```bash
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash

# in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"

# Download and install Node.js:
nvm install 25
```

### 5. Install APK in emulator
```bash
adb install apk/wikipedia.apk
```

### 6. Install Appium
```bash
npm install -g appium
```

### 7. Install Appium driver
```bash
appium driver install uiautomator2
```

### 8. Create virtual environment
```bash
python3 -m venv venv
source path/to/venv/bin/activate
```

### 9. Install requirements
```bash
pip3 install -r requirements.txt
```

---
## Running Tests

### Run Appium server
```bash
appium
```

### Run emulator
```bash
emulator -avd AppiumTest
```

### Run tests
```bash
pytest -v -s tests/ 
```

### Run tests with logs
```bash
pytest -v -s --log-cli-level=ERROR tests/ 
```
