import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Function to calculate embeddings (placeholder)
def calculate_embeddings(text):
    # Replace with actual embedding calculation
    return np.random.rand(10)

# Function to calculate site embedding
def calculate_site_embedding(page_embeddings):
    return np.mean(page_embeddings, axis=0)

# Function to calculate focus score and radius
def calculate_focus_score_and_radius(page_embeddings, site_embedding):
    distances = np.linalg.norm(page_embeddings - site_embedding, axis=1)
    focus_score = np.mean(distances)
    radius = np.std(distances)
    return focus_score, radius

# Streamlit app
st.title("SEO Topical Focus Tool")

# Input domains
domain1 = st.text_input("Enter first domain")
domain2 = st.text_input("Enter second domain")

# Input topics
topics = []
topic1 = st.text_input("Enter topic")
if st.button("Add Topic"):
    topics.append(topic1)

# Visualization type
visualization_type = st.selectbox("Choose Visualization Type", ["2D Visualization"])

# Submit button
if st.button("Submit"):
    if domain1 and topic1:
        # Placeholder for page embeddings
        page_embeddings = np.array([calculate_embeddings(f"Page {i}") for i in range(10)])
        site_embedding = calculate_site_embedding(page_embeddings)
        focus_score, radius = calculate_focus_score_and_radius(page_embeddings, site_embedding)

        # Display metrics
        st.write(f"Domain 1 Focus Score: {focus_score:.2f}")
        st.write(f"Domain 1 Radius: {radius:.2f}")

        # PCA for 2D visualization
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(page_embeddings)

        # Plot
        fig, ax = plt.subplots()
        ax.scatter(pca_result[:, 0], pca_result[:, 1])
        ax.set_xlabel("Principal Component 1")
        ax.set_ylabel("Principal Component 2")
        st.pyplot(fig)
    else:
        st.error("Please enter at least one domain and topic.")

# Run the app
if __name__ == "__main__":
    st.run()