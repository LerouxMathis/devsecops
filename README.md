# API Python — Exercice 2 DevSecOps

## Description
API Python minimale utilisée pour mettre en place une CI avec tests,
contrôle qualité et analyse sécurité via GitHub Actions.

---

## Lancer l’application avec Docker

```bash
docker build -t api-devsecops .
docker run -p 5000:5000 api-devsecops
