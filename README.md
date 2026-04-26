# ACEest Fitness & Gym – DevOps CI/CD Pipeline

A Flask-based web application developed for **ACEest Fitness & Gym** as part of a DevOps assignment.  
This project demonstrates the implementation of a complete DevOps CI/CD pipeline for a Flask-based fitness application. The pipeline automates code integration, testing, quality analysis, containerization, and deployment using industry-standard tools.

---

## 1. Project Overview

The goal of this assignment was to implement a complete DevOps lifecycle around a gym management application. The required flow included:

- building a Flask application
- managing source code through Git and GitHub
- adding automated testing using Pytest
- containerizing the application with Docker
- configuring Jenkins as a build validation environment
- configuring GitHub Actions to run CI on every push and pull request

These expectations are aligned with the assignment brief, which asks for a Flask application, version control maturity, test coverage, Docker support, Jenkins-based build validation, and a GitHub Actions workflow for automated build and test stages.

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
## 7. Local Setup Instructions

1. Clone the repository:
   git clone https://github.com/NandhiyaN/aceest-fitness-gym-devops.git

2. Navigate to the project folder:
   cd aceest-fitness-gym-devops

3. Install dependencies:
   pip install -r requirements.txt

4. Run the application:
   python app.py

5. Open the application in browser:
   http://localhost:5000

---
## 8. Running Tests

Run automated tests using Pytest:

python -m pytest

This validates core application functionality such as login, client management, program generation, and workout operations.

---
## 9. Docker Setup

Build Docker image:
docker build -t aceest-app .

Run Docker container:
docker run -p 5000:5000 aceest-app

---
## 10. Jenkins Build Process

Jenkins is configured as a clean build environment to validate the application.

It performs the following steps:
- Pulls the latest code from the GitHub repository
- Installs project dependencies
- Executes automated tests using Pytest
- Validates the application build process

Jenkins ensures that the application is built and tested in an isolated environment, independent of local configurations.

---
## 11. GitHub Actions CI Pipeline

GitHub Actions is configured to automatically trigger on every push and pull request.

The pipeline performs the following stages:
- Source code checkout
- Dependency installation
- Automated testing using Pytest
- Docker image build validation

This ensures continuous integration and early detection of issues.

---
## 12. VM-Based Execution

The complete DevOps pipeline was executed and validated in a Virtual Machine (VM) environment.

This ensures:
- Environment consistency across deployments
- Reproducible builds
- Simulation of a real-world deployment setup

Final validation of the application was performed in the VM using Jenkins and Docker.

---
## 13. Project Structure

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
├── sonar-project.properties
├── k8s/
│   ├── rolling-update/
│   ├── blue-green/
│   ├── canary/
│   ├── shadow/
│   ├── ab-testing/
|   ├── base/
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        └── main.yml

```
---
## 14. Tech Stack

| Category           | Tools Used            |
| ------------------ | --------------------- |
| Version Control    | Git, GitHub           |
| CI/CD              | Jenkins               |
| Testing            | Pytest                |
| Code Quality       | SonarQube             |
| Containerization   | Docker                |
| Container Registry | Docker Hub            |
| Orchestration      | Kubernetes (Minikube) |

---
## 15. CI/CD Pipeline Flow
1. Code Commit
      - Developers push code to GitHub (feature → develop branch)
2. Jenkins Pipeline Trigger
      - Jenkins automatically triggers build
3. Build & Test
      - Python environment setup
      - Dependencies installed
      - Pytest executed
4. Code Quality Analysis
      - SonarQube analysis performed
      - Quality gate validated
5. Docker Build
      - Docker image created
6. Docker Push
      - Image pushed to Docker Hub with version tags
7. Deployment
      - Deployed to Kubernetes (Minikube)

---
## 16. Docker
   - Docker image built using Dockerfile
   - Images pushed to Docker Hub

Example: docker pull nandhiyan/aceest-fitness-gym:<version>

---
## 17. Kubernetes (Minikube)
Application deployed locally using Minikube with YAML configurations.

Commands used:
kubectl apply -f k8s/
kubectl get pods
kubectl get services
minikube service <service-name>

---
## 18. Deployment Strategies Implemented
1. Rolling Update
Gradual replacement of old version with new version
2. Blue-Green Deployment
Two environments (Blue & Green)
Traffic switched between versions
3. Canary Deployment
New version released to small subset of users
4. Shadow Deployment
New version tested silently without impacting users
5. A/B Testing
Different versions served to different user groups

---
## 19. Rollback Mechanism
   - Kubernetes supports rollback using:
   - kubectl rollout undo deployment/<deployment-name>

Ensures system stability in case of failure.

---
## 20. Testing
   - Unit tests implemented using Pytest
   - Automated execution in Jenkins pipeline

Command: python -m pytest -v

---
## 21. Code Quality
   - Integrated SonarQube for static analysis
   - Ensures:
      - Code quality
      - Maintainability
      - Bug detection

---
## 22. Key Outcomes

 - Implemented end-to-end CI/CD pipeline
 - Automated testing and quality checks
 - Containerized application using Docker
 - Deployed using Kubernetes
 - Implemented advanced deployment strategies
 - Ensured zero-downtime deployment and rollback

 ---
 ## 23. Conclusion
 This project demonstrates a complete CI/CD pipeline for the ACEest Fitness & Gym application, integrating Jenkins, Docker, SonarQube, Pytest, and Kubernetes. The pipeline automates code integration, testing, quality checks, containerization, and deployment.

 Advanced deployment strategies like Rolling, Blue-Green, and Canary ensure zero-downtime releases and reliable rollback. Overall, the implementation highlights how DevOps practices improve automation, code quality, and deployment efficiency in real-world applications.
