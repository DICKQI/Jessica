#!/bin/bash
uwsgi --socket :8001 --buffer-size 32768 --module Jessica.wsgi &