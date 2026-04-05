import numpy as np

def distance(a, b):
	return np.sqrt(((a-b)**2).sum(axis=1))

def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	# Your code here
	points = np.array(points, dtype=float)
	centroids = np.array(initial_centroids, dtype=float)
	for iteration in range(max_iterations):
		# compute distance
		distances = np.array([distance(points, centroid) for centroid in centroids])
		# assignments
		assignments = np.argmin(distances, axis=0)
		# compute new centroids
		new_centroids = np.array([points[assignments == i].mean(axis=0) if len(points[assignments == i]) > 0 else centroids[i] for i in range(k)])
		# check convergence
		if np.all(centroids == new_centroids):
			break
		centroids = new_centroids
		centroids = np.round(centroids, 4)

	return [tuple(centroid) for centroid in centroids]
