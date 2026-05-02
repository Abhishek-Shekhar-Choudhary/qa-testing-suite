# QA Automation Practice Suite

A practical QA automation portfolio project covering **browser E2E testing (Cypress)**, **browser automation (Selenium + pytest)**, and **API testing (Postman + Newman)** against public demo targets.

## Prerequisites

- **Node.js 18+** (Cypress and Newman)
- **Python 3.10+** and **pip** (Selenium suite)
- **Google Chrome** installed locally (Selenium uses Chrome via webdriver-manager)

## Project overview

| Suite | Target | Purpose |
|--------|--------|---------|
| `cypress-saucedemo/` | [SauceDemo](https://www.saucedemo.com/) | Fast feedback, modern E2E patterns, custom commands |
| `selenium-saucedemo/` | SauceDemo | Language/framework diversity, Page Object Model, explicit waits |
| `postman-api-tests/` | [JSONPlaceholder](https://jsonplaceholder.typicode.com/) | Contract-style checks, negatives, chaining, Newman in CI |

SauceDemo credentials are the ones published on the site: `standard_user` / `secret_sauce` (demo only, not secrets).

**API note:** ReqRes was originally planned, but its public API now requires an `x-api-key`. This repo uses JSONPlaceholder for keyless, reliable runs; the Postman README explains how to adapt to ReqRes with a key if you add one privately (never commit keys).

## Tools used

- **Cypress** — E2E browser tests
- **Python, pytest, Selenium 4, webdriver-manager** — UI automation with Chrome
- **Postman collection format + Newman** — API tests from the CLI

## Folder structure

Run all commands from the **repository root** (`cd` into the suite folder as shown below).

```
qa-automation-practice/
├── README.md
├── cypress-saucedemo/
├── selenium-saucedemo/
├── postman-api-tests/
└── .gitignore
```

*(If your GitHub repository is named `qa-automation-practice`, use that name when you create the remote; the contents match this layout.)*

## What each suite tests

### Cypress (`cypress-saucedemo/`)

- Successful and failed login
- Add / remove items, cart badge count
- Full checkout flow
- Sort products by price (low → high), verified by ordered prices (not hard-coded product titles)
- Logout

Selectors favor `[data-test="..."]`. Shared login uses **`cy.login`** / **`cy.logoutViaUi`** (see `cypress/support/commands.js`).

### Selenium (`selenium-saucedemo/`)

- Successful and failed login
- Add product to cart
- Checkout through confirmation

Uses **explicit waits** (`WebDriverWait`) and a small **Page Object Model** under `pages/`.

### Postman / Newman (`postman-api-tests/`)

- GET/POST/PUT/DELETE on **users** and **posts**
- Status and body assertions, response time checks
- Negative cases (missing resources → 404)
- Environment variable usage and a **chained** list → single-user flow

## How to run — Cypress

```bash
cd cypress-saucedemo
npm install
npm test
npm run cy:open
```

- `npm test` — headless `cypress run` (first install may download the Cypress binary; requires network access)
- `npm run cy:open` — interactive runner (useful locally; not for headless CI)

## How to run — Selenium

**Windows (PowerShell), from repository root:**

```powershell
cd selenium-saucedemo
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

**macOS / Linux (bash), from repository root:**

```bash
cd selenium-saucedemo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
```

Chrome must be installed; ChromeDriver is downloaded via **webdriver-manager**.

## How to run — Postman / Newman

```bash
cd postman-api-tests
npm install
npm test
```

Import the `.postman_collection.json` and `.postman_environment.json` files into Postman for interactive runs.

## Testing concepts demonstrated

- **Smoke testing** — quick critical-path checks (login, one purchase path, core API GETs)
- **Regression testing** — repeatable suites you can run on every change
- **Negative testing** — invalid login, 404 API cases
- **End-to-end (E2E) testing** — full checkout in browser suites
- **API contract-style validation** — status codes, required JSON fields, response time budgets
- **Explicit waits** — Selenium avoids blind `sleep()`
- **Stable selectors** — `data-test` in Cypress; same attributes in Selenium page objects (with a single documented exception for the stock hamburger menu control)
- **Reusable commands / page objects** — DRY login and navigation abstractions
- **Test data handling** — inline demo data only; no secrets or production credentials
- **CI/CD readiness** — headless Cypress, headless Chrome in pytest, Newman CLI with exit codes

## Why these tests matter

They exercise the same risks teams care about in production: **authentication**, **critical user journeys**, **regression on catalog and checkout**, and **API behavior** including error paths. Showing this repo in an interview gives concrete talking points for **how** you structure automation, not only that you can click record.

## What I would improve in a production QA framework

- **Parallelization and sharding** — faster PR feedback (Cypress parallel, pytest-xdist, Newman split)
- **Reporting** — Allure, HTML dashboards, trace artifacts for flaky debugging
- **Environment matrix** — multiple browsers/devices, staging URLs, feature flags
- **Data strategy** — factories, API seeding, cleanup, or dedicated test tenants instead of shared demos
- **Secrets** — vault or CI variables for any real keys (e.g. if ReqRes or private APIs are used)
- **Visual and accessibility checks** — optional plugins or dedicated tools where product risk warrants them
- **Contract tests** — formal schemas (JSON Schema, Pact) alongside example-based Postman assertions

---

Built for clarity and interview discussion: small scope, readable code, and honest documentation about third-party demo limitations.
