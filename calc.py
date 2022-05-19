'''
This program has been made by Jacob Hamilton all credits go to him.
the program is updated regularly when bugs arise
or new formulas are updated.
'''





from math import sqrt
import math
import os
import time

'''
os.system('cls' if os.name == 'nt' else 'clear') is a single command if i cannot use the console clearing
function i can always resort to this single line command for the same effect.
'''

'''
The code below are vars for information the formulas
'''
sides = ['A', 'a', 'B', 'b', 'C', 'c']
operation_signs = ['+', '-', '*', '/', 'sqrt', 'SQRT', '**']
main_options = ['1', '2', '3', '4', '5', '6', '7', '8' ,'9', '10', '11']
circle_options = ['1', '2', '3', '4', '5', '6', '7']
Triangle_Selection = ['1', '2']
RightTriangle_Selection = ['1', '2']
TriangularPrisim_Selection = ['1', '2']
Equation_Options_Seletions = ['1', '2']
Physics_Options_Selections = ['1', '2', '3', '4']
Arithmetic_OPS = ['1', '2']
program_STATE = ''
PIE = float(3.14)
'''
in main options
1. is Pythagorean Thereom
2. is Basic math
3. is Circles
4. slope
'''
'''
The Formulas will be at the top and the function for choosing which function to use will be at the very bottom
'''
'''
the function below will clear the console when it is called upon or needed.
'''
def ConsoleClear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    time.sleep(2.5)
    os.system(command)

def ErrorValidation():
    try:
        if not KeyboardInterrupt:
            print('1')
    except:
        print('2')
##########################
def PythagoreanTheorem():
    program_STATE = 'pythagorean theorem'
    ConsoleClear()
    formula = input('Which side A, B, C: ')

    if formula not in sides:
        print('Not Found.')
        ConsoleClear()
    elif formula == 'A' or formula == 'a':
        side_b = int(input('Side B length: '))
        side_c = int(input('Side C length: '))
        #
        side_a = sqrt((side_c ** 2 - (side_b ** 2)))

        print('Side A Length: ' + str(side_a))
        ConsoleClear()

    elif formula == 'B' or formula == 'b':
        side_a = int(input('Side A length: '))
        side_c = int(input('Side C length: '))
        #
        side_b = sqrt(side_c ** 2 - side_a ** 2)

        print('Side B length: ' + str(side_b))
        ConsoleClear()

    elif formula == 'C' or formula == 'c':
        side_a = int(input('A Side length: '))
        side_b = int(input('B Side length: '))
        #
        # The pythagorean Theorem Formula to calculate side C below
        side_c = sqrt(side_a ** 2 + side_b ** 2)
        #
        print('Side C length: ' + str(side_c))
        ConsoleClear()
