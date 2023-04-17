

class AddMachine: 


    def addmachine_event(self):
        print("Adding an machine")

        #We best read the size we wanna store, soo we get the best result. 
        # Read table, read all  
        def read_csv_file(): 
            df = pd.read_excel('tabel.xlsx')
            print(df)
            return df

        def print_tabel(self):
            df = pd.read_excel('tabel.xlsx')
            print(df)
    
            self.textbox.delete("0.0", "end")

            # Before printing we clean the output 
            for i in range(100): 
                        # We extract the row 
                        index_list = [i]
                        df.loc[df.index[index_list]]
                        print("ELEMENTS in tabel", index_list) 
                        
                        #we get an list of how many elements 
                        #print(df.loc[index_list,:])
                        # We print all the elements from the list 
                        # We want to reverse what we show:  
                        # We store in an array and we reverse the elements


                        self.textbox.insert("0.0", df.loc[index_list,:])

                        self.scrollable_label_button_frame.add_item("Config", i)


            # We need to read how many elements and than we can add the new one on the correct index 

        def createtableFanuc(self):
            print("Adding Fanuc")
            # Create multiple lists
            mdescription = [self.combobox_1_1.get()]
            machinetype = ["Fanuc"]
            Protocol = ["EU 63"]
            IP = ["x.x.x.x.x"]
          
            columns=['mdescription','Machinetype','Protocol','IP']
            newdf = pd.DataFrame(list(zip(mdescription, machinetype, Protocol, IP)), columns=columns)
            Olddf = read_csv_file()
            df_row_merged = pd.concat([Olddf, newdf], ignore_index=True)
            df_row_merged.to_excel('tabel.xlsx', index=None)
            

        def createtableArburg(self): 
            print("Adding Arburg")
            # Create multiple lists
            machinetype = ["Arburg"]
            Protocol = ["OPC UA"]
            username = [self.combobox_1.get()]
            endpoint = [self.combobox_3.get()]
            addressNs = [self.combobox_4.get()]
            password = [' ']
            columns=['Machinetype','Protocol','Username','Password', 'Endpoint', 'AddressNs']

            # Create DataFrame from multiple listss
            newdf = pd.DataFrame(list(zip(machinetype,Protocol,username, password, endpoint, addressNs)), columns=columns)

            # We wanna first read the table and write one more than the last index.

            Olddf = read_csv_file()

            # We add the old data frame to the new one:
        
            df_row_merged = pd.concat([Olddf, newdf], ignore_index=True)

            df_row_merged.to_excel('tabel.xlsx', index=None)

            # After we add an table, we also print it 
            
            print(self.tabview.get())
           
            # Wanna remove an configuration click on remove

            # We have  to make ur table and than be able to retrive the data: 
            # We add than every time and index more than the last. 
        
        if (self.tabview.get() == "Arburg" ): 
            print("if Arburg")
            createtableArburg(self)
            print_tabel(self)
            #read_csv_file()
            #get_data()

        elif (self.tabview.get() == "Fanuc" ):
            print("if Fanuc")
            createtableFanuc(self)
            print_tabel(self)
            #read_csv_file()
            #get_data()


        # We coud call an other function 
        # Before we load the tabel already esxiting
        # We select an csv file we wanna add
        # We read it
        # We add one position more
        # We load the new table


    # We load the data from the tabel on the start 