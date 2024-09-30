import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


def main():

    st.markdown("# Exploratory Clustering")

    seed = st.number_input("Random Seed", 0, value=0, step=1)

    fig, ax = plt.subplots()

    np.random.seed(seed)
    x = np.random.normal(2, 2, 200)
    y = np.random.normal(3, 1, 200)

    ax.scatter(x, y)
    ax.set_xlim([2 - 3 * 2, 2 + 3 * 2])
    ax.set_ylim([3 - 3 * 2, 3 + 3 * 2])
    ax.set_xlabel("x-axis", fontsize=20)
    ax.set_ylabel("y-axis", fontsize=20)
    ax.set_title("Random scatter plot", fontsize=20)

    st.pyplot(fig=fig)


if __name__ == "__main__":
    main()
