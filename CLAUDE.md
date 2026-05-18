# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies (requires Playwright browsers after pip install)
pip install -r requirements.txt
playwright install chromium

# Run all tests
pytest

# Run a single test file
pytest tests/test_01_login.py

# Run a specific test by name
pytest tests/test_01_login.py::test_login_valid_credentials

# Run headless (override pytest.ini default)
pytest --no-header --headed=false

# Run without slowmo
pytest --slowmo=0
```

`pytest.ini` sets these defaults for all runs: `--headed --browser chromium --html=reports/report.html --self-contained-html --slowmo=200 --screenshot=on`

## Architecture

This is a **Page Object Model (POM)** Playwright test suite targeting [https://app.sibme.com](https://app.sibme.com).

**Layer responsibilities:**

- `locators/` — All selectors live here (role-based Playwright selectors). Never put selectors directly in page objects or tests.
- `pages/` — Page Object classes. Each class wraps one page/screen of the app with action methods. No assertions here — only interactions.
- `tests/` — pytest test functions that compose page object methods to drive scenarios.
- `config/settings.py` — Reads `config/.env` via `python-dotenv` and exports `BASE_URL`, `LOGIN_URL`, `DEFAULT_TIMEOUT`, `USERNAME`, `PASSWORD`.
- `conftest.py` — Three fixtures: `browser` (session-scoped Chromium launch), `page` (per-test new page), and `launch_page` (logs in via `LoginPage` and returns an authenticated page for tests that start post-login).

**Test dependency chain:** Tests in `test_02_launchpad.py` and `test_03_vupload_workspace.py` use the `launch_page` fixture, meaning they begin already authenticated. `test_01_login.py` uses the bare `page` fixture and tests login itself.

**Credentials:** Stored in `config/.env` as `TEST_USER` and `TEST_PASS`. The `.env` file is not committed (listed in git status as untracked).

**Test assets:** `videos/test_video.mp4` is used by the workspace upload test — it must exist locally before running `test_03_vupload_workspace.py`.

## Adding New Tests

1. Add selectors to an existing file in `locators/` or create a new `locators/<page>_locators.py`.
2. Add or extend a Page Object in `pages/`.
3. Write the test in `tests/test_NN_<name>.py`.
4. If the test needs an authenticated session, use the `launch_page` fixture from `conftest.py`.
