class ViewMalopolskaAreaContainer():

    def pprint_one_column_collection(self, collection, table_header=None):
        print(self.set_elements_of_table_construction()[0],
              self.set_elements_of_table_construction(table_header)[2],
              sep='\n')
        for i in collection:
            print(self.set_elements_of_table_construction()[1],
                  "|{}|{}|".format('{:>4}'.format(i[1]), '{:31}'.format(i[0])),
                  sep='\n')
        print(self.set_elements_of_table_construction()[0])

    def pprint_two_columns_collection(self, collection, table_header=None):
        print("\n\nFound " + str(len(collection)) + " location(s):\n\n",
              self.set_elements_of_table_construction()[4],
              self.set_elements_of_table_construction(table_header)[3],
              self.set_elements_of_table_construction()[5],
              sep='\n')
        for i in collection:
            print("|{}|{}|".format('{:26}'.format(i[0]), '{:25}'.format(i[1])))
        print(self.set_elements_of_table_construction()[4])

    def pprint_lines(self, collection, table_header):
        print("\n" + table_header + "\n")
        for i in collection:
            print("{}. {}".format(collection.index(i) + 1, i))

    def set_elements_of_table_construction(self, header=None):
        return ["@------------------------------------@",
                "|----+-------------------------------|",
                "|" + str(header) + "                         |",
                "| LOCATION                 | TYPE                    |",
                "@----------------------------------------------------@",
                "|--------------------------+-------------------------|"]
