import math
import csv
import collections

def main():

    # opens the big dataset and removes punctuation and unwanted characters
    with open("data/spamHamDataset.csv", "r" ,encoding='cp850') as csv_file:
        reader = csv.reader(csv_file)
        train = []
        for email in reader:
            email = clean_up(email)
            train.append(email)

    # opens the test dataset and removes punctuation and unwanted characters
    with open("data/testSet.csv", "r" ,encoding='cp850') as csv_file:
        reader = csv.reader(csv_file)
        test = []
        for email in reader:
            email = clean_up(email)
            test.append(email)

    # opens the validation dataset and removes punctuation and unwanted characters
    with open("data/validationSet.csv", "r" ,encoding='cp850') as csv_file:
        reader = csv.reader(csv_file)
        validation = []
        for email in reader:
            email = clean_up(email)
            validation.append(email)

        input = transform(train)
        trainedTeta, tetaZero = perceptron(input)
        testPerceptron(validation, trainedTeta, tetaZero)

# removes unwanted characters
def clean_up(email):
    chars = [":", ";", "-", "~", "^", "´", "`", "«", "»", "=", "?", "!", "/", "//", "|", "+", "*", "&", "%", "€", "£", "§", "{", "}", "[", "]", "(", ")", "º", "ª", "<", ">", "#",".", ","]
    for c in chars:
        email[1] = email[1].replace(c, ' ').lower()
    email[1] = " ".join(email[1].split())    
    return email


def transform(emails):
    for email in emails:

        #changes the labels spam and ham to -1 and 1 respectively
        if email[0] == 'spam':
            email[0] = -1
        if email[0] == 'ham':
            email[0] = 1

        # splits the email content by a blank space
        words = email[1].split(" ")

        # words = list  (i am happy happy)
        # counter =   counter({i:1, am:1, happy:2})
        # frequency is the ammount of time each word appears in that email
        frequency = collections.Counter(words)
        # email[1] is now the Counter
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
        # accessing the Counter object with the .items() function
        # line 84 assigs counters to the Counter objects
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
    tentativas = 0
    tentativasCertas = 0
    tentativasIncorretas = 0
    emailsSpam = 0
    emailsHam = 0
    truePositives = 0
    trueNegatives = 0
    falsePositives = 0
    falseNegatives = 0

    for email in validation:
        classifier = classify(trainedTeta,email[1], tetaZero)
        if classifier >= 0:
            classifier = 1
        else:
            classifier = -1
        if classifier == email[0]:
            tentativasCertas += 1
            if classifier == -1:
                truePositives += 1
            elif classifier == 1:
                trueNegatives += 1
        else:
            tentativasIncorretas += 1
            if classifier == -1:
                falsePositives += 1
            elif classifier == 1:
                falseNegatives += 1
        if email[0] == -1:
            emailsSpam += 1
        elif email[0] == 1:
            emailsHam += 1
        tentativas += 1

    print("\nPerceptron: \n")
    print("O Algoritmo do perceptron percorreu ", tentativas, "emails, sendo observado o seguinte: \n")
    print("Dos ", emailsSpam, "emails de spam, avaliou corretamente ", truePositives, " emails e ", emailsSpam - truePositives, " emails foram avaliados de forma incorreta.")
    print("Dos ", emailsHam, "emails de ham, avaliou corretamente ", trueNegatives, " emails e ", emailsHam - trueNegatives, " emails foram avaliados de forma incorreta.")
    print("A taxa de sucesso geral é de", ((tentativasCertas/tentativas) * 100), "% e uma taxa de insucesso geral de", ((tentativasIncorretas/tentativas * 100)), "% \n")
    print("Métricas de Classificação: \n")
    print("A Accuracy calculada é:", (tentativasCertas / tentativas))
    print("A Error rate calculada é:", (tentativasIncorretas / tentativas))
    print("A Sensivity calculada é:", (truePositives / (truePositives + falseNegatives)))
    print("A Specificity calculada é:", (trueNegatives / (trueNegatives + falsePositives)))
    print("A Precision calculada é:", (truePositives / (truePositives + falsePositives)))
    print("O Recall calculado é:", (truePositives / (truePositives + trueNegatives)))
    p = truePositives / (truePositives + falsePositives)
    r = truePositives / (truePositives + trueNegatives)
    print("A F-Measure calculada é:", ((2 * p * r) / (p + r)))
    print("O Geometric-mean calculado é:", math.sqrt(truePositives * trueNegatives))



# if the namespace is __main__ it runs the main() function
if __name__ == "__main__":
    main()

#mudar o codigo aka portugues ingles e diferenciar do nazi e do outro x
#adicionar comments
#adicionar metricas
#para o percetrao , saber a cena do 70 15 15 ou 70 30 x
#train list , test list , validation list x
#pq o test list é para o naive bayes calcular o c x
