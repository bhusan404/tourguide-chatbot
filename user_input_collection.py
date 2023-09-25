import json
from pymongo import MongoClient
from datetime import datetime

# MongoDB configuration
mongodb_host = 'localhost'
mongodb_port = 27017
mongodb_database = 'user_inputs'
mongodb_collection = 'inputs'

# Connect to MongoDB
client = MongoClient(mongodb_host, mongodb_port)
db = client[mongodb_database]
collection = db[mongodb_collection]

def collect_and_store_user_input(user_id, user_input, other_fields=None):
    """
    Collect user input, format it as JSON, and store it in MongoDB.

    Args:
        user_id (str): Unique identifier for the user.
        user_input (str): User's input text.
        other_fields (dict): Additional fields you want to include in the JSON data.

    Returns:
        dict: The JSON data that was stored in MongoDB.
    """
    timestamp = datetime.now().isoformat()

    input_data = {
        "user_id": user_id,
        "user_input": user_input,
        "timestamp": timestamp
    }

    if other_fields:
        input_data.update(other_fields)

    # Insert the JSON data into MongoDB
    result = collection.insert_one(input_data)

    # Return the inserted JSON data
    return input_data

def main():
    print("User Input Collector")
    user_id = input("Enter user ID: ")
    
    while True:
        user_input = input("Enter user input (or 'exit' to quit): ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Collect and store the user input
        stored_data = collect_and_store_user_input(user_id, user_input)
        print("User input stored:", json.dumps(stored_data, indent=4))

if __name__ == "__main__":
    main()
