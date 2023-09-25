import random

# Dictionary of tourist destinations with detailed information
destinations = {
    "paris": {
        "name": "Paris",
        "description": "Paris is the capital of France and is known for its romantic ambiance, world-class art, and iconic landmarks like the Eiffel Tower.",
        "rating": 4.8,
        "activities": ["Visit the Louvre Museum", "Take a Seine River cruise", "Explore Montmartre"],
        "image_url": "https://example.com/paris.jpg"
    },
    "kyoto": {
        "name": "Kyoto",
        "description": "Kyoto, Japan, is famous for its traditional temples, beautiful gardens, and historic streetscapes.",
        "rating": 4.5,
        "activities": ["Visit Kinkaku-ji (Golden Pavilion)", "Stroll through Gion district", "Explore Arashiyama Bamboo Grove"],
        "image_url": "https://example.com/kyoto.jpg"
    },
    "new york": {
        "name": "New York City",
        "description": "New York City is a bustling metropolis known for its diverse culture, skyscrapers, and famous attractions like Times Square.",
        "rating": 4.7,
        "activities": ["Visit the Statue of Liberty", "Explore Central Park", "Visit the Museum of Modern Art (MoMA)"],
        "image_url": "https://example.com/newyork.jpg"
    }
}

def suggest_destination(query):
    """
    Suggest a tourist destination based on user input.

    Args:
        query (str): The user's input.

    Returns:
        str: A formatted suggestion with destination information.
    """
    query = query.lower()
    if query in destinations:
        destination = destinations[query]
        suggestion = f"Destination: {destination['name']}\n"
        suggestion += f"Description: {destination['description']}\n"
        suggestion += f"Rating: {destination['rating']}\n"
        suggestion += f"Activities: {' • '.join(destination['activities'])}\n"
        suggestion += f"Image: {destination['image_url']}"
        return suggestion
    else:
        return "I'm sorry, I don't have information about that destination. Please try another one."

def main():
    """
    Main function to run the Tourist Destination Chatbot.
    """
    print("Welcome to the Tourist Destination Chatbot!")
    print("Ask me about a tourist destination, and I'll suggest one for you.")
    print("Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        response = suggest_destination(user_input)
        print("Chatbot:")
        print(response)

if __name__ == "__main__":
    main()
