#!/bin/bash
bash scripts/docker_build_dev.sh
echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
docker push smmoosavi/performance-review-api
docker push smmoosavi/performance-review-statics
