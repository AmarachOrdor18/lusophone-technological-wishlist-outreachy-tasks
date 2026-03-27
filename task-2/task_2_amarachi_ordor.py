import csv
import requests

# Open the CSV file and read all URLs
with open("Task 2 - Intern.csv", newline="", encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        url = row["urls"].strip()
        try:
            response = requests.get(url, timeout=10, allow_redirects=True)
            print(f"({response.status_code}) {url}")
        except requests.exceptions.ConnectionError:
            print(f"(CONNECTION ERROR) {url}")
        except requests.exceptions.Timeout:
            print(f"(TIMEOUT) {url}")
        except requests.exceptions.RequestException:
            print(f"(ERROR) {url}")
