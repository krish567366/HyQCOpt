#!/bin/bash
API_URL=$(terraform output -raw api_endpoint)

# Test job submission
JOB_ID=$(curl -s -X POST $API_URL/jobs \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"problem_type":"tsp","nodes":4}' | jq -r .job_id)

# Test result retrieval
curl -s $API_URL/results/$JOB_ID | jq