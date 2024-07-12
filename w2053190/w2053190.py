# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20230183
# Date: 12-12-2023

from graphics import *

credit_pass = 0
credit_defer = 0
credit_fail = 0
count_progress = 0
count_mtrailer = 0
count_exclude = 0
count_mretriever = 0
valid_ranges = [0, 20, 40, 60, 80, 100, 120]
progress_data = []
module_trailer_data = []
module_retriever_data = []
exclude_data = []

def predict_results(credit_pass, credit_defer, credit_fail):
    global count_progress, count_mtrailer, count_exclude, count_mretriever
    
    while True:
        try:
            credit_pass = int(input("\nEnter your total pass credits: "))
            if credit_pass not in valid_ranges:
                print("Out of Range")
            else:
                break
        except ValueError:
            print('Integer required')

    while True:
        try:
            credit_defer = int(input("Enter your total defer credits: "))
            if credit_defer not in valid_ranges:
                print("Out of Range")
            else:
                break
        except ValueError:
            print('Integer required')

    while True:
        try:
            credit_fail = int(input("Enter your total fail credits: "))
            if credit_fail not in valid_ranges:
                print("Out of Range")
            else:
                break
        except ValueError:
            print('Integer required')

    if credit_pass + credit_defer + credit_fail != 120:
        print("\nTotal Incorrect")
    else:
        if credit_pass == 120:
            print("progress")
            count_progress += 1
            progress_data.append([credit_pass, credit_defer, credit_fail])

        elif credit_pass == 100:
            print("progress(module trailer)")
            count_mtrailer += 1
            module_trailer_data.append([credit_pass, credit_defer, credit_fail])

        elif credit_fail >= 80:
            print("exclude")
            count_exclude += 1
            exclude_data.append([credit_pass, credit_defer, credit_fail])

        else:
            print("do not progress - module retriever")
            count_mretriever += 1
            module_retriever_data.append([credit_pass, credit_defer, credit_fail])

predict_results(credit_pass, credit_defer, credit_fail)

while True:
    continue_prompt = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
    if continue_prompt == 'y':
        predict_results(credit_pass, credit_defer, credit_fail)
    elif continue_prompt == 'q':

        def draw_histogram(count_progress, count_mtrailer, count_exclude, count_mretriever):
            win = GraphWin("Histogram", 600, 500)
            label = Text(Point(300, 20), 'Histogram Results')
            label.setSize(14)
            label.draw(win)
            
            def draw_bar(x, height, color, label_text):
                box = Rectangle(Point(x - 46, 430), Point(x + 46, 430 - height * 10))
                box.setFill(color)
                box.draw(win)
                label = Text(Point(x, 440), label_text)
                label.setSize(11)
                label.draw(win)
                label2 = Text(Point(x, 420 - height * 10), height)
                label2.setSize(11)
                label2.draw(win)

            draw_bar(120, count_progress, "light green", "Progress")
            draw_bar(240, count_mtrailer, "dark green", "Module Trailer")
            draw_bar(360, count_mretriever, "green", "Module Retriever")
            draw_bar(480, count_exclude, "pink", "Exclude")

            total_count = count_progress + count_mtrailer + count_exclude + count_mretriever
            label2 = Text(Point(100, 480), str(total_count) + " outcomes in total")
            label2.setSize(14)
            label2.draw(win)

            win.getMouse()
            win.close()

        draw_histogram(count_progress, count_mtrailer, count_exclude, count_mretriever)
        
        # Part 3
        with open("output_data.txt", "x") as file:
            for entry in progress_data:
                file.write(f"progress: {entry[0]}, {entry[1]}, {entry[2]}\n")
            
            for entry in module_trailer_data:
                file.write(f"module trailer: {entry[0]}, {entry[1]}, {entry[2]}\n")
            
            for entry in module_retriever_data:
                file.write(f"module retriever: {entry[0]}, {entry[1]}, {entry[2]}\n")
            
            for entry in exclude_data:
                file.write(f"exclude: {entry[0]}, {entry[1]}, {entry[2]}\n")

            #Flexiple. (2023) How to use python to create file. [online]
            #Available from: https://flexiple.com/python/python-create-file
            #Accessed on 3rd December
        
        break
    else:
        print("Enter a valid input! (y/q)")

#Part 2
print("\nPart 2:")

for entry in progress_data:
    print('progress: ', *entry)
for entry in module_trailer_data:
    print('module trailer: ', *entry)
for entry in module_retriever_data:
    print('module retriever: ', *entry)
for entry in exclude_data:
    print('exclude: ', *entry)

#Flexiple. (2023) How to create and printa list in python. [online]
#Available from: https://flexiple.com/python/python-print-list
#Accessed on 3rd December





