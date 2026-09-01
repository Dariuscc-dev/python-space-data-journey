# Roadmap

Detailed phase-by-phase plan. Timelines are approximate and adapt to real pace, not the other way around. Each phase is only considered complete when its final mission works end to end and its README has been updated with lessons learned.

## Phase 0 — Environment and Git (weeks 1-2)

Goal: prepare the lab before learning "programming".

- Install Python, terminal basics, editor setup
- Create and activate virtual environments
- Use pip to install packages
- Understand .gitignore
- Read and interpret tracebacks
- Make small, descriptive commits

Mission: python-launchpad — a countdown/terminal tool for a mission date.

## Phase 1 — Python Foundations (months 1-3)

Source material: 30 Days of Python, days 1-14 (used as a topic checklist, not copied).

- Variables, types, operators, strings
- Conditionals and loops
- Lists, tuples, sets, dictionaries
- Functions and scope
- Modules
- Comprehensions (only after mastering plain loops)

Mission: Space Calculator — terminal tool for astronomical conversions and planet comparisons.

## Phase 2 — Core Python and Files (months 3-5)

Source material: 30 Days of Python, days 15-20.

- pathlib, csv, json
- datetime
- Errors and exceptions
- Data validation
- Debugging with print, variable inspection, tracebacks

Mission: Meteor Observation Log — clean a deliberately messy CSV of meteor sightings.

## Phase 3 — Data Analysis with Python (months 5-8)

- Descriptive statistics
- NumPy
- Pandas: filtering, groupby, merge, pivot
- Data cleaning: nulls, duplicates, types
- Visualisation: Matplotlib, Seaborn, Plotly

Mission: Earth & Space Data Explorer — EDA notebook on a fascinating public dataset (meteorites, exoplanets, launches, earthquakes...).

SQL starts in parallel here: SELECT, WHERE, GROUP BY, basic JOIN.

## Phase 4 — SQL for Data (months 6-9, overlapping Phase 3)

- Relational modelling
- SELECT, filtering, ordering
- GROUP BY and aggregations
- JOINs
- Subqueries and CTEs
- Window functions
- SQLite and PostgreSQL

Mission: Flight Data Warehouse — relational model of airports, airlines, flights, delays; answer real analytical questions.

## Phase 5 — APIs and Data Collection (months 9-12)

- HTTP, status codes, JSON
- requests library
- Public APIs, pagination, rate limits
- Environment variables for keys
- Responsible web scraping (BeautifulSoup) when no API exists

Mission: Space Data Pipeline — extract, validate, transform and store data from a public API on a repeatable schedule.

## Phase 6 — Software Engineering (months 12-15)

- Project structure and packaging
- OOP where it adds value
- pytest
- logging, config files, environment variables
- Type hints
- Refactoring old code

Mission: Telemetry Anomaly Detector — detect anomalies in simulated sensor data, with tests.

## Phase 7 — Backend and Deployment (months 15-18)

- FastAPI and REST design
- SQLAlchemy with PostgreSQL
- Docker
- GitHub Actions (CI)
- Deployment basics

Mission: Mission Control API — API exposing missions, events, telemetry and flight data.

## Phase 8 — Applied ML and Cloud (from month 18)

- Scikit-learn: regression, classification, clustering
- Time series basics
- Azure data services and Python SDK

Mission: Aerospace Operations Intelligence — end-to-end system: ingestion, SQL storage, analysis, API/dashboard, cloud execution.

## Working rhythm: 70-20-10

- 70% building: code, selected exercises, refactoring, projects
- 20% theory: official docs, course material
- 10% free exploration: a curious API, an odd dataset, a new concept

## Definition of done per phase

- [ ] Concepts can be explained in my own words
- [ ] Selected exercises completed without looking at solutions
- [ ] Final mission works end to end
- [ ] Errors and lessons documented
- [ ] Phase README updated with status and "what I learned"
