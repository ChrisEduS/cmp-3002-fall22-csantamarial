from UnitTests import Test_Sum, Test_Reverse_LL, Test_MergeLL, Test_Insertion_Sort, Test_Quick_Sort, Test_Merge_Sort, Test_Factorial, Test_Fibonacci, Test_MergeArrays
import os
from datetime import date
from time import sleep

def by_author_files(files):
    files.sort(key=lambda x: x.split('_')[1][0], reverse=True)
    autor_regs=dict(zip(reversed(range((len(files))+1)),files))

    for key, val in autor_regs.items():
        print(str(key) + '\t-' + str(val))

def getfiles(dir):
    '''Get only files of a directory
    In this case, take all unit test stored results'''
    basepath = 'TestResults/'+dir   # 'TestResults/Sum_R'
    files_list = []
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):  
            files_list.append(entry)
    return files_list

def good_files(files):
    good_ones = []
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            if not ('FAILED' in lines[-1]):
                good_ones.append(file)
    return good_ones

def find_index(scores):
    lista = []
    tiempo_minimo = 1_000_000_000.0
    indiceResultado = -1

    for i in range(len(scores)):
        a = scores[i].split(' ')
        b = (a[4].split('s'))[0]
        b = float(b)
        if b < float(tiempo_minimo):
            tiempo_minimo = b 
            indiceResultado = i
        lista.append(b)
    return (indiceResultado, tiempo_minimo)

def get_scores(files):
    scores = []
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            scores.append(lines[-3])
    return scores


line = '------------------------------------------------------------------------------'
def menu():
    print("-------------------------Unit Testing for Algorithms-------------------------")
    print('Options')
    print('\t1. New Test\n\t2. See registers\n\t3. Quit')
    print(line)
    while True:
        fchoice = int(input('Your choice: '))
        if fchoice == 1:
            newTestW()
            break
        elif fchoice == 2:
            dispRegistersW()
            break
        elif fchoice == 3:
            print(line)
            print("\t\tThank you for testing with us!")
            print(line)
            break
        else:
            print('\n'+line)
            print('\tMake sure you select a valid option number.\n')

def dispCases():
    funcs_to_test = ['Sum of first n numbers', 'Reverse a linked list', 'Merge two linked lists', 'Insertion sort',
                    'Quick sort', 'Merge two arrays','Merge sort', 'Factorial', 'Fibonacci']
    for i, func in enumerate(funcs_to_test):
        print('\t\t'+str(i+1)+'. '+func)
    print(line) 

