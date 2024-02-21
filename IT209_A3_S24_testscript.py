#--------------------------------------------------------------------------
# IT209_A3_S24_testscript.py - IT-209 Assignment #3 (A3) test script 
#
# The code below runs a number of tests of your Department and Student
# classes and methods.  Most features are exercised, but the test is
# not comprehensive and successful completion does not guarantee your
# code is free of defects. 
#--------------------------------------------------------------------------
                
# Copy/paste the following code into yours after your class definitions.
# There are 14 tests that are run when prompted in order
              
# Global/executable code ---------------------------------------------------

print('\nStart of Department and Student class demo **************')
input('\nTest1. Hit "Enter" to create 16 student objects for use in the demo ')
s1 = Student('David Miller', major = 'Hist',
      enrolled = 'y', credits = 30, qpoints = 90)           
s2 = Student('Emma Maria Vicente', major = 'Math',
      enrolled = 'y', credits = 90, qpoints = 315)
s3 = Student('Chris Squire', major = 'Musc',
      enrolled = 'y', credits = 45, qpoints = 160)           
s4 = Student('Tal Wilkenfeld', major = 'ARTS',
      enrolled = 'y', credits = 70, qpoints = 225)
s5 = Student('Larry Graham', major = 'CHHS',
      enrolled = 'y', credits = 105, qpoints = 315)           
s6 = Student('Dave Holland', major = 'CSci',
      enrolled = 'y', credits = 15, qpoints = 39)
s7 = Student('Esperanza Spalding', major = 'ENGR',
      enrolled = 'y', credits = 65, qpoints = 250)           
s8 = Student('Tim Bogert', major = 'Hist',
      enrolled = 'y', credits = 45, qpoints = 126)
s9 = Student('Gordon Sumner', major = 'Musc',
      enrolled = 'y', credits = 15, qpoints = 45)           
s10 = Student('Paul McCartney', major = 'ARTS',
      enrolled = 'y', credits = 110, qpoints = 330)
s11 = Student('Tina Weymouth', major = 'ENGR',
      enrolled = 'y', credits = 85, qpoints = 250)
s12 = Student('John McVie', major = 'Hist',
      enrolled = 'y', credits = 45, qpoints = 126)
s13 = Student('Nawt enrolled', major = 'Hist',
      enrolled = 'n', credits = 45, qpoints = 120)
s14 = Student('Toolow G. Peyay', major = 'Undc',
      enrolled = 'y', credits = 20, qpoints = 38)
s15 = Student('Stanley Clark', major = 'Chem',
      enrolled = 'y', credits = 95, qpoints = 295)
s16 = Student('Geddy Lee', major = 'Chem',
      enrolled = 'y', credits = 58, qpoints = 143)

print('\nList of Students created-------------------------------:\n ')
print('s1=  ',s1)
print('s2=  ',s2)
print('s3=  ',s3)
print('s4=  ',s4)      
print('s5=  ',s5)
print('s6=  ',s6)      
print('s7=  ',s7)
print('s8=  ',s8)
print('s9=  ', s9)
print('s10= ',s10)
print('s11= ',s11)
print('s12= ',s12)      
print('s13= ',s13)
print('s14= ',s14)
print('s15= ', s15)
print('s16= ', s16)
d1 = Department('ENGR', 'Engineering', 5, 3.0)
d2 = Department('ARTS', 'Art and Architecture', 5, 2.5)
d3 = Department('CHHS', 'College of Health and Human Services', 3, 2.75)
d4 = Department('Hist', 'History Department', 5, 2.50)

input('\n\nTest2. Hit "Enter" to see the list of 4 Department objects created ')
print('\n\nDepartments established---------------------------------:')
print(d1)
print(d2)
print(d3)
print(d4)

input('\n\n\nTest3. Hit "Enter" to add s1 - s5 to ENGR Department- print student list\n')
d1.addStudent(s1)      
d1.addStudent(s2)
d1.addStudent(s3)      
d1.addStudent(s4)
d1.addStudent(s5)
d1.listRoster()      


