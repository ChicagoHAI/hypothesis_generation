f"""You're a professional hotel review analyst.
Given a set of hotel reviews, we want to generate hypotheses that are useful for predicting whether a review is truthful or deceptive. In other words, we want to know whether the review is written by a someone who actually lived in the hotel.

Using the given examples, please propose {num_hypotheses} possible hypothesis pairs.
These hypotheses should identify specific patterns that occur across the provided reviews.

Each hypothesis should contain a pair of the following:
a. A hypothesis about what makes reviews more likely to be truthful
b. The opposite hypothesis about what makes reviews more likely to be deceptive 

Generate them in the format of 1. [hypothesis], 2. [hypothesis], ... {num_hypotheses}. [hypothesis].
The hypotheses should analyze what kind of reviews are likely to be truthful or deceptive.
"""