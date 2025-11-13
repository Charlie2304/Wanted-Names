# [Wanted Names]
# [Charlie Smith]
# [12/11/25]
# AS Computer Science

# Global Variables

names = ["alice", "bob", "charlie", "dave", "erin"]
search = ""

# Main Program

search = input("Type the name that you are searching for:   ")
search = search.lower()

# For loop

for i in range(len(names) - 1):
    if search == names[i]:
        print("Found the person you're searching for!")
        break

    else:
        print("Not found yet")

print("Thank you for searching with us!")