def newTestW():
    print('\n\n'+line)
    print('----------------------------- New Algortihm Testing ---------------------------')
    usrName = input("\tEnter tester name: ").strip() #Username sin blankspaces laterales
    today = date.today() ## Toma la fecha de hoy
    print('\tWhat algorithm do you want to test?...')
    dispCases()
    while True:
        topt = int(input('Your choice: '))
        print('Antes de continuar, asegurate de subir el archivo que contiene su algoritmo de la siguiente manera:')
        if topt == 1:
            ## Sum of first n numbers
            print("En el directorio /FilestoTest...")
            print("Nombre del archivo: {}, Nombre de la funcion: {}".format('Sum.py', 'sum'))
            input('Press Enter when all is set up...')
            with open('TestResults/SumRes/{}_{}_sumR.out'.format(today, usrName), 'w') as f1:
                Test_Sum.main(f1)
                f1.close()
            print("TESTING...")
            sleep(2)
            print(line)
            print('######################---RESULTS---####################')
            # Lectura y display del test
            with open('TestResults/SumRes/{}_{}_sumR.out'.format(today, usrName), 'r') as f1:
                read_file = f1.read(-1)
                print(read_file)
                f1.close()
            break
        elif topt == 2:
            ## Reverse a linked list
            print("En el directorio /DataStructures...")
            print("Nombre del archivo: {}. Sube las clases SinlgyLinkedLists, Node y sus funciones.".format('Singly_Linked_List.py'))
            input('Press Enter when all is set up...')
            with open('TestResults/ReverseLLRes/{}_{}_revLLR.out'.format(today, usrName), 'w') as f2:
                Test_Reverse_LL.main(f2)
                f2.close()
            # Lectura y display del test
            print("TESTING...")
            sleep(2)
            print(line)
            print('######################---RESULTS---####################')
            with open('TestResults/ReverseLLRes/{}_{}_revLLR.out'.format(today, usrName), 'r') as f2:
                read_file = f2.read(-1)
                print(read_file)
                f2.close()
            break
        elif topt == 3:
            ## Merge two linked lists
            print("En el directorio /FilestoTest...")
            print("Nombre del archivo: {}, Nombre de la funcion: {}".format('Merge_Linked_Lists.py', 'merge_linked_lists'))
            input('Press Enter when all is set up...')
            # Guardado del test
            with open('TestResults/MergeLLRes/{}_{}_mergLLR.out'.format(today, usrName), 'w') as f3:
                Test_MergeLL.main(f3)
                f3.close()
            print("TESTING...")
            sleep(2)
            print(line)
            print('######################---RESULTS---####################')
            # Lectura y display del test
            with open('TestResults/MergeLLRes/{}_{}_mergLLR.out'.format(today, usrName), 'r') as f3:
                read_file = f3.read(-1)
                print(read_file)
                f3.close()
            break
        elif topt == 4:
            ## Insertion sort
            print("En el directorio /FilestoTest...")
            print("Nombre del archivo: {}, Nombre de la funcion: {}".format('Insertion_Sort.py', 'insertion_sort'))
            input('Press Enter when all is set up...')
            # Guardado del test
            with open('TestResults/InsertionSortRes/{}_{}_inSR.out'.format(today, usrName), 'w') as f4:
                Test_Insertion_Sort.main(f4)
                f4.close()
            print("TESTING...")
            sleep(2)
            print(line)
            print('######################---RESULTS---####################')
            # Lectura y display del test
            with open('TestResults/InsertionSortRes/{}_{}_inSR.out'.format(today, usrName), 'r') as f4:
                read_file = f4.read(-1)
                print(read_file)
                f4.close()
            break
        elif topt == 5:
            ## Quick sort
            print("En el directorio /FilestoTest...")
            print("Nombre del archivo: {}, Nombre de la funcion: {}".format('Quick_Sort.py', 'quick_sort'))
            input('Press Enter when all is set up...')
            # Guardado del test
            with open('TestResults/QuickSortRes/{}_{}_quickSR.out'.format(today, usrName), 'w') as f5:
                Test_Quick_Sort.main(f5)
                f5.close()
            print("TESTING...")
            sleep(2)
            print(line)
            print('######################---RESULTS---####################')
            # Lectura y display del test
            with open('TestResults/QuickSortRes/{}_{}_quickSR.out'.format(today, usrName), 'r') as f5:
                read_file = f5.read(-1)
                print(read_file)
                f5.close()
            break
        elif topt == 6:
            ## Merge two arrays
            print("En el directorio /FilestoTest...")
            print("Nombre del archivo: {}, Nombre de la funcion: {}".format('Merge_arrs.py', 'merge_sorted_arrays'))
            input('Press Enter when all is set up...')
            # Guardado del test
            with open('TestResults/MergeArrsRes/{}_{}_mer2arrR.out'.format(today, usrName), 'w') as f6:
                Test_MergeArrays.main(f6)
                f6.close()
            print("TESTING...")
            sleep(2)
            print(line)
            print('######################---RESULTS---####################')
            # Lectura y display del test
            with open('TestResults/MergeArrsRes/{}_{}_mer2arrR.out'.format(today, usrName), 'r') as f6:
                read_file = f6.read(-1)
                print(read_file)
                f6.close()
            break
        elif topt == 7:
            ## Merge sort
            print("En el directorio /FilestoTest...")
            print("Nombre del archivo: {}, Nombre de la funcion: {}".format('Merge_sort.py', 'merge_sort'))
            input('Press Enter when all is set up...')
            # Guardado del test
            with open('TestResults/MergeSortRes/{}_{}_mergeSR.out'.format(today, usrName), 'w') as f7:
                Test_Merge_Sort.main(f7)
                f7.close()
            print("TESTING...")
            sleep(2)
            print(line)
            print('######################---RESULTS---####################')
            # Lectura y display del test
            with open('TestResults/MergeSortRes/{}_{}_mergeSR.out'.format(today, usrName), 'r') as f7:
                read_file = f7.read(-1)
                print(read_file)
                f7.close()
            break
        elif topt == 8:
            ## Factorial
            print("En el directorio /FilestoTest...")
            print("Nombre del archivo: {}, Nombre de la funcion: {}".format('Factorial.py', 'factorial'))
            input('Press Enter when all is set up...')
            # Guardado del test
            with open('TestResults/FactorialRes/{}_{}_factR.out'.format(today, usrName), 'w') as f8:
                Test_Factorial.main(f8)
                f8.close()
            print("TESTING...")
            sleep(2)
            print(line)
            print('######################---RESULTS---####################')
            # Lectura y display del test
            with open('TestResults/FactorialRes/{}_{}_factR.out'.format(today, usrName), 'r') as f8:
                read_file = f8.read(-1)
                print(read_file)
                f8.close()
            break
        elif topt == 9:
            ## Fibonacci
            print("En el directorio /FilestoTest...")
            print("Nombre del archivo: {}, Nombre de la funcion: {}".format('Fibonacci.py', 'fibonacci'))
            input('Press Enter when all is set up...')
            # Guardado del test
            with open('TestResults/FibonacciRes/{}_{}_fiboR.out'.format(today, usrName), 'w') as f9:
                Test_Fibonacci.main(f9)
                f9.close()
            print("TESTING...")
            sleep(2)
            print(line)
            print('######################---RESULTS---####################')
            # Lectura y display del test
            with open('TestResults/FibonacciRes/{}_{}_fiboR.out'.format(today, usrName), 'r') as f9:
                read_file = f9.read(-1)
                print(read_file)
                f9.close()
            break
        else:
            print('\n'+line)
            print('\tMake sure you select a valid option number.\n')
    print('\n\tGracias por usar :)!!')

