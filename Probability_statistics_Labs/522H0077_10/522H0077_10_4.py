import matplotlib.pyplot as plt
from collections import Counter
import re


text = """
The quick brown fox jumps over the lazy dog. The dog barks back at the fox, but the fox is too quick to catch. Brown bears are known to be excellent climbers. The lazy cat watches the fox and dog play from a distance. The quick fox jumps over the dog again. The dog chases the fox, but the fox escapes into the woods. Brown rabbits are often seen hopping around in the fields. The lazy dog lies down under a shady tree. The fox and dog are fast friends. Foxes are known for their cunning nature. The dog enjoys running and playing with the fox. The quick fox jumps over a log. The dog barks happily. Brown squirrels scurry up the trees. The lazy cat yawns and stretches. The fox and dog frolic in the meadow. The quick fox runs circles around the dog. The dog pants and tries to keep up. Brown owls hoot in the night. The lazy cat curls up for a nap. The fox and dog rest under the moonlight.
"""

words = re.findall(r'\w+', text.lower())  
word_counts = Counter(words)
word_frequencies = sorted(word_counts.values(), reverse=True)

plt.figure(figsize=(10, 6))
plt.hist(word_frequencies, bins=30, edgecolor='black')
plt.title('Histogram of Word Frequencies')
plt.xlabel('Word Frequency')
plt.ylabel('Number of Words')
plt.grid(True)
plt.show()