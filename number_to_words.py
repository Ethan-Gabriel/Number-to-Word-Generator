# This program will take a number as an input and will display that number in words. 

# This global dictionary stores all the word values for single digits, including prefixes for some numbers
single_digit_words = {
        '0': ["zero"],
        '1': ["one"],
        '2': ["two", "twen"],
        '3': ["three", "thir"],
        '4': ["four", "four"],
        '5': ["five", "fif"],
        '6': ["six"],
        '7': ["seven"],
        '8': ["eight"],
        '9': ["nine"],
    }

# This global list holds the first three double digit words (the other double digit words will be formed)
double_digit_words = [
    "ten", 
    "eleven", 
    "twelve"
    ]

# This global string stores the word "hundred"
hundred = "hundred"

# This global list stores all the words representing all large numbers
large_sum_words = [
    "thousand", 
    "million", 
    "billion", 
    "trillion", 
    "quadrillion", 
    "quintillion", 
    "sextillion", 
    "septillion", 
    "octillion", 
    "nonillion"
    ]

# This function will grab the user's input in the "ask user input" function and will return the disired output
def num_to_word(n):
    word = []

    # condiitonal statement for negative numbers
    if n.startswith('-'):
        word.append("negative")
        n = n[1:]
    
    # removes all leading 0's from number
    # adds certain number of leading zeros to make number a length of a multiple of 3
    n = n.lstrip('0')
    if len(n) % 3 != 0 and len(n) > 3:
        n = n.zfill(3 * (((len(n) - 1) // 3) + 1))

    # list stores all numbers in groups of 3 within the updated user input from above
    sum_list = [n[i:i + 3] for i in range(0, len(n), 3)]
    skip = False

    # for loop used to create the words for each group of 3 numbers
    for i, num in enumerate(sum_list):
        
        # if a group of 3 numbers is all 0's, the program will skip it for naming
        if num != '000': 
            skip = False
        else:
            skip = True
        
        # for loop used to name each number within the group of 3 numbers
        for _ in range(len(num)):
            num = num.lstrip('0')
            
            # after removing leading 0's, if the group is 1 number, the program will name it using the global varibales
            if len(num) == 1:
                if (len(sum_list) > 1 or (len(sum_list) == 1 and len(sum_list[0]) == 3)) and i == len(sum_list) - 1 and (word[-1] in large_sum_words or hundred in word[-1]):
                    word.append("and")
                word.append(single_digit_words[num][0])
                num = num[1:]
                break

            # after removing leading 0's, if the group is 2 numbers, the program will name it using the global varibales
            if len(num) == 2:
                if num[0] != '0':
                    if (len(sum_list) > 1 or (len(sum_list) == 1 and len(sum_list[0]) == 3)) and i == len(sum_list) - 1:
                        word.append("and")
                    if num.startswith('1'):
                        if int(num[1]) in range(3):
                            word.append(double_digit_words[int(num[1])])
                        else:
                            number = single_digit_words[num[1]][1 if int(num[1]) in range(3, 6, 2) else 0] 
                            word.append(number + ("teen" if not number[-1] == 't' else "een"))
                    else:
                        word.append(single_digit_words[num[0]][1 if int(num[0]) in range(2, 6) else 0] + ("ty " if num[0] != '8' else 'y ') + (single_digit_words[num[1]][0] if num[1] != '0' else ""))
                    break
                else:
                    num = num[1:]
                    continue
            
            # after removing leading 0's, if the group is 3 numbers, the program will name it using the global varibales
            if len(num) == 3:
                if num[0] != '0':
                    word.append(single_digit_words[num[0]][0] + " " + hundred)
                    if num[1:] == '00': 
                        break
                num = num[1:]
 
        # attaches correct term from large_sum_words list 
        if len(sum_list[i:]) > 1 and not skip:
            word.append(large_sum_words[len(sum_list[i:]) - 2])
            skip = True
    
    # joins all the groups of 3 numbers together using spaces 
    word = " ".join(map(str.strip, word))

    # returns the final output back to the "ask_user_input" function to print desired output
    return word[0].lstrip().lower() + word[1:].rstrip().lower() if "negative" not in word else word[:11].lstrip().lower() + word[11].lower() + word[12:].rstrip().lower()

# This function will ask the user for a number in numerical form and will use the "num_to_word" function to return the designated value. This function will print the desired output
def ask_user_input():
    if __name__ == "__main__":
        print("Hello! Welcome to my Number-to-Words Generator!")

        # This infinite while loop will keep asking the user to input a number and will output the desired text
        while True:
            try:
                # Asks user for input
                n = input("Enter any number to convert it into words or type 'exit' to exit the program: ")
                # if user types "exit" using any case, the loop will be broken and the program will end
                if n.upper() == "EXIT":
                    print("Thank you for using my Number-to-Words Generator! Goodbye!")
                    break
                # If the user inputs a valid input, the program will use the "num_to_word" function and output the desired text
                else:
                    int(n)
                    print(n, "-->", num_to_word(n))
            # This output will only display if the user input is invalid
            except ValueError:
                print("Error: Invalid Input!")

# This line will call the "ask_user_input" function and begin the program
ask_user_input()