def search(l, searched):
    if not l:
        return None
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (high + low) // 2
        guess = l[mid]
        if guess == searched:
            return mid
        if guess > searched:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == '__main__':
    print(search([1, 3, 5, 6], 3))

            
