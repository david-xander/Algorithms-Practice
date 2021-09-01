favorite_movies_in_order_of_preference = {
'Biutiful',
'Black Bread',
'Chico and Rita',
'Cicatrices',
'Entrelobos',
'Exorcismus',
'Flatmate',
'Intruders',
'Los ojos de Julia',
'Maximum Shame',
'Mission Park',
'The New Daughter',
'A Sad Trumpet Ballad',
'Kidnapped',
'También la Lluvia',
'Three Steps Above Heaven',
'We Are What We Are Somos Lo Que Hay'
}
other_person_preference_score = [4,2,9,5,3,4,1,5,7,9,3,2,4,5,1,8,4]


# O( n^2 )
def counting_inversions_hardway():
    n = len(other_person_preference_score)
    count = 0
    j = 0
    while j < n-1:
        k = j + 1
        while k < n:
            if other_person_preference_score[j] > other_person_preference_score[k]:
                count += 1
            k += 1
        j += 1

    return count

# O( nLog(n) )
def counting_inversions_divide_and_conquer(input = other_person_preference_score):
    n = len(input)
    half = n//2

    L = input[:half]
    R = input[half:]
    
    count = 0
    if len(L) > 1:
        count += counting_inversions_divide_and_conquer(L)
    if len(R) > 1:
        count += counting_inversions_divide_and_conquer(R)

    count += combine(L,R)

    return count


def combine(L, R):
    count = 0
    for l in L:
        for r in R:
            if l > r:
                count += 1
    return count



if __name__ == "__main__":
    # execute only if run as a script
    print("HARDWAY:::::")
    print(counting_inversions_hardway())
    print('DIVIDE AND CONQUER::::')
    print(counting_inversions_divide_and_conquer())
