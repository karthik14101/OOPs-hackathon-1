a= int(input(print(" Enter your profile:\n 1. Admin \n 2. User\n ") ) )
if a==1:
  print('Admin\n')
  b=int(input('Please check the following things and enter your required ones\n 1. for adding New Blood Bank\n 2. For Finding donors\n 3. For checking Blood Requests\n 4. Exit\n'))
  if b==1:
    add=input(' Please enter the name of the hospital in which you want to add:')
    print(add+' hospital added\n')
  if b==2:
    print(' Chippagiri Karthik (B+)\n Raviteja (B-)\n Jagadeesh(O+)\n Mithun chakravarthy (A-)\n Suraj Reddy (B+)\n Steve smith(O-)\n Anand(O+)')
  if b==3:
    print('Saveera Hospital Blood Bank needs A+,B+,B- blood groups\n')
  if b!=4:
    print('Warning! Please enter a valid choice ')
if a==2:
  print('User')
  c=int(input('Please check the following things and enter your required ones\n 1. for asking Blood\n 2. for donating Blood\n 3. for seeing blood Requests\n 4. Exit\n'))
  if c==1:
    request=input('Please enter your blood group in which you want:')
    print('Your request for blood donation of '+request+' type has been sent\n')
  if c==2:
    donate=input('Please enter your blood group for donating:')
    print('Your blood type '+donate+' has beeen registered for blood donations\n')
  if c==3:
    d=int(input('Raghuveera hospital is in need of O+,O-,A+ blood groups\n 1.ACCEPT\n 2.IGNORE\n'))
    if d==1:
        print(' We are appreciating you for accepting the blood donation request and you will get all details further through notifications\n')
  while c!=4:
       c=int(input('Please check the following things and enter your required ones\n 1. for asking Blood\n 2. for donating Blood\n 3. for seeing blood Requests\n 4. Exit\n'))
  if c==1:
    request=input('Please enter your blood group in which you want:')
    print('Your request for blood donation of '+request+' type has been sent\n')
  if c==2:
    donate=input('Please enter your blood group for donating:')
    print('Your blood type '+donate+' has beeen registered for blood donations\n')
  if c==3:
    d=int(input('Raghuveera hospital is in need of O+,O-,A+ blood groups\n 1.ACCEPT\n 2.IGNORE\n'))
    if d==1:
        print(' We are appreciating you for accepting the blood donation request and you will get all details further through notifications\n')
