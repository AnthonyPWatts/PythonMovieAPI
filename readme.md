# Project Name

## Overview
This project provides a CRUD interface for three database tables using the example database from [SQLDockerDeployKit](https://github.com/AnthonyPWatts/SQLDockerDeployKit). The setup includes a development container, Docker integration, and necessary dependencies defined in `requirements.txt`.

## Features
- Full CRUD operations for three database tables
- Preconfigured `.devcontainer` for VS Code integration
- Docker support with a `Dockerfile`
- Dependency management with `requirements.txt`

## Setup

### Prerequisites
- Docker installed
- Python installed (if running outside Docker)
- VS Code (optional, for `.devcontainer` support)

### Installation
1. Clone this repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Build and run the Docker container:
   ```sh
   docker build -t my-app .
   docker run -d --name my-app-container my-app
   ```

3. If using VS Code, open the project in a dev container:
   - Open the project in VS Code
   - Reopen in container when prompted

4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the Application
Depending on your setup, run the application using:
```sh
python main.py
```
or within Docker:
```sh
docker exec -it my-app-container python main.py
```

### API Endpoints
(TODO: Document available API endpoints)

## Database Information
This project uses the example database from SQLDockerDeployKit, a tool designed for rapid setup of SQL Server databases in Docker containers. More details can be found [here](https://github.com/AnthonyPWatts/SQLDockerDeployKit).

## Contributing
Feel free to open issues or submit pull requests.

## License
(TODO: Add proper license details one day)
Open to all.

