curl -X POST https://gdpai8c3re.us-east-1.awsapprunner.com/dbt \
  -H 'Content-Type: application/json' \
  -d '{"cmd":"dbt debug --project-dir example --profiles-dir example"}'
