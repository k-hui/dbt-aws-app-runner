export $(grep -v '^#' .env | xargs)
dbt debug --project-dir example --profiles-dir example
