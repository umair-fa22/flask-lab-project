# Flask Lab Project

## Overview
This project is a collaborative Flask web application built using GitHub, Docker, and a CI/CD pipeline (GitHub Actions). The objective is to containerize and continuously deploy the application.

## Team Setup
- **Total Members:** 2
- **Roles:**
  - **Member 1 [UMAIR ALI FA22-BSE-137] (Backend Lead & DevOps Engineer):** Implements core Flask routes and logic, handles Docker configuration, testing, and CI/CD pipeline setup.
  - **Member 2 [AZAN WAHLA FA22-BSE-105] (Frontend/API Integration):** Works on templates, static files, and API endpoints.

## Project Structure
```
flask_lab_project/
├── main/                      # Main directory
│   ├── app.py                 # Main Flask app
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── tests/                 # Unit tests
│   │   └── test_app.py
│   ├── templates/
│   ├── static/
│   └── .github/
│       └── workflows/
│           └── ci-cd.yml      # GitHub Actions pipeline
├── member1_backend-devops/    # Subdirectory for backend and DevOps work
├── member2_frontend/          # Subdirectory for frontend/API work
```

## How to Build, Test, and Run the Project

### Prerequisites
- Docker installed on your machine
- Python 3.9+
- Git

### Build
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd flask_lab_project
   ```
2. Build the Docker image:
   ```bash
   docker build -t flask-app main/
   ```

### Test
1. Run unit tests locally:
   ```bash
   cd main
   python -m unittest tests/test_app.py
   ```
   - Ensure `test_home()` and `test_health()` pass.

### Run
1. Start the Docker container:
   ```bash
   docker run -p 5000:5000 flask-app
   ```
2. Access the app in your browser at `http://localhost:5000`.

## Additional Notes
- The CI/CD pipeline automates testing and building on pushes to the `main` branch.
- Use Pull Requests to merge changes from `backend-devops` and `frontend` branches.