# Task 1 - Format and Display Wikipedia Article Data

**Contributor:** Amarachi Ordor

---

## What it does

Reads a list of Wikipedia articles from a JavaScript array and displays each one on the page in this format:

```
Article "André Baniwa" (Page ID 6682420) was created at September 13, 2021.
```

---

## How to run it

1. Download `Task_1_Amarachi_Ordor.html`
2. Double-click it to open in any browser
3. The results appear on the page automatically

---

## Notes

Dates are parsed manually by splitting the `YYYY-MM-DD` string instead of using `new Date()`, which can shift the date by one day due to timezone issues.
