#!/bin/bash

# It is responsability of the deployment orchestration to execute before
# migrations, create default admin user, populate minimal data, etc.

gunicorn dukaan_service.wsgi --config dukaan_service/gunicorn_conf.py

