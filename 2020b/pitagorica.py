for ren in range(1,11) :

    for col in range(1,11):
        #print ('$%04d.00 '%(ren * col), end='')
        print ('|{:05d}'.format(ren * col), end='')

    print('|')

