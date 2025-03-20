# Use Ubuntu as the base image
FROM ubuntu:latest

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pandas \
    python3-numpy \
    python3-seaborn \
    python3-matplotlib \
    python3-sklearn \
    python3-scipy \
    && rm -rf /var/lib/apt/lists/*

# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1/

# Set working directory
WORKDIR /home/doc-bd-a1/

# Copy dataset from host to container
COPY Iris.csv /home/doc-bd-a1/

# Keep container running with a bash shell
CMD ["/bin/bash"]
