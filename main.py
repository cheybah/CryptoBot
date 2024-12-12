import requests
import tweepy
from apscheduler.schedulers.blocking import BlockingScheduler

# Twitter API Keys (Replace with your actual keys)
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"

# Initialize Twitter API
def twitter_api():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)

# Step 2: Fetch Crypto Prices
# Example: Fetch Bitcoin price using CoinGecko API
def get_crypto_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[crypto_id]['usd']
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Step 3: Calculate Trends (Stub for now)
def calculate_trend(current_price, previous_price):
    if previous_price is None:
        return "No data for trend calculation"
    change = ((current_price - previous_price) / previous_price) * 100
    return f"{change:.2f}%"

# Step 4: Post Updates to Twitter
def post_to_twitter(message):
    api = twitter_api()
    try:
        api.update_status(message)
        print("Tweet posted successfully!")
    except Exception as e:
        print(f"Error posting tweet: {e}")

# Step 5: Schedule Regular Updates
scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', hours=1)
def scheduled_task():
    crypto_id = "bitcoin"
    current_price = get_crypto_price(crypto_id)
    if current_price:
        # Placeholder for trend calculation (implement historical tracking)
        trend = calculate_trend(current_price, None)  # Replace 'None' with previous price tracking logic
        message = f"Bitcoin price: ${current_price} USD. Trend: {trend} in the last hour."
        post_to_twitter(message)

if __name__ == "__main__":
    print("Starting Crypto/Stock Price Bot...")
    scheduler.start()
