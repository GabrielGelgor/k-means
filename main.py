'''
Input:
m lines L
    L - a coordinate n-tuple for a training example, separated by a comma.
K
    K - the number of cluster centroids to be used.
e
    e - the number of epochs to run for
'''

#NOTE: Distortion has random spikes then smooth declines, then random spikes then smooth declines. Possible cause in cluster assignment...

import random as rand
import math
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
            attempt = rand.randint(0, len(data)-1)
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


    #For every epoch of running:
    for epoch in range(epochs):
        distortion_data = []
        
        #Initialize clusters
        clusters = []
        for i in range(len(centroids)):
            clusters.append([])

        #for every datapoint:
        for point in (data):
            #set a temp min-distance as infinity
            min_dist = [math.inf] * len(point)
            cluster = None
            #for every centroid:
            for centroid in range(len(centroids)):
                #determine the distance between the point and this centroid
                dist = [abs(a - b) for a,b in zip(point,centroids[centroid])]
                #Is this distance smaller than the minimum distance? If so:
                for coord in range(len(point)):
                    if (dist[coord] > min_dist[coord]):
                        break
                    if (coord == (len(point) - 1)):
                        cluster = centroid
                        min_dist = dist[:]

                    #Set this point as a member of that cluster
                    #Update the minimum distance
            
            #Store this datapoint's cluster classification
            clusters[cluster].append(point)         #Clusters should be reset after every centroid move...
            distortion_data.append(min_dist)

        #for every centroid:
        for cluster in range(len(clusters)):
            mean = [0] * len(clusters[cluster][0])

            #Sum every tuple in the cluster, then divide each dimension by the cardinality
            for point in clusters[cluster]:
                mean = [a + b for a,b in zip(mean, point)]

            for point in range(len(mean)):
                mean[point] = mean[point]/len(clusters[cluster])
            
            #Move the position of the centroid to here
            centroids[cluster] = mean[:]

        #Print distortion here for debugging purposes.
        distortion = 0
        for dist in distortion_data:
            cur = [point ** 2 for point in dist]
            distortion += (sum(cur))
        distortion /= len(distortion_data)

        print("EPOCH", epoch, "DISTORTION:", distortion)
    
    return clusters, distortion


'''
Output:
Cluster array - A 2D array containing K clusters of training examples.
J - Distortion value for this run of k-means.
'''

data = []
final_clusters = []

with open("dataset_simple.txt") as file:
    for line in file:
        string = line[0:-2]
        data.append([float(i) for i in string.split(',')])

centroids = randomInit(data, 4)

for i in range (len(centroids)):
    final_clusters.append(kmeans(data,centroids[i], 50))

print(len(final_clusters))