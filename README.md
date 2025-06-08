# Website Security Header Analyzer

Ett verktyg för att analysera säkerhetsrelaterade HTTP-headrar på webbplatser. Verktyget är byggt i Python och använder Streamlit för ett enkelt användargränssnitt .

## Vad som analyseras:

- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Content-Type-Options`
- `X-Frame-Options`
- `Referrer-Policy`
- `Permissions-Policy`

## Hur du kör projektet:

1. 

```bash
git clone https://github.com/Artin21/website-security-header-analyzer.git
cd website-security-header-analyzer
```

2. 

```bash
pip install -r requirements.txt
```

3. 

```bash
streamlit run app.py
```

4. 

```bash
python3 tests/test_headers_check.py
```

## Säkerhetsklassificering:

- **Säker** – alla viktiga headrar finns
- **Varning** – 1–2 saknas
- **Osäker** – 3 eller fler saknas

## Exempel-URL:er att testa:

- https://www.google.com
- https://example.com
- http://neverssl.com
- https://badssl.com

## Etik:

Verktyget gör endast passiva analyser (läser headers). Inga attacker eller intrång görs.

## Teknikstack:

- Python 3
- requests
- streamlit
