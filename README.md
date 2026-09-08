# Kafka Bank Transactions Streaming Demo

A simple event-streaming project using Apache Kafka to simulate and monitor bank transactions in real time.

## Overview

This project demonstrates a basic Kafka producer-consumer architecture:

- **Producer** generates fake bank transaction events (transaction ID, account ID, amount, currency, merchant, location, status) and publishes them to a Kafka topic every 2 seconds.
- **Consumer** subscribes to the topic and prints each transaction as it arrives, simulating a bank monitoring system.

## Architecture
