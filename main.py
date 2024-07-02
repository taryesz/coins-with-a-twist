print("\n"
      "--- Problem Description | Credit: HarvardX STAT110x on edX ---\n\n"
      "A hat contains 100 coins, where 99 are fair but one is double-headed (always landing Heads).\n"
      "A coin is chosen uniformly at random. The chosen coin is flipped 7 times, and it lands Heads all 7 times.\n"
      "Given this information, what is the probability that the chosen coin is double-headed?\n"
      "(Of course, another approach here would be to look at both sides of the coin—but this is a metaphorical coin).\n"
      "\n--- End Problem Description ---\n")

# Constants
TOTAL_COINS = 100
DOUBLE_HEADED_COINS = 1
COIN_FLIPS = 7

print("--- SOLUTION: ---\n")

# prior probability that the chosen coin is double-headed
prior_double_headed = DOUBLE_HEADED_COINS / TOTAL_COINS
print("1. -- Probability of getting a double-headed coin --\n"
      f"Sample Space consists of {TOTAL_COINS} outcomes, since that's how many coins we have and can choose any of them."
      f"\n"
      f"There is {DOUBLE_HEADED_COINS} double-headed coin, so we are interested in {DOUBLE_HEADED_COINS} out of "
      f"{TOTAL_COINS} coins which is {DOUBLE_HEADED_COINS / TOTAL_COINS} "
      f"(or {(DOUBLE_HEADED_COINS / TOTAL_COINS) * 100:.0f}%).\n")

# probability of getting 7 heads in a row with a fair coin
probability_heads_fair_coin = 1 / (2 ** COIN_FLIPS)
print(f"2. -- Probability of getting {COIN_FLIPS} Heads in a row given a coin is normal --\n"
      f"We have {COIN_FLIPS} spots for each coinflip.\n"
      f"There are 2 possible outcomes of each coinflip: Heads or Tails.\n"
      f"(Here we do not consider that there exists a double-head coin).\n"
      f"So, the number of possible combinations of coin flips: 2 * 2 * ... * 2 ({COIN_FLIPS} times) or 2^{COIN_FLIPS} "
      f"(or {2 ** COIN_FLIPS}).\n"
      f"The above number becomes our Sample Space, and there is only one possible string of 7 'H's in a row, so "
      f"1 / 2^{COIN_FLIPS} or {1 / (2 ** COIN_FLIPS)}, which is {(1 / (2 ** COIN_FLIPS)) * 100:.2f}%.\n")


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
print("3. -- Likelihood or Probability of getting 7 Heads in a row given a coin is double-headed --\n"
      "The probability of generating a 7-char string of 'H' by flipping a double-headed coin is always 100%.\n")

# total probability of getting 7 heads in a row (evidence)
evidence = (likelihood_double_headed * prior_double_headed) + (probability_heads_fair_coin * (1 - prior_double_headed))
print("4. -- Evidence --\n"
      "Using above parts, use the formula to get the probability of getting 7 Heads in a row.\n")

# calculate posterior probability
posterior_double_headed = bayes(prior_double_headed, likelihood_double_headed, evidence)


print(f"5. -- Update the prior using evidence --\n"
      f"The probability that the chosen coin is double-headed given 7 heads in a row is: {posterior_double_headed:.4f} "
      f"or {posterior_double_headed*100:.1f}%\n")

print("--- END SOLUTION ---\n")
