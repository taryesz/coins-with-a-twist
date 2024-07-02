print("A hat contains 100 coins, where 99 are fair but one is double-headed (always landing Heads).\n"
      "A coin is chosen uniformly at random. The chosen coin is flipped 7 times, and it lands Heads all 7 times.\n"
      "Given this information, what is the probability that the chosen coin is double-headed?\n"
      "(Of course, another approach here would be to look at both sides of the coin—but this is a metaphorical coin.)\n")

# Constants
TOTAL_COINS = 100
DOUBLE_HEADED_COINS = 1
COIN_FLIPS = 7

# prior probability that the chosen coin is double-headed
prior_double_headed = DOUBLE_HEADED_COINS / TOTAL_COINS

# probability of getting 7 heads in a row with a fair coin
probability_heads_fair_coin = 1 / (2 ** COIN_FLIPS)


def bayes(prior, likelihood, evidence):
    """
    Calculate the posterior probability using Bayes' theorem.

    :param prior: Prior probability of the hypothesis (double-headed coin)
    :param likelihood: Likelihood of the evidence given the hypothesis
    :param evidence: Probability of the evidence under all hypotheses
    :return: Posterior probability of the hypothesis
    """
    posterior = (likelihood * prior) / evidence
    return posterior


# likelihood of getting 7 heads in a row with a double-headed coin is 1
likelihood_double_headed = 1

# total probability of getting 7 heads in a row (evidence)
evidence = (likelihood_double_headed * prior_double_headed) + (probability_heads_fair_coin * (1 - prior_double_headed))

# Calculate posterior probability
posterior_double_headed = bayes(prior_double_headed, likelihood_double_headed, evidence)

print(f"The probability that the chosen coin is double-headed given 7 heads in a row is: {posterior_double_headed:.4f} "
      f"or {posterior_double_headed*100:.1f}%\n")
