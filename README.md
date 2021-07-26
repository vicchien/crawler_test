# Quick start
```bash
pip install pipenv
pipenv sync

# Get today's value
pipenv run python main.py

# Get value from start_date to end_date
pipenv run python main.py $start_date $end_date
# Example
pipenv run python main.py 2021/07/23 2021/07/26
```