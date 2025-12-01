# MultiUsers welcome app
users_data = []

add_user = input("Do you want to join? ").strip().lower() # yes / no
print() # For adding space
while add_user == "yes":
    user_name = input("Enter your name: ").strip().title()
    user_age = input("Enter your age: ").strip()   
    country = input("Enter your country: ").strip().title()
    fav_skill = input("Enter your favorite skill: ").strip().title()
    # Add user to users_data
    user = {
        "username":user_name,
        "age":user_age,
        "country":country,
        "skill":fav_skill
    }
    users_data.append(user)
    add_user = input("Do you want to add another user? ")
    print() # For adding space
print("\n================= All users ================\n")
for user in users_data:
    print(f"Hello {user['username']} !")
    print(f"You are {user['age']} from {user['country']}.")
    print(f"Your favorite skill is {user['skill']}.")
    print("Nice to meet you!")
    print()
    






    


  