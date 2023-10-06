import numpy as np

#EX10
print("EX10")
def recommend_item(M, user):
    user_row = M[user - 1]  # Get the row corresponding to the user (subtract 1 to convert to zero-based index)
    unrated_items = np.where(user_row == np.inf)[0]  # Find the indices of unrated items (where value is infinity)

    if len(unrated_items) == 0:
        return "No item to review"  # No unrated items
    else:
        return unrated_items


# Example usage
M = np.array([
    [np.inf, np.inf, 3],
    [2, np.inf, 5],
    [5, 6, 7],
    [np.inf, np.inf, np.inf]
])

users = np.arange(1, M.shape[0]+1)  # Generate an array of user numbers [1, 2, ..., number of rows]
for user in users:
    recommended_items = recommend_item(M, user)
    if recommended_items == "No item to review":
        print(f"Recommendation for User {user}: {recommended_items}")
    else:
        recommended_item = np.random.choice(recommended_items)
        print(f"Recommendation for User {user}: Item {recommended_item+1}")

