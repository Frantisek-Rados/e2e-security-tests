# E2E a bezpecnostne testy

Tento repozitar obsahuje ukazky E2E a bezpecnostnych testov.

## Obsah
- **E2E test:** Kompletny nakupny proces (SauceDemo)
- **Bezpecnostne hlavicky:** Kontrola HSTS, CSP, X-Frame-Options
- **XSS:** Testovanie Cross-Site Scripting (skipped)
- **SQL injection:** Testovanie SQL injection (skipped)

## Spustenie
1. Nainstaluj zavislosti:
```bash
pip install -r requirements.txt
playwright install
```

2. Spusti vsetky testy:
```bash
pytest -v tests/
```

## Autor
František Radoš
