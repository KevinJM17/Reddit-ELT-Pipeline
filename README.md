# Reddit-ELT-Pipeline
A data pipeline designed to extract

## Architecture
![alt img](images/architecture.png)

- __Apache Airflow__:

## Setup
1. Clone the repository.
   ```bash
   git clone
   ```
3. Create a new virtual environment and activate it.
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
4. Create the configuration file `config.conf`.
5. Build the docker container.
   ```bash
    docker compose up -d --build
   ```
6. Launch Airflow Web UI.
   ```bash
   http://localhost:8080
   ```
