#!/usr/bin/python3
def multiple_returns(sentence):
    ln = len(sentence)
    if ln == 0:
        return None
    return (ln, sentence[0])
