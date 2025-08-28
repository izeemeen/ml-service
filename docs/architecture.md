# Архитектура сервиса (минимальная)


- Inference API (FastAPI) — принимает запросы, возвращает предсказания
- Model store (models/) — хранение артефактов модели
- CI/CD: GitHub Actions — тесты и сборка образа
- Monitoring: логирование запросов, производительности; далее — Prometheus/Grafana
- Retrain pipeline: scripts/train.py + GitHub Actions schedule или Airflow/Prefect