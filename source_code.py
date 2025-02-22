import tweepy
import time
from datetime import datetime
import pytz

# Claves de autenticación para el bot (para obtenerlas se necesita cuenta de desarrollador de Twitter)
CONSUMER_KEY = " "
CONSUMER_SECRET = " "
ACCESS_TOKEN = " "
ACCESS_SECRET = " "
BEARER_TOKEN = " "

# Frases para los tweets, siguen un ciclo para evitar error de tweet duplicado (separadas por ",")
frases = [ 
    "Salú! #FelizSabado https://x.com/GabrielBoric/status/1269441927432282112",
    "Buenas noches! #FelizSabado https://x.com/GabrielBoric/status/1269441927432282112",
    "Hacía falta. #FelizSabado https://x.com/GabrielBoric/status/1269441927432282112",
    ";) #FelizSabado https://x.com/GabrielBoric/status/1269441927432282112",
    "Una y a dormir. #FelizSabado https://x.com/GabrielBoric/status/1269441927432282112",
    "Grande Presi! #FelizSabado https://x.com/GabrielBoric/status/1269441927432282112",
    "Por la patria 🍻 #FelizSabado https://x.com/GabrielBoric/status/1269441927432282112",
]

# Función para enviar tweet
def send_tweet(opcion):
    text = frases[opcion]

    consumer_key = CONSUMER_KEY
    consumer_secret = CONSUMER_SECRET
    access_token = ACCESS_TOKEN
    access_token_secret = ACCESS_SECRET
    bearer_token = BEARER_TOKEN

    # Autenticación con Twitter
    client = tweepy.Client(bearer_token=bearer_token,
                    consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret)
    # Enviar tweet
    try:
        client.create_tweet(text=text)
        print("Tweet sent successfully!")
        
    except tweepy.TweepyException as e:
        print(f"Error: {e}")

# Función para quitar retweet
def unretweet():
    consumer_key = CONSUMER_KEY
    consumer_secret = CONSUMER_SECRET
    access_token = ACCESS_TOKEN
    access_token_secret = ACCESS_SECRET
    bearer_token = BEARER_TOKEN

    # Autenticación con Twitter
    client = tweepy.Client(bearer_token=bearer_token,
                    consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret)
    # Quitar Retweet
    try:
        client.unretweet(source_tweet_id=1269441927432282112, user_auth=True)
        print("Unretweet sent successfully!")
    except tweepy.TweepyException as e:
        print(f"Error: {e}")

# Función para dar retweet
def retweet():
    consumer_key = CONSUMER_KEY
    consumer_secret = CONSUMER_SECRET
    access_token = ACCESS_TOKEN
    access_token_secret = ACCESS_SECRET
    bearer_token = BEARER_TOKEN

    # Autenticación con Twitter
    client = tweepy.Client(bearer_token=bearer_token,
                    consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret)
    # Retweetear
    try:
        client.retweet(tweet_id=1269441927432282112, user_auth=True)
        print("Retweet sent successfully!")
    except tweepy.TweepyException as e:
        print(f"Error: {e}")

# Función para ejecutar el ciclo de quitar retweet, poner citado y retweetear de vuelta
def cycle(opcion):
    unretweet()
    time.sleep(10)
    send_tweet(opcion)
    time.sleep(10)
    retweet()
    time.sleep(40)

tz = pytz.timezone("America/Santiago")

# Opción para el texto, se actualiza cada vez que se ejecuta el ciclo
opcion = 0

# Loop principal
while True: 
    now = datetime.now(tz).strftime("%H:%M")
    daynow = datetime.now(tz).strftime("%A")

    # Si es sábado y son las 21:30, ejecutar el ciclo
    if now == "21:30" and daynow == "Saturday":
        if opcion < 6:
            opcion += 1
        elif opcion == 6:
            opcion = 0
        cycle(opcion)

    # Si no, esperar (muestra la fecha y hora actual en consola)
    print(f"[{datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')}] Waiting...")
    time.sleep(60)
