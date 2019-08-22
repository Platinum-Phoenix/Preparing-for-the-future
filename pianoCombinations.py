def permutations(string, pointer = 0):

    # if we've gotten to the end, print the permutation
    if pointer == len(string):
        print ("".join(string))

    # everything to the right of the pointer has not been swapped yet
    for i in range(pointer, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the pointer
        dummy=string_copy[pointer]
        string_copy[pointer]=string_copy[i]
        string_copy[i]= dummy

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with pointer + 1)
        permutations(string_copy, pointer + 1)

name = input("What do you want to permutate ")
type(name)
permutations("".join(name))







