def calculate_payout(amount, odds):
    if odds > 0:
        payout = amount * (1 + odds / 100)
    else:
        payout = amount * (1 + 100 / abs(odds))
    return payout

def calculate_all_payouts(bets):
    payouts = []
    for amount, odds in bets:
        payout = calculate_payout(amount, odds)
        payouts.append(payout)
    return payouts

# Example list of tuples (amount, odds)
bets = [
    (100, -150),
    (50, 200),
    (75, 120),
    (200, -110)
]

# Calculate all payouts
payouts = calculate_all_payouts(bets)

# Print table header
print("Amount    | Odds   | Payout")
print("----------|--------|-------")

# Print each row of the table
for i, (amount, odds) in enumerate(bets):
    print(f"${amount:<9}| {odds:<7}| ${payouts[i]:.2f}")