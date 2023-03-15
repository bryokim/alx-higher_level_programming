#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        highest_score = max(a_dictionary.values())
        for key, score in a_dictionary.items():
            if score == highest_score:
                return key

    else:
        return None
