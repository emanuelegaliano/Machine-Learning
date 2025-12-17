import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

# Dataset 2D
X, y = make_moons(n_samples=300, noise=0.25, random_state=0)  # y in {0,1}

# AdaBoost (SAMME) con decision stump
T = 50
base = DecisionTreeClassifier(max_depth=1, random_state=0)

clf = AdaBoostClassifier(
    estimator=base,          # se la tua versione è più vecchia: base_estimator=base
    n_estimators=T,
    learning_rate=1.0,
    algorithm="SAMME",
    random_state=0
)
clf.fit(X, y)

# Round da visualizzare (2x2)
rounds = [1, T // 4, T // 2, T]
titles = ["t = 1", f"t = {T//4}", f"t = {T//2}", f"t = {T} (finale)"]

# Predizione dell'ensemble troncato ai primi t weak learners (SAMME)
def predict_partial_samme(clf, Xgrid, t):
    estimators = clf.estimators_[:t]
    alpha = clf.estimator_weights_[:t]

    # score in {-inf,+inf}: somma pesata dei voti
    scores = np.zeros(Xgrid.shape[0], dtype=float)
    for a, h in zip(alpha, estimators):
        pred = h.predict(Xgrid)          # {0,1}
        vote = 2 * pred - 1              # -> {-1,+1}
        scores += a * vote

    return (scores >= 0).astype(int)

# Meshgrid per boundary
x_min, x_max = X[:, 0].min() - 0.8, X[:, 0].max() + 0.8
y_min, y_max = X[:, 1].min() - 0.8, X[:, 1].max() + 0.8
xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 400),
    np.linspace(y_min, y_max, 400)
)
Xgrid = np.c_[xx.ravel(), yy.ravel()]

# Plot 2x2
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.ravel()

for ax, t, title in zip(axes, rounds, titles):
    Z = predict_partial_samme(clf, Xgrid, t).reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.35)
    ax.scatter(X[:, 0], X[:, 1], c=y, s=18, edgecolors="k", linewidths=0.3)
    ax.set_title(title)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

plt.tight_layout()
plt.savefig("adaboost_boundaries.png", dpi=200)
plt.show()
