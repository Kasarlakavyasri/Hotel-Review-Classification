# SeekTruth.py : Classify text objects into two categories
#
# Vishal Dung (vidung) , Kavya Sri Kasarla (kkasarla), Prathyusha Reddy Thumma (pthumma)
#
# Based on skeleton code by D. Crandall, October 2021
#

import sys

def load_file(filename):
    objects=[]
    labels=[]
    with open(filename, "r") as f:
        for sentence in f:
            parsed = sentence.strip().split(' ',1)
            labels.append(parsed[0] if len(parsed)>0 else "")
            objects.append(parsed[1] if len(parsed)>1 else "")

    return {"objects": objects, "labels": labels, "classes": list(set(labels))}

# classifier : Train and apply a bayes net classifier
#
# This function should take a train_data dictionary that has three entries:
#        train_data["objects"] is a list of strings corresponding to reviews
#        train_data["labels"] is a list of strings corresponding to ground truth labels for each review
#        train_data["classes"] is the list of possible class names (always two)
#
# and a test_data dictionary that has objects and classes entries in the same format as above. It
# should return a list of the same length as test_data["objects"], where the i-th element of the outcome
# list is the estimated classlabel for test_data["objects"][i]
#
# Do not change the return type or parameters of this function!
#
def classifier(train_data, test_data):
    expression_add = {}  # To get a dictionary of the number of times an expression occurs in the deceptive and truthful sentences.
    outcome = []  # Outcome to store the final results.
    end_phrase = [ "YOU", "HE", "HIM", "HIS", "JUST", "SHOULD","SHOULDN'T", "NOW", "!", "ME", "MY", "MYSELF", "WE", "OUR", "OURS", "OURSELVES","HIMSELF", "SHE", "HER", "HERS", "HERSELF","YOUR", "YOURS", "YOURSELF",  "WHAT", "WHICH", "WHO", "WHOM", "THIS", "THAT", "THESE", "THOSE", "IT", "ITS", "ITSELF", "THEY", "THEM","ARE", "WAS", "WERE", "BE", "BEEN", "BEING", "HAVE", "WHAT", "WHICH", "WHO",  "THIS", "THAT", "THESE", "THOSE", "AM", "IS", "ARE", "WAS", "WERE", "HAVE", "HAS", "HAD", "UNTIL", "WHILE", "OF", "AT", "BY", "FOR", "WITH", "ABOUT", "AGAINST", "HAVING",  "IF", "OR", "BECAUSE", "AS", "DO", "DOES", "DID", "BETWEEN", "INTO", "THROUGH", "DURING", "BEFORE",  "DOING", "A", "AN", "IN", "OUT", "ON", "OFF", "OVER", "UNDER", "AGAIN", "FURTHER", "THE", "AND", "BUT", "AFTER", "ABOVE", "BELOW", "TO", "FROM", "SO", "THAN", "TOO", "VERY", "CAN","CAN'T", "WILL","WON'T", "UP", "DOWN", "THEN", "ONCE", "HERE", "THERE", "WHEN", "WHERE",     ]
    i = 0
    while i < (len(train_data["objects"])):
        sentence = train_data["objects"][i]  # Dividing sentences
        phrase = sentence.strip().upper()  # Getting each phrase formatted as needed 
        phrase = phrase.split()       # Splitting the phrases
        clean_phrase = [expression for expression in phrase if expression not in end_phrase] # Getting the clean_phrase by processing the end_phrase     
        for expression in clean_phrase:
            if expression not in expression_add:
                expression_add[expression] = {}  # appending the expression to the dictionary
            
            if train_data['labels'][i] == 'deceptive':
                if 'deceptive' not in expression_add[expression]:
                    expression_add[expression]['deceptive'] = 0  # expression_add[expression]['deceptive'] = 0 if the expression is not deceptive
                expression_add[expression]["deceptive"] += 1  # increment

            elif train_data['labels'][i] == 'truthful':  # checking the occurrence each expression in truthful
                if 'truthful' not in expression_add[expression]:
                    expression_add[expression]['truthful'] = 0  # expression_add[expression]['truthful'] = 0 if the expression is not truthful  
                expression_add[expression]['truthful'] += 1  # increment 
        i = i+1
    j=0
    while j < (len(test_data['objects'])):      
        r = 1
        sentence = test_data['objects'][j]
        for expression in sentence.strip().upper().split():
            if expression not in expression_add:
                continue
            else:
                if 'truthful' not in expression_add[expression] or 'deceptive' not in expression_add[expression]:  # continue if both of them are not present together 
                    continue  
                else:
                    chance_true = expression_add[expression]['truthful'] / (expression_add[expression]['truthful'] + expression_add[expression]['deceptive'])   # Here we calculate how much the chance is to get truthful  
                    chance_false = expression_add[expression]['deceptive'] / (expression_add[expression]['truthful'] + expression_add[expression]['deceptive']) # Here we calculate how much the chance is to get deceptive 
                    r *= chance_true / (chance_false)  # calculate final r by dividing chance_true and chance_false 
        if (r > 1):  
            outcome.append('truthful')  # append truthful if r > 1
        else:  
            outcome.append('deceptive') # append deceptive if r < 1
        j = j+1
    return outcome
                
            
if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Usage: classify.py train_file.txt test_file.txt")

    (_, train_file, test_file) = sys.argv
    # Load in the training and test datasets. The file format is simple: one object
    # per sentence, the first expression one the sentence is the label.
    train_data = load_file(train_file)
    test_data = load_file(test_file)

    
    
    if(sorted(train_data["classes"]) != sorted(test_data["classes"]) or len(test_data["classes"]) != 2):
        raise Exception("Number of classes should be 2, and must be the same in test and training data")

    # make a copy of the test data without the correct labels, so the classifier can't cheat!
    test_data_sanitized = {"objects": test_data["objects"],"labels":[], "classes": test_data["classes"]}
 

    results= classifier(train_data, test_data_sanitized)

    # calculate accuracy
    correct_ct = sum([ (results[i] == test_data["labels"][i]) for i in range(0, len(test_data["labels"])) ])
    print("Classification accuracy = %5.2f%%" % (100.0 * correct_ct / len(test_data["labels"])))
