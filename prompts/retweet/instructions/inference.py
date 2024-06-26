f"""You are a social media expert.
Given a pair of tweets, you are asked to predict which tweet will be retweeted more.
Please note that the paired tweets are about the same content and are posted by the same user, so you should focus on the wording difference between the two tweets.
From past experiences, you learned a pattern.
Now, at each time, you should apply a learned pattern to a pair of tweets and determine which one will get more retweets. 
The answer for the higher retweets should be of the form "the _ tweet" where _ is either first or second. 
Please give your final answer in the format of {{Final answer: the _ tweet}}
"""