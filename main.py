import random
import backlog
print("Welcome to the Basketball Player Creator")
print("--------------------------------------------")
print(backlog.name)
print(f"Age: {backlog.age}")
print(f"Height: {backlog.truehgt} ")
print(f"Weight: {backlog.weight} KG ")
print("Player Position:", backlog.position)
# Ratings
if backlog.overall >= 900:
    print(f"{backlog.name}: Superstar Level : ***** : {backlog.overall} Rating ")
elif backlog.overall >= 750:
    print(f"{backlog.name}: All-star Level : **** : {backlog.overall} Rating ")
elif backlog.overall >= 500:
    print(f"{backlog.name}: Starter : *** : {backlog.overall} Rating ")
elif backlog.overall >= 400:
    print(f"{backlog.name}: Role : ** : {backlog.overall} Rating ")
else: print(f"{backlog.name}: Bum : * : {backlog.overall} Rating ")
print("--------------------------------------------")
print(f"The height attribute of this player is {backlog.height}")
print(f"The strength attribute of this player is {backlog.strength}")
print(f"The speed attribute of this player is {backlog.speed}")
print(f"The jump attribute of this player is {backlog.jump}")
print(f"The endurance attribute of this player is {backlog.endurance}")
print(f"The inside attribute of this player is {backlog.inside}")
print(f"The dunk attribute of this player is {backlog.dunk}")
print(f"The midrange attribute of this player is {backlog.midrange}")
print(f"The threepointer attribute of this player is {backlog.threepointer}")
print(f"The freethrow attribute of this player is {backlog.freethrow}")
print(f"The offensiveiq attribute of this player is {backlog.offensiveiq}")
print(f"The defensiveiq attribute of this player is {backlog.defensiveiq}")
print(f"The dribbling attribute of this player is {backlog.dribbling}")
print(f"The rebounding attribute of this player is {backlog.rebounding}")
print("--------------------------------------------")





