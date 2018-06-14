# importing the required packages
from time import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import offsetbox
from sklearn import (manifold, datasets, decomposition, ensemble,
             discriminant_analysis, random_projection)
from sklearn.feature_selection import SelectKBest, chi2
# Loading and curating the data
digits = datasets.load_digits(n_class=10)
X = digits.data
y = digits.target
n_samples, n_features = X.shape
n_neighbors = 30


# Function to Scale and visualize the embedding vectors
def plot_embedding(X, title=None):
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)
    plt.figure()
    ax = plt.subplot(111)
    for i in range(X.shape[0]):
        plt.text(X[i, 0], X[i, 1], str(digits.target[i]),
                 color=plt.cm.Set1(y[i] / 10.), fontdict={'weight': 'bold', 'size': 9})
    if hasattr(offsetbox, 'AnnotationBbox'):
        # only print thumbnails with matplotlib> 1.0
        shown_images = np.array([[1., 1.]])  # just something big
        for i in range(digits.data.shape[0]):
            dist = np.sum((X[i] - shown_images) ** 2, 1)
            if np.min(dist) < 4e-3:
                # don't show points that are too close
                continue
            shown_images = np.r_[shown_images, [X[i]]]
            imagebox = offsetbox.AnnotationBbox(
                offsetbox.OffsetImage(digits.images[i], cmap=plt.cm.gray_r),
                X[i])
            ax.add_artist(imagebox)
    plt.xticks([]), plt.yticks([])
    if title is not None:
        plt.title(title)


def process_mode(modelname, model, X):
    print("Computing %s embedding" % modelname)
    t0 = time()
    # tsne = manifold.TSNE(n_components=2, init='random', random_state=0)
    x_trans = model.fit_transform(X)
    plot_embedding(x_trans,
                   "%s embedding of the digits (time %.2fs)" %
                   (modelname, time() - t0))


# ----------------------------------------------------------------------
# Plot images of the digits
n_img_per_row = 20
img = np.zeros((10 * n_img_per_row, 10 * n_img_per_row))
for i in range(n_img_per_row):
    ix = 10 * i + 1
    for j in range(n_img_per_row):
        iy = 10 * j + 1
        img[ix:ix + 8, iy:iy + 8] = X[i * n_img_per_row + j].reshape((8, 8))
plt.imshow(img, cmap=plt.cm.binary)
plt.xticks([])
plt.yticks([])
plt.title('A selection from the 64-dimensional digits dataset')

models = list()
models.append(['PCA', decomposition.PCA(n_components=2), X])
# models.append(['LDA', decomposition.LatentDirichletAllocation(n_components=2), X])
models.append(['TruncatedSVD', decomposition.TruncatedSVD(n_components=2), X])
models.append(['KernelPCA linear', decomposition.KernelPCA(n_components=2, kernel='linear'), X])
models.append(['FastICA', decomposition.FastICA(n_components=2), X])
models.append(['NMF', decomposition.NMF(n_components=2), X])
# 传说中的T-SNE，效果比PCA好多了，耗时比较长
models.append(['TSNE', manifold.TSNE(n_components=2, init='random', random_state=0), X])

for model in models:
    process_mode(*model)

plt.show()

