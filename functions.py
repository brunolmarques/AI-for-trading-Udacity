import scipy.stats as stats

def return(pandas_stock):
    """
    Compute returns for each ticker and date in close.

    Parameters
    ----------
    pandas_stock : DataFrame
        Close prices for each ticker and date

    Returns
    -------
    returns : DataFrame
        Returns for each ticker and date at d+1
    """
    return (pandas_stock - pandas_stock.shift(1)) / pandas_stock.shift(1)



def log_ return(pandas_stock):
    """
    Compute log returns for each ticker and date in close.

    Parameters
    ----------
    pandas_stock : DataFrame
        Close prices for each ticker and date

    Returns
    -------
    returns : DataFrame
        Returns for each ticker and date at d+1
    """
    return np.log((pandas_stock - pandas_stock.shift(1)) / pandas_stock.shift(1))



def generate_positions(pd_prices, long_stocks, long_trigger, short_stocks, short_trigger):
    """
    Generate the following signals:
     - Long stocks when the price is above long_trigger value
     - Short stocks when its price is below short_trigger value

    Parameters
    ----------
    pd_prices : DataFrame
        Prices for each ticker and date
    long_stocks: Integer
        Number of shares to long
    long_trigger: Float
        Value of stock that triggers long momentum
    short_stocks: Integer
        Number of shares to short
    short_trigger: Float
        Value of stock that triggers short momentum

    Returns
    -------
    final_positions : DataFrame
        Final positions for each ticker and date
    """

    long_pos = (pd_prices > long_trigger).astype(np.int) * long_stocks # plus signals buy
    short_pos = (pd_prices < short_trigger).astype(np.int) * - short_stocks # minus signals sell

    return long_pos + short_pos


def date_top_industries(prices, sector, date, top_n):
    """
    Get the set of the top industries for the date

    Parameters
    ----------
    prices : DataFrame
        Prices for each ticker and date
    sector : Series
        Sector name for each ticker
    date : Date
        Date to get the top performers
    top_n : int
        Number of top performers to get

    Returns
    -------
    top_industries : set
        Top industries for the date
    """
    top_performers = prices.loc[date].nlargest(top_n)
    top_set = {top_x for top_x in sector.loc[top_performers.index]}

    return top_set


def analyze_returns(net_returns):
    """
    Perform a t-test, with the null hypothesis being that the mean return is zero.

    Parameters
    ----------
    net_returns : Pandas Series
        A Pandas Series for each date

    Returns
    -------
    t_value
        t-statistic from t-test
    p_value
        Corresponding p-value
    """
    # Hint: You can use stats.ttest_1samp() to perform the test.
    #       However, this performs a two-tailed t-test.
    #       You'll need to divde the p-value by 2 to get the results of a one-tailed p-value.
    null_hypothesis = 0.0
    t_stat, p_value = stats.ttest_1samp(net_returns, null_hypothesis)

    return t_stat, p_value/2
