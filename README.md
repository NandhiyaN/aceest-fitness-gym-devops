# ACEest Fitness & Gym Management

A Flask-based web application developed for **ACEest Fitness & Gym** as part of a DevOps assignment.  
This project modernizes the latest provided Python-based ACEest version into a web-based system and demonstrates a practical DevOps workflow using **GitHub, Pytest, Docker, Jenkins, and GitHub Actions**.

---

## 1. Project Overview

The goal of this assignment was to implement a complete DevOps lifecycle around a gym management application. The required flow included:

- building a Flask application
- managing source code through Git and GitHub
- adding automated testing using Pytest
- containerizing the application with Docker
- configuring Jenkins as a build validation environment
- configuring GitHub Actions to run CI on every push and pull request

These expectations are aligned with the assignment brief, which asks for a Flask application, version control maturity, test coverage, Docker support, Jenkins-based build validation, and a GitHub Actions workflow for automated build and test stages :contentReference[oaicite:0]{index=0}

---

## 2. Problem Statement

ACEest Fitness & Gym is treated as a growing startup that needs a more reliable and automated delivery workflow. The objective of this implementation was to move from a Python-based standalone application approach to a web-based solution that supports:

- consistent setup across environments
- build validation in Jenkins
- automated checks on every code change
- easier packaging and deployment using Docker

---

## 3. Solution Approach

The latest provided Python version was used as the reference for core functionality. The application was then redesigned as a Flask-based web application.

The final solution includes:

- **Flask web application** for user interaction
- **SQLite database** for lightweight data persistence
- **HTML templates with Jinja2** for UI rendering
- **Pytest** for validating core backend flows
- **Docker** for containerizing the application
- **Jenkins** for manual clean-build validation
- **GitHub Actions** for automated CI checks

---

## 4. Key Features Implemented

The application currently supports the following features:

- Admin login
- Dashboard summary
- Add and view clients
- Membership status tracking
- Program generation for clients
- Add and view workouts
- Health endpoint for basic validation
- Automated tests for major flows

---

## 5. Backend Design

The backend was implemented as a **single Flask application**.

### Backend responsibilities
- handle user requests through Flask routes
- manage authentication using session-based login
- interact with the SQLite database
- perform business logic for client and workout operations
- render UI pages with server-side templates
- provide a simple health check endpoint

### Database handling
SQLite was used as the persistence layer because it is lightweight, file-based, and easy to set up for assignment purposes.  
The following logical entities were handled:

- `users`
- `clients`
- `workouts`

### Business logic handled in backend
The backend includes logic for:
- validating login credentials
- counting dashboard summary values
- inserting client records
- generating a program for a client
- viewing membership details
- inserting workout records
- fetching client and workout data for UI pages

### Why one backend only
This project was implemented as a **single Flask application**, so both UI rendering and backend logic are packaged together.  
There is no separate frontend app and backend API as independent services in the current design.

---

## 6. Frontend / UI Approach

The UI was implemented using:

- Flask templates
- Jinja2 rendering
- HTML
- simple CSS styling

The templates are kept under the `templates/` folder, and the application renders pages such as:

- Login
- Dashboard
- Clients
- Add Client
- Membership Details
- Workouts
- Add Workout

This keeps the project simple, maintainable, and suitable for the current assignment scope.

---

## 7. Project Structure

```text
aceest-fitness-gym-devops/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── README.md
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── clients.html
│   ├── add_client.html
│   ├── membership.html
│   ├── workouts.html
│   └── add_workout.html
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        └── main.yml