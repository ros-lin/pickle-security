"""
Create sample pickle file.
"""
import pickle as pkl
import os


root = os.getcwd()

with open(f"{root}/container/sample.pkl", "wb") as file:
    pkl.dump("Hello World!", file)
    