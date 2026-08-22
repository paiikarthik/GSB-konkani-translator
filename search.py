import csv

# Dictionary to store English -> Konkani
dictionary = {}

# Load CSV
with open("cleaned_data.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Remove spaces from column names and values
        row = {k.strip(): v.strip() for k, v in row.items()}

        # Store meaning -> word
        dictionary[row["meaning"].lower()] = row["word"]

print(f"Loaded {len(dictionary)} words.")

# Input sentence
sentence = input("Enter English sentence: ")

# Split into words
words = sentence.lower().split()

# Translate each word
translated = []

for word in words:
    if word in dictionary:
        translated.append(dictionary[word])
    else:
        translated.append(f" {word}")  # Word not found

# Join translated words
result = " ".join(translated)

print("\nKonkani Translation:")
print(result)