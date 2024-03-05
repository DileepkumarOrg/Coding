def possibleChanges(usernames):
    results = []

    for username in usernames:
        # Iterate through all possible pairs of positions to swap
        for i in range(len(username) - 1):
            for j in range(i + 1, len(username)):
                # Create a new string with the letters swapped
                new_username = list(username)
                new_username[i], new_username[j] = new_username[j], new_username[i]
                new_username = ''.join(new_username)

                # Check if the new username is smaller in alphabetical order
                if new_username < username:
                    results.append("YES")
                    break
            else:
                continue
            break  # Break the outer loop if a valid swap is found

        else:
            # If no valid swap is found
            results.append("NO")

    return results

if _name_ == '_main_':
    usernames_count = int(input().strip())
    usernames = [input().strip() for _ in range(usernames_count)]

    result = possibleChanges(usernames)

    for res in result:
        print(res)