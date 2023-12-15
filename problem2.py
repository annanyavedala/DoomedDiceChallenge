import itertools

#Function to generate all combinations of dice and return the new die after comparing probabilities
def undoom_dice(dieA, dieB):
    possible_sums=range(2, 13)
    total_outcomes=len(dieA)*len(dieB) 

    t=list(itertools.product([2,3], repeat=4))
    allCombinationsA=list()
    for x in t:
        lst=[1]+list(x)+[4]
        allCombinationsA.append(lst)
    allCombinationsB=list(itertools.combinations([1,2,3,4,5,6,7,8], len(dieB)))

    for newA in allCombinationsA:
        for newB in allCombinationsB:
            if is_probability_preserved(newA, newB, total_outcomes, possible_sums):
                return newA, newB

    return None, None  

#Check if the sum probability distributions are the same
def is_probability_preserved(newA, newB, total_outcomes, possible_sums):
    original_probabilities=calculate_probabilities(dieA, dieB)
    new_probabilities=calculate_probabilities(newA, newB)
    orig_probs=list(original_probabilities.values())
    new_probs=list(new_probabilities.values())

    for orig_prob, new_prob in zip(orig_probs, new_probs):
        if abs(orig_prob-new_prob)>=1e-6:
            break
    else:
        return True
    return False


#Calculate the sum probability distributions
def calculate_probabilities(dieA, dieB):
    total_outcomes=len(dieA)*len(dieB)  
    probabilities={}
    for outcome in range(2, 13):
        count=0
        for faceA in dieA:
            for faceB in dieB:
                if faceA+faceB==outcome:
                    count+= 1
        
        probability=count/total_outcomes
        probabilities[outcome]=probability
    return probabilities


dieA=list(map(int, input('Enter die A ').split(',')))
dieB=list(map(int, input('Enter die B ').split(',')))


newA, newB=undoom_dice(dieA, dieB)

print("New_Die_A = ", newA)
print("New_Die_B = ", list(newB))