##########################
def Basic_Math():
    program_STATE = 'basic math'
    ConsoleClear()
    operation_choice = input('Operation (+, -, *, /, sqrt, **): ')
    if operation_choice not in operation_signs:
        print('Not an operation sign')
        ConsoleClear()
    elif operation_choice == '+':
        '''
        expression_a, expression_b and expression_c are used for the basic math function
        sqrt means square root
        ^ means an exponet
        '''
        expression_a = int(input('Expression A Value: '))
        expression_b = int(input('Expression B Value: '))
        expression_C = expression_a + expression_b
        if expression_C == 69:
            print(str(expression_a) + str(operation_choice) + str(expression_b) + '=' + str(expression_C) + ' ;)')
            ConsoleClear()
        else:
            print(str(expression_a) + str(operation_choice) + str(expression_b) + '=' + str(expression_C))
            ConsoleClear()
    elif operation_choice == '-':
        expression_a = int(input('Expression A Value: '))
        expression_b = int(input('Expression B Value: '))
        expression_C = expression_a - expression_b
        if expression_C == 69:
            print(str(expression_a) + str(operation_choice) + str(expression_b) + '=' + str(expression_C) + ' ;)')
            ConsoleClear()
        else:
            print(str(expression_a) + str(operation_choice) + str(expression_b) + '=' + str(expression_C))
            ConsoleClear()
    elif operation_choice == '*':
        expression_a = int(input('Expression A Value: '))
        expression_b = int(input('Expression B Value: '))
        expression_C = expression_a * expression_b
        if expression_C == 69:
            print(str(expression_a) + str(operation_choice) + str(expression_b) + '=' + str(expression_C) + ' ;)')
            ConsoleClear()
        else:
            print(str(expression_a) + str(operation_choice) + str(expression_b) + '=' + str(expression_C))
            ConsoleClear()
    elif operation_choice == 'sqrt' or operation_choice == 'SQRT':
        expression_a = int(input('Expression A Value: '))
        expression_C = sqrt(expression_a)
        if expression_C == 69:
            print('sqrt: ' + str(expression_a) + '= ' + str(expression_C) + ' ;)')
            ConsoleClear()
        else:
            print('sqrt: ' + str(expression_a) + '= ' + str(expression_C))
            ConsoleClear()
        '''
        The code below labeled in the elif statment with ^
        is trying to do powers so far does not work but will shortly.
        so for exponets and powers we will use ** operator followed by the power
        '''
    elif operation_choice == '**':
        expression_a = int(input('Expression A Value: '))
        expression_Exponet = int(input('Exponet Value: '))
        expression_C = expression_a ** expression_Exponet
        if expression_C == 69:
            print(str(expression_a) + ' ** ' + str(expression_Exponet) + ' = ' + str(expression_C) + ' ;)')
            ConsoleClear()
        else:
            print(str(expression_a) + ' ** ' + str(expression_Exponet) + ' = ' + str(expression_C))
            ConsoleClear()
        '''
        The code below in the else statement is doing division.
        '''
    else:
        expression_a = int(input('Expression A Value: '))
        expression_b = int(input('Expression B Value: '))
        expression_C = expression_a / expression_b
        if expression_C == 69:
            print(str(expression_a) + str(operation_choice) + str(expression_b) + '=' + str(expression_C) + ' ;)')
            ConsoleClear()
        else:
            print(str(expression_a) + str(operation_choice) + str(expression_b) + '=' + str(expression_C))
            ConsoleClear()
##########################
def Circles():
    program_STATE = 'circles'
    ConsoleClear()
    '''
    Formulas that are going to be used are
    area
    Diameter
    radius
    A = pi * r * r
    D = 2 * r
    C = 2 * pi * r
    '''
    print('1. Area of a Circle')
    print('2. Diameter of a Circle')
    print('3. Circumfrence of a circle')
    print('4. Sphere Surface Area')
    print('5. Sphere Volume')
    print('6. Sphere Diameter')
    print('7. Sphere Radius') # ha 169
    #
    circle_input = input(': ')

    if circle_input not in circle_options:
        print('not an option.')
        ConsoleClear()
    elif circle_input == '1':
        expression_a = int(input('Radius: '))
        expression_c = PIE * expression_a * expression_a
        print(str(PIE) + ' * ' + str(expression_a) + ' * ' + str(expression_a) + ' = ' + str(expression_c))
        ConsoleClear()
    elif circle_input == '2':
        expression_a = int(input('Radius: '))
        expression_c = 2 * expression_a
        print('2 * ' + str(expression_a) + ' = ' + str(expression_c))
        ConsoleClear()
        '''
        the code in the else statement is for Circumfrence
        '''
    elif circle_input == '3':
        expression_a = int(input('Radius: '))
        expression_c = 2 * PIE * expression_a
        print('2 * ' + str(PIE) + ' * ' + str(expression_a) + ' = ' + str(expression_c))
        ConsoleClear()
    elif circle_input == '4':
        expression_SPHERE_RADIUS = int(input('Radius Value: '))
        expression_SPHERE_SURFACE_AREA = 4 * PIE * expression_SPHERE_RADIUS ** 2
        print('4 * ' + ' 3.14 * ' + str(expression_SPHERE_RADIUS) + ' ** 2 = ' + str(expression_SPHERE_SURFACE_AREA))
        ConsoleClear()
    elif circle_input == '5':
        expression_SPHERE_RADIUS = int(input('Radius Value: '))
        expression_SPHERE_VOLUME = (4/3) * PIE * expression_SPHERE_RADIUS ** 3
        print('(4/3) * 3.14 * ' + str(expression_SPHERE_RADIUS) + ' ** 3 = ' + str(expression_SPHERE_VOLUME))
        ConsoleClear()
    elif circle_input == '6':
        expression_SPHERE_RADIUS = int(input('Radius Value: '))
        expression_SPHERE_DIAMETER = 2 * expression_SPHERE_RADIUS
        print('2 * ' + str(expression_SPHERE_RADIUS) + ' = ' + str(expression_SPHERE_DIAMETER))
        ConsoleClear()
    elif circle_input == '7':
        expression_SPHERE_DIAMETER = int(input('Diameter Value: '))
        expression_SPHERE_RADIUS = expression_SPHERE_DIAMETER / 2
        print(str(expression_SPHERE_DIAMETER) + ' / 2 = ' + str(expression_SPHERE_RADIUS))
        ConsoleClear()
