#from nb import naivebayes
#from perceptron import function
import naive_bayes
import sudk

def main():
    choice = input("Escolha o algoritmo a usar NB / Perceptron / AC3\n")
    if (choice == "nb"):
        naive_bayes.main()
    elif(choice =="perceptron"):
        #function()
        return
    elif(choice =="ac3"):
        sudk.main()
        return
    else:
        print("invalido")

if __name__ == "__main__":
    main()
