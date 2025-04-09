import collections, random

def create_transition_graph(text):
    words = text.lower().split()
    transitions = collections.defaultdict(lambda: collections.defaultdict(int))
    
    for i in range(len(words) - 1):
        transitions[words[i]][words[i + 1]] += 1
    
    transition_probs = {}
    for word, next_words in transitions.items():
        total = sum(next_words.values())
        transition_probs[word] = {k: v / total for k, v in next_words.items()}

    return transition_probs

def generate_sentence(transition_probs, start_word=None, length=10):
    if start_word is None:
        start_word = random.choice(list(transition_probs.keys()))
    
    sentence = [start_word]
    for _ in range(length - 1):
        if start_word not in transition_probs:
            break
        next_word = random.choices(
            list(transition_probs[start_word].keys()),
            weights=list(transition_probs[start_word].values())
        )[0]
        sentence.append(next_word)
        start_word = next_word
    
    return ' '.join(sentence)