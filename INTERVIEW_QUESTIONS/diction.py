database={"name":"vipin","name":"mathew"}#if we provide 2 keys the second one will override the first one 
print(database["name"])


database2={"vipin":"mathew","ebin":"123"}

x=[[key,value] for key,value in enumerate(database2)]
print(x)