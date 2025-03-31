# Choose a base python image
FROM python:3.10-slim

# Set up work directory in container's file system
WORKDIR /app

# Create empty instance directory that is mapped to
# the `instance` dir in local
RUN mkdir -p instance && chmod 777 instance

# Copy the all files at the same level as the `Dockerfile`
# to the `app` dir in the container
COPY . /app

# Now, given `requirements.txt` is copied in `app`, install the dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask server
EXPOSE 5000

# Run the app
CMD [ "python", "app.py" ]