'''
Input:
m lines L
    L - a coordinate n-tuple for a training example, separated by a comma.
K
    K - the number of cluster centroids to be used.
e
    e - the number of epochs to run for
'''

#Function to select random starting points based off of the training examples. 
#Options for running multiple times is provided as a way to break out of local optima.
def randomInit(data, K, iterations=1):
    #while we have iterations left:
        #while we haven't picked K centroids:
            #Pick a record index within the range of the data set
            #Have we already picked this index?
            #No:
                #Store this number

        #add these centroid starting points to the output set of centroid starting points.
    pass

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

#TODO: Parse incoming data.