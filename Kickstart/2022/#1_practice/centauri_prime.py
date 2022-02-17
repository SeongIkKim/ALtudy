# TODO: Complete the get_ruler function
def get_ruler(kingdom):
    vowel = ['a', 'e', 'i', 'o', 'u']
    name_end = kingdom[-1].lower()
    if name_end in vowel:
        ruler = 'Alice'
    elif name_end == 'y':
        ruler = 'nobody'
    else:
        ruler = 'Bob'
    return ruler

def main():
    # Get the number of test cases
    T = int(input())
    for t in range(T):
        # Get the kingdom
        kingdom = input()
        print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))

if __name__ == '__main__':
    main()
