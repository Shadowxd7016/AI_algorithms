## 🧠 Additional Core Algorithms Overview

This section provides a conceptual overview of the key algorithms that can be used to expand, optimize, or benchmark this autonomous robotic platform.

---

### 1. Genetic Algorithm (GA)
A Genetic Algorithm is an evolutionary optimization heuristic inspired by the process of natural selection. In robotic control, instead of manually designing or training a neural network using gradient descent, a GA can be used to "evolve" the optimal weights of the controller or find the best path configuration.

* **How it works**: It maintains a population of candidate solutions (represented as chromosomes). Each solution is evaluated using a **Fitness Function** (e.g., total distance traveled without colliding). The best-performing solutions are selected to pass their traits to the next generation via **Crossover** (combining parts of two solutions) and **Mutation** (introducing random modifications to prevent local minima entrapment).
* **Role in this project**: Can be deployed as an offline optimization loop to evolve the weights and biases of the neural network or to tune hyper-parameters without human intervention.

### 2. Expectimax Search
Expectimax is a game-theoretic decision-making algorithm used in artificial intelligence for environments that involve uncertainty or probabilistic outcomes (stochastic environments). It extends the classic Minimax algorithm by incorporating chance nodes.

* **How it works**: The algorithm builds a game/decision tree where the robot (Max node) attempts to maximize its expected reward (e.g., navigating smoothly), while the environment or obstacles act as **Chance nodes**. Instead of assuming an adversary will make the absolute worst-case move, it calculates the *expected value* of adjacent states based on the probabilities of environmental transitions.
* **Role in this project**: Useful for high-level tactical planning when ultrasonic sensor readings are noisy or when dynamic obstacles (like moving people) behave probabilistically.

### 3. K-Means Clustering
K-Means is an unsupervised machine learning algorithm designed to partition unlabelled data points into $K$ distinct, non-overlapping groups (clusters) based on spatial feature similarity.

* **How it works**: It randomly initializes $K$ cluster centroids. It then iteratively assigns each data point to its closest centroid (typically using Euclidean distance) and updates the centroid positions by calculating the mean of all points assigned to that cluster. This loop continues until centroid positions stabilize.
* **Role in this project**: Can be used to automatically categorize raw sensor states during exploratory drives. For instance, clustering raw distance vectors to discover hidden environmental topologies (e.g., automatically separating "Dead Ends", "T-Junctions", or "Corridors") without requiring manual labeling.

### 4. K-Nearest Neighbors (KNN)
KNN is a simple, non-parametric, instance-based supervised learning algorithm used for classification or regression tasks. 

* **How it works**: KNN does not explicitly learn a mathematical model during a training phase (lazy learning). Instead, it stores the entire training dataset. When a new sensor reading is received, the algorithm calculates the distance (e.g., Manhattan or Euclidean) between the new input and all stored instances, identifies the $K$ closest points, and assigns the label that has the majority vote among those neighbors.
* **Role in this project**: Serves as an alternative classification brain to the Multi-Layer Perceptron. It can classify the robot's next action (e.g., `"Move-Forward"` vs. `"Sharp-Right-Turn"`) directly by looking at how past paths match current real-time distance inputs.
