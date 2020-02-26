'''
Input:
m lines L
    L - a coordinate n-tuple for a training example, separated by a comma.
K
    K - the number of cluster centroids to be used.
e
    e - the number of epochs to run for
'''


from matplotlib import pyplot as plt 
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

def scatterplot2D(clusters, centroids, epoch='end'):
    #set up graph space
    x_vec = []
    y_vec = []
    plt.style.use('seaborn-whitegrid')
    plt.subplot(111)
    ax = plt.gca()

    #for each cluster:
    for cluster in range(len(clusters)):
        #for each point in the cluster:
        for point in clusters[cluster]:
            #add the x to the x vector
            x_vec.append(point[0])
            #add the y to the y vector
            y_vec.append(point[1])
        
        #Plot the cluster, with its label being its cluster name
        color = next(ax._get_lines.prop_cycler)['color']
        plt.scatter(x_vec, y_vec, s=5, marker='o', label="cluster '{0}'".format(cluster), cmap='viridis', color=color)
        x_vec = []
        y_vec = []

    #for each centroid
    for point in centroids:
        #add the x to the x vector
        x_vec.append(point[0])
        #add the y to the y vector
        y_vec.append(point[1])

    #plot the centroids so their progress can be mapped.
    color = next(ax._get_lines.prop_cycler)['color']
    plt.scatter(x_vec, y_vec, s=5, marker='o', label="Centroids", cmap='viridis', color=color)

    #Show the plot, save it.
    plt.title('Clustering post epoch '+str(epoch))
    plt.savefig('results/epoch'+str(epoch)+'.png')
    plt.clf()

def kmeans(data, centroids, epochs):
    prev_distortions = []

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
            min_dist = math.inf
            cluster = None
            #for every centroid:
            for centroid in range(len(centroids)):
                #determine the distance between the point and this centroid
                dist = [abs(a - b) for a,b in zip(point,centroids[centroid])]
                #Calculate the euclidean distance between the current centroid and point.
                euc_dist = 0
                for coord in range(len(point)):
                    euc_dist += dist[coord] ** 2
                
                #Is this distance smaller than the minimum distance? If so:
                euc_dist = math.sqrt(euc_dist)
                if (euc_dist < min_dist):
                    #Set this point as a member of that cluster
                    min_dist = euc_dist
                    #Update the minimum distance
                    cluster = centroid

            #Store this datapoint's cluster classification
            clusters[cluster].append(point)
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
            cur = dist ** 2
            distortion += cur
        distortion /= len(distortion_data)
        prev_distortions.append(distortion)

        print("EPOCH", epoch, "DISTORTION:", distortion)

        for i in range(len(prev_distortions)-1, -1, -1):
            if (i == len(prev_distortions)-1):
                current = prev_distortions[i]
                count = 1
                continue
            if (prev_distortions[i] == current):
                count += 1
            
        if count == 3:
            print("CONVERGENCE ACHIEVED")
            break
    
    
        #scatterplot2D(clusters,centroids, epoch)
    return clusters, distortion


'''
Output:
Cluster array - A 2D array containing K clusters of training examples.
J - Distortion value for this run of k-means.
'''

data = []
final_clusters = []
distortions = []

with open("dataset_simple.txt") as file:
    for line in file:
        string = line[0:-2]
        data.append([float(i) for i in string.split(',')])


K = int(input("How many clusters would you like to form? "))
epochs = int(input("How many epochs would you like to run for? "))
repeat = int(input('How many times would you like to repeat the process (takes best run to avoid local optima)? '))

centroids = randomInit(data, K, repeat)

for i in range (len(centroids)):
    result = kmeans(data,centroids[i], epochs)
    final_clusters.append(result[0])
    distortions.append(result[1])

best_i = distortions.index(min(distortions))
print("BEST RUN: "+str(best_i),"\nDISTORTION: "+str(distortions[best_i]))
best = final_clusters[best_i]
scatterplot2D(best,centroids[best_i],epochs)