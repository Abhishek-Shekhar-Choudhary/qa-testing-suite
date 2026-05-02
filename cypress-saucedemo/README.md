# Cypress — SauceDemo

End-to-end tests for [SauceDemo](https://www.saucedemo.com/) (Swag Labs) using Cypress. Selectors favor `data-test` attributes; the hamburger menu control is wrapped in **`cy.openSideMenu()`** because the stock site does not expose `data-test` on that button (see `cypress/support/commands.js`).

## Prerequisites

- Node.js 18 or newer
- Network access on **first** `npm install` / first `npm test` (Cypress downloads its app binary once)

## Setup

```bash
npm install
```

## Run tests

| Command | Description |
|---------|-------------|
| `npm test` | Run all specs headless (`cypress run`) |
| `npm run cy:open` | Open the Cypress interactive runner |

Headless runs use Cypress’s default browser (bundled Electron unless configured otherwise).

## Credentials (demo site)

Use `standard_user` / `secret_sauce` (published by SauceDemo for learning; not production secrets).
