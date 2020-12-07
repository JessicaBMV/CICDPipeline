#! /usr/bin/env bash

az webapp up --name jess-pipeline --sku FREE  -l westeurope

# application configuration

az webapp config set -g jess.menesses11_rg_Linux_westeurope -n jess-pipeline --startup-file 'gunicorn -w 4 -b 0.0.0.0:8000 "ml_app:create_app()"'

# tailling log files
az webapp log tail