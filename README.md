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

### Initialize dbt project

```bash
pip install dbt-postgres
# initialize dbt project
dbt init example
# clone the profiles.yml to local project
cp ~/.dbt/profiles.yml ./example
# debug
dbt debug --project-dir example --profiles-dir example
# test dbt run
dbt run --project-dir example --profiles-dir example
```

### Development

```bash
# for local
uvicorn app.main:app --reload
# for production
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Test

```bash
curl -X POST http://127.0.0.1:8000/dbt \
  -H 'Content-Type: application/json' \
  -d '{"cmd":"dbt debug --project-dir example --profiles-dir example"}'
  
curl -X POST http://127.0.0.1:8000/dbt \
  -H 'Content-Type: application/json' \
  -d '{"cmd":"dbt run --project-dir example --profiles-dir example"}'
```

### Test remote database

```bash
# first call this
export $(grep -v '^#' .env | xargs)
# then
dbt debug --project-dir example --profiles-dir example
# combine
sh debug-remote.sh
```

## Deployment

### Build command:

```bash
sudo yum install git -y; pip install -r requirements.txt;
```

### Start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Update apprunner.yaml (if Use a configuration file)

- Update your database configurations
