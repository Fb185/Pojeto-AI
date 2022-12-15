from nb import naivebayes
from perceptron import function

def main():
    choice = input("Escolha o algoritmo a usar NB ou Perceptron\n")
    if (choice == "nb"):
        naivebayes(hambag, spambag)
    elif(choice =="perceptron"):
        function()
    else:
        print("invalido")

if __name__ == "__main__":
    main()
