# Cryptoverse ⚡


Cryptoverse is an all-in-one streamlit python app that offers a comprehensive platform for predicting various types of cryptocurrencies, engaging with a financial cryptocurrency chatbot, and gaining insightful comparisons between different cryptos with a heatmap. This app allows regular investors to stay ahead of the crypto game by making informed decisions about their investments and leveraging a well-rounded analysis of cryptocurrency in a market that is characterized by uncertainty.


## Tools Used 🔧

* [Python 3.10.0](https://www.python.org/downloads/release/python-3100/)
* [Streamlit](https://streamlit.io/)
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/) 
* [Tensorflow](https://www.tensorflow.org/)
* [Yfinance](https://pypi.org/project/yfinance/)
* [Voiceflow](https://www.voiceflow.com/)


## How It Works 
![image](https://i.ibb.co/R71myDc/cryptoverse-pg-1.jpg)

<h3>Cryptocurrency price prediction component:</h3>

1. The user can predict cryptocurrency prices with full customizability of the type of currency, the start/end window used for prediction, and how far into the future the user wishes to predict.

2. The program fetches the price data of the window defined by the user from Yahoo Finance and configures it in a numpy array after training it.

3. The program leverages a sequential model built with LSTM layers to understand the relationships of the price data. 

4. The program fits the model and compares the predicted prices of the test data and the actual prices, plotting their respective graphs using pandas and streamlit.

</br>

![image](https://i.ibb.co/Kj7JZJ4/cryptoverse-pg-2.jpg)

<h3>Cryptocurrency comparison and heatmap component:</h3>

1. The program creates multiple columns with simultaneous data provided by the tickers selected by the user

2. The program plots each respective column on a single graph

3. The creates subplots and a heatmap by calculating the percentage change of the combined data
   
</br>

![image](https://i.ibb.co/wY6mxVH/cryptoverse-pg-4.jpg)

<h3>Cryptocurrency financial chatbot component:</h3>

1. The program uses Voiceflow's streamlined flowchart structure to build responses trained on financial Q&A data.

2. The program feeds the training data to GPT 3.5.

3. The user can then ask a question, which then prompts the chatbot to query the training data to generate a response based on the most relevant information.

![image](https://i.ibb.co/xFLGdx1/cryptoverse-pg-3.jpg)
   
<details><summary><b>Show requirements</b></summary>
    
Install with ```pip install -r requirements.txt```
</details>
