#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if [ -f .env ]; then
    set -a
    . ./.env
    set +a
fi

exec docker exec -i sqlserver /opt/mssql-tools18/bin/sqlcmd \
    -S localhost -U "${MSSQL_USER:-sa}" -P "${MSSQL_SA_PASSWORD}" -C "$@"
