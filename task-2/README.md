# Task 2 - Check HTTP Status Codes for a List of URLs

**Contributor:** Amarachi Ordor

---

## What it does

Reads 166 URLs from a CSV file and prints the HTTP status code for each one:

```
(200) https://example.com/article
(404) https://example.com/missing-page
(CONNECTION ERROR) https://example.com/dead-site
```

Common status codes:
- **200** — page loaded fine
- **301/302** — page has moved/redirected
- **403** — access denied
- **404** — page not found
- **CONNECTION ERROR / TIMEOUT** — site could not be reached

---

## Requirements

- Python 3
- `requests` library — install it by running `pip install requests`

---

## How to run it

1. Download both `task_2_amarachi_ordor.py` and `Task_2_-_Intern.csv` into the same folder
2. Open your terminal in that folder
3. Run `pip install requests`
4. Run `python task_2_amarachi_ordor.py`

Results will print one line at a time. It may take a few minutes since it contacts 166 websites.
