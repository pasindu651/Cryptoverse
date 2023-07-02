import streamlit as st
from streamlit_extras.no_default_selectbox import selectbox
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
import yfinance as yf

import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential
from streamlit.components.v1 import html
import random

st.title("Cryptoverse :lightning:")

longShort = {
"Bitcoin" : "BTC",
"Ethereum" : "ETH",
"Tether" : "USDT",
"BNB" : "BNB",
"USD Coin" : "USDC",
"XRP" : "XRP",
"Cardano" : "ADA",
"Dogecoin" : "DOGE",
"Litecoin" : "LTC",
"Solana" : "SOL",
"TRON" : "TRX",
"Polkadot" : "DOT",
"Polygon" : "MATIC",
"Bitcoin Cash" : "BCH",
"Wrapped Bitcoin" : "WBTC",
"Toncoin" : "TON",
"Dai" : "DAI",
"Avalanche" : "AVAX",
"Shiba Inu" : "SHIB",
"Binance USD" : "BUSD",
"UNUS SED LEO" : "LEO",
"Chainlink" : "LINK",
"Cosmos" : "ATOM",
"Monero" : "XMR",
"Uniswap" : "UNI",
"TrueUSD" : "TUSD",
"Stellar" : "XLM",
"Ethereum Classic" : "ETC",
"OKB" : "OKB",
"Lido DAO" : "LDO",
"Internet Computer" : "ICP",
"Filecoin" : "FIL",
"Hedera" : "HBAR",
"Aptos" : "APT",
"Arbitrum" : "ARB",
"VeChain" : "VET",
"Cronos" : "CRO",
"Quant" : "QNT",
"NEAR Protocol" : "NEAR",
"Aave" : "AAVE",
"Pax Dollar" : "USDP",
"Stacks" : "STX",
"The Graph" : "GRT",
"Algorand" : "ALGO",
"MultiversX" : "EGLD",
"Optimism" : "OP",
"Fantom" : "FTM",
"Bitcoin SV" : "BSV",
"ApeCoin" : "APE",
"EOS" : "EOS",
"Maker" : "MKR",
}

encouraging_messages = [
    "Get ready for a soaring ride!",
    "Your crypto journey is about to skyrocket!",
    "Embrace the future of finance with crypto!",
    "Don't miss out on the crypto wave!",
    "Time to shine with your crypto investments!",
    "Hop on the crypto train to success!",
    "Unlock the potential of crypto investments!",
    "Your financial revolution starts here!",
    "Discover the magic of crypto growth!",
    "Empower your portfolio with crypto assets!",
]


cryptoOptions = list(longShort.keys())


cryptoType = selectbox("Select a type of cryptocurrency for prediction", cryptoOptions)

start = st.date_input('Start', value=pd.to_datetime('2016-1-1'))
end = st.date_input('End', value=pd.to_datetime('today'))

future_dict = {"1 day": "1", "1 week": "7", "2 weeks" : "14", "1 month": "30", "2 months": "60", "6 months": "180"}

futureDiologue = {"1 day": "after a day", "1 week": "after a week", "2 weeks" : "after two weeks", "1 month": "after a month", "2 months": "after two months", "6 months": "after 6 months"}

futureDuration = selectbox("Select duration for future prediction", future_dict.keys())



if cryptoType is not None and futureDuration is not None:
  tf.keras.backend.clear_session()
  future = future_dict[futureDuration]
  load_state = st.text("Loading data...")

  crypto_currency = f"{longShort[cryptoType]}-USD"
  scale_currency = 'USD'
  data = yf.download(crypto_currency, start=start, end=end)
  scaler = MinMaxScaler(feature_range=(0,1))
  scaled_data= scaler.fit_transform(data['Close'].values.reshape(-1,1))
  prediction_days = 90
  future_days = 30

  x_train, y_train = [] ,[]
  for x in range (prediction_days, len (scaled_data)-future_days):
    x_train.append(scaled_data[x-prediction_days:x,0])
    y_train.append(scaled_data[x-future_days,0])
  x_train, y_train = np.array(x_train), np.array(y_train)
  x_train = np.reshape(x_train, ( x_train.shape[0], x_train.shape[1],1))

  load_state.text("Creating model...")


  model = Sequential ()
  model.add(LSTM(units=50, return_sequences=True, input_shape= (x_train.shape[1],1)))
  model.add(Dropout(0.2))
  model.add(LSTM(units=50, return_sequences=True))
  model.add(Dropout(0.2))
  model.add(LSTM(units=50))
  model.add(Dropout(0.2))
  model.add(Dense(units=1))


  model.compile(optimizer='adam', loss='mean_squared_error')
  model.fit(x_train, y_train, epochs=25, batch_size=32)


  test_start = start
  test_end = end
  test_data = yf.download(crypto_currency, start=test_start, end=test_end)
  actual_prices=  test_data['Close'].values
  total_dataset = pd.concat((data['Close'], test_data['Close']),axis=0)
  model_inputs = total_dataset[len(total_dataset)-len(test_data)-prediction_days:].values
  model_inputs=  model_inputs.reshape(-1,1)
  model_inputs = scaler.fit_transform(model_inputs)


  x_test = []
  for x in range (prediction_days, len (model_inputs)):
    x_test.append(model_inputs[x-prediction_days:x,0])
  x_test= np.array(x_test)
  x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1],1))


  prediction_prices = model.predict(x_test)
  prediction_prices = scaler.inverse_transform(prediction_prices)


  load_state.text("Done!")

  data = {'index' : test_data.index,
    'Predicted prices':  prediction_prices.flatten(),
          'Actual Prices': actual_prices.flatten()}
  df = pd.DataFrame(data)

  st.subheader('Forecast data')
  st.dataframe(df.set_index('index'))

  st.subheader(f'Time vs {crypto_currency} prices')
  st.line_chart(df)

  real_data = [model_inputs[len(model_inputs)+1-prediction_days:len(model_inputs)+int(future),0]]
  real_data = np.array(real_data)
  real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1],1))

  prediction = model.predict(real_data)
  prediction = scaler.inverse_transform(prediction)


  st.success(f'{random.choice(encouraging_messages)} :rocket: The price of {cryptoType} {futureDiologue[futureDuration]}: ${round(float(prediction[0][0]), 2)} USD')

js_code = """
    (function (d, t) {
      var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
      v.onload = function () {
        window.voiceflow.chat.load({
          verify: {projectID: '64a02ea0e70a190007b2ad86'},
          url: 'https://general-runtime.voiceflow.com',
          versionID: 'production'
        });
      }
      v.src = "https://cdn.voiceflow.com/widget/bundle.mjs"; v.type = "text/javascript"; s.parentNode.insertBefore(v, s);
    })(document, 'script');
"""

chat_html = f"<script>{js_code}</script>"

html(chat_html, width=950, height=400)


