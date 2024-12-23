import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def plot_histogram(data, column, title=None, bins=30):
    """
    Plot a histogram for the specified column in the dataframe.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        The input dataframe
    column : str
        The column name to plot
    title : str, optional
        The title for the plot
    bins : int, optional
        Number of bins for the histogram
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x=column, bins=bins)
    if title:
        plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

def plot_boxplot(data, column, title=None):
    """
    Create a boxplot for the specified column.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        The input dataframe
    column : str
        The column name to plot
    title : str, optional
        The title for the plot
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=data[column])
    if title:
        plt.title(title)
    plt.xlabel(column)
    plt.show()

def plot_heatmap(correlation_matrix, title=None):
    """
    Create a heatmap from a correlation matrix.
    
    Parameters:
    -----------
    correlation_matrix : pandas.DataFrame
        The correlation matrix to plot
    title : str, optional
        The title for the plot
    """
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    if title:
        plt.title(title)
    plt.show()

def scatter_pca(data, features, title=None):
    """
    Create a PCA scatter plot of the data.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        The input dataframe
    features : list
        List of column names to use for PCA
    title : str, optional
        The title for the plot
    """
    # Standardize the features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(data[features])
    
    # Apply PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(scaled_features)
    
    # Create the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(pca_result[:, 0], pca_result[:, 1], alpha=0.5)
    plt.xlabel(f'First PC (Explained variance ratio: {pca.explained_variance_ratio_[0]:.3f})')
    plt.ylabel(f'Second PC (Explained variance ratio: {pca.explained_variance_ratio_[1]:.3f})')
    if title:
        plt.title(title)
    plt.show()

def plot_pie_chart(data, title=None, figsize=(10, 8)):
    """
    Create a pie chart from a pandas Series (like value_counts()).
    
    Parameters:
    -----------
    data : pandas.Series
        The data to plot (typically result of value_counts())
    title : str, optional
        The title for the plot
    figsize : tuple, optional
        Figure size as (width, height)
    """
    plt.figure(figsize=figsize)
    plt.pie(data.values, 
            labels=data.index,
            autopct='%1.1f%%',
            startangle=90)
    if title:
        plt.title(title)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.show()

def plot_bar_chart(data, title=None, figsize=(12, 6), rotation=45):
    """
    Create a bar chart visualization.
    
    Parameters:
    -----------
    data : pandas.Series or DataFrame
        The data to plot. If Series, index will be x-axis and values will be y-axis.
    title : str, optional
        The title of the plot
    figsize : tuple, optional
        Figure size as (width, height)
    rotation : int, optional
        Rotation angle for x-axis labels
    """
    plt.figure(figsize=figsize)
    
    if isinstance(data, pd.Series):
        plt.bar(data.index, data.values)
    else:
        plt.bar(data[data.columns[0]], data[data.columns[1]])
    
    plt.xticks(rotation=rotation, ha='right')
    
    if title:
        plt.title(title)
    
    plt.tight_layout()
    plt.show()