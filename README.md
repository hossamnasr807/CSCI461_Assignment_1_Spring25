# CSCI461 Assignment 1 - Spring 2025

This project demonstrates a data pipeline implemented using Docker. The pipeline performs preprocessing, exploratory data analysis (EDA), visualization, and K-Means clustering on the Iris dataset.

## Project Overview

The pipeline consists of the following scripts:

1. `Dockerfile` - Defines the container environment, including dependencies and script execution settings.
2. `load.py` - Loads the Iris dataset.
3. `dpre.py` - Preprocesses the data.
4. `eda.py` - Performs exploratory data analysis.
5. `vis.py` - Generates visualizations.
6. `model.py` - Trains a K-Means clustering model.
7. `final.sh` - Copies the output files from the container to the local machine and stops the container.

All scripts are executed inside a Docker container, and the final results are extracted to the host system.

---
### Image link on Dockerhub
[bd-a1-img](https://hub.docker.com/r/hossamnasr807/bd-a1-img)

## How to Run the Project  

### Clone the Repository  
```bash
git clone https://github.com/hossamnasr807/CSCI461_Assignment_1_Spring25.git
cd CSCI461_Assignment_1_Spring25/bd-a1 
```
### Build and Run the Docker Container
```bash
# Build the Docker image
docker build -t bd-a1-image .

# Run the container
docker run -it --name bd-a1-container bd-a1-img
```
### Copy Scripts into the Container
Copy Scripts from your local machine into the Container<br>
Run the following commands in another terminal after running the container
```bash
docker cp load.py bd-a1-container:/home/doc-bd-a1/
docker cp dpre.py bd-a1-container:/home/doc-bd-a1/
docker cp eda.py bd-a1-container:/home/doc-bd-a1/
docker cp vis.py bd-a1-container:/home/doc-bd-a1/
docker cp model.py bd-a1-container:/home/doc-bd-a1/
```

### Start the Pipeline Execution
Start the pipeline by running the load.py script inside the container:
```bash
python3 load.py /home/doc-bd-a1/Iris.csv
```
This will automatically trigger the execution of the subsequent scripts (dpre.py → eda.py → vis.py → model.py), as each script calls the next one in sequence.

### Extract Results from the Container
Once the pipeline finishes, use the provided final.sh script to copy the output files to your local machine and stop the container:
<br>Run git bash inside the container directory "CSCI461_Assignment_1_Spring25/bd-a1"
<br>Inside git bash run the following commands:

```bash
chmod +x final.sh # to give execute permissions
bash final.sh
```
This script:
- Copies the output files from the container to the bd-a1/service-result/ directory.
- Stops the container.

### Restarting the Container
To rerun the container:
<br>In your local machine run the following command

```bash
docker start -ai bd-a1-container
```
or restart the container from Docker Desktop GUI
### Final Outputs

After running the pipeline, the following files will be available in bd-a1/service-result/:

- eda-in-1.txt (EDA Insight 1)

- eda-in-2.txt (EDA Insight 2)

- eda-in-3.txt (EDA Insight 3)

- vis.png (Visualization output)

- trained_model.pkl (Saved K-Means model)

- loaded_data.csv (Iris dataset)

- res_dpre.csv (preprocessed Iris dataset)

- k.txt (Cluster counts)

### List of Docker Commands Used inside the final.sh script:
```bash
# Copy results from container to host
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-1.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-2.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-3.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/vis.png bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/kmeans_model.pkl bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/k.txt bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/loaded_data.csv bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/res_dpre.csv bd-a1/service-result/

# Stop the container
docker stop bd-a1-container
```
