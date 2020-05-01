import string
import numpy as np
import math
# This maps key will be a word in the vocab. the Value will be a list with first element being
# number of times it occured in ham and second will be occurences in spam
word_map = {}
# Used to remove punctuation and digits from strings
translator = str.maketrans('', '', string.punctuation)
digits_remove = str.maketrans('', '', string.digits)
stop_list = []
ham_total = 0
spam_total = 0

def build_vocab(train_file, stop_words):
    #open the test file for reading
    global spam_total
    global ham_total
    stop_words = open(stop_words, "r")
    for line in stop_words:
        line = line.strip()
        stop_list.append(line)

    train_file = open(train_file, "r", encoding = 'unicode-escape')
    for line in train_file:
        # Remove punctuation and make lowercase
        line = line.translate(translator)
        # Get type of mail (spam or ham)
        mail_type = line[0]
        if mail_type == "0":
            ham_total += 1
        elif mail_type == "1":
            spam_total += 1
        # Remove the digits them split them into seperate words
        line = line.lower().strip().split()

        # Make the list a set to remove duplicates
        line_set = set(line)

        # Remove stop words from the list
        line_set = line_set - set(stop_list)

        # Iterate through each word in the line
        for word in line_set:
            # If the word is not found in the dictionary yet, add it and
            # set its list components
            if word not in word_map.keys():
                temp_list = []
                if mail_type == "0":
                    temp_list.append(1)
                    temp_list.append(0)

                elif mail_type == "1":
                    temp_list.append(0)
                    temp_list.append(1)
                word_map.update({word : temp_list})
            # If the word already exist in dictionary, update the values
            else:
                value = word_map.get(word)
                if mail_type == "0":
                    value[0] += 1
                elif mail_type == "1":
                    value[1] += 1
    # Need to smooth list with probabilities
    k = 1
    for each_key in word_map:
        ham_count = word_map[each_key][0]
        new_value_ham = (k + ham_count) / (2*k + ham_total)
        new_value_ham = round(new_value_ham, 3)
        spam_count = word_map[each_key][1]
        new_value_spam = (k + spam_count) / (2*k + spam_total)
        new_value_spam = round(new_value_spam, 3)
        temp_list = []
        temp_list.append(new_value_ham)
        temp_list.append(new_value_spam)
        word_map.update({each_key : temp_list})


def spam_filter(test_file, stop_words):
    accuracy = 0
    TPTot = 0
    TNTot = 0
    FPTot = 0
    FNTot = 0
    test_ham = 0
    test_spam = 0
    test_file = open(test_file, "r", encoding = 'unicode-escape')

    for line in  test_file:

        # Remove punctuation and make lowercase
        line = line.translate(translator)
        # Get type of mail (spam or ham)
        mail_type = line[0]
        # Remove the digits them split them into seperate words
        line = line.lower().strip().split()
        # Make the list a set to remove duplicates
        line_set = set(line[1:])
        # Remove stop words from the list
        line_set = line_set - set(stop_list)

        #spam
        p_spam = 1
        for each_value in word_map:
            if each_value in line_set:
                p_spam = p_spam + np.log(word_map[each_value][1])
            else:
                p_spam = p_spam + np.log(1 - word_map[each_value][1])

        #ham
        p_ham = 1
        for each_value in word_map:
            if each_value in line_set:
                p_ham = p_ham + math.log(word_map[each_value][0])
            else:
                p_ham = p_ham + math.log(1 - word_map[each_value][0])

        total = spam_total + ham_total
        pofs = spam_total/total
        pofh = ham_total/total

        p_ham = math.exp(p_ham)
        p_spam = math.exp(p_spam)
        e = (np.log(p_ham * pofh) - np.log(p_spam * pofs))
        e = math.exp(e)
        p = 1 / ( 1 + e)

        if (mail_type == "0") & (p < 0.5):
            TPTot += 1
            test_ham += 1
        elif (mail_type == "1") & (p >= 0.5):
            TNTot += 1
            test_spam += 1
        elif (mail_type == "0") & (p >= 0.5):
            FPTot += 1
            test_ham += 1
        elif (mail_type == "1") & (p < 0.5):
            FNTot += 1
            test_spam += 1

    accuracy = (TPTot + TNTot) / (TPTot + TNTot + FPTot + FNTot)
    precision = (TPTot) / (TPTot + FPTot)
    recall = (TPTot) / (TPTot + FNTot)
    f1 = 2 * (1 / ((1/ precision) + (1/recall)))
    print('Accuracy: ' + str(accuracy))
    print('Precision: ' + str(precision))
    print('Recall: ' + str(recall))
    print('F1 Score: ' + str(f1))
    print('Total Spam messages in Test Set: ' + str(test_spam))
    print('Total Ham messages in Test Set: ' + str(test_ham))


def main():
    train_set = input("Please enter the training set file: ")
    stop_words = input("Please enter the stop words file: ")
    build_vocab(train_set, stop_words)
    print("Voacabulary has been built from the training file you provided.")
    test_set = input("Please enter the test set file: ")
    print("Your results for the test file you entered: ")
    spam_filter(test_set, stop_words)


if __name__ == "__main__":
    main()
