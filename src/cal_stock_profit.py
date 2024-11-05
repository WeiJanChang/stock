from typing import Union
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display
from pathlib import Path
from datetime import datetime

plt.rcParams['axes.unicode_minus'] = False  # To show positive or negative symbol

Pathlike = Union[Path | str]


def cal_stock_profit(df: pd.DataFrame):
    print('Your stocks include: ', df['stock'].unique())
    name = input("Please enter the stock name: ")
    stock_assigned = df.loc[df["stock"] == name]
    print(stock_assigned)
    display(stock_assigned.dropna())
    profit = stock_assigned.dropna()['profit'].to_list()
    print(f'Total profit in {name}: ' + 'NTD ' + str(sum(profit)))
    stock_assigned['date_sold'] = pd.to_datetime(stock_assigned['date_sold']).dt.strftime(
        '%Y/%m/%d').str.extract(r'(\d{4})')
    profit_count = stock_assigned.groupby(['date_sold', 'stock'])['profit'].sum().unstack()
    ax = profit_count.plot(kind='bar', stacked=True, figsize=(50, 6))
    plt.xlabel('sale year')
    plt.ylabel("Profit(+/-)")
    plt.title(f'Profit of {name}')
    plt.legend(title='stock', loc='upper left', bbox_to_anchor=(1, 1))
    plt.xticks(rotation=0)
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge', fontsize=8)

    plt.show()

# todo:1. 計算total profit. how calculate df[''] - df['']
# todo: fix error