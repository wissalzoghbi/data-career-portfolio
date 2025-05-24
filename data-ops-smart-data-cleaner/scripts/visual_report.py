import matplotlib.pyplot as plt
import seaborn as sns

def generate_visual_report(df, output_dir="outputs"):
    import os
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # Missing Values heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
    plt.title("Missing values Heatmap")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "missing_heatmap.png"))
    plt.close()
    
    
    # Missing values count barplot
    null_counts = df.isnull().sum()
    null_counts = null_counts[null_counts > 0]
    if not null_counts.empty:
        plt.figure(figsize=(12, 6))
        null_counts.sort_values(ascending=False).plot(kind="bar")
        plt.title("Missing Values per Column")
        plt.ylabel("Count")
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "missing_values_barplot.png"))
        plt.close()

    # Histogram for numeric data
    numeric_cols = df.select_dtypes(include=["int", "float"]).columns
    df[numeric_cols].hist(figsize=(16, 12), bins=30)
    plt.suptitle("Numeric Column Distributions")
    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.savefig(os.path.join(output_dir, "numeric_histograms.png"))
    plt.close()

    print("Visual report saved to:", output_dir)