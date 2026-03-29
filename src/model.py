import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)
n_students = 1000

data = {
    'cgpa': np.round(np.random.uniform(6, 10, n_students), 2),
    'aptitude_score': np.random.randint(50, 100, n_students),
    'communication_score': np.random.randint(1, 10, n_students),
    'internships': np.random.randint(0, 3, n_students),
    'projects': np.random.randint(1, 5, n_students),
    'backlogs': np.random.randint(0, 3, n_students),
    'technical_skills': np.random.randint(1, 10, n_students)
}

df = pd.DataFrame(data)

# Logic: A student is 'Placed' (1) if they meet a weighted score threshold
# We add some 'noise' so the AI has to work to find the pattern
score = (df['cgpa'] * 2) + (df['internships'] * 1.5) + (df['projects'] * 0.8) - (df['backlogs'] * 2)
df['placement'] = (score > 16).astype(int)

# Save to your data folder
df.to_csv('placement_data.csv', index=False)
print("✅ placement_data.csv has been created in the data/ folder!")