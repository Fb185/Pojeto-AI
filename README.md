
# Spam filter


This is a Python program that uses the Naive Bayes algorithm to create a spam filter. Given a dataset of labeled emails, the program can train a model to classify new emails as spam or non-spam (also known as "ham").

## Dependencies
The program uses the following libraries:

    csv: for reading and parsing data from CSV files
    math: for performing logarithmic calculations

## Data

The program expects the training and test data to be in CSV format, with each row containing an email label (either `spam` or `ham`) and the email's content.

## Training

The `train` function is responsible for training the spam filter model. It takes in the file path for the training data (`X`) and a tuple containing validation documents and labels (validation_data).

The function reads the training data from the CSV file, storing the email labels and contents in separate lists. It then creates a dictionary `D` of all the unique words in the training emails and calculates `n`, the size of the dictionary. `n` is used as a feature in the Naive Bayes algorithm.

The function also calculates the total number of emails in the training set (`m`) and the number of ham and spam emails (`mham` and `mspam`, respectively).

A global variable `b` is initialized using the equation `b = log(c) + log(mham) - log(mspam)`, where `c` is a small positive constant.

The program initializes a matrix `p` with `p[0][j]` representing the probability of word `j` in `D` appearing in a spam email, and `p[1][j]` representing the probability of word `j` appearing in a ham email. The matrix is initialized with all values equal to `c`.

The function then counts the occurrence of each word in the emails, using these counts to update the values in `p` and the total number of words in spam and ham emails (`wspam` and `wham`, respectively).

Finally, the function normalizes the values in `p` by dividing them by `wspam + 2` and `wham + 2`, respectively, to yield the final word probabilities.
## Classification
The `classify` function is responsible for classifying a new email as spam or ham based on the trained model. It takes in the email content (`x`), the global variable `b`, and the matrix `p` as input.

The function initializes a score threshold `t` to `-b`. It then loops through each word in the dictionary `D` and updates the score threshold by adding the product of the word's count in the email and the logarithmic difference of its probabilities in spam and ham emails.

Finally, the function classifies the email as spam if `t` is greater than 0, or as ham otherwise.
## Evaluation
The `evaluate` function is used to evaluate the performance of the spam filter on a test dataset. It takes in the file path for the test data (`test_file`), the global variable `b`, and the matrix `p` as input.

The function reads the test data from the CSV file, storing the email labels and contents in separate lists. It then classifies each email using the `classify` function and compares the predicted label to the actual label. The function counts the number of correctly classified emails andreturns the precision of the spam filter, calculated as the number of correctly classified emails divided by the total number of emails in the test set.
