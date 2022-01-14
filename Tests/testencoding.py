# learning how to encode a variable string to be sent to the microscope

x = 'XMR 169'                       # test a potential input command
y = (x + '\n').encode('utf-8')      # encode the input command string

print(x)                            # output same as x string 'XMR 169'
print(y)                            # output encoded x string 'b'XMR 169\n''