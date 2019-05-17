'''
general folder and file handling functions for the crawler
'''
import os

#create new dir for each website the crawlers works on
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project: ' + directory)
        os.makedirs(directory)

#create open list and  closed list (if not created)
def create_data_file(project_name, base_url):
        open_list = os.path.join(project_name , 'to_visit.txt') 
        close_list = os.path.join(project_name , 'visited.txt')
        if not os.path.isfile(open_list):
                write_file(open_list, base_url)
        if not os.path.isfile(close_list):
                write_file(close_list, '')

#create new files
def write_file(path, data):
        with open(path, 'w') as file:
                file.write(data)


#add data to file
def append_to_file(path, data):
        with open(path,'a') as file:
                file.write(data+'\n')

#remove data from file
def remove_data_from_file(path):
        open(path, 'w').close()

#file to set method (convert to set items)
def convert_to_set(filename):
        results = set()
        with open(filename,'rt') as file:
                for line in file:
                        results.add(line.replace('\n', ''))#delete the new line at the end of a line
        return results

#set iteration and back to the file
def convert_to_file(set_variable, file):
        with open(file,'w') as f:
                for entry in sorted(set_variable):
                        f.write(entry+'\n')
        
        remove_data_from_file(file) #to clear the file from the previous data
        for entry in sorted(set_variable):
                append_to_file(file, entry)