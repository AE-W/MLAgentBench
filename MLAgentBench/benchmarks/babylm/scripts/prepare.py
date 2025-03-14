import subprocess
import pandas as pd

taskname = "babylm"
download_dir = "../env"

subprocess.run(["wget", "https://github.com/babylm/babylm.github.io/raw/main/babylm_10M.zip"], cwd=download_dir) 
subprocess.run(["unzip", "-n", f"babylm_10M.zip"], cwd=download_dir)
subprocess.run(["rm", f"babylm_10M.zip"], cwd=download_dir)
subprocess.run(["rm", "-rf", f"babylm_data/babylm_10M"], cwd=download_dir)
subprocess.run(["rm", "-rf", f"__MACOSX"], cwd=download_dir)