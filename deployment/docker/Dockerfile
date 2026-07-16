FROM python:3.12-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Enable unbuffered logs
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first (better Docker caching)
COPY requirements.txt .

# Install Python dependencies
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Streamlit Port
EXPOSE 8501

# Run Streamlit Dashboard
ENTRYPOINT ["streamlit", "run", "Week7/analysis/app.py", "--server.port=8501", "--server.address=0.0.0.0"]