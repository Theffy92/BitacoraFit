# BitacoraFit

**A personal logbook for understanding weight changes in context.**

BitacoraFit brings weight tracking, menstrual-cycle records, food intake, movement, and personal reflections into one place. Its central purpose is to help users explore their progress over time with more context than a number on a scale can provide.

The project is in active development and is transitioning from a Django-template web application to a cross-platform application built with React Native, Expo, and TypeScript, supported by a Django API and PostgreSQL.

## Why BitacoraFit?

BitacoraFit began as a personal project motivated by the need to bring useful tracking features together in one application, with core functionality available for free.

Weight records alone do not capture a person's experience. Cycle dates, changes in routines, food intake, movement, and personal observations can provide additional context when reviewing progress.

The idea behind the name *bitácora*—a logbook—is central to the product: a place to record, reflect, and explore patterns without treating every daily fluctuation as a success or failure.

## Intended Audience

BitacoraFit is primarily designed for people who menstruate and want to explore weight fluctuations alongside their menstrual-cycle records.

The planned experience will allow users to leave cycle information unknown or incomplete. Recorded information and app-generated estimates will be clearly distinguished.

## Product Principles

- **Context alongside numbers:** Bring tracking records and personal observations together.
- **Long-term perspective:** Make it easier to review progress beyond individual weigh-ins.
- **Optional reflection:** Allow users to add context without requiring extensive journaling.
- **Free core functionality:** Keep tracking, history, visualizations, reflections, and basic summaries free.
- **Transparent uncertainty:** Distinguish recorded facts, estimates, and possible explanations.
- **Privacy and user control:** Treat personal records as sensitive and design access controls accordingly.
- **Accessible across devices:** Support phones, tablets, and desktop browsers with appropriate layouts.

## Planned Core Features — Free

### Accounts and Personal Context

- Sign up, log in, and log out.
- Access user-specific records and dashboards.
- Optionally describe personal weight history, goals, and tracking preferences.
- Update personal information and preferences.

### Weight Tracking

- Create, edit, and delete weight entries.
- Record dates and optional notes.
- Review weight history and trends.
- Explore changes across selected time periods.

### Menstrual-Cycle Tracking and Context

- Record period dates.
- View cycle records alongside weight history.
- Compare weight patterns across recorded cycles.
- Distinguish user-recorded information from any estimated cycle information.
- Support missing or uncertain records without forcing a phase assignment.

Exploring weight and cycle records together is a central part of BitacoraFit's planned experience.

### Food and Calorie Tracking

- Log food and calorie intake.
- Create reusable foods and meals.
- Review intake history alongside other tracking records.

### Movement Tracking

- Record exercise and other movement.
- Review activity records alongside weight, cycle information, and reflections.

### Reflections

- Add optional notes about experiences such as travel, stress, sleep, or routine changes.
- Review reflections alongside tracking history.
- Record progress and observations beyond weight.

### Visualizations and Basic Summaries

- View weight charts and historical comparisons.
- Explore weight and cycle records together.
- Review summaries calculated from recorded data without requiring AI.

These features describe the planned product. They are not all implemented, and they will be developed incrementally.

## Planned AI Guide — Optional Paid Subscription

An optional AI guide will help users explore their records conversationally and access general educational context.

Planned capabilities include:

- Summarizing selected periods of tracking history.
- Highlighting observations across recorded weight, cycle, food, movement, and reflection data.
- Helping users compare their records across time.
- Offering reflection prompts.
- Explaining possible reasons for fluctuations while communicating uncertainty.

The AI guide will distinguish observations in a user's records from general educational explanations. It will not present associations as proof of causation or estimated cycle phases as confirmed facts.

Core tracking and reflection features will remain available without an AI subscription. Subscription pricing and usage allowances have not yet been defined.

## Health Information Boundaries

BitacoraFit is intended for personal tracking, reflection, and general education. It is not intended to diagnose conditions, prescribe treatment, or provide personalized medical or nutritional advice.

The application will not claim to determine the medical cause of a weight change from tracking records.

AI-generated explanations may be incomplete or incorrect. The planned experience will communicate those limitations and avoid presenting generated output as a clinical assessment.

## Platforms and Design Approach

The planned application will support:

- iOS phones and iPads.
- Android phones and tablets.
- Web browsers on mobile and desktop devices.

Development will follow a mobile-first design approach, with layouts adapted for larger screens.

The goal is to share application logic and suitable interface components across platforms while allowing platform-specific behavior and layouts where needed.

## Technical Architecture

### Current Implementation

The repository currently contains a Django-template application with:

- A `WeightEntry` model associated with a user.
- Weight-entry creation with optional notes.
- A login-protected dashboard.
- A login-protected weight-history page.
- Queries scoped to the authenticated user.
- Django authentication routes.
- Tailwind CSS and DaisyUI styling.
- Tests covering tracking models, forms, and views.

### Planned Architecture

| Layer | Technology | Responsibility |
|---|---|---|
| Client | React Native, Expo, TypeScript | Screens, navigation, forms, and client-side interactions across mobile and web |
| Backend | Django | Business logic, validation, accounts, and data access |
| API | Django REST Framework | Authenticated communication between the client and backend |
| Database | PostgreSQL | Persistent storage of user records |
| AI integration | Backend-managed service integration; provider undecided | AI requests, subscription checks, and usage controls |

The client will communicate with Django through an API. Django will enforce permissions, validate requests, and access PostgreSQL.

Database credentials and AI service credentials will remain on the backend.

Authentication details, deployment infrastructure, charting libraries, and subscription infrastructure will be selected as their requirements are defined.

## Transition Plan

The existing Django implementation will be evolved incrementally.

1. Document the product direction and planned architecture.
2. Verify the existing backend behavior and tests.
3. Introduce authenticated API endpoints for weight records.
4. Create the Expo application.
5. Connect the client to the API.
6. Validate the first complete tracking flow on mobile and web.
7. Expand the product around weight and menstrual-cycle context.
8. Add food, movement, and reflection capabilities incrementally.
9. Introduce the optional AI guide after the core experience is established.

Existing templates will remain available during the initial transition. Changes to the interface do not require discarding the existing data models or database.

### First Technical Milestone

An authenticated user can:

- View their own weight history.
- Create a weight entry.
- See the saved entry in their history.
- Complete this flow on a phone and in a desktop browser.

The backend must prevent access to another user's records.

## Development Goals

BitacoraFit is both a meaningful personal product and an opportunity to practice:

- Product discovery and scope management.
- Cross-platform interface development.
- API design and integration.
- Relational data modeling.
- Authentication and authorization.
- Testing important application behavior.
- Privacy-conscious handling of sensitive records.
- Deployment and maintainability.
- Responsible integration of AI features.

Technology choices will be driven by product requirements and maintainability.

## Project Status

**Active development — transitioning the architecture.**

The current repository contains the initial Django web implementation. The React Native client, API transition, menstrual-cycle features, food tracking, movement tracking, and AI guide are planned work unless explicitly identified as implemented above.
