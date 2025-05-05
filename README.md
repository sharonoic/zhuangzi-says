# zhuangzi-says

A tiny web app where grandpa-zhuang whispers at you through confusing metaphors and oddly personal advice.

Built with Flask, SQLite, and Zhuangzi's existential dread.

## What It Does

- Asks you three vague questions about your mood, life crisis, or butterfly dream
- Tags your responses with vibes like `illusion`, `urgency`, or `detachment`
- Fetches a quote from Zhuangzi
- Slaps your name into the commentary like a passive-aggressive sage

## Technologies

- Python + Flask
- SQLite database
- HTML 

## Why

- Mainly because I was bored and didn't want to work on things I was supposed to do
- And because sometimes you just want a philosophical quote generator that lightly roasts you with ancient wisdom

## Setup

```bash
git clone https://github.com/sharonoic/zhuangzi-says.git
cd zhuangzi-says
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python seed/seed_quotes.py
python app.py
```
