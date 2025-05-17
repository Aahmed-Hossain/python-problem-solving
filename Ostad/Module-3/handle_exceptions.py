try:
    with open('file.txt', 'r') as f:
        print(f.read())
        #print(10/0)
        # print(int('abc'))
        a = [1,3,4,5]
        # print(a[100])
        # name = Rahim

except Exception as e:
    print('Error: some error occured:', e)
except IndexError:
    print('Error: Index error')
except ValueError:
    print('Error: Invalid value')
except ZeroDivisionError:
    print('Error: Zero division erro')
except FileNotFoundError:
    print('Error: File not found')

else:
    print('Great!!! Code executed successfully')

finally:
    print('This will be printed whenever code run')


def check_file_name(file_name):
    if not file_name.endswith('name.txt'):
        raise ValueError('Only txt file allowed')
    print('Valid file uploaded')

try:
    check_file_name('name.tt')
except Exception as err:
    print(err)
