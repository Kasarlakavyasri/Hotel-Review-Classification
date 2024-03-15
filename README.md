**Aim**
* The aim is to work with Naive Bayes parameters. We train the dataset and then utilize those parameters to determine whether given reviews are legitimate or not.

**Review**
* We are provided with two text files, deceptive.test.txt and deceptive.train.txt, where one contains training data and the other holds test data.
* Based on observations from these files, we aim to construct and train a model for probability, ultimately predicting the legitimacy of a given statement.

***Decision Design and Approach***

**Technique Used**
Bayes Net Classifier

**Bayes Net Classifier**
* Works well for classifying data with large datasets.
* Prediction of the probability: P(C|X) where C is the class variable and X is the given feature.

**Working**
* Read the training file.
* Initialize and utilize dictionaries of lists where keys correspond to classes, labels, and objects, and values represent comments and categories.
* Utilize a dictionary to count occurrences of expressions in deceptive and truthful statements.
* Split and format the phrases, cleaning them by processing end phrases.
* Append processed phrases to the dictionary.
* Calculate the probability of a statement being truthful or deceptive.

**Loading and Processing Datasets**
* Load the training and test datasets, considering each object and sentence as a label. Traverse each token and skip if it's a word related to truthful or deceptive comments.
* Multiply the probability for a given comment as truthful if present, and repeat the process.

**References**
* https://towardsdatascience.com/beating-the-world-record-in-tetris-gb-with-genetics-algorithm-6c0b2f5ace9b
* https://www.youtube.com/watch?v=ptUXxWumxfE
* https://github.com/explosion/spaCy/discussions/10470
