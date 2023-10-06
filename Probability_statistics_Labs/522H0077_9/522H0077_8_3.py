import matplotlib.pyplot as plt
from collections import Counter

def plot_word_frequency(text, num_words):
    # Split the text into individual words
    words = text.split()

    # Count the frequency of each word
    counts = Counter(words)

    # Get the most common words and their frequencies
    most_common = counts.most_common(num_words)

    # Extract the words and frequencies into separate lists
    word_list = [word for word, count in most_common]
    count_list = [count for word, count in most_common]

    # Create a line plot of word frequencies
    plt.figure(figsize=(12, 6))
    plt.plot(word_list, count_list, marker = 'o')
    plt.xlabel('Word')
    plt.ylabel('Frequency')
    plt.title('Most Common Words')
    plt.xticks(rotation = 90)
    plt.show()

# Example usage
text = """
The quick brown fox jumps over the lazy dog. The dog barks back at the fox, but the fox is too quick to catch. Brown bears are known to be excellent climbers. The lazy cat watches the fox and dog play from a distance. The quick fox jumps over the dog again. The dog chases the fox, but the fox escapes into the woods. Brown rabbits are often seen hopping around in the fields. The lazy dog lies down under a shady tree. The fox and dog are fast friends. Foxes are known for their cunning nature. The dog enjoys running and playing with the fox. The quick fox jumps over a log. The dog barks happily. Brown squirrels scurry up the trees. The lazy cat yawns and stretches. The fox and dog frolic in the meadow. The quick fox runs circles around the dog. The dog pants and tries to keep up. Brown owls hoot in the night. The lazy cat curls up for a nap. The fox and dog rest under the moonlight.
"""

plot_word_frequency(text, 30)