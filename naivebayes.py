
import csv
import math
from collections import defaultdict

def word_counts(email):
    """Returns a dictionary of word counts for the given email"""
    counts = defaultdict(int)
    for word in email.split():
        counts[word] += 1
    return counts

def train_naive_bayes(emails):
    """Trains a multinomial naive Bayes classifier on the given emails"""
    # Count the number of spam and ham emails
    num_spam = sum(1 for label, _ in emails if label == "spam")
    num_ham = len(emails) - num_spam

    # Calculate the prior probabilities of the two classes
    prior_spam = num_spam / len(emails)
    prior_ham = num_ham / len(emails)

    # Count the number of times each word appears in spam and ham emails
    word_counts_spam = defaultdict(int)
    word_counts_ham = defaultdict(int)
    for label, counts in emails:
        if label == "spam":
            for word, count in counts.items():
                word_counts_spam[word] += count
        else:
            for word, count in counts.items():
                word_counts_ham[word] += count

    # Calculate the conditional probabilities for each word in the vocabulary
    vocabulary = set(word for _, counts in emails for word in counts)
    cond_probs_spam = defaultdict(lambda: 1 / (num_spam + 2))
    cond_probs_ham = defaultdict(lambda: 1 / (num_ham + 2))
    for word in vocabulary:
        cond_probs_spam[word] = (word_counts_spam[word] + 1) / (num_spam + 2)
        cond_probs_ham[word] = (word_counts_ham[word] + 1) / (num_ham + 2)

    return prior_spam, prior_ham, cond_probs_spam, cond_probs_ham

def classify(prior_spam, prior_ham, cond_probs_spam, cond_probs_ham, email):
    """Classifies the given email as spam or ham using the trained naive Bayes classifier"""
    counts = word_counts(email)

    # Calculate the probability of the email being spam or ham
    prob_spam = math.log(prior_spam)
    prob_ham = math.log(prior_ham)
    for word, count in counts.items():
        prob_spam += count * math.log(cond_probs_spam[word])
        prob_ham += count * math.log(cond_probs_ham[word])

    # Return the most likely label
    if prob_spam > prob_ham:
        return "spam"
    else:
        return "ham"

if __name__ == "__main__":
    emails = []
    with open("./data/spamHamDataset.csv", "r") as f:
        # Read the emails from the CSV file
        reader = csv.reader(f)
        for row in reader:
            label, email = row
            emails.append((label, word_counts(email)))
    prior_spam, prior_ham, cond_probs_spam, cond_probs_ham = train_naive_bayes(emails)

    test_emails = [
        ("spam", "Free viagra now!"),
        ("ham", "Hi, how are you?"),
        ("spam", "Win a free vacation!"),
        ("spam", "Your account has been compromised"),
        ("ham", "New updates are available for your software"),
        ("spam", "You have been selected for a special offer"),
        ("spam", "Get the best deals on the latest gadgets"),
        ("spam", "Don't miss out on this incredible opportunity!"),
        ("spam", "Your account has been suspended"),
        ("spam", "You have won a million dollars!"),
        ("spam", "Earn money from home with this simple opportunity"),
        ("spam", "Get a free quote for home insurance"),
        ("spam", "You have been selected to receive a free gift"),
        ("spam", "You are eligible for a free credit report"),
        ("spam", "Free trial for weight loss pills"),
        ("spam", "Double your money with this amazing investment opportunity"),
        ("spam", "Get rich quick with this simple system"),
        ("spam", "Work from home and make a fortune"),
        ("spam", "Learn how to make money online"),
        ("spam", "Find the perfect match with our dating service"),
        ("spam", "Get a loan with no credit check"),
        ("spam", "Sign up for this amazing offer today"),
        ("spam", "Boost your energy with these natural supplements"),
        ("spam", "Satisfy your partner with this proven solution"),
        ("ham", "Your purchase is ready for shipment"),
        ("spam", "Save up to 50% on your next vacation"),
        ("spam", "Special promotion for our valued customers"),
        ("spam", "You have been chosen for a discounted rate"),
        ("spam", "Don't miss out on this limited time offer"),
        ("spam", "Upgrade your home with these amazing deals"),
    ]
    
# Predict the labels for the test emails
    y_pred = [classify(prior_spam, prior_ham, cond_probs_spam, cond_probs_ham, email) for _, email in test_emails]

# Get the true labels for the test emails
    y_true = [label for label, _ in test_emails]

# Calculate the number of correct predictions
    num_correct = sum(1 for y1, y2 in zip(y_true, y_pred) if y1 == y2)

# Calculate the accuracy as a percentage
    accuracy = num_correct / len(test_emails) * 100
    print("Accuracy: {:.2f}%".format(accuracy))
    for email, label in zip(test_emails, y_pred):
        print(email[1], ":", label)

