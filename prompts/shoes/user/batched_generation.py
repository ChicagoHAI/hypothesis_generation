f"""We made some observations:
{observations}
Based on the above observations, generate {num_hypotheses} hypotheses.
Please be concise and keep the hypotheses to be one-sentence long.  
Please generate them in the format of 
{{1. [hypothesis]. 
2. [hypothesis].
... 
{num_hypotheses}. [hypothesis].}}
Only propose {num_hypotheses} possible hypotheses in total.
"""
