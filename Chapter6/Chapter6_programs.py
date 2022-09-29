def display_file1():
    filename = input("Enter a file name: ")
    infile = open(filename, 'r')
    contents = infile.read()
    print(contents)
    infile.close()
    
def display_file2():
    filename = input("Enter a file name: ")
    try:
        infile = open(filename, 'r')
        contents = infile.read()
        print(contents)
        infile.close()
    except IOError as err:
        print("file does not exist. Exception:", err)
        
def sales_report1():
    total = 0
    try:
        infile = open('sales_data.txt', 'r')
        for line in infile:
            amount = float(line)
            total += amount
        infile.close()
        print(format(total, ',.2f'))
    except IOError:
        print("Error: An error occured trying to read the file")
    except ValueError:
        print("Error: Non-numberic data found calculations haulted")
    except:
        print("Error: We don't know what happened.")

def sales_report2():
    total = 0
    try:
        infile = open('sales_data.txt', 'r')
        for line in infile:
            amount = float(line)
            total += amount
        infile.close()
    except IOError:
        print("Error: An error occured trying to read the file")
    except ValueError:
        print("Error: Non-numberic data found calculations haulted")
    except Exception:
        print("Error: We don't know what happened.")
    else:
        print(format(total, ',.2f'))
    finally:
        infile.close()