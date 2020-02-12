def checkForAnagrams(word, arr):
    # Checking if the word has an anagram in the sliced array.
    for x in arr:
        if (sorted(word) == sorted(x)):
            return True
    return False
            
def funWithAnagrams(text):
    limit = len(text)
    text.reverse()
    # Creating a copy of the list which will be modified,
    # and will not affect the array slicing during the loop.
    final_text = list(text)

    # Looping through the list in reverse since we're eliminating
    # the second anagram we find from the original list order.
    for i in range(0, limit):
        if text[i+1:] and checkForAnagrams(text[i], text[i+1:]):
            final_text.pop(0)

    return sorted(final_text)

def main():
    # Loading Test Cases from .txt files
    inputs = []
    outputs = []
    for i in range(0,5):
        # Reading input lists of text
        f = open('test_cases/input00{}.txt'.format(i+1), 'r')
        input_file = f.read().splitlines()
        # Cleaning the list of the N number in the first element
        input_file.pop(0)
        inputs.append(input_file)

        # Reading output lists of text
        f = open('test_cases/output00{}.txt'.format(i+1), 'r')
        output_file = f.read().splitlines()
        outputs.append(output_file)
    f.close
    
    # Running 5 test cases
    results = []
    for i in range(0,5):
        results.append(funWithAnagrams(inputs[i]))

    # Testing results with expected outputs
    for i in range(0,5):
        if results[i] == outputs[i]:
            print("Test case #{} matches!".format(i+1))
        else:
            print("Test case #{} is not a match.".format(i+1))

if __name__ == "__main__":
    main()