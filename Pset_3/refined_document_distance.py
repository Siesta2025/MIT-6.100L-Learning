import string
import math
from collections import Counter # Use collection.Counter to help us simplify the code!

# -----------
# Basic Tools
# -----------

def load_file(filename):
    with open(filename,'r') as f:
        text=f.read().strip().lower()
    return text.translate(str.maketrans('','',string.punctuation)) # Efficient way to remove punctuations

def text_to_list(input_text):
    return input_text.split()

# ----------
# Core Logic
# ----------

def get_frequencies(input_iterable):
    return dict(Counter(input_iterable)) # Cast Counter to a dictionary, pay attention that in Python the type name is just 'dict'

def get_letter_frequencies(word):
    return get_frequencies(word)

def calculate_similarity_score(freq_dict1,freq_dict2):
    all_words=set(freq_dict1)|set(freq_dict2) # Get the union of two sets

    diff=sum(abs(freq_dict1.get(w,0)-freq_dict2.get(w,0)) for w in all_words) 
    # .get(key,default) is a convenient way to grab the dict value without having to check if the key exists 
    # Generator expression
    total=sum(freq_dict1.get(w,0)+freq_dict2.get(w,0) for w in all_words)

    if total ==0: return 1.0 # Edge case
    
    return round(1-(diff/total),2)

def get_most_frequent_words(freq_dict1,freq_dict2):
    combined=Counter(freq_dict1)+Counter(freq_dict2) # Great property: additivity

    if not combined: # Check if it's empty(suitable for all containers)
        return []
    max_freq=max(combined.values())

    result=[word for word, count in combined.items() if count==max_freq] # Counter is essentially a dict
    return sorted(result)

# -----------
# Calculation
# -----------

def get_tf(file_path):
    words=text_to_list(load_file(file_path))
    total_words=len(words)
    counts=Counter(words)
    return {word: count/total_words for word, count in counts.items()} # Dict comprehension

def get_idf(file_paths):
    docs_vocab=[set(text_to_list(load_file(f))) for f in file_paths] # List comprehension
    total_docs=len(file_paths)

    all_unique_words=set().union(*docs_vocab) # .union() allow us to get the union of more than two sets, and * means unpacking the list (because .union() expects sets as parameters)

    idf={}
    for word in all_unique_words:
        num_docs_with_word=sum(1 for doc in docs_vocab if word in doc)
        idf[word]=math.log10(total_docs/num_docs_with_word)
    
    return idf

def get_tfidf(tf_file_path, idf_file_paths):
    tf=get_tf(tf_file_path)
    idf=get_idf(idf_file_paths)
    result=[(w,tf[w]*idf[w]) for w in tf if w in idf]
    return sorted(result,key=lambda x: (x[1],x[0]))
