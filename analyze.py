import json
# import csv   # Uncomment this line if you want to export the results to a CSV file


# Load the accounts you follow (following)
def load_following(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return {
        item["string_list_data"][0]["value"]
        for item in data["relationships_following"]
    }


# Load the accounts that follow you (followers)
def load_followers(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return {
        item["string_list_data"][0]["value"]
        for item in data
    }


def main():
    following = load_following("data/following.json")
    followers = load_followers("data/followers_1.json")

    # Find accounts that don't follow you back
    not_following_back = following - followers

    print(f"Following: {len(following)}")
    print(f"Followers: {len(followers)}")
    print(f"Not following back: {len(not_following_back)}\n")

    print("Users who don't follow you back:\n")

    for user in sorted(not_following_back):
        print(user)

    # -------------------------------------------------
    # OPTIONAL: Export results to CSV
    # -------------------------------------------------
    # Uncomment this section if you want to save the results
    # as a CSV file.

    """
    with open("not_following_back.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["username"])

        for user in sorted(not_following_back):
            writer.writerow([user])

    print("\nResults exported to not_following_back.csv")
    """


if __name__ == "__main__":
    main()
