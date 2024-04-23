from abc import ABC, abstractmethod
import os
import re

code_repo_path = os.environ.get("CODE_REPO_PATH")

if code_repo_path:
    print(f"Code repo path: {code_repo_path}")
else:
    print("Environment variable not set.")


class Task(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def extract_label(self, text):
        pass



class Shoe(Task):
    def __init__(self):
        self.task = 'shoe'
        self.label_classes = ['white', 'red', 'orange', 'green', 'blue', 'black']
        self.train_data_path =  f'{code_repo_path}/data/shoe_rec_1100.pkl'
        self.eval_data_path = None # because we use train_data_path to do the train/test split

    def extract_label(self, text):
        if text == None:
            return 'other'
            
        """
        # only keep the part after "label:"
        text = text.lower()
        if "label:" in text:
            text = text[text.index("label:") + len("label:"):]

        # only keep the part after "Final answer:"
        if "final answer:" in text:
            text = text[text.index("final answer:") + len("final answer:"):]
            # keep the 10 characters after "final answer:"
            text = text[:10]

        # remove the trailing period
        if '.' == text[-1]:
            text = text[:-1]
        text = text.lower()
        """

        pattern = r"final answer:\s+(white|red|orange|green|blue|black)"

        match = re.search(pattern, text.lower())
        if match:
            answer = match.group(1)
            if answer in ['white', 'red', 'orange', 'green', 'blue', 'black']:
                return answer
            else:
                return "other"               
            
        return 'other'

        """
        for color in ['white', 'red', 'orange', 'green', 'blue', 'black']:
            if color in text:
                return color

        return 'other'
        """


class HotelReviews(Task):
    def __init__(self):
        self.task = 'hotel_reviews'

        # The order matters! preceding word should not be substrings of following words
        self.label_classes = ['deceptive', 'truthful']

        self.train_data_path =  f'{code_repo_path}/data/hotel_reviews_train.jsonl'
        self.val_data_path =  f'{code_repo_path}/data/hotel_reviews_val.jsonl'
        self.test_data_path =  f'{code_repo_path}/data/hotel_reviews_test.jsonl'
        self.ood_test_data_path = f'{code_repo_path}/data'

    def extract_label(self, text):
        """
        This seems old, I'm commenting this out for now (Haokun)
        """
        if text == None:
            return 'other'
        
        # only keep the part after "Final answer:"
        text = text.lower()
        '''
        if "final answer:" in text:
            text = text[text.index("final answer:") + len("final answer:"):]
            
        

        if "label:" in text:
            # only keep the part after "label:"
            text = text[text.index("label:") + len("label:"):]
        '''
        
        pattern = r"final answer:\s+(truthful|deceptive|other)"

        match = re.search(pattern, text.lower())
        if match:
            answer = match.group(1)
            if answer == "truthful":
                return "truthful"
            elif answer == "deceptive":
                return "deceptive"
            else:
                return "other"               
            
        return 'other'


class HeadlineBinary(Task):
    def __init__(self):
        self.task = 'headline_binary'
        self.label_classes = ['headline 1', 'headline 2']
        self.train_data_path =  f'{code_repo_path}/data/headline_binary_training_dataset.csv'
        self.test_data_path =  f'{code_repo_path}/data/headline_binary_test_dataset.csv'
        self.val_data_path =  f'{code_repo_path}/data/headline_binary_validation_dataset.csv'

    def extract_label(self, text):
        if text == None:
            return 'other'
        text = text.lower()
        pattern = r"answer:\s+(headline 1|headline 2|other)"
        match = re.search(pattern, text.lower())
        '''
        if "Answer:" in text:
            text = text[text.index("Answer:") + len("Answer:"):]
        for x in self.label_classes:
            if x.lower() in text.lower():
                return x
        '''
        if match:
            answer = match.group(1)
            if answer == "headline 1":
                return "headline 1"
            elif answer == "headline 2":
                return "headline 2"
            else:
                return "other"               

        return 'other'
    

class Retweet(Task):
    def __init__(self):
        self.task = 'retweet'
        self.label_classes = ['first', 'second']
        self.train_data_path =  f'{code_repo_path}/data/retweet_train.csv'
        self.val_data_path =  f'{code_repo_path}/data/retweet_val.csv'
        self.test_data_path =  f'{code_repo_path}/data/retweet_test.csv'


    def extract_label(self, text):
        """
        `text` follows the format "the <label> tweet got more retweets"
        """
        if text == None:
            return 'other'
        text = text.lower()
        import re
        pattern = r"answer: the (\w+) tweet"
        match = re.search(pattern, text)
        if match:
            return match.group(1)
        else:
            return 'other'


TASKS = {
    'shoe': Shoe,
    'hotel_reviews': HotelReviews, 
    'headline_binary': HeadlineBinary,
    'retweet': Retweet,
}
