#!/bin/bash
bash scripts/docker_build.sh
echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
docker push kgolezardi/performance-review-api
docker push kgolezardi/performance-review-statics
