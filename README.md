# dbt-aws-app-runner

dbt AWS App Runner

## Reference

- https://docs.aws.amazon.com/apprunner/latest/dg/getting-started.html

## Getting Started

### Setup

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Libraries

```bash
pip install fastapi
pip install "uvicorn[standard]"
pip install httpx
pip install pytest
```

### Development

```bash
# for development
uvicorn main:app --reload
# for production
gunicorn -k uvicorn.workers.UvicornWorker
```

### Test

```bash
curl -X POST http://127.0.0.1:8000/dbt \
  -H 'Content-Type: application/json' \
  -d '{"command":"dbt debug"}'
```

## Deployment

- apprunner.yaml