##########################
def SlopeCalculator():
    program_STATE = 'slope'
    ConsoleClear()
    print(' You cannot divide by ZERO.')
    expression_y1 = int(input('y1 Value: '))
    expression_y2 = int(input('y2 Value: '))
    expression_x1 = int(input('x1 Value: '))
    expression_x2 = int(input('x2 Value: '))
    expression_SLOPE = (expression_y2 - expression_y1) / (expression_x2 - expression_x1)
    print('( ' + str(expression_y2) + ' - ' + str(expression_y1) + ' ) / ( ' + str(expression_x2) + ' - ' + str(expression_x1) + ' ) = ' + str(expression_SLOPE))
    ConsoleClear()
##########################
''' Right Triangle  Calculator Function'''
def RightTriangleCalculator():
    program_STATE = 'right triangle'
    ConsoleClear()
    print('1. Surface Area')
    print('2. Height')
    RightTriangle_SelectionInput = input(': ')
    if RightTriangle_SelectionInput not in RightTriangle_Selection:
        print('Not an option.')
    elif RightTriangle_SelectionInput == '1':
        expression_BASE = int(input('Base Value: '))
        expression_HEIGHT = int(input('Height Value: '))
        expression_AREA = (expression_BASE * expression_HEIGHT) / 2
        print('( ' + str(expression_BASE) + ' * ' + str(expression_HEIGHT) + ' ) ' + ' / ' + '2 = ' + str(expression_AREA))

    elif RightTriangle_SelectionInput == '2':
        expression_HYPOTENUSE = int(input('Hypotenuse Value: '))
        expression_BASE = int(input('Base Value: '))
        expression_HEIGHT = sqrt(expression_HYPOTENUSE ** 2) - sqrt(expression_BASE ** 2)
        print('sqrt( ' + str(expression_HYPOTENUSE) + '**' + ' - ' + str(expression_BASE) + '**' + ')' + ' = ' + str(expression_HEIGHT))
