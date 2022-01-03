#!/bin/bash
VERSION=$(python -c "import toml; print(toml.load('review/pyproject.toml')['tool']['poetry']['version'])")
docker build \
  -t "smmoosavi/performance-review-api:latest" \
  -t "smmoosavi/performance-review-api:$VERSION" \
  -f review/api.Dockerfile \
  review

docker build \
  -t "smmoosavi/performance-review-statics:latest" \
  -t "smmoosavi/performance-review-statics:$VERSION" \
  -f review/statics.Dockerfile \
  review
