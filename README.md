# Advanced Desktop Session Guard 🛡️

A professional, lightweight Python utility engineered to protect your personal computer from unauthorized physical access when you are away from your desk. It establishes a secure, full-screen lock overlay that prevents local tampering and desktop snooping.

---

## 🚀 Full Step-by-Step Installation Guide (For Beginners)

Follow these exact steps to install Python and launch the project on Windows without any errors.

### Step 1: Install Python Correctly (Crucial!)
If you don't have Python installed, or if Windows opens the Microsoft Store instead of running your script, follow this:
1. Go to the official website: [python.org/downloads](https://python.org) and download the latest version for Windows.
2. Run the downloaded installer.
3. **🚨 IMPORTANT:** At the very bottom of the installer window, check the box that says **"Add python.exe to PATH"**. If you skip this, your system won't recognize Python commands!
4. Click **Install Now** and wait for it to finish.

### Step 2: Clone or Download the Project
* **Option A (Easy):** Click the green **"Code"** button at the top right of this GitHub page, then click **"Download ZIP"**. Extract the downloaded archive into any folder on your PC.
* **Option B (Git):** Run this command in your terminal:
  ```bash
  git clone https://github.com
  cd advanced-desktop-session-guard
  ```

### Step 3: Install Required Libraries
This project relies on third-party libraries for networking and image rendering. You must install them before running the script.
1. Open **Command Prompt** (Terminal). Press `Win + R`, type `cmd`, and press Enter.
2. Navigate to your project folder using the `cd` command (e.g., `cd C:\Users\YourName\Desktop\advanced-desktop-session-guard`).
3. Run the following command to automatically install all dependencies:
  ```bash
  pip install Pillow
  ```

### Step 4: Run the Application
Once everything is installed, you can launch the session locker:
* **Via Terminal:** Inside your project folder, type:
  ```bash
  python main.py
  ```
* **Via Double-Click:** Alternatively, you can simply double-click the `main.py` file inside your folder to lock your workstation instantly.

---

## 🛠️ Internal Technology Stack
* **User Interface:** Tkinter (Native GUI Toolkit)
* **Image Processing:** Pillow (`PIL`) for high-quality background scaling
* **Networking:** Sockets & Urllib for secure local/remote connectivity sync
* **System Control:** OS & Sys modules for session handling

## 🔒 Security & Compliance Disclaimer
This project is developed strictly for personal privacy, physical access control, and educational purposes in system administration. It does not modify Windows registry files, alter core OS authentication mechanisms, or contain any malicious payloads.
