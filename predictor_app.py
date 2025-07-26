
import streamlit as st
import random

st.title("Coin Pattern Predictor")

st.write("Enter previous results (e.g., AABAC):")
input_sequence = st.text_input("History", "")

transitions = {}

if len(input_sequence) >= 2:
    for i in range(len(input_sequence) - 1):
        pair = input_sequence[i:i+1]
        next_char = input_sequence[i+1]
        if pair not in transitions:
            transitions[pair] = {}
        if next_char not in transitions[pair]:
            transitions[pair][next_char] = 0
        transitions[pair][next_char] += 1

    last_char = input_sequence[-1]
    prediction = None
    confidence = 0.0
    if last_char in transitions:
        next_moves = transitions[last_char]
        prediction = max(next_moves, key=next_moves.get)
        total = sum(next_moves.values())
        confidence = next_moves[prediction] / total

    st.subheader("Prediction")
    if prediction:
        st.write(f"**Next likely result: {prediction}**")
        st.write(f"Confidence: {confidence * 100:.1f}%")
    else:
        st.write("Not enough data to predict.")
else:
    st.write("Please enter at least 2 characters.")
