#Task 1: Keyword Highlighter

# Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average".
# We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they 
# stand out.
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

keywords = ["good", "excellent", "bad", "poor", "average"]

def caps(reviews, keywords):
    for review in reviews:
        caps_keyword = review
        for keyword in keywords:
            keyword_lower = keyword.lower()
            if keyword in review.lower():
                start = review.lower().index(keyword_lower)
                end = start + len(keyword)
                original_keyword = review[start:end]
                caps_keyword = caps_keyword.replace(original_keyword, keyword.upper())
                print(caps_keyword)
caps(reviews,keywords)

#Task 2: Sentiment Tally

# Develop a function that tallies the number of positive and negative words in each review.  
# The function should return the total count of positive and negative words.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def tally(reviews, positive_words, negative_words):
   
    positive_count = 0 
    negative_count = 0

    for review in reviews:
        review_lower = review.lower()
        for positive in positive_words:
            positive_count += review_lower.count(positive)
        for negative in negative_words:
            negative_count += review_lower.count(negative)
    return positive_count, negative_count

positive_count, negative_count = tally(reviews, positive_words, negative_words)

print(f"Total amount of positive words: {positive_count}")
print(f"Total amount of negative words: {negative_count}")



#Task 3: Review Summary

# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.

def summarize_reviews(reviews, max_length=30):
    summaries = []
    for review in reviews:
        if len(review) <= max_length:
            summaries.append(review)
        else:
            summary = review[:max_length]
            if summary[-1] != ' ' and review[max_length] != ' ':
                last_space = summary.rfind(' ')
                if last_space != -1:
                    summary = summary[:last_space]
            summaries.append(summary + "…")
    return summaries

summaries = summarize_reviews(reviews)
for summary in summaries:
    print(summary)

# Example: "This product is really good. I'm...",