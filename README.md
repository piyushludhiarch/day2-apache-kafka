# Kafka Bank Transactions Streaming Demo

A simple event-streaming project using Apache Kafka to generate and monitor simulated bank transactions in real time.

## Overview

This project demonstrates a basic Kafka producer-consumer architecture:

- The producer creates a fake bank transaction every two seconds.
- Each transaction is serialized as JSON and published to the `bank-transactions` topic.
- The consumer subscribes to that topic and prints transactions as they arrive.

Transaction events include a transaction ID, account ID, amount, currency, merchant, location, and status.

## Project Structure

```text
.
├── consumer/
│   └── consumer.py
├── producer/
│   └── producer.py
├── docker-compose.yml
├── requirements.txt
└── README.md
```

The local `venv/` directory is intentionally excluded from Git through `.gitignore`.

## Prerequisites

- Python 3.9 or newer
- Docker Desktop with Docker Compose

## Setup

1. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install the Python dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Start Kafka and ZooKeeper:

   ```powershell
   docker compose up -d
   ```

   The services expose Kafka on `localhost:9092` and ZooKeeper on `localhost:2181`.

## Run the Demo

Open two terminals in the project directory, activate the virtual environment in both, and run:

**Terminal 1: consumer**

```powershell
python consumer\consumer.py
```

**Terminal 2: producer**

```powershell
python producer\producer.py
```

The producer prints each generated event. The consumer receives and prints the same events from Kafka.

## Stop Kafka

When finished, stop and remove the containers with:

```powershell
docker compose down
```

## Notes

- Kafka is configured for local development and uses a single broker.
- The producer and consumer both connect to `localhost:9092`.
- Transaction data is generated in memory and is not persisted by the Python scripts.
