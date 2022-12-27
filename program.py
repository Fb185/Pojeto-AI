#from nb import naivebayes
#from perceptron import function
import naivebayes
import sudk

def main():
    choice = input("Escolha o algoritmo a usar NB ou Perceptron\n")
    if (choice == "nb"):
        naivebayes.main()
    elif(choice =="perceptron"):
        #function()
        return
    elif(choice =="sdk"):
        sudk.main()
        return
    else:
        print("invalido")

if __name__ == "__main__":
    main()
