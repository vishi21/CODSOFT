class SimpleRecommendationSystem:
    def __init__(self):
        self.user_preferences = {}  # Dictionary to store user preferences and item ratings

    def add_user_preferences(self, user_id, preferences):
        self.user_preferences[user_id] = preferences

    def recommend_items(self, user_id):
        if user_id not in self.user_preferences:
            print("User not found.")
            return []

        user_prefs = self.user_preferences[user_id]

        # Calculate item scores based on user preferences
        item_scores = {}
        for other_user_id, other_user_prefs in self.user_preferences.items():
            if other_user_id == user_id:
                continue

            for item, rating in other_user_prefs.items():
                if item not in user_prefs:  # Only recommend items not already rated by the user
                    item_scores.setdefault(item, 0)
                    item_scores[item] += rating

        # Sort items by score in descending order
        recommended_items = sorted(item_scores.keys(), key=lambda item: item_scores[item], reverse=True)

        return recommended_items

# Example usage
recommender = SimpleRecommendationSystem()

# Adding user preferences and item ratings
recommender.add_user_preferences("user1", {"3 Idiots": 5, "Dangal": 4, "Adipurush": 2})
recommender.add_user_preferences("user2", {"Rebecca": 4, "Verity": 5, "Misery": 3})
recommender.add_user_preferences("user3", {"Beloved": 3, "Lolita": 4, "Moby-Dick": 5})

# Recommend items for a user
user_id = "user1"
recommended_items = recommender.recommend_items(user_id)

print(f"Recommended items for {user_id}: {recommended_items}")
