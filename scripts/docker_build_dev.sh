#!/bin/bash

docker build \
  -t "smmoosavi/performance-review-api:dev" \
  -t "smmoosavi/performance-review-api:dev-$TRAVIS_COMMIT" \
  -t "smmoosavi/performance-review-api:dev-$TRAVIS_BUILD_NUMBER" \
  -f review/api.Dockerfile \
  review

docker build \
  -t "smmoosavi/performance-review-statics:dev" \
  -t "smmoosavi/performance-review-statics:dev-$TRAVIS_COMMIT" \
  -t "smmoosavi/performance-review-statics:dev-$TRAVIS_BUILD_NUMBER" \
  -f review/statics.Dockerfile \
  review
