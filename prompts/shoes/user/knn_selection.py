f"""Here are some previously generated patterns with some examples where it predicted correcly what color of shoe the customer bought.
{knn_info_prompt}
New scenario: {appearance} is buying a pair of shoes, the shoes should be which color?
Look at the new customer and compare this scenario with the set of examples associated with each provided pattern. 
Find the set of examples that is the most similar to the new scenario, pick and repeat the pattern associated with that set of examples.
Please give your final answer in the following format:
Reasoning for choosing pattern: reason,
Chosen pattern: pattern <number>.
"""