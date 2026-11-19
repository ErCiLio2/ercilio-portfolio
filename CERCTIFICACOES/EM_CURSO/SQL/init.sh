#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if [ -f .env ]; then
    echo ".env já existe, nada a fazer."
    exit 0
fi

if ! command -v python3 >/dev/null 2>&1; then
    echo "python3 é necessário para gerar a password." >&2
    exit 1
fi

PASSWORD="Str0ng!$(python3 -c "import secrets,string;a=string.ascii_letters+string.digits;print(''.join(secrets.choice(a) for _ in range(14)))")"
PORT="${MSSQL_PORT:-1433}"

sed -e "s|^MSSQL_SA_PASSWORD=.*|MSSQL_SA_PASSWORD=${PASSWORD}|" \
    -e "s|^MSSQL_PORT=.*|MSSQL_PORT=${PORT}|" \
    .env.example > .env

chmod 600 .env
echo ".env criado com password gerada (guarda-a em segurança)."
