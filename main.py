import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

file_name = input("Enter the file name : ")
data = pd.read_excel(file_name)
data.head()


def simple_moving_average(data, window_size):
    return data[['Close']].rolling(window_size, min_periods=window_size).mean()


def exponential_moving_average(data, window_size):
    return data[['Close']].ewm(span=window_size, adjust=False, min_periods=window_size).mean()


def macd_line(type, data):
    if type == 'simple':
        return simple_moving_average(data, 12).subtract(simple_moving_average(data, 26))
    elif type == 'exponential':
        return exponential_moving_average(data, 12).subtract(exponential_moving_average(data, 26))


def macd_ma(macd, type):
    if type == 'simple':
        return simple_moving_average(macd, 9)
    elif type == 'exponential':
        return exponential_moving_average(macd, 9)


def macd_histogram(macd, macd_ma):
    return macd.subtract(macd_ma)


def macd_profit_loss(data, initial_capital, commission):
    funds_available = initial_capital
    stock_position = 0.0
    num_of_trades = 0.0
    bought = True
    for index, date in enumerate(data['Date']):
        if data.iloc[index].bears:
            funds_available += stock_position * data.iloc[index].Close
            funds_available = funds_available * (1 - commission)
            stock_position = 0
            num_of_trades += 1
            bought = False


        elif data.iloc[index].bulls:
            funds_available = funds_available * (1 - commission)
            stock_position += funds_available / data.iloc[index].Close
            funds_available = 0
            num_of_trades += 1
            bought = True
 
    print(bought)
    final_value = funds_available + stock_position * (data.iloc[-1].Close)
    print(final_value)
    return num_of_trades, (final_value - initial_capital) / num_of_trades, (final_value - initial_capital)


def buy_hold_sell(data, initial_capital, commission):
    funds_available = initial_capital * (1 - commission)
    stock_position = funds_available / data.Close.iloc[0]
    funds_available = 0
    funds_available = stock_position * (data.Close.iloc[-1])
    funds_available *= (1 - commission)
    stock_position = 0
    return (funds_available + stock_position) - (initial_capital)


S_or_E = input("Type 'simple' if you want to calculate SMA, 'exponential' if you want to calculate EMA : ")
sign_reversals = np.sign(MACD_Histogram(MACD_line(S_or_E, data), MACD_MA(MACD_line(S_or_E, data), S_or_E))).diff().ne(0)


sign_reversals['Date'] = data['Date']
sign_reversals.head(50)
sign_reversals.set_index('Date', inplace=True)




hist_data = MACD_Histogram(MACD_line(S_or_E, data), MACD_MA(MACD_line(S_or_E, data), S_or_E))
hist_data['Date'] = data['Date']
hist_data.loc[hist_data.Date == '2018-02-01']


plt.bar(data=hist_data, x='Date', height='Close', width=10)


bulls = pd.DataFrame(np.sign(hist_data['Close']).diff().gt(0))
bears = pd.DataFrame(np.sign(hist_data['Close']).diff().lt(0))


bulls['Date'] = data['Date']
bears['Date'] = data['Date']


bulls.head()


len(bulls.loc[bulls.Close == True])


bears.loc[bulls.Close == True]


init_capital = 100000.00
commission = 1.0/800.0


data['bears'] = bears['Close']
data['bulls'] = bulls['Close']


data.head()


data.loc[(data['bears'] == True) & (data['bulls'] == 'True')]


num_of_trades, avg_return, diff1 = macd_profit_loss(data, 100000, commission)


diff2 = buy_hold_sell(data, 100000, commission)


print(diff1)
print(diff2)
print(avg_return)
