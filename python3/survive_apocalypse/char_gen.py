#!/usr/bin/env python

from random import choice

temperaments = ["sanguine", "choleric", "melancholic", "phlegmatic"]
personalities = ["introvert", "extrovert"]
# Based on the former job will be the starting inventory
former_jobs = ["a fireman", "a policeman", "a medic", "unemployed", "a doctor", "a demolitions expert", "an IT guy", "an accountant"]

def generate_character():
    results = []
    results.append(choice(personalities))
    results.append(choice(temperaments))
    return results