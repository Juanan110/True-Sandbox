# BACKEND/DOCKERFILE
FROM python:3.9

#Working directory
WORKDIR /app

#Copy the requirements file
COPY app/requirements.txt .

# Dependencies
RUN pip install --no-cache-dir -r requirements.txt 

# Copy the rest of the aplication code

COPY app/ .

# Run the aplication
CMD ["python", "main.py"]
