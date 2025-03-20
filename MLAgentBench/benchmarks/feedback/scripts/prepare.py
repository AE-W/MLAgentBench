import subprocess
import pandas as pd
import os

taskname = "feedback-prize-english-language-learning"
# download_dir = f"benchmarks/{taskname}/env"
download_dir = "benchmarks/" + taskname + "/env"

# make sure the directory exixst
os.makedirs(download_dir, exist_ok=True)

input(f"Consent to the competition at https://www.kaggle.com/competitions/{taskname}/data; Press any key after you have accepted the rules online.")

subprocess.run(["kaggle", "competitions", "download", "-c", taskname], cwd=download_dir) 
subprocess.run(["unzip", "-n", f"{taskname}.zip"], cwd=download_dir) 
subprocess.run(["rm", f"{taskname}.zip"], cwd=download_dir) 

## split train to train and test in env
trainset = pd.read_csv(f"{download_dir}/train.csv")
trainset = trainset.sample(frac=1, random_state=42)
trainset = trainset.reset_index(drop=True)
trainset.iloc[:int(len(trainset)*0.7)].to_csv(f"{download_dir}/train.csv", index=False)
testset = trainset.iloc[int(len(trainset)*0.7):]
# split testset to only full_text and labels
testset.drop(['full_text'], axis=1).to_csv(f"answer.csv", index=False)
testset = testset.drop(['cohesion', 'vocabulary', 'syntax', 'phraseology', 'grammar', 'conventions'], axis=1).to_csv(f"{download_dir}/test.csv", index=False)





