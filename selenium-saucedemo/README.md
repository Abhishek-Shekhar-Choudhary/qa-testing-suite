# Selenium — SauceDemo

Python UI tests for [SauceDemo](https://www.saucedemo.com/) using pytest, Selenium 4, and a small Page Object Model. Waits are explicit (`WebDriverWait`); there are no fixed `sleep()` calls.

## Prerequisites

- Python 3.10+
- Google Chrome installed (ChromeDriver is resolved via `webdriver-manager`)

## Setup

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows (PowerShell):** `.\venv\Scripts\Activate.ps1`  
  If execution policy blocks the script, use: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`
- **macOS/Linux:** `source venv/bin/activate`

Then install dependencies:

```bash
pip install -r requirements.txt
```

## Run tests

From this directory (`selenium-saucedemo/`):

```bash
pytest
```

Tests run Chrome in headless mode by default (`tests/conftest.py`).

## Layout

| Path | Role |
|------|------|
| `pages/` | Page objects (locators + actions) |
| `tests/` | pytest specs |
| `requirements.txt` | Python dependencies |

Demo credentials are the ones published on SauceDemo (`standard_user` / `secret_sauce`).
