# Django Backend Baseline

## Reference

- Verified on: 2026-11-06
- Branch: `chore/document-backend-baseline`
- Related issue: [#64](https://github.com/Theffy92/BitacoraFit/issues/64)
- Predecessor baseline issue: [#56](https://github.com/Theffy92/BitacoraFit/issues/56)
- Python version: 3.11.0
- Django version: 5.2.12
- Database: PostgreSQL, configured through environment variables; the server version was not
  recorded during these checks

This baseline covers the existing Django application before the
API transition.

## Local Setup

From the repository root:

1. Activate the existing virtual environment:
   `source /Users/username/Dev_foldername/BitacoraFit/.venv/bin/activate`
2. Copy `.env.example` to `.env` and replace the placeholders with local
   development values.
3. Create the PostgreSQL database and user named by the database
   environment variables.
4. Change into the Django project directory:
   `cd src`
5. Apply migrations:
   `python manage.py migrate`
6. Install the Tailwind dependencies:
   `cd globaltheme/static_src && npm install`
7. Build the Tailwind stylesheet after making Tailwind changes:
   `npm run build`
8. Start the Tailwind development watcher in `src/globaltheme/static_src`:
   `npm run dev`
9. In a separate terminal, activate the virtual environment, change into
   `src`, and start the Django development server:
   `python manage.py runserver`

Keep the Tailwind watcher running while using the web application. Run
`npm run build` in `src/globaltheme/static_src` whenever Tailwind changes
need to be compiled for a new build.

Required environment variables:

- `DJANGO_SECRET_KEY`: Django signing and cryptographic secret.
- `DEBUG`: Enables development behavior; currently set to `True` for local use.
- `DB_NAME`: PostgreSQL database name.
- `DB_USER`: PostgreSQL username.
- `DB_PASSWORD`: PostgreSQL password.
- `DB_HOST`: PostgreSQL host.
- `DB_PORT`: PostgreSQL port.

The `.env` file contains local values and must not be committed.

## Verification Results

| Check | Command | Observed result |
|---|---|---|
| Django system checks | `python manage.py check` | Passed; no issues reported. |
| Tracking tests | `python manage.py test tracking` | Passed; 9 tests ran successfully. |
| Migration status | `python manage.py showmigrations` | Passed; all listed migrations for `admin`, `auth`, `contenttypes`, `sessions`, and `tracking` are applied. |
| Ruff lint checks | `ruff check .` | Passed. |
| Black formatting | `black --check .` | Passed; 23 files would be left unchanged. |

## Manual Verification

Start commands:

1. In `src/globaltheme/static_src`:
   `npm run dev`
2. In a separate terminal, after activating the virtual environment and
   changing into `src`:
   `python manage.py runserver`

- Application starts with Tailwind watcher and Django server: Not rerun as
  part of this documentation update.
- Login works: Not rerun as part of this documentation update.
- Dashboard displays the signed-in user's records: Not rerun as part of this documentation update.
- Weight-entry creation works: Not rerun as part of this documentation update.
- Weight history displays records: Not rerun as part of this documentation update.

Use a development account and fictional entries for manual checks.

## Test Database

Django uses the configured `default` PostgreSQL connection for tests and
creates a separate test database from it. The tracking test run reported
`Creating test database for alias 'default'...` and
`Destroying test database for alias 'default'...`, confirming that the
development database is not used for test data.

## Changes Made During Verification

- Corrected import ordering, formatting, and Ruff class-attribute warnings
  during the backend baseline work.
- Removed the redundant `WeightEntry.fields` attribute from
  `src/tracking/models.py`; Django already provides model field metadata,
  while `WeightEntryForm.Meta.fields` remains the form field definition.

## Known Limitations or Blockers

- Manual browser checks were not rerun during this documentation update.
- The PostgreSQL server version was not captured.
- The application is still the pre-API Django-template implementation;
  API implementation and client migration remain out of scope.

## Verification Scope

These results cover the commands and manual checks listed above.
They do not establish that every application behavior has been tested.
