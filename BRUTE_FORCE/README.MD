# Brute Force Attack on OWASP Juice Shop

## Overview
This script performs a brute force attack on the login page of **OWASP Juice Shop**, a deliberately insecure web application designed for security training and testing. The script automates sending login attempts using a username and a wordlist of passwords.

**Disclaimer:** This script is for educational and ethical hacking purposes only. Unauthorized use on systems you do not own or have explicit permission to test is illegal.

## Features
- Uses a wordlist to attempt multiple passwords.
- Sends JSON payloads to simulate login requests.
- Parses responses to detect successful logins.

## Requirements
- Python 3.x
- Requests library
- A wordlist file (e.g., `rockyou.txt`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bruteforce-juiceshop.git
   cd bruteforce-juiceshop
   ```
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. Ensure you have a wordlist (e.g., `rockyou.txt`) placed in the same directory.

## Usage
Run the script with the target URL and username:
```bash
python brute_force.py --url http://localhost:3000 --username admin --wordlist rockyou.txt
```

### Example
```bash
python brute_force.py --url http://localhost:3000 --username admin --wordlist C:\Users\Administrator\Downloads\rockyou.txt
```

## Configuration
- Modify `brute_force.py` to customize headers or request payloads.
- Adjust delays or retries to prevent detection.

## Legal Disclaimer
This tool is intended for educational use only. Use it responsibly and only on systems where you have explicit permission. Unauthorized use is illegal and unethical.

## References
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)

