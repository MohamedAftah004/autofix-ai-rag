from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.data.loader import load_faults


class FaultRetriever:
    def __init__(self):
        self.df = load_faults()

        self.df["search_text"] = (
            self.df["fault"].astype(str)
            + " "
            + self.df["description"].astype(str)
        )

        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            min_df=1,
            max_df=0.9
        )

        self.vectors = self.vectorizer.fit_transform(
            self.df["search_text"]
        )

    def retrieve(
        self,
        description: str,
        car_model: str,
        min_confidence: float = 0.25
    ):
        query = f"{description} {car_model}"
        query_vec = self.vectorizer.transform([query])

        similarities = cosine_similarity(query_vec, self.vectors)[0]

        best_idx = similarities.argmax()
        best_score = float(similarities[best_idx])

        # 🚨 هنا القرار المهم
        if best_score < min_confidence:
            return None

        record = self.df.iloc[best_idx].to_dict()
        record["confidence"] = best_score
        return record