#Function that returns the total number of combinations
def total_combinations(dieA, dieB):
    return len(dieA)*len(dieB)

#Function that returns all the possible combinations when the two dice are thrown together
def display_combinations(dieA, dieB):
    numberFacesDieA=len(dieA) 
    numberFacesDieB=len(dieB) 

    output=[[0]*numberFacesDieB for i in range(numberFacesDieA)]
    for i in range(1,numberFacesDieA+1):
        for j in range(1, numberFacesDieB+1):
            output[i-1][j-1]=(i, j)
    return output

#Function that prints all the sums and their probabilities
def calculate_probabilities(dieA, dieB):
    total_outcomes=len(dieA)*len(dieB)  
    probabilities={}
    for outcome in range(2, 13):
        count= 0
        for faceA in dieA:
            for faceB in dieB:
                if faceA+faceB==outcome:
                    count+= 1
        
        probability=count/total_outcomes
        probabilities[outcome]=probability
    for key, val in probabilities.items():
        print('P(Sum = '+str(key)+') = '+str(round(val, 4)))


#Initial dice
dieA=[1, 2, 3, 4, 5, 6]
dieB=[1, 2, 3, 4, 5, 6]


#Function calls

total_combinations_number=total_combinations(dieA, dieB)
print('The total possible combinations are: '+str(total_combinations_number))
print()

total_combinations_matrix=display_combinations(dieA, dieB)
print('The combination matrix is given by:')
print()
print(total_combinations_matrix)
print()

print('The probabilities of all possible sums occurring among the number of combinations are:')
print()
calculate_probabilities(dieA, dieB)


