# Flask API with Google Cloud Logging

## Overview

This project demonstrates a simple Flask API server integrated with Google Cloud Logging for robust logging capabilities.

## Prerequisites

1. **Docker and Docker Compose:** Ensure you have Docker and Docker Compose installed on your system. The most convenient way is to simply install Docker Desktop:
- MacOS: [Docker Desktop installation on MacOS](https://docs.docker.com/desktop/install/mac-install/)
- Windows: [Docker Desktop installation on Windows](https://docs.docker.com/desktop/install/windows-install/)

2. **After installation, start Docker Desktop. You can confirm that Docker Engine is running correctly in the lower left corner of the interface, as shown below:**
![image](https://hackmd.io/_uploads/rJ1JF_joR.png)

3. **Available Port:** Make sure port **9543** is available on your machine. If not, modify the port number in `docker-compose.yml` and `main.py`.

## Deployment
1. **Clone this Repository:** Clone this repository to your local machine.
   ```bash
   git clone git@github.com:tc2230/qs-case-study.git;
   cd qs-case-study
   ```

2. **Replace the GA4 measurement protocol Measurement ID/API Secret in the .env file with your own, and place the GCP key within the project folder (in the same directory as `main.py`), rename key file as `gcp_logging_key.json`**
    *Notice: need to enable Cloud Logging and Measurement protocol write permissions*

3. **Build and Run:** Navigate to the project directory and run the following command to build and start the API:
   ```bash
   docker-compose up
   ```
   This will build the Docker image, start the container and the API service. Add option `-d` for detached mode.
  
  
4. **Verify Startup:** Check your terminal. You should see the test results from pytest, and a message indicating the API is listening for requests.

   ![Docker Compose Startup](https://hackmd.io/_uploads/rkPOiwjsR.png)

## Testing the API

1. **Endpoint:** The API provides a single endpoint for generating PNG images:
   - **URL:** `http://localhost:9543/generate_png`
   - **Method:** GET
   - **Required Parameters:**
     - `width`: The desired width of the PNG image.
     - `height`: The desired height of the PNG image.

2. **Test Tools:** You can visit example endpoint (http://localhost:9543/generate_png?width=100&height=100) using a web browser, or send request with client tool like [Postman](https://www.postman.com/downloads/), or curl.

    For example, using curl:
      ```bash
       curl -o output.png "http://localhost:9543/generate_png?width=100&height=100"
      ```
