# First Weight-History Experience

## Goal

An existing user can access their account and review their own
previous weight entries and notes.

## Included

- Login and logout.
- Viewing the signed-in user's weight history.
- Entry dates, weights, units, and optional notes.
- Newest-first ordering.
- Empty-history, loading, and failure states.

## Excluded

- Signup and password recovery.
- Creating, editing, or deleting entries in the new client.
- Charts and cycle comparisons.
- Food and movement tracking.
- AI guidance.

The existing Django application remains the reference for current
behavior. These requirements describe the first experience in the
replacement client.

## WH-01 — Review weight history

Related epic: E02

As a user, I want to review my previous weight entries and notes
so I can reflect on changes over time.

### Acceptance criteria

- A signed-in user can view only their own weight entries.
- Each entry displays its recorded date, weight, and unit.
- Entries appear by recorded date, newest first.
- Entries with the same recorded date appear by creation time,
  newest first.
- An entry's notes are available when provided.
- An entry without notes displays without an error or a literal
  "None" or "null" value.
- A user without entries sees a clear empty-history message.
- Loading and failed requests have distinguishable states.
- A failed request provides a way to retry.
- Existing entries remain readable without requiring re-entry.

### Related technical issues

- [Weight-history API issue](https://github.com/Theffy92/BitacoraFit/issues/58)
- [React Native client issue](https://github.com/Theffy92/BitacoraFit/issues/59)

| Story | User need | Testable cceptance criteria |
| --- | --- | --- |
| AA-01-Access my account | "As a returning user, I want to sign in so I can access my personal tracking history." | Valid credentials open the authenticated experience. Invalid credentials show a clear error. Unauthenticated users are asked to sign in before accessing history. |
| AA-02-End my session | "As a signed-in user, I want to log out so I can end access to my personal records on this device." | Logout ends the relevant session or credential's validity as designed. The client clears displayed personal records. Protected history requires authentication again. |

## Open Product Questions
- Will the first experience display pounds only, or support a user-selected unit?
- Should long notes expand within the list or open an entry-detail view?
- What wording should appear when history is empty?
- Should the new history screen load all entries at once, or load a limited number with a “Load more” option for older entries?
> The current Django application provides access to older entries through the weight-history page. The replacement client must preserve that access.
