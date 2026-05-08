# Uptime Monitoring Tool

A production-style uptime monitoring system built with Django, Celery, and Redis that periodically checks website availability, measures response latency, and tracks service health asynchronously.

----------

## Features

-   Website uptime monitoring
-   HTTP status validation
-   Response latency tracking
-   Asynchronous background task processing
-   Periodic monitoring using Celery Beat
-   Redis-backed task queue
-   Scalable task architecture



# Architecture

```
Celery Beat
    ↓
Redis Broker
     ↓
Celery Worker
     ↓
Django Application

```

### Workflow

1.  Celery Beat schedules monitoring tasks
2.  Tasks are pushed into Redis queue
3.  Celery Worker consumes tasks
4.  Worker sends HTTP requests to monitored URLs
5.  Status and latency are stored in the database


# Installation

## 1. Clone Repository

```
git clone https://github.com/manjinder-27/umt.git
cd umt
```

----------

## 2. Create Virtual Environment

```
python -m venv venv
```

### Linux / Mac

```
source venv/bin/activate
```

### Windows

```
venv\Scripts\activate
```


## 3. Install Dependencies

```
pip install -r requirements.txt
```



# Redis Setup

## Ubuntu

```
sudo apt install redis-server
```

Start Redis:

```
redis-server
```

Verify:

```
redis-cli ping
```

Expected output:

```
PONG
```

# Running the Project

You need **3 terminals**.


## Terminal 1 — Django Server

```
python3 manage.py runserver
```

## Terminal 2 — Celery Worker,Redis

```
sudo systemctl start redis-server

celery -A umt_server worker -l info
```



## Terminal 3 — Celery Beat

```
celery -A umt_server beat -l info
```


# Example Task Flow

## `tasks.py`

```
@shared_taskdef check_url_status(monitor_id):    ...
```

The worker:

-   Sends HTTP request
-   Measures latency
-   Compares status code
-   Updates database asynchronously

----------

# Future Improvements
-   Email alerts
-   SMS/Discord/Slack notifications
-   Historical uptime analytics
-   Charts and dashboards
-   Docker support
-   Kubernetes deployment
-   Retry strategies
-   Multi-region monitoring
-   WebSocket live updates


