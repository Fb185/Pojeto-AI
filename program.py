#from nb import naivebayes
#from perceptron import function
import naive_bayes
import perceptron
import sudk

def main():
    choice = input("Escolha o algoritmo a usar NB / Perceptron / AC3\n")
    if (choice == "nb"):
        naive_bayes.main()
    elif(choice =="perceptron"):
        perceptron.main()
      
        return
    elif(choice =="ac3"):
        puzzle = [
            [0, 0, 3, 0, 2, 0, 6, 0, 0],
            [9, 0, 0, 3, 0, 5, 0, 0, 1],
            [0, 0, 1, 8, 0, 6, 4, 0, 0],
            [0, 0, 8, 1, 0, 2, 9, 0, 0],
            [7, 0, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 6, 7, 0, 8, 2, 0, 0],
            [0, 0, 2, 6, 0, 9, 5, 0, 0],
            [8, 0, 0, 2, 0, 3, 0, 0, 9],
            [0, 0, 5, 0, 1, 0, 3, 0, 0]
            ]
        sudk.main(puzzle)
        return
    else:
        print("invalido")

if __name__ == "__main__":
    main()
