import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['axes.unicode_minus'] = False  # To show positive or negative symbol


def cal_stock_profit(df: pd.DataFrame, stock_name: int) -> pd.Series:
    """
    Calculate and plot the yearly profit for a given stock.

    :param df: DataFrame
    :param stock_name: Integer code representing the stock to be analyzed
    :return: pd.Series containing yearly profit for the specified stock
    """
    stock_assigned = df.loc[df["stock"] == stock_name]
    stock_assigned['date_sold'] = pd.to_datetime(stock_assigned['date_sold'], errors='coerce')
    # errors='coerce' ensures any invalid date formats are handled by assigning NaT (Not a Time).
    # Extract the year
    stock_assigned['year_sold'] = stock_assigned['date_sold'].dt.year
    yearly_profit = stock_assigned.groupby('year_sold')['profit'].sum()
    ax = yearly_profit.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.xlabel('the year of sold')
    plt.ylabel("Profit(+/-)")
    plt.title(f'Profit of the {stock_name}')
    plt.legend(title='stock', loc='upper left', bbox_to_anchor=(1, 1))
    plt.xticks(rotation=0)
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge', fontsize=8)

    plt.show()
    # Return calculated values for further analysis or testing
    return yearly_profit
