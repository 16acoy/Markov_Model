#state_1 = rainy
#state_2 = cloudy

#observation_1 = umbrella
#observation_2 = no_umbrella

#training data

global O_observations
O_observations = ['k0','k1','k1', 'k2','k1','k1','kf']
N = 2

global X_states
X_states = ['s0','s1','s1','s2','s1','s1','sf']
M = 2

global length_of_sequence
length_of_sequence = len(X_states)-1

#program

def transition_probability_of_si_to_sj(i,j):
    count1 = 0 #top of fraction
    count2 = 0 #bottom on fraction
    for x in range(length_of_sequence):
        if X_states[x] == 's'+str(i):
            count2 = count2 + 1
            if x<5:
                if X_states[x+1] == 's'+str(j):
                    count1 = count1 + 1
    if count1 == 0 or count2 == 0:
        probability = 0
    else:
        probability = (count1/count2)
    return probability


def emission_probability_of_kj_given_state_is_si(i,j):
    count1 = 0 #top of fraction
    count2 = 0 #bottom on fraction
    for x in range(length_of_sequence+1):
        if X_states[x] == 's'+str(j):
            count2 = count2 + 1
            if O_observations[x] == 'k'+str(i):
                count1 = count1 + 1
    if count1 == 0 or count2 == 0:
        probability = 0
    else:
        probability = (count1/count2)
    return probability           


A_transition_probability_matrix = []
for i in range(M+2):
    A_transition_probability_matrix.append([])
    for j in range(N+2):
        A_transition_probability_matrix[i].append([])
        A_transition_probability_matrix[i][j].append('a'+str(i)+str(j))

print('\n'+'A_transition_probability_matrix:'+'\n')
for x in range(N+2):
       print(A_transition_probability_matrix[x])

B_emission_probability_matrix = []
for j in range(N+2):
    B_emission_probability_matrix.append([])
    for i in range(N+2):
        B_emission_probability_matrix[j].append([])
        B_emission_probability_matrix[j][i].append('b'+str(i)+'(k'+str(j)+')')

print('\n'+'B_emission_probability_matrix:'+ '\n')
for x in range(N+2):
       print(B_emission_probability_matrix[x])

for i in range(0,M+2):
    for j in range(1,N+2):
        A_transition_probability_matrix[i][j].append(transition_probability_of_si_to_sj(i,j))
        pass

print('\n'+'A_transition_probability_matrix:'+'\n')
for x in range(N+2):
       print(A_transition_probability_matrix[x])


#---

for i in range(1,N+2):
    for j in range(1,N+2):
        B_emission_probability_matrix[i][j].append(emission_probability_of_kj_given_state_is_si(i,j))

print('\n'+'B_emission_probability_matrix:'+'\n')
for x in range(N+2):
       print(B_emission_probability_matrix[x])