'''Triangular Prisim Calculator Function'''
def TriangularPrisimCalculator():
    program_STATE = 'triangle'
    ConsoleClear()
    print('1. Surface Area')
    print('2. Volume')
    TriangularPrisim_SelectionInput = input(': ')
    if TriangularPrisim_SelectionInput not in TriangularPrisim_Selection:
        print('not an option')
    elif TriangularPrisim_SelectionInput == '1':
        expression_TRIANGULAR_BASE = int(input('Base Value: '))
        expression_TRIANGULAR_HEIGHT = int(input('Height Value: '))
        expression_TRIANGULAR_SIDE_ONE = int(input('Side One Value: '))
        expression_TRIANGULAR_SIDE_TWO = int(input('Side Two Value: '))
        expression_TRIANGULAR_SIDE_THREE = int(input('Side Three Value: '))
        expression_TRIANGULAR_LENGTH = int(input('Length Value: '))
        expression_SURFACE_AREA = expression_TRIANGULAR_BASE * expression_TRIANGULAR_HEIGHT + (expression_TRIANGULAR_SIDE_ONE + expression_TRIANGULAR_SIDE_TWO + expression_TRIANGULAR_SIDE_THREE) * expression_TRIANGULAR_LENGTH # ha 269
        print('( ' + str(expression_TRIANGULAR_BASE) + ' * ' + str(expression_TRIANGULAR_HEIGHT) + ' + (' + str(expression_TRIANGULAR_SIDE_ONE) + ' + ' + str(expression_TRIANGULAR_SIDE_TWO) + ' + ' + str(expression_TRIANGULAR_SIDE_THREE) + ') * ' + str(expression_TRIANGULAR_LENGTH) + ' ) = ' + str(expression_SURFACE_AREA))
    elif TriangularPrisim_SelectionInput == '2':
        expression_TRIANGULAR_BASE = int(input('Base Value: '))
        expression_TRIANGULAR_LENGTH = int(input('Length Value: '))
        expression_TRIANGULAR_HEIGHT = int(input('Height Value: '))
        expression_TRIANGULAR_VOLUME = (1/2) * expression_TRIANGULAR_BASE * expression_TRIANGULAR_HEIGHT * expression_TRIANGULAR_LENGTH
        print('(1/2) * ' + str(expression_TRIANGULAR_BASE) + ' * ' + str(expression_TRIANGULAR_HEIGHT) + ' * ' + str(expression_TRIANGULAR_LENGTH) + ' = ' + str(expression_TRIANGULAR_VOLUME))
''''''
def GeometryCalculator():
    program_STATE = 'geometry'
    ConsoleClear()
    print('1. Right Traingles')
    print('2. Triangular Prisims')
    Triangle_Selection_input = input(': ')
    if Triangle_Selection_input not in Triangle_Selection:
        print('not an option.')
    elif Triangle_Selection_input == '1':
        RightTriangleCalculator()
    elif Triangle_Selection_input == '2':
        TriangularPrisimCalculator()
##########################
def QuadraticRoots():
    program_STATE = 'quadratics'
    ConsoleClear()
    expression_QUADRATIC_ROOT_A = int(input('A Value: '))
    expression_QUADRATIC_ROOT_B = int(input('B Value: '))
    expression_QUADRATIC_ROOT_C = int(input('C Value: '))
    '''ERROR FOR IF THE QUADRATIC IS FALSE'''
    if expression_QUADRATIC_ROOT_A == 0:
        print('Enter a correct quadratic equation')
    else:
        #Finds the discriminant of the quadratic
        espression_QUADRATIC_ROOT_DISCRIMINANT = expression_QUADRATIC_ROOT_B * expression_QUADRATIC_ROOT_B - 4 * expression_QUADRATIC_ROOT_A * expression_QUADRATIC_ROOT_C
        expression_QUADRATIC_ROOT_SQRT_VAL1 = math.sqrt(abs(espression_QUADRATIC_ROOT_DISCRIMINANT))
        expression_QUADRATIC_ROOT_SQRT_VAL = math.trunc(expression_QUADRATIC_ROOT_SQRT_VAL1)
        ''' The code below checks the condition for the discriminant and what kind it is.'''
        if espression_QUADRATIC_ROOT_DISCRIMINANT > 0:
            print('real with different roots')
            expression_QUADRATIC_DIFF_ROOTS_1 = (-expression_QUADRATIC_ROOT_B + expression_QUADRATIC_ROOT_SQRT_VAL) / (2 * expression_QUADRATIC_ROOT_A)
            expression_QUADRATIC_DIFF_ROOTS_2 = (-expression_QUADRATIC_ROOT_B - expression_QUADRATIC_ROOT_SQRT_VAL) / (2 * expression_QUADRATIC_ROOT_A)
            print('( -' + str(expression_QUADRATIC_ROOT_B) + ' +- ' + str(expression_QUADRATIC_ROOT_SQRT_VAL) + ' ) / ( 2 * ' + str(expression_QUADRATIC_ROOT_A) + ' ) = roots: {: ' + str(expression_QUADRATIC_DIFF_ROOTS_1) + ', ' + str(expression_QUADRATIC_DIFF_ROOTS_2) + ' }')
        elif espression_QUADRATIC_ROOT_DISCRIMINANT == 0:
            print('real with same roots')
            expression_QUADRATIC_SAME_ROOT = (-expression_QUADRATIC_ROOT_B / (2 * expression_QUADRATIC_ROOT_A))
            print('( -' + str(expression_QUADRATIC_ROOT_B) + ' / ( 2 * ' + str(expression_QUADRATIC_ROOT_A) + ' )) =  roots: {: ' + str(expression_QUADRATIC_SAME_ROOT) + ' }')
        else:
            print('complex roots')
            expression_QUADRATIC_COMPLEX_ROOT = (-expression_QUADRATIC_ROOT_B / (2 * expression_QUADRATIC_ROOT_A))
            print('( -' + str(expression_QUADRATIC_ROOT_B) + ' / ( 2 * ' + str(expression_QUADRATIC_ROOT_A) + ' )) = roots: {: ' + str(expression_QUADRATIC_COMPLEX_ROOT) + ' +-i ' + str(expression_QUADRATIC_ROOT_SQRT_VAL) + ' }')
