# GitLab → GitHub Migration Lab

A small Python service with realistic Git history for practicing repository migration.

## Run locally

```bash
python -m unittest discover -s tests -v
python app.py
```

See `MIGRATION_LAB.md` for migration and validation exercises. The repository includes GitLab CI (`.gitlab-ci.yml`) and a GitHub Actions starter workflow (`.github/workflows/ci.yml`).
