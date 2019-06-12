#########################
######## Imports ########
#########################

import matplotlib.pyplot as plt
import numpy as np
import typing
import json

#########################
### Helper Functions ####
#########################

def user_input_json(pathname):
    with open(pathname) as json_file:
        data = json.loads(json_file.read())
        print(data)

def generate_graph():
    pass


def draw_graph():
    pass

#########################
##### Main Function #####
#########################

def main():
    user_input_json("./samples/sample1.json")

if __name__ == "__main__":
    main()
