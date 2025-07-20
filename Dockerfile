FROM python:3.9

WORKDIR /app

COPY app/app.py .
COPY app/model.pkl ./app/model.pkl

RUN pip install flask joblib scikit-learn

EXPOSE 5000

CMD ["python", "app.py"]
