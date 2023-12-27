FROM python:3.8-slim

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy the application code
COPY . /app

EXPOSE 80
EXPOSE 8010

# Command to run the application with SSL support on port 8010
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8010", "--ssl-keyfile", "/app/privkey.pem", "--ssl-certfile", "/app/fullchain.pem"]