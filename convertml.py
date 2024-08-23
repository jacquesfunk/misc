import polars as pl

# Create a DataFrame with the specified columns
moneyline_values = [-160, -110]
num_values = len(moneyline_values) + 1

df = pl.DataFrame({
    'GameNumber': range(1, num_values),
    'Moneyline': moneyline_values
})

# Initialize the initial investment
initial_investment = 7.86

# Calculate winnings, return, profit, and cumulative ML rollover odds
risk = initial_investment
wins = []
returns = []
profits = []
ml_rollover_odds = []

for moneyline in df['Moneyline']:
    if moneyline < 0:
        win = abs(risk / (moneyline / 100))
    else:
        win = risk * (moneyline / 100)

    returns.append(risk + win)
    profits.append((risk + win) - initial_investment)
    ml_rollover_odds.append(((risk + win) - initial_investment) / initial_investment * 100)

    risk = returns[-1]
    wins.append(win)

df = df.with_columns([
    pl.Series('Risk', [initial_investment] + returns[:-1]),
    pl.Series('Win', wins),
    pl.Series('Return', returns),
    pl.Series('Profit', profits),
    pl.Series('MLRolloverOdds', ml_rollover_odds)
])

# Round the values as specified and format as currency
df = df.with_columns([
    pl.col('Risk').round(2).map_elements(lambda x: f"${x:,.2f}", return_dtype=pl.Utf8),
    pl.col('Win').round(2).map_elements(lambda x: f"${x:,.2f}", return_dtype=pl.Utf8),
    pl.col('Return').round(2).map_elements(lambda x: f"${x:,.2f}", return_dtype=pl.Utf8),
    pl.col('Profit').round(2).map_elements(lambda x: f"${x:,.2f}", return_dtype=pl.Utf8),
    pl.col('MLRolloverOdds').round(0).cast(pl.Int32)
])

# Display the DataFrame with calculated columns
print(df)