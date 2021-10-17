import requests
import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


def get_token():
    auth = requests.post("https://auth.lemon.markets/oauth2/token",
                         data={
                             "client_id": client_id,
                             "client_secret": client_secret,
                             "grant_type": "client_credentials"
                         })
    token: str = "Bearer " + auth.json()['access_token']
    return token


def get_ohlc():
    response = requests.get(
        'https://paper-data.lemon.markets/v1/ohlc/d1/?isin=US0378331005&from=2021-06-25T00:00:00&to=2021-08-24T00:00:00',
        headers={"Authorization": get_token()})

    results = response.json()['results']
    return results


def calculate_returns():
    df = pd.DataFrame(get_ohlc())
    # calculate returns based on closing price
    df['r'] = df['c'].pct_change().fillna(method='bfill')
    df.tail()
    return df


def plot_returns():
    returns = calculate_returns()['r']

    # plot returns
    plt.hist(returns, bins=25, density=True, alpha=0.6, color='darkorange')

    # plot normal distribution fitted to returns
    mu, std = norm.fit(returns)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    plt.xlabel('Daily Tesla Returns')
    plt.ylabel('Probability Density Function')

    plt.show()


plot_returns()