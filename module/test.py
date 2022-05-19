
import os

def test():
    path="dataset/"
    
    list_dir = os.listdir(path)
    print(list_dir)


    for i in range(len(list_dir)):  
        path_imgs = path + list_dir[i]
        print(path_imgs) # dossier
        list_images = os.listdir(path_imgs)
        
        for i in range(len(list_images)):
            imagePath = path_imgs + '/' + list_images[i]
            print(imagePath)
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            print("------>id " + str(id))

        
test()