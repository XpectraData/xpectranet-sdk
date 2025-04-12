def score_emotion_divergence(current, previous):
    emotion_pairs = {
        ("awe", "grief"): 0.8,
        ("grief", "awe"): 0.8,
        ("hope", "doubt"): 0.6,
        ("doubt", "hope"): 0.6,
        ("awe", "awe"): 0.0,
        ("grief", "grief"): 0.0
    }
    return emotion_pairs.get((current, previous), 0.5)
