#744. Find Smallest Letter Greater Than Target

def search_next_letter(letters, key):
    # TODO: Write your code here

    lw,rw = 0, len(letters) - 1
    smallest_letter = 'zz'

    while lw<=rw:
        mid = (rw+lw) // 2

        if letters[mid] > key:
            smallest_letter = min(letters[mid],smallest_letter)
            rw = mid - 1
        else:
            lw = mid + 1
        
    if smallest_letter == 'zz':
        return letters[0]

    return smallest_letter


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'h'))

main()
