msg_model='Hi %s,This is a reminder that you have %s assignments left to submit before you can graduate. Your current grade is %s and can increase to %s if you submit all assignments before the due date.'

nameinput=input('please input name dic separated by commas: ')
names=nameinput.split(',')

assignmentcountsinput=input('please input assignmentcounts separated by commas: ')
assignmentcounts=assignmentcountsinput.split(',')

gradesinput=input('please input grades separated by commas: ')
grades=gradesinput.split(',')

for i in range(len(names)):
    print(msg_model % (names[i],assignmentcounts[i],grades[i]))

