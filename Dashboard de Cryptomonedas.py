import krakenex
from pykrakenapi import KrakenAPI
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

#First try and except of the Kraken API
try:
    api = krakenex.API()
    k = KrakenAPI(api)
except:
    st.write("Error en la conexión del API.")

#Crypto selection
pairs = k.get_tradable_asset_pairs()
opciones = [valor for indice, valor in enumerate(pairs["altname"]) if valor[-3:] == "USD" or valor[-3:] == "ETH"]
seleccion_criptomonedas = st.sidebar.selectbox(label='Seleccione una criptomoneda', options=opciones)
seleccion_interval = st.sidebar.selectbox(label='Seleccione un intervalo', options=('5', '60', '1440'))


# FUNCTIONS
# Calculate RSI
def rsi(df, periods, ema):
	# Calculate the change in price
	delta = df['close'].diff()
	
	# Create the gain and loss columns
	gain = delta.where(delta > 0, 0)
	loss = -delta.where(delta < 0, 0)
	
	# Calculate the average gain and loss
	avg_gain = gain.rolling(periods).mean()
	avg_loss = loss.rolling(periods).mean()
	
	# Calculate the relative strength
	rs = avg_gain / avg_loss
	
	# Calculate the RSI
	rsi = 100 - (100 / (1 + rs))
	if ema:
	    rsi = rsi.ewm(span=periods, adjust=False).mean()
	
	return rsi.fillna(0)

# API SETUP
#One try and except to validate the selection of crypto
try:
    ohlc = k.get_ohlc_data(seleccion_criptomonedas, interval=seleccion_interval, ascending=True)
except:
    st.write("Error al obtener datos de la criptomoneda seleccionada.")

# DOWNLOAD DATA
df = pd.DataFrame(ohlc[0])
df.reset_index(inplace=True)

# GRAPH DATA
# Create graph 
fig = go.Figure(data=[go.Candlestick(x=df['dtime'],
									 open=df['open'],
									 high=df['high'],
									 low=df['low'],
									 close=df['close'])])
fig.update_layout(title=f"Gráfico de {seleccion_criptomonedas}", xaxis_title="Fecha", yaxis_title="Precio")

# Calculate & graph Moving Avg 
df['mean_close'] = df['close'].rolling(window=14).mean()
fig.add_trace(go.Scatter(x=df['dtime'], y=df['mean_close'], name='Media Móvil', line=dict(color='blue')))

#RSI stof
fig_rsi = go.Figure()
df['rsi'] = rsi(df=df, periods=14, ema=True)
# Calculate rsi
fig_rsi.add_trace(go.Scatter(x=df['dtime'], y=df['rsi'], name='RSI', line=dict(color='red')))
fig_rsi.update_layout(title=f"RSI de {seleccion_criptomonedas}", xaxis_title="Fecha", yaxis_title="RSI")

#Plot the graph
st.plotly_chart(fig)
st.plotly_chart(fig_rsi)