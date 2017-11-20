class ViewMalopolskaAreaContainer():

    def pprint_one_column_collection(self, collection, column_name="MAŁOPOLSKIE"):
        top_and_bottom_table = "@------------------------------------@"
        print(top_and_bottom_table)
        print("|       " + str(column_name) + "                  |")
        for i in collection:
            print("|----+-------------------------------|")
            print("|{}|{}|".format('{:>4}'.format(i[1]), '{:>31}'.format(i[0])))
        return top_and_bottom_table
