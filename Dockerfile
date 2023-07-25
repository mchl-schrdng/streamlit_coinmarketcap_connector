# Use an official lightweight Python 3.9 image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local code to the container
COPY . .

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Set the command to run your Streamlit app
CMD streamlit run app.py --server.port 8080 --browser.serverAddress 0.0.0.0 --browser.gatherUsageStats False
