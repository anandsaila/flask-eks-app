FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create a file and add content
RUN touch wizexercise.txt
RUN echo "This is the Wiz Exercise lab" > wizexercise.txt

EXPOSE 5000

CMD ["python", "app.py"]
