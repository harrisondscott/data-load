import os

os.system("mongoimport --type csv -d weather -c user_info --headerline --drop sample_data.csv")