##########################
def PercentageCalc():
    program_STATE = 'percentage'
    '''This is going to be a function calculating percentages and transferring from a decimal to a percenage
    and vice versa
    '''
    ConsoleClear()
    print('A. Calculate %, B. decimal to %')
    PercentageCalcInput = input(': ').upper()
    '''A was selected'''
    if PercentageCalcInput == 'A':
        expression_PERCENT = int(input('Percent: '))
        expression_PERCENT_OF = int(input('Percent Of: '))
        expression_DECIMAL = expression_PERCENT / expression_PERCENT_OF
        print(str(expression_PERCENT) + ' / ' + str(expression_PERCENT_OF) + ' = ' + str(expression_DECIMAL))
    elif PercentageCalcInput == 'B':
        expression_DECIMAL = float(input('Decimal: '))
        expression_PERCENT_OF = int(input('Percent Of: '))
        expression_PERCENT = expression_DECIMAL * expression_PERCENT_OF
        print(str(expression_DECIMAL) + ' * ' + str(expression_PERCENT_OF) + ' = ' + str(expression_PERCENT) + '%')
##########################
def Equations():
    program_STATE = 'equations'
    ConsoleClear()
    print('1. One Step Equation')
    print('2. Two Step Equation')
    equation_input = input(': ')
    if equation_input not in Equation_Options_Seletions:
        print('Not an option provided')
    elif equation_input == '1':
        # 3x=12
        x_input = int(input('Number with the X: '))
        num_input = int(input('Number after the = sign: '))
        answer = num_input / x_input
        print(str(x_input) + 'x = ' + str(num_input) + '{X= ' + str(answer))
    elif equation_input == '2':
        # 3x+12=16
        x_input = int(input('Number with the X: '))
        num_input = int(input('Num without a var: '))
        print('ex: +, -')
        operation_sign = input('The sign between the var and the real num: ')
        answer_input = int(input('Num after the = sign: '))

        if operation_sign == '+':
            step_1 = (answer_input - num_input)
            step_2 = (step_1 / x_input)
            print(str(x_input) + 'x ' + operation_sign + ' ' + str(num_input) + ' = X = ' + str(step_2))
        elif operation_sign == '-':
            step_1 = (answer_input + num_input)
            step_2 = (step_1 / x_input)
            print(str(x_input) + 'x ' + operation_sign + ' ' + str(num_input) + ' = X = ' + str(step_2))
##########################


cyclic_quad_ops = ['1', '2']


