import random

def generate_random_ids(num_ids):
    """Generate specified number of random packet IDs."""
    random_ids = []
    for _ in range(num_ids):
        random_id = random.randint(0, 65535)  # Generate random ID in the range 0 to 65535
        random_ids.append(random_id)
    return random_ids

def main():
    num_ids = 10  # Number of random packet IDs to generate
    random_ids = generate_random_ids(num_ids)
    print("Random Packet IDs:")
    for id in random_ids:
        print(id)

if __name__ == "__main__":
    main()
