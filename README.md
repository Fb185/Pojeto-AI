
# Documentation

## Introduction

This code is a Naive Bayes classifier that can be used to classify text documents as either 'spam' or 'ham' (not spam). The classifier is trained on a dataset of labeled documents and then used to predict the labels of a separate test dataset. The classifier uses a Bernoulli model, which means that it only considers whether a given word appears in a document or not, rather than considering the number of times the word appears.

## Dependencies

This code requires the following Python libraries:

- `csv`: for reading data from CSV files
- `math`: for mathematical operations such as logarithms

## Code Structure

The code consists of two main functions:

1. `train(X)`: This function is used to train the classifier on a given dataset of labeled documents. It takes in the filepath of the training dataset as an input (`X`) and returns the bias term `b` of the classifier.

2. `classify(test_file, b)`: This function takes in the filepath of a test dataset (`test_file`) and the bias term `b` of the classifier, and returns the precision of the classifier on the test dataset.

## Function Details

### `train(X)`

This function performs the following steps:

1. Reads the training dataset from the file at filepath `X` and stores the documents and labels in separate lists.

2. Computes the dictionary `D` of all the unique words in the training documents. The size of the dictionary (`n`) is also stored.

3. Computes the number of documents in the training dataset (`m`) and the number of 'ham' and 'spam' documents (`mham` and `mspam` respectively).

4. Initializes the bias term `b` as `b = log(c) + log(mham) - log(mspam)`, where `c` is a hyperparameter (set to 0.1 in this code).

5. Initializes the word probabilities `p` as a 2D list, where `p[0][j]` is the probability that word `j` in the dictionary appears in a 'spam' document, and `p[1][j]` is the probability that word `j` appears in a 'ham' document. `p[0][j]` and `p[1][j]` are initialized to 0 for all `j`. The variables `wspam` and `wham` are also initialized to `n` each, which will be used to store the total number of words in 'spam' and 'ham' documents respectively.

6. Loops through the training documents and counts the occurrence of each word in the dictionary. For each 'spam' document, the count for each word is added to `p[0][j]` and to `wspam`. For each 'ham' document, the count for each word is added to `p[1][j]` and to `wham`.

7. Normalizes the word counts to yield word probabilities by dividing each count by the total number of words in the corresponding class (`wspam` or `wham`) and adding a small positive value (1 in this case) to the result to prevent a math domain error.

    Returns the bias term b.

### `classify(test_file, b)`

This function performs the following steps:

    Reads the test dataset from the file at filepath test_file and stores the documents and labels in separate lists.

    Loops through the test documents and computes the score for each document using the following formula:

`score_threshold = -b
for j in range(n):
  word = list(dictionary)[j]
  score_threshold += x.count(word) * (log(p[0][j]) - log(p[1][j]))`

This formula calculates the sum of the log probabilities that each word in the dictionary appears in a 'spam' document, minus the sum of the log probabilities that each word appears in a 'ham' document.

    If the score is greater than 0, the document is classified as 'spam'; otherwise, it is classified as 'ham'. The predicted label is added to a list of predictions.

    Calculates the precision of the classifier by comparing the predicted labels to the true labels and dividing the number of correct predictions by the total number of predictions.

    Returns the precision.

Example

The code includes an example of using the classifier to train on the file ./data/shortdataset.csv and test on the file ./data/testSet.csv. The bias term b is computed using the train() function and then passed to the classify() function along with the test filepath. The precision of the classifier on the test dataset is then printed.
