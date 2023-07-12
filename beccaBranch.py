import numpy as np
import json
import math
from operator import attrgetter

class UserIdComparisonVal():
    def __init__(self, userid, val):
        self.userid = userid
        self.val = val

    def __repr__(self):
        return f'UserIdComparisonVal("{self.userid}","{self.val}")'

class User():
    name = str()
    interests = dict()
    userID = str()
    sortedEucDists = dict()

    def __init__(self):
        self.ID_intr = {}

    def __repr__(self):
        return f'User("{self.userID}","{str(self.sortedEucDists)}")'

    def assign_data(self, data):
        # figure out how to assign different user ids and answers to individual users
        self.userID = data["userID"]
        self.name = data["userName"]
        self.interests = data["userInterests"]

    def get_interests(self):
        return self.interests

class Math:
    def __init__(self):
        self.d = 0.0
        self.r = 0.0

    def euclid_distance(user1_data, user2_data):
        # self.d = math.sqrt(sum(pow(a - b, 2) for a, b in zip(user1_data, user2_data)))
        sum = 0
        for i in range(1, len(user1_data)):
            sum += pow(user1_data["q"+str(i)] - user2_data["q"+str(i)], 2)
        return math.sqrt(sum)

    def pearson_coefficient(self):
        X = np.array(self.user1_data)
    def pearson_coefficient(self):

        print(self.r)
        return self.r

class Comparison:
    """
    Holds comparison data between the client and the users
    Calls Math class
    """
    comp_users = list()

    pass

class Data:
    '''
    dictionary of keys and values.
    '''
    def __init__(self):
        self.data_dict = {}
    def process_data(self):
        with open(r"users.json") as file:
            # Load the file from Firebase as a json object
            profile_json = json.load(file)
            # Loop through 
            for profile in profile_json:
                # Assign the original userID and userInterests data to temporary variables
                U = User()
                U.assign_data(profile)
                # self.id = profile["userID"]
                # self.interests = profile["userInterests"]
                # Assign the userInterests with the userID to the empty dictionary
                self.data_dict[U.userID] = U

            return self.data_dict

    def calc_euc_dists(self, userid):
        interests = self.data_dict[userid].interests
        compVals = []
        for i in self.data_dict:
            user = self.data_dict[i]
            if userid != user.userID:
                ed = Math.euclid_distance(interests, user.interests)
                compVals.append(UserIdComparisonVal(user.userID, ed))

        #print(compVals)
        compVals = sorted(compVals, key=attrgetter('val'))
        print(compVals)
        self.data_dict[userid].sortedEucDists = compVals


def main():
    D = Data()   # Extract all necessary user data, to pass to User()

    extracted_data = D.process_data()

    print(type(extracted_data))

    user1_data = extracted_data["0zJNMsXJusc0eSjAsLpJiK2qKFA3"].interests
    #print(user1_data)
    user2_data = extracted_data["23YTrKsZbfahA72gd0zlXXgTzRb2"].interests
    #print(user2_data)

    ed = Math.euclid_distance(user1_data, user2_data)
    #print(ed)

    D.calc_euc_dists("0zJNMsXJusc0eSjAsLpJiK2qKFA3")
    #print(D.data_dict["0zJNMsXJusc0eSjAsLpJiK2qKFA3"])

    # for i in extracted_data:
    #     M.euclid_distance()

if __name__ == "__main__":
    main()