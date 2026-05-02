# Postman / Newman — API tests

Runnable API checks against **[JSONPlaceholder](https://jsonplaceholder.typicode.com/)** (public, no API key).

**Note on ReqRes:** [ReqRes](https://reqres.in/) now responds with `401` and requires an `x-api-key` header for its hosted API. This portfolio uses JSONPlaceholder so `npm test` works out of the box in CI and on interview machines. You can still import the same patterns into Postman and swap `baseUrl` to ReqRes with your own key if you want both demos.

## What is covered

| Area | Details |
|------|---------|
| HTTP verbs | GET, POST, PUT, DELETE for `/users` and `/posts` |
| Status codes | Assertions for 200, 201, 404 (and 200 on DELETE, as returned by JSONPlaceholder) |
| Body checks | Key presence and representative values (schema-style checks) |
| Performance | `pm.response.responseTime` upper bound on selected requests |
| Environment | `baseUrl`, `userId` (filled by the chained folder) |
| Chaining | List users → store first `userId` → GET `/users/{{userId}}` |
| Negative tests | Non-existent user and post IDs (expect 404) |

Import `QA-Automation-Practice.postman_collection.json` and `QA-Automation-Practice.postman_environment.json` into Postman to run or edit requests interactively.

## Prerequisites

- Node.js 18+

## Setup

```bash
npm install
```

## Run with Newman

```bash
npm test
```

Or:

```bash
npx newman run QA-Automation-Practice.postman_collection.json -e QA-Automation-Practice.postman_environment.json --timeout-request 20000
```

`npm test` applies the same per-request timeout so slow networks fail fast instead of hanging.
