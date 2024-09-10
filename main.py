from pyxt.spot import Spot
import pandas as pd
import sqlalchemy
import os

# Fetch data from the API
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")
xt = Spot(host="https://sapi.xt.com", access_key=api_key, secret_key=secret_key)
responseData = xt.get_kline(symbol='btc_usdt', interval="1d")

# Convert the response to JSON and normalize it into a DataFrame

df = pd.json_normalize(responseData)

#df_users = pd.read_csv('users.csv', header=None, names=['user_ID', 'movie_ID', 'rating'], index_col=False)
#df_movies = pd.read_csv('movies.csv', header=None, names=['movie_ID', 'Title', 'Description', 'Genre'], index_col=False)

sqlite_file_path = 'BTC_data.db'

# Create a connection to SQLite and save the data
engine = sqlalchemy.create_engine(f'sqlite:///{sqlite_file_path}', echo=False)
df.to_sql(name="Crypto", con=engine, index=False, if_exists='replace')


