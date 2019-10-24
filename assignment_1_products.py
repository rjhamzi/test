import csv
class Products:
    def __init__(self):
        pass

    def file_reader(self):
        file_list = []
        with open('E:\Python 2.7\products.csv',mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                file_list.append(row)
        return file_list

    def display_category(self):
        prod1 = Products()
        unset_list = []
        set_list = []
        for row in prod1.file_reader():
            unset_list.append(row["category"])
        set_unset = set(unset_list)
        for ele in set_unset:
            set_list.append(ele)
        print set_list

    def display_filters(self):
        prod1 = Products()
        for row in prod1.file_reader():
            print row["brand"],row["color"],row["size"],row["price"]

    def max_price(self,max_value):
        prod1 = Products()
        max = 0
        num =0
        line_count = 0
        for row in prod1.file_reader():
            if max < int(row["price"]):
                max = int(row["price"])
        for row in prod1.file_reader():
            if line_count == 0:
                print {", ".join(row)}
                line_count += 1
            if max == int(row["price"]):
                if num ==max_value:
                    break
                print row["product_id"],row["title"]
                num+=1
            line_count+=1
        print "Lines count {0}".format(line_count)
    def mini_price(self,mini_value):
        prod1 = Products()
        min = 1000000
        num =0
        line_count = 0
        for row in prod1.file_reader():
            if min > int(row["price"]):
                min = int(row["price"])
        for row in prod1.file_reader():
            if line_count == 0:
                print {", ".join(row)}
                line_count += 1
            if min == int(row["price"]):
                if num ==mini_value:
                    break
                print row["product_id"],row["title"]
                num+=1
            line_count+=1
        print "Lines count {0}".format(line_count)

    def top_rated(self,max_items):
        line_count = 0
        max = 0
        num = 0
        prod1 = Products()
        for row in prod1.file_reader():
            if max < int(row["rating"]):
                max = int(row["rating"])
        for row in prod1.file_reader():
            if line_count == 0:
                print {", ".join(row)}
                line_count += 1
            if max == int(row["rating"]):
                if num == max_items:
                    break
                print row["product_id"], row["title"]
                num+=1
            line_count += 1
        print "Lines count {0}".format(line_count)

    def latest_products(self,latest_value):
        prod1 = Products()
        num = 0
        line_count = 0
        list_dates = []
        for row in prod1.file_reader():
            list_dates.append(row["arrival_date"])
        list_dates.sort()
        for row in prod1.file_reader():
            if line_count == 0:
                print {", ".join(row)}
                line_count += 1
            if row["arrival_date"] == list_dates[0]:
                if num == latest_value:
                    break
                print row["product_id"], row["title"]
                num+=1
            line_count += 1
        print "Lines count {0}".format(line_count)



myproduct = Products()
myproduct.display_category()
myproduct.display_filters()
print "1.  show max price 10 items"
print "2.  show min price 10 items"
print "3.  show top rated 10 items"
print "4.  show latest 10 items"
a = int(raw_input())
if a is 1:
    myproduct.max_price(10)
elif a is 2:
    myproduct.mini_price(10)
elif a is 3:
    myproduct.top_rated(10)
elif a is 4:
    myproduct.latest_products(10)