input('\n\n\n\nTest4. Hit "Enter" to add additional students to various departments -------------------:')
a, b = d1.addStudent(s15)
print('\nAttempting to add ', s15.name, ' to ', d1.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
print('\nDepartment ', d1.d_name, ' student list is now: ')
d1.listRoster()
      
input('\n\n\n\nTest5. Hit "Enter" to add two students to the ARTS Department ')
print('\nAttempting to add ', s6.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s6)
print('\t\t\treturn values: ', a, '  reason code: ', b)
print('\nAttempting to add ', s7.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s7)
print('\t\t\treturn values: ', a, '  reason code: ', b)
d2.listRoster()

input('\n\n\n\nTest6. Hit "Enter" to add two students to the CHHS Department' )
print('\nAttempting to add ', s8.name, ' to ', d3.d_code, ' result: ')
a, b = d3.addStudent(s8)
print('\t\t\treturn values: ', a, '  reason code: ', b)
print('\nAttempting to add ', s9.name, ' to ', d3.d_code, ' result: ')
a, b = d3.addStudent(s9)
print('\t\t\treturn values: ', a, '  reason code: ', b)
d3.listRoster()

input('\n\n\n\nTest7. Hit "Enter" to try adding a student with low GPA to CHHS')
a, b = d3.addStudent(s14)
print('\nAttempting to add ', s14.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)


input('\n\n\n\nTest8. Hit "Enter" to try to add a non-enrolled student to the CHHS Department')
print('\nAttempting to add ', s13.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s13)
print('\t\t\treturn values: ', a, '  reason code: ', b)


input('\n\n\n\nTest9. Hit "Enter" to try adding a duplicate student ')
print('\nAttempting to add ', s8.name, ' to ', d3.d_code, ' result: ')
a, b = d3.addStudent(s8)
print('\t\t\treturn values: ', a, '  reason code: ', b)


input('\n\n\n\nTest10. Hit "Enter" to add s10 to ENGR, s11 to ARTS, s12 to CHHS.')
print('  then print all 4 department student lists')
print('\nAttempting to add ', s10.name, ' to ', d1.d_code, ' result: ')
a, b = d1.addStudent(s10)
print('\t\t\treturn values: ', a, '  reason code: ', b)
print('\nAttempting to add ', s11.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s11)
print('\t\t\treturn values: ', a, '  reason code: ', b)
print('\nAttempting to add ', s12.name, ' to ', d3.d_code, ' result: ')
a, b = d3.addStudent(s12)
print('\t\t\treturn values: ', a, '  reason code: ', b)


input('\n\n\n\nTest11. Hit "Enter" to try to add s16 to ARTS, which will fail for low gpa, ')
print('    then add a new course grade of "A"/3 credits to s15, and try the add again.')
print('\nStudent to be added to ARTS is ', s16)      
a, b = d2.addStudent(s16)
print('\nResult of attempt to add ', s16.name, ' gpa: ', str(s16.gpa()), ' to ', d2.d_code)
print('\tis ', a, ', with reson code: ', b)


input('\n\n\n\nTest12. Adding 3 credit course with grade of "A" to ' + s16.name )
s16.addGrade("A", 3)
print('\nStudent profile is now: ', s16)
a, b = d2.addStudent(s16)
print('\nResult of second attempt to add ', s16.name, ' to ', d2.d_code)
print('\tis ', a, ', with reason code:  ', b)
print('\nNote: ', s16.name, ' is now a ', s16.classLevel(), ' with gpa ', str(s16.gpa()))


input('\n\n\n\nTest13. Hit "Enter" to add s15 to ARTS.')
print('\nAttempting to add ', s15.name, ' to ', d2.d_code, ' result: ')
a, b = d2.addStudent(s15)
print('\t\t\treturn values: ', a, '  reason code: ', b)


input ('\n\n\n\nT14Hit "Enter" to see the final student list for all departments')
print('\nNumber of students in ', d1.d_code, ' is ', len(d1.studentRoster))
d1.listRoster()
print('\nNumber of students in ', d2.d_code, ' is ', len(d2.studentRoster))
d2.listRoster()
print('\nNumber of students in ', d3.d_code, ' is ', len(d3.studentRoster))
d3.listRoster()      
print('\nNumber of students in ', d4.d_code, ' is ', len(d4.studentRoster))
d4.listRoster()      

print('\n\n\n***** End of A3 F23 Output **********')
   
