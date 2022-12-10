from nb import func
from perceptron import function

def main():
    choice = input("Escolha o algoritmo a usar NB ou Perceptron\n")
    if (choice == "nb"):
        func()
    elif(choice =="perceptron"):
        function()
    else:
        print("invalido")

if __name__ == "__main__":
    main()
