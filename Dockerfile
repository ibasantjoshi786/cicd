FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy everything into the container (adjust if you want to exclude files)
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir pandas pytest scikit-learn

# Run the pipeline.py inside src folder when container starts
CMD ["python","-m", "src.pipeline"]
