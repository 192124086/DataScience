import pandas as pd
df = pd.read_csv("review.csv")
likes_distribution = df['comments'].value_counts().reset_index()
likes_distribution.columns = ['Comments', 'Frequency']
print("Review Frequency Distribution:")
print(likes_distribution)
