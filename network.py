import random
print("\n ------------------- A NETWORK DESIGN ------------ \n")


user_input = int(input("Are you sending a: \n 1: Image file \n 2: File.txt \n"))

print(user_input, "\n")

path_choice = ["TRD", "DIA"]

# Priviledge
priviledge = ["Normal", "VIP"]
random_priviledge = random.choice(priviledge)


# Type of network
network_type = ["LAN", "MAN"]
random_network = random.choice(network_type)



if user_input == 1 or user_input == 2:
    print("Sending a file\n")

    # printing the priviledge
    print("User Priviledge is: ", random_priviledge, "\n")

    # printing the Network Type
    print("User Network is: ", random_network, "\n")

    # check priviledge
    if random_priviledge == "Normal":
        # print Path 1 --> TRD
        print("Use:", path_choice[0])
    else:
        # print Path 2 --> DIA
        print("Use:", path_choice[1])
else:
    print("Invalid Input!!")

