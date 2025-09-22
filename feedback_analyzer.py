reviews = [
    "Great park with amazing views!",
    "The staff was rude and unhelpful.",
    "Loved the atmosphere, will come again.",
    "Too crowded and dirty.",
    "Affordable and family friendly.",
]
positive_words = ("great", "amazing", "loved", "friendly", "affordable")
negative_words = ("rude", "dirty", "crowded", "bad", "unhelpful")

def clean_text(text):
    text = text.lower().strip()
    
    for ch in [".", ",", "!", "?"]:
        text = text.replace(ch, "")
    
    return text

def get_word_freq(reviews):
    
    freq = {}
    for review in reviews:
        words = clean_text(review).split()
        for word in words:
            freq[word] = freq.get(word, 0) + 1

        return freq

def get_top_words(freq, n=3):
    return sorted(freq.items(), key=lambda x:x[1], reverse=True)[:n]

def analyze_sentiment(review):
    words = clean_text(review).split()
    for word in words:
        if word in positive_words:
            return "Positive"
        
        elif word in negative_words:
            return "Negative"
        
        return "Neutral"

        


def get_unique_words(reviews):
    pass 

def main():
    while True:
        print("\n--- Customer feedback Analyzer ---")
        print("1. Show all reviews")
        print("2. Show word frequency")
        print("3. Show top 3 frequent words")
        print("4. Analyze Sentiment of reviews")
        print("5. Show unique words")
        print("Exist")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        if choice == 1:
            for i, review in enumerate(reviews, 1):
                print(f"{i}. {review}")

        elif choice == 2:
            freq = get_word_freq(reviews)
            print("Word Frequency:")
            for word, count in freq.items():
                print(f"{word}: {count}")

        elif choice == 3:
            freq = get_word_freq(reviews)
            top_words = get_top_words(freq, 3)
            print("Top 3 Words:", top_words)

        elif choice == 4:
            for review in reviews:
                sentiment = analyze_sentiment(review)
                print(f"Review: {review} → {sentiment}")

        elif choice == 5:
            unique = get_unique_words(reviews)
            print("Unique Words:", unique)

        elif choice == 6:
            print("✅ Exiting program. Goodbye!")
            break

        else:
            print("❌ Invalid choice, try again.")

if  __name__ == "__main__":
    main()
