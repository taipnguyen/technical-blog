import random 
import matplotlib.pyplot as plt 


coin_face = ["H","T"]
tosses = []
tosses.append(random.choice(coin_face))
in_a_row = 0
max = 0  
for i in range(1,100):
    coin_flip = random.choice(coin_face)
    tosses.append(coin_flip)
    if tosses[i] == tosses[i-1]:
        in_a_row = in_a_row + 1 
        if in_a_row > max:
            max = in_a_row
            
    else:
        in_a_row = 0 
        
def count_consecutive_outcomes(outcomes, target_streak):
    current_streak_heads = 0
    current_streak_tails = 0 
    count = 0

    for outcome in outcomes:
        if outcome == 'H':  # Assuming 'H' represents heads and 'T' represents tails
            current_streak_heads += 1
        else:
            current_streak_heads = 0
            
        if outcome == 'T':  # Assuming 'H' represents heads and 'T' represents tails
            current_streak_tails += 1
        else:
            current_streak_tails = 0
            
        if current_streak_heads >= target_streak:
            count += 1
        if current_streak_tails >= target_streak:
            count += 1 


    return count

data = {}
already_counted = 0 
for target_streak in range(8,3,-1):
    result = count_consecutive_outcomes(tosses,target_streak)
    temp = result
    # Remove from smaller streaks already counted bigger streaks
    result = result - already_counted
    data[target_streak] = result
    already_counted =  already_counted + temp



streak = list(data.keys())
amount = list(data.values())
fig = plt.figure(figsize=(10,5))

plt.bar(streak, amount, color="maroon", width=0.4)
plt.xlabel("Streak of heads")
plt.ylabel("Amount of streaks")
plt.title(f"Amount of streaks in {len(tosses)} coin tosses")
plt.show()

output = f"If you bet martingale with max bet {2**(6)} dollars. You would lose {data[6]} times..{2**6*data[6]} dollars lost"
print(output)

    