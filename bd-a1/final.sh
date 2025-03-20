#!/bin/bash

# Ensure the service-result directory exists
mkdir -p bd-a1/service-result

# Copy results from container to host
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-1.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-2.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-3.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/vis.png bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/kmeans_model.pkl bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/k.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/loaded_data.csv bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/res_dpre.csv bd-a1/service-result/

echo "Results copied to 'bd-a1/service-result' directory."

# Stop the container
docker stop bd-a1-container
echo "Container stopped"
