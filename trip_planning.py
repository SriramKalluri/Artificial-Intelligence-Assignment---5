# tripplanning.py
# Simple AI Travel Recommendation System

# Each destination contains:
# budget
# climate
# interests

destinations = [
    {
        "name": "Manali, Himachal Pradesh",
        "budget": "low",
        "climate": "cold",
        "interests": ["adventure", "nature", "trekking", "snow"]
    },
    {
        "name": "Goa",
        "budget": "medium",
        "climate": "hot",
        "interests": ["beach", "nightlife", "relaxation", "water sports"]
    },
    {
        "name": "Jaipur, Rajasthan",
        "budget": "medium",
        "climate": "hot",
        "interests": ["culture", "history", "architecture", "shopping"]
    },
    {
        "name": "Coorg, Karnataka",
        "budget": "medium",
        "climate": "cool",
        "interests": ["nature", "coffee", "trekking", "relaxation"]
    },
    {
        "name": "Leh-Ladakh",
        "budget": "high",
        "climate": "cold",
        "interests": ["adventure", "nature", "biking", "trekking"]
    },
    {
        "name": "Kerala Backwaters",
        "budget": "medium",
        "climate": "warm",
        "interests": ["nature", "relaxation", "culture", "boat rides"]
    },
    {
        "name": "Rishikesh",
        "budget": "low",
        "climate": "warm",
        "interests": ["adventure", "yoga", "trekking", "river rafting"]
    },
    {
        "name": "Andaman Islands",
        "budget": "high",
        "climate": "hot",
        "interests": ["beach", "diving", "water sports", "relaxation"]
    },
    {
        "name": "Varanasi",
        "budget": "low",
        "climate": "warm",
        "interests": ["culture", "history", "spirituality", "photography"]
    },
    {
        "name": "Spiti Valley",
        "budget": "medium",
        "climate": "cold",
        "interests": ["adventure", "nature", "trekking", "photography"]
    }
]


def recommend_places(budget, climate, interests):

    results = []

    for place in destinations:

        score = 0

        # Budget match
        if place["budget"] == budget:
            score += 3

        # Climate match
        if place["climate"] == climate:
            score += 2

        # Interest match
        for interest in interests:

            if interest in place["interests"]:
                score += 1

        if score > 0:
            results.append((place["name"], score, place))

    # Sort by highest score
    results.sort(key=lambda x: x[1], reverse=True)

    return results[:3]


def get_user_input():

    print("\nAI Travel Recommendation System\n")

    budget = input(
        "Enter budget (low / medium / high): "
    ).lower()

    climate = input(
        "Enter climate (cold / cool / warm / hot): "
    ).lower()

    print("\nEnter interests separated by commas")
    print("Example: adventure,nature,beach\n")

    interests = input(
        "Your interests: "
    ).lower().split(",")

    interests = [i.strip() for i in interests]

    return budget, climate, interests


def main():

    budget, climate, interests = get_user_input()

    recommendations = recommend_places(
        budget,
        climate,
        interests
    )

    print("\nTop Recommendations:\n")

    if not recommendations:

        print("No matching destinations found.")

    else:

        for i, (name, score, info) in enumerate(recommendations, 1):

            print(f"{i}. {name}")
            print(f"   Budget: {info['budget']}")
            print(f"   Climate: {info['climate']}")
            print(f"   Interests: {', '.join(info['interests'])}")
            print(f"   Match Score: {score}\n")


if __name__ == "__main__":
    main()
