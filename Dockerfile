# Use Ubuntu as the base image
FROM ubuntu:latest

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update \
    && apt-get install -y \
        gcc \
        g++ \
        cmake \
        ninja-build \
        python3 \
        python3-pip \
        curl \
        git \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to the PATH
ENV PATH="/root/.local/bin/:${PATH}"

# Set up a volume for the project
VOLUME /app
WORKDIR /app
COPY . .
RUN poetry install --only main

EXPOSE 8000
ENTRYPOINT ["poetry", "run", "start"]

# Test command
# CMD ["poetry", "run", "uvicorn", "compiler_exploter.main:app", "--host", "0.0.0.0", "--port", "8000"]
