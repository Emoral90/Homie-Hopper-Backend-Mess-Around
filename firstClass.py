
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Possible class structure for handling back end of Homie Hopper
# There will be 3 classes: User, Math, and Data
#   User: will store an individual user's data
#   Math: will store euclidean distance as d, pearson correlation coefficient as r, and
#   use user data from the user class
#   Data: will extract and format necessary user data from the json
# 
# ALL CLASS STRUCTURES ARE SUBJECT TO CHANGE
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import numpy as np
import json
import math

class User:
    '''
    A class to organize and choose which user's data will be returned. There will be one member attribute: ID_intr. There will be one member method assign_data() to reorganize and elect which user's data will be returned.
    ID_intr, stands for ID and Interests, will save the extracted data to its own variable. It will then be passed in as a parameter to choose which specific users to eventually return and use in the custom Math class.
    '''
    def __init__(self):
        self.ID_intr = {}

    def assign_data(data):
        # figure out how to assign different user ids and answers to individual users
        pass            

class Math:
    '''
    A class to handle user data and calculate similarity values. 4 member attributes: user1_data, user2_data as dictionaries, and d, r as floating point integers, and 2 member methods: euclid_distance(), and pearson_coeffictient().
    Where user1_data and user2_data will be passed in as parameters, d is Euclidean distance between 2 points and r is Pearson's correlation coefficient will be calculated from within the class structure.
    '''

    # Pass in data as parameters as data?
    def __init__(self):
        self.user1_data = {}
        self.user2_data = {}
        self.d = 0.0
        self.r = 0.0

    def euclid_distance(self):
        self.d = math.sqrt(sum(pow(a - b, 2) for a, b in zip(self.user1_data, self.user2_data)))
        print(self.d)
        return self.d

    def pearson_coefficient(self):
        X = np.array(self.user1_data)
        Y = np.array(self.user2_data)

        mean_x = np.mean(X)
        mean_y = np.mean(Y)

        dev_x = X - mean_x
        dev_y = Y - mean_y

        sum_prod_devs = np.sum(dev_x * dev_y)

        std_dev_x = np.std(X)
        std_dev_y = np.std(Y)

        self.r = sum_prod_devs / (len(X) * std_dev_x * std_dev_y)

        print(self.r)
        return self.r

class Data:
    '''
    A class to extract all necessary user data from a JSON file. There will be 3 member attributes: interests, ids, data_dict. There will be 1 member method: process_data().
    interests and ids will be used as variables to be assigned the original userInterests and userID data from the JSON. Where data_dict will be intialized as a blank dictionary and be used to save the necessary data with the userIDs as the keys, and userInterests as an embedded dictionary of keys and values.
    '''
    def __init__(self):
        self.interests = None
        self.ids = None
        self.data_dict = {}

    def process_data(self):
        with open(r"users.json") as file:
            # Load the file from Firebase as a json object
            profile_json = json.load(file)

            # Loop through 
            for profile in profile_json:
                # Assign the original userID and userInterests data to temporary variables
                self.ids = profile["userID"]
                self.interests = profile["userInterests"]

                # Assign the userInterests with the userID to the empty dictionary
                self.data_dict[self.ids] = self.interests

            return self.data_dict
        

def main():
    D = Data()   # Extract all necessary user data, to pass to User()
    U = User()   # reorganize data and choose users, to pass to Math()
    M = Math()   # Calculate the distance (d) and pearson coefficient (r) for the users chosen

    # P.S. This program can be run as is if you would like to see the extracted data for yourself ^_^
    D.process_data()
    extracted_data = D.process_data()
    print(extracted_data)
    print(type(extracted_data))



if __name__ == "__main__":
    main()