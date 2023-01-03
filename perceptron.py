import csv
import collections

def main():

    with open("data/spamHamDataset.csv", "r" ,encoding='cp850') as csv_file:
        reader = csv.reader(csv_file)
        train = []
        for email in reader:
            email = clean_up(email)
            train.append(email)

    with open("data/testSet.csv", "r" ,encoding='cp850') as csv_file:
        reader = csv.reader(csv_file)
        test = []
        for email in reader:
            email = clean_up(email)
            test.append(email)

    with open("data/validationSet.csv", "r" ,encoding='cp850') as csv_file:
        reader = csv.reader(csv_file)
        validation = []
        for email in reader:
            email = clean_up(email)
            validation.append(email)

        input = transform(train)
        trainedTeta, tetaZero = perceptron(input)
        testPerceptron(validation, trainedTeta, tetaZero)

def clean_up(email):
    chars = [":", ";", "-", "~", "^", "´", "`", "«", "»", "=", "?", "!", "/", "//", "|", "+", "*", "&", "%", "€", "£", "§", "{", "}", "[", "]", "(", ")", "º", "ª", "<", ">", "#",".", ","]
    for c in chars:
        email[1] = email[1].replace(c, ' ').lower()
    email[1] = " ".join(email[1].split())    
    return email


def transform(emails):
    for email in emails:

        if email[0] == 'spam':
            email[0] = -1
        if email[0] == 'ham':
            email[0] = 1

        words = email[1].split(" ")
        frequency = collections.Counter(words)
        email[1] = frequency

    return emails


def perceptron(emails, T = 20):
    teta = create_teta(emails)
    tetaZero = 0
    for _ in range(T):
        for email in emails:
            if email[0] * classify(teta, email[1], tetaZero) <= 0:
                counters = email[1].items()
                for word, count in counters: 
                    teta[word] += email[0] * count
                tetaZero += email[0] ## ver se posso mudar isto
    return teta, tetaZero


def create_teta(emails): 
    teta = {}
    for email in emails:
        counters = email[1].items()
        for word in counters:
            if word[0] not in teta:
                teta[word[0]] = 0
    return teta

def classify(teta, counters, tetaZero):
    sum= 0
    items = counters.items()
    for word, count in items:
        if word in teta:
            sum+= teta[word] * count
    return sum+ tetaZero

def testPerceptron(validation, trainedTeta, tetaZero):
    validation = transform(validation)

    right = 0
    wrong = 0

    for email in validation:
        classifier = classify(trainedTeta, email[1], tetaZero)
        if classifier >= 0:
            lable = 1
        else:
            lable = -1
        if lable == email[0]:
            right +=1
        else:
            wrong +=1
    print(right)
    print(wrong)
    print(right / (right+wrong))



if __name__ == "__main__":
    main()

#mudar o codigo aka portugues ingles e diferenciar do nazi e do outro x
#adicionar comments
#adicionar metricas
#para o percetrao , saber a cena do 70 15 15 ou 70 30 x
#train list , test list , validation list x
#pq o test list é para o naive bayes calcular o c x
