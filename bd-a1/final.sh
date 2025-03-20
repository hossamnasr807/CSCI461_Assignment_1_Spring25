#!/bin/bash

# Ensure the service-result directory exists
mkdir -p bd-a1/service-result

# Copy all output files from the container to the host
docker cp bd-a1-container:/home/doc-bd-a1/. bd-a1/service-result/

echo "Results copied to 'bd-a1/service-result' directory."

# Stop the container
docker stop bd-a1-container
echo "Container stopped"
