f"""You're a helpful assistant. Your task is given as follows:
Given a set of observations, we want to generate hypotheses that are useful for predicting the color of the shoes given the appearance of the person. 
Please be concise and keep the hypotheses to be one-sentence long.  
Please generate them in the format of 
{{1. [hypothesis]. 
2. [hypothesis].
... 
{num_hypotheses}. [hypothesis].}}
Only propose {num_hypotheses} possible hypotheses in total.
Please make the hypotheses general and applicable to new examples.
"""