def orderOfReg():
    print("\tHow do you want to get the registers?")
    print('\tBy date:\n\t\t1. Recent to Oldest\n\t\t2. Oldest to Recent')
    print('\t3. By author')
    print(line)

def regOpts(files, basepath):
    ## AGREGANDO LOS BASE PATHS A LO FILES PARA NO TENER PROBLEMAS DE FILENOTFOUND
    goodfiles = []
    for i in range(len(files)):
        goodfiles.append(basepath+files[i])
    goodfiles = good_files(goodfiles)
    ##/--------------
    ropt = int(input('Your choice: '))
    while True:
        if ropt == 1:
           ## Show registers by date recent to oldest
            rfiles = sorted(files)
            for num, file in enumerate(rfiles):
                print('{} \t- {}'.format(len(rfiles)-num, file))
            print(line+'\n')
            print('El mejor registro de este Test fue:')
            best_file_ind = find_index(get_scores(goodfiles))
            print(goodfiles[best_file_ind[0]] + '\nCon un tiempo de ejecucion: '+str(best_file_ind[1]))
            break
        elif ropt == 2:
             ## Show registers by date oldest to recent
            rfiles = sorted(files)
            rfiles.reverse()
            for num, file in enumerate(rfiles):
                print('{} \t- {}'.format(len(rfiles)-num, file))
            print(line+'\n')
            print('El mejor registro de este Test fue:')
            best_file_ind = find_index(get_scores(goodfiles))
            print(goodfiles[best_file_ind[0]] + '\nCon un tiempo de ejecucion: '+str(best_file_ind[1]))
            break
        elif ropt == 3:
            ## Show registers by author name
            by_author_files(files)
            print(line+'\n')
            print('El mejor registro de este Test fue:')
            best_file_ind = find_index(get_scores(goodfiles))
            print(goodfiles[best_file_ind[0]] + '\nCon un tiempo de ejecucion: '+str(best_file_ind[1]))
            break
        else:
            print('\n'+line)
            print('\tMake sure you select a valid option number.\n')

def dispRegistersW():
    print('\n\n'+line)
    print('---------------------------------- Registers ------------------------------------')
    print('\tWhat algorithm do you want to see registers?...')
    dispCases()
    
    while True:
        algopt = int(input('Your choice: '))
        if algopt == 1: # SUM
            files = getfiles('SumRes/')
            if not len(files):
                print("Not registers made yet")
                continue
            orderOfReg()
            regOpts(files, 'TestResults/SumRes/') 
            break

        elif algopt == 2: # REVERSE LL
            files = getfiles('ReverseLLRes/')
            if not len(files):
                print("Not registers made yet")
                continue
            orderOfReg()
            regOpts(files)
            break

        elif algopt == 3: # MERGE LL
            files = getfiles('MergeLLRes/')
            if not len(files):
                print("Not registers made yet")
                continue
            orderOfReg()
            regOpts(files, 'TestResults/MergeLLRes/')
            break

        elif algopt == 4: # INSERTION
            files = getfiles('InsertionSortRes/')
            if not len(files):
                print("Not registers made yet")
                continue
            orderOfReg()
            regOpts(files, 'TestResults/InsertionSortRes/')
            break

        elif algopt == 5: # QUICK 
            files = getfiles('QuickSortRes/')
            if not len(files):
                print("Not registers made yet")
                continue
            orderOfReg()
            regOpts(files, 'TestResults/QuickSortRes/')
            break

        elif algopt == 6: # MERGE ARRS
            files = getfiles('MergeArrsRes/')
            if not len(files):
                print("Not registers made yet")
                continue
            orderOfReg()
            regOpts(files, 'TestResults/MergeArrsRes/')
            break

        elif algopt == 7: # MERGE 
            files = getfiles('MergeSortRes/')
            if not len(files):
                print("Not registers made yet")
                continue
            orderOfReg()
            regOpts(files, 'TestResults/MergeSortRes/')
            break

        elif algopt == 8: # FACT
            files = getfiles('FactorialRes/')
            if not len(files):
                print("Not registers made yet")
                continue
            orderOfReg()
            regOpts(files, 'TestResults/FactorialRes/')
            break

        elif algopt == 9: # FIBO
            files = getfiles('FibonacciRes/')
            if not len(files):
                print("Not registers made yet")
                continue
            orderOfReg()
            regOpts(files, 'TestResults/FibonacciRes/')
            break

        else: 
            print('\n'+line)
            print('\tMake sure you select a valid option number.\n')

if __name__ == '__main__':
    #To-run code. 
    menu()
        
