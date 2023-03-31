
import matplotlib.pyplot as plt
import pandas as pd

class Mygraph(): 

        def drawgraph(self, output, input_ds, machineID, machineType):
            # We coud show it as an image, after we save it as an image
            # How are we gone build ur table
            # Description 
            
            print("From graph")

            print("Output from dataplot: ", output )
           
            x = output
            # The values 
            y  = input_ds
            
            # plotting the points 
            plt.plot(x, y)
            
            # naming the x axis
            plt.xlabel('x - Description')
            # naming the y axis
            plt.ylabel('y - Values')
            
            # giving a title to my graph 
            plt.title("For the"+ machineType +'Machine ID:'+ machineID)
            
            plt.savefig('Graph.png')

            # We want to overwire the graphs with the new data every iteration 


            # If we want to show it as an image inide of the application
            # self.Graph_img = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Graph.png")), size=(500, 150))

            #self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.Graph_img)
            # self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

            # function to show the plot
            plt.show()