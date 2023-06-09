# DESCRIPTION:
# Given two Arrays in which values are the power of each soldier, return true if you survive the attack or false if you perish.
# CONDITIONS
# Each soldier attacks the opposing soldier in the same index of the array. The survivor is the number with the highest value.
# If the value is the same they both perish
# If one of the values is empty(different array lengths) the non-empty value soldier survives.
# To survive the defending side must have more survivors than the attacking side.
# In case there are the same number of survivors in both sides, the winner is the team with the highest initial attack power. If the total attack power of both sides is the same return true.
# The initial attack power is the sum of all the values in each array.
# EXAMPLES
# attackers=[ 1, 3, 5, 7 ]   defenders=[ 2, 4, 6, 8 ]
# 0 survivors                4 survivors
# return true
# attackers=[ 1, 3, 5, 7 ]   defenders=[ 2, 4 ]
# 2 survivors  (16 damage)   2 survivors (6 damage)
# return false
# attackers=[ 1, 3, 5, 7 ]   defenders=[ 2, 4, 0, 8 ]
# 1 survivors                3 survivors
# return true

attacker1 = [1,3,5,7]
attacker2 = [2,4,6,8]

def war_of_2(attacker1,attacker2):
    survivers = [0,0]
    if not attacker1:
        return True
    elif not attacker2:
        return False

    for i in range(len(attackers)):
       if  attacker1[i] > attacker2[i]:
            survivors[0] + 1
        elif attacker1[i] < attacker2[i]:
           survivors[1] += 1
        
    return survivor[0] < survivor[1]
print(war_of_two(attacker1,attacker2))