def cyclic_quad_area():
    
    CYCLIC_SIDE_A = int(input('Side A: '))
    CYCLIC_SIDE_B = int(input('Side B: '))
    CYCLIC_SIDE_C = int(input('Side C: '))
    CYCLIC_SIDE_D = int(input('Side D: '))

    CYCLIC_PERM = (1/2)*(CYCLIC_SIDE_A + CYCLIC_SIDE_B + CYCLIC_SIDE_C + CYCLIC_SIDE_D)

    print('( 1 / 2 ) * ( ' + str(CYCLIC_SIDE_A) + ' + ' + str(CYCLIC_SIDE_B) + ' + ' + str(CYCLIC_SIDE_C) + ' + ' + str(CYCLIC_SIDE_D) + ' ) = ' + str(CYCLIC_PERM))


    CYCLIC_AREA = sqrt((CYCLIC_PERM - CYCLIC_SIDE_A)*(CYCLIC_PERM - CYCLIC_SIDE_B) * (CYCLIC_PERM - CYCLIC_SIDE_C) * (CYCLIC_PERM - CYCLIC_SIDE_D))
    print(str(CYCLIC_AREA))
    #print('sqrt( ( ' + str(CYCLIC_PERM) + ' - ' + str(CYCLIC_SIDE_A) + ' ) * ( ' + str(CYCLIC_PERM) + ' - ' + str(CYCLIC_SIDE_B) + ' ) * ( ' + str(CYCLIC_PERM) + ' - ' + str(CYCLIC_SIDE_C) + ' ) * ( ' str(CYCLIC_PERM) + ' - ' + str(CYCLIC_SIDE_D) + ' ) = ' + str(CYCLIC_AREA))

def cyclic_quad_perimeter():
    CYCLIC_SIDE_A = int(input('Side A: '))
    CYCLIC_SIDE_B = int(input('Side B: '))
    CYCLIC_SIDE_C = int(input('Side C: '))
    CYCLIC_SIDE_D = int(input('Side D: '))

    CYCLIC_PERM = (1/2)*(CYCLIC_SIDE_A + CYCLIC_SIDE_B + CYCLIC_SIDE_C + CYCLIC_SIDE_D)

    print('( 1 / 2 ) * ( ' + str(CYCLIC_SIDE_A) + ' + ' + str(CYCLIC_SIDE_B) + ' + ' + str(CYCLIC_SIDE_C) + ' + ' + str(CYCLIC_SIDE_D) + ' ) = ' + str(CYCLIC_PERM))


def cyclic_quad():
    print('1. Area')
    print('2. perimeter')
    cyclic_quad_input = input(': ')

    if cyclic_quad_input not in cyclic_quad_ops:
        print('Not an option provided.')
    elif cyclic_quad_input == '1':
        cyclic_quad_area()
    elif cyclic_quad_input == '2':
        cyclic_quad_perimeter()


def gravitational_Pull():
    Grav_Constant = float(0.0000000000667)
    Mass_One_Input = float(input('Mass 1: '))
    Mass_Two_Input = int(input('Mass 2: '))
    Dist_Of_OBJS = int(input('Distance: '))
    #
    Force_VAL = (Grav_Constant * (Mass_One_Input * Mass_Two_Input) / (Dist_Of_OBJS ** 2))
    #
    #
    print(str(Grav_Constant) + ' * ( ' + str(Mass_One_Input) + ' * ' + str(Mass_Two_Input) + ' / ' + str(Dist_Of_OBJS) + ' ^2 ) = ' + str(Force_VAL))
    ConsoleClear()

def velocity_Calculation():
    Displacement_Input = int(input('displacement: '))
    Time_input = int(input('time: '))

    VELOCITY = (Displacement_Input / Time_input)

    print('( ' + str(Displacement_Input) + ' / ' + str(Time_input) + ' ) = ' + str(VELOCITY))
    ConsoleClear()


def acceleration_CALC():
    FINAL_VEL = int(input('Final Velocity: '))
    starting_VEL = int(input('Start velocity: '))
    Time_Input = int(input('Time; '))

    ACCELERATION = (FINAL_VEL - starting_VEL / Time_Input)

    print('( ' + str(FINAL_VEL) + ' - ' + str(starting_VEL) + ' / ' + str(Time_Input) + ' ) = ' + str(ACCELERATION))
    ConsoleClear()

def Physics():
    program_STATE = 'physics'
    ConsoleClear()
    print('1. gravitational Force')
    print('2. velocity')
    print('3. acceleration')
    print('4. Cyclic Quadrilateral')
    Physics_Option_Input = input(': ')
    #
    if Physics_Option_Input not in Physics_Options_Selections:
        print('Not Found.')
    elif Physics_Option_Input == '1':
        gravitational_Pull()
    elif Physics_Option_Input == '2':
        velocity_Calculation()
    elif Physics_Option_Input == '3':
        acceleration_CALC()
    elif Physics_Option_Input == '4':
        cyclic_quad()
##########################

def Arithmetic_Sequence():
    ConsoleClear()
    Sequence_Num_ONE_Input = int(input('First Num of sequence: '))
    Term_VAL_Input = int(input('Term: '))
    Difference_Input = int(input('Difference: '))

    VAL_OF_TERM = Sequence_Num_ONE_Input + (Term_VAL_Input - 1) * (Difference_Input)

    print(str(Sequence_Num_ONE_Input) + ' + ( ' + Term_VAL_Input + ' - 1 ) * ( ' + str(Difference_Input) + ' ) = ' + VAL_OF_TERM)


def Arithmetic_SUM():
    ConsoleClear()
    TERM_Input = int(input('n term: '))
    TERM_ONE_INPUT = int(input('first value: '))

    SUM_OF_SEQUENCE = TERM_INPUT * ( TERM_ONE_INPUT + TERM_INPUT / 2)

    print(str(TERM_INPUT) + ' ( ' + str(TERM_ONE_INPUT) + ' + ' + str(TERM_INPUT) + ' / 2 ) = ' + str(SUM_OF_SEQUENCE))


def Arithmetic_Calcs():
    ConsoleClear()
    print('1. Arithmetic Sequence')
    print('2. Arithmetic Sum')
    Arithmetic_OPS_Input = input(': ')

    if Arithmetic_OPS_Input not in Arithmetic_OPS:
        print('Not Found.')
    elif Arithmetic_OPS_Input == '1':
        Arithmetic_Sequence()
    elif Arithmetic_OPS_Input == '2':
        Arithmetic_SUM()

##########################
Conic_Ops = ['1', '2', '3']


def Conic_Circle():
    X_VAL_INPUT = int(input('X: '))
    H_VAL_INPUT = int(input('H: '))
    Y_VAL_INPUT = int(input('Y: '))
    K_VAL_INPUT = int(input('K: '))

    R_VAL = ((X_VAL_INPUT - H_VAL_INPUT) ** 2) + ((Y_VAL_INPUT - K_VAL_INPUT) ** 2)

    FORMULA_ANS = R_VAL ** 2

    print('( ' + str(X_VAL_INPUT) + ' - ' + str(H_VAL_INPUT) + ')^2 + ( ' + str(Y_VAL_INPUT) + ' - ' + str(K_VAL_INPUT) + ' )^2 = ' + str(FORMULA_ANS))

    ConsoleClear()


def Conic():
    print('1. Circle')
    print('2. Ellipse (DOES NOT WORK)')
    print('3. Hyperbola (DOES NOT WORK)')

    Conic_Ops_Input = input(': ')

    if Conic_Ops_Input not in Conic_Ops:
        print('Not an option provided')
    elif Conic_Ops_Input == '1':
        Conic_Circle()
    elif Conic_Ops_Input == '2':
        pass
    elif Conic_Ops_Input == '3':
        pass

##########################

'''
The Code below is the main menu and everything else has to stay above
Only modify the main menu when a new formula function is added.
When a new formula is added you will have to add the main menu option.
You will aslo have to add the exact same option to the main menu option index aswell.
'''

def credits():
    ConsoleClear()
    print('Advanced Calculator\n By Jacob Hamilton')
    print('#.....')
    ConsoleClear()
    print('Advanced Calculator\n By Jacob Hamilton')
    print('.#....')
    ConsoleClear()
    print('Advanced Calculator\n By Jacob Hamilton')
    print('..#...')
    ConsoleClear()
    print('Advanced Calculator\n By Jacob Hamilton')
    print('...#..')
    ConsoleClear()
    print('Advanced Calculator\n By Jacob Hamilton')
    print('....#.')
    ConsoleClear()
    print('Advanced Calculator\n By Jacob Hamilton')
    print('.....#')
    ConsoleClear()

def ValueErrorMSG(msg):
    msg = ValueError
    print(msg)
    time.sleep(3)
    ConsoleClear()
    Main()


def Main():
    program_STATE = 'menu'
    running = True
    while running:
        print('*************************************************')
        print('*         Advanced Calculator                   *')
        print('*         By: Jacob Hamilton                    *')
        print('*   Git: https://github.com/hamilton-griffin    *')
        print('*                                               *')
        print('*                                               *')
        print('*        1. Pythagorean Theorem                 *')
        print('*        2. Basic Math                          *')
        print('*        3. Circles                             *')
        print('*        4. Slope                               *')
        print('*        5. Geometry                            *')
        print('*        6. Quadratic Equation / roots          *')
        print('*        7. Percentages                         *')
        print('*        8. Equations (ex: 2x+10)               *')
        print('*        9. physics                             *')
        print('*        10. Arithmetic sequences & series      *')
        print('*        11. Conic                              *')
        print('*                                               *')
        print('*      All units are using the Metric System    *')
        print('*************************************************')
        user_input = input(': ')
        if user_input not in main_options:
            print('not an option.')
        elif user_input == '1':
            PythagoreanTheorem()
        elif user_input == '2':
            Basic_Math()
        elif user_input == '3':
            Circles()
        elif user_input == '4':
            SlopeCalculator()
        elif user_input == '5':
            GeometryCalculator()
        elif user_input == '6':
            QuadraticRoots()
        elif user_input == '7':
            PercentageCalc()
        elif user_input == '8':
            Equations()
        elif user_input == '9':
            Physics()
        elif user_input == '10':
            Arithmetic_Calcs()
        elif user_input == '11':
            Conic()
'''
try:
    Main()
except KeyboardInterrupt:
    if program_STATE == 'menu':
        print('Already at main menu.')
        time.sleep(2.5)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print('going back to main menu.')
        time.sleep('2')
        os.system('cls' if os.name == 'nt' else 'clear')
        Main()

the code above is supposed to be a universal back button but i keep getting an error
for handling multiple exceptions at onces giving me an error and not doing what i want the program to do.
we will try and fix that.
first i have to do hella research on it and see if i can find ant quick fixes.

Main()

ALL THE CODE ABOVE IS FOR DEBUGGING AND IS ALSO EXPERIMENTAL AND DOESNT WORK :(
    BUT IF WE NEED TO DEBUG ANYTHING
    ADD THE CODE THEN WHEN DEBUGGIN IS DONE DONT DELETE THE DEBUG CODE USED
    COMMENT IT OUT SO IT CAN BE USED IF NEEDED AT A LATER TIME.
'''

'''
The code below works and is improved the code above doesnt work do not use.
the code below will catch any value errors or keyboard interuptions as a back button
'''
'''
menu art below


        print('*************************************************')
        print('*         Advanced Calculator                   *')
        print('*         By: Jacob Hamilton                    *')
        print('*                                               *')
        print('*                                               *')
        print('*        1. Pythagorean Theorem                 *')
        print('*        2. Basic Math                          *')
        print('*        3. Circles                             *')
        print('*        4. Slope                               *')
        print('*        5. Geometry                            *')
        print('*        6. Quadratic Equation / roots          *')
        print('*        7. Percentages                         *')
        print('*        8. Equations (ex: 2x+10)               *')
        print('*        9. physics                             *')
        print('*        10. Arithmetic sequences & series      *')
        print('*        11. Conic                              *')
        print('*                                               *')
        print('*      All units are using the Metric System    *')
        print('*************************************************')

'''


credits()
try:
    Main()
except ValueError:
    valMSG = 'VALUE ERROR'
    ValueErrorMSG(valMSG)
except KeyboardInterrupt:
    ConsoleClear()
    Main()