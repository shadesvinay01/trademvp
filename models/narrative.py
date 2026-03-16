from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

class NarrativeCluster:

    def __init__(self, clusters=5):

        self.vectorizer = TfidfVectorizer(
            max_features=100,
            stop_words="english"
        )

        self.kmeans = KMeans(n_clusters=clusters)

    def cluster(self, tweets):

        X = self.vectorizer.fit_transform(tweets)

        labels = self.kmeans.fit_predict(X)

        return labels
