# import fetch_repo function from ucimlrepo
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
tetouan = fetch_ucirepo(id=849) 
  
# data (as pandas dataframes) 
X = tetouan.data.features 
y = tetouan.data.targets 
  
# metadata 
print(tetouan.metadata) 
  
# variable information 
print(tetouan.variables) 