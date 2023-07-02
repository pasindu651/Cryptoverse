# Cryptoverse


Cryptoverse is an all-in-one streamlit python app that offers a comprehensive platform for predicting various types of cryptocurrences, engaging with a financial cryptocurrency chatbot, and gaining insight into sentiment analysis of cryptocurrency-related tweats. This app allows regular investors to stay ahead of the crypto game by making informed decisions about their investments and leveraging a well-rounded analysis of cryptocurrency in a market that is characterized by uncertainty.


## Tools Used

* [Python 3.10.0](https://www.python.org/downloads/release/python-3100/)
* [Streamlit](https://streamlit.io/)
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/) 
* [Tensorflow](https://www.tensorflow.org/)
* [Yfinance](https://pypi.org/project/yfinance/)
* [Voiceflow](https://pypi.org/project/yfinance/)


## How It Works
![image](https://i.ibb.co/R71myDc/cryptoverse-pg-1.jpg)

<h3>Cryptocurrency price prediction component:</h3>
1. The user can predict cryptocurrency prices with full customizability of the type of currency, the start/end window used for prediction, and how far into the future the user wishes to predict.
2. The program fetches the price data of the window defined by the user from Yahoo Finance and configures it in a numpy array after training it.
3. The program leverages a sequential model built with LSTM layers to understand the relationships of the price data.
4. The program fits the model and compares the predicted prices of the test data and the actual prices, plotting their respective graphs using pandas and streamlit. 

</br>
</br>
</br>


![image](https://i.ibb.co/Kj7JZJ4/cryptoverse-pg-2.jpg)

Cryptocurrency financial chatbot component:
![image](https://i.ibb.co/xFLGdx1/cryptoverse-pg-3.jpg)

1. The program uses Voiceflow's streamlined flowchart structure to build responses trained on financial Q&A data.......
   
<details><summary><b>Show requirements</b></summary>
    
1. Install streamlit:
    
    ```sh
    pip install streamlit
    ```
2. Install numpy:
   
    ```sh
    pip install numpy
    ```
1. Install pandas:
   
    ```sh
    pip install pandas
    ```
1. Install datetime:
   
    ```sh
    pip install datetime
    ```
1. Install sklearn:
   
    ```sh
    pip install sklearn
    ```
1. Install yfinance:
   
    ```sh
    pip install yfinance
    ```
1. Install tensorflow:
   
    ```sh
    pip install tensorflow
    ```
1. Install random:
   
    ```sh
    pip install random
    ```
1. Run the python file to create a localhost server:
   
    ```sh
    python3 -m streamlit run main.py
    ```
</details>
