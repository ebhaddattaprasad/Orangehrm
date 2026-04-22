# Playwright Python Framework Scaffold

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
python -m playwright install
pre-commit install
```

## Run Tests

```bash
pytest
```

## Tagging test_case_id

Use marker in tests:

```python
@pytest.mark.test_case_id("test_case_001")
def test_example(page, case_data):
    ...
```
