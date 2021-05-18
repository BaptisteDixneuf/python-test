import os
import shutil

for root, dirs, files in os.walk("folder_exercise"):  
   
   for dir in dirs:
        full_dir = os.path.join(root,dir)
        print("full_dir", full_dir)

        dest = full_dir.replace("folder_exercise", "dest")
        print("dest",dest)

        if not os.path.exists(dest):
            os.makedirs(dest)
   
   
   for file in files:
      
        path_file = os.path.join(root,file)
        print("form", path_file)
        
        dest = path_file.replace("folder_exercise", "dest")
        print("dest",dest)

        if dest[-3:] == ".py":
            shutil.copy2(path_file,dest) 
    