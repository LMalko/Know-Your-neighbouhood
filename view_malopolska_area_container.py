class ViewMalopolskaAreaContainer():

    def pprint_one_column_collection(self, collection, table_header):
        top_and_bottom_table = "@------------------------------------@"
        print(top_and_bottom_table)
        print("|" + str(table_header) + "                         |")
        for i in collection:
            print("|----+-------------------------------|")
            print("|{}|{}|".format('{:>4}'.format(i[1]), '{:>31}'.format(i[0])))
        print(top_and_bottom_table)
