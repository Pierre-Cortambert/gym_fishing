#!/bin/bash
python3 -m pytest --cov-config .coveragerc --cov-report html --cov-report term --cov=. -v tests/*.py
