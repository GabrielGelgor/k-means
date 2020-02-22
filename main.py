'''
Input:
m lines L
    L - a coordinate n-tuple for a training example, separated by a comma.
K
    K - the number of cluster centroids to be used.
e
    e - the number of epochs to run for
'''
import random as rand

#Function to select random starting points based off of the training examples. 
#Options for running multiple times is provided as a way to break out of local optima.
def randomInit(data, K, iterations=1):
    #while we have iterations left:
    centroids = []
    for iters in range(iterations):
        p_mu = []
        #while we haven't picked K centroids:
        while (len(p_mu) < K):
            #Pick a record index within the range of the data set
            attempt = rand.randint(0, len(data))
            #Have we already picked this index?
            if (len(p_mu) == 0):
                p_mu.append(data[attempt])
                continue

            for i in range(len(p_mu)):
                if (p_mu[i] == data[attempt]):
                    break
                
                #No: Store this number
                if (i == len(p_mu)-1):
                    p_mu.append(data[attempt])

        #add these centroid starting points to the output set of centroid starting points.
        centroids.append(p_mu[:])
    return centroids

def kmeans(data, centroids, epochs):
    #for every epoch of running:
        #for every datapoint:
            #set a temp min-distance as infinity
            #for every centroid:
                #determine the distance between the point and this centroid
                #Is this distance smaller than the minimum distance? If so:
                    #Set this point as a member of that cluster
                    #Update the minimum distance
            
            #Store this datapoint's cluster classification

        #for every centroid:
            #Sum every tuple in the cluster, then divide each dimension by the cardinality
            #Move the position of the centroid to here

        #NOTE: Print distortion here for debugging purposes.      
    pass

'''
Output:
Cluster array - A 2D array containing K clusters of training examples.
J - Distortion value for this run of k-means.
'''

data = []

with open("dataset_simple.txt") as file:
    for line in file:
        string = line[0:-2]
        data.append([float(i) for i in string.split(',')])

