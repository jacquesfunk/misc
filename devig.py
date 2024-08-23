def implied_probability(odds):
    """Convert odds to implied probability"""
    if odds < 0:
        return abs(odds) / (abs(odds) + 100)
    else:
        return 100 / (odds + 100)


def fair_odds(odds1, odds2, odds3):
    """Calculate fair odds from three sets of odds"""
    odds = [odds1, odds2, odds3]
    implied_probs = [implied_probability(o) for o in odds]
    avg_implied_prob = sum(implied_probs) / len(implied_probs)
    fair_odds = 100 / (avg_implied_prob / 100)
    return fair_odds


def overround(odds1, odds2):
    """Calculate overround"""
    implied_prob1 = implied_probability(odds1)
    implied_prob2 = implied_probability(odds2)
    return (1 / (1 - implied_prob1)) + (1 / (1 - implied_prob2)) - 1


def devig_odds(fair_odds, overround):
    """Devig odds"""
    return fair_odds / (1 + (overround / 100))


# Example usage
odds1 = -150
odds2 = -160
odds3 = -170

fair_odds_A = fair_odds(odds1, odds2, odds3)
fair_odds_B = fair_odds(-130, -140, -150)

overround = overround(fair_odds_A, fair_odds_B)

devigged_odds_A = devig_odds(fair_odds_A, overround)
devigged_odds_B = devig_odds(fair_odds_B, overround)

print("Fair Odds:")
print("Team A:", fair_odds_A)
print("Team B:", fair_odds_B)

print("\nOverround:", overround)

print("\nDevigged Odds:")
print("Team A:", devigged_odds_A)
print("Team B:", devigged_odds_B)
