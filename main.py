from enum import Enum

class MatchState(Enum):
    Tie = 0
    LocalIsWinning = 1
    VisitorIsWinning = 2
    
class Team:
    def __init__(self, x):
        try:
            self.winning = float(x['winning'])
            self.losing = float(x['losing'])
            self.tieing = float(x['tieing'])
        except ValueError:
            exit("could not convert to float")
        except IndexError:
            exit("typo in dictionary expressing team probabilities")
            
class Simulation:
    def __init__(self, visting_team, local_team):
        assert(isinstance(visting_team, Team))
        assert(isinstance(local_team, Team))
        self.visting_team = visting_team
        self.local_team = local_team

class Bet:
    def __init__(self, factor_local_wins, factor_tie, factor_visiting_wins):
        try:
            self.factor_tie = float(factor_tie)
            self.factor_local_wins = float(factor_local_wins)
            self.factor_visiting_wins = float(factor_visiting_wins)
        except ValueError:
            exit()
    
if __name__ == "__main__":
    barca = {
        'perdiendo' : 12.5,
        'ganando' : 40.0,
        'empatando' : 30.0,
    }
    madrid = {
        'perdiendo' : 20.0,
        'ganando' : 40.0,
        'empatando' : 30.0,
    }
    s = Simulation(barca, madrid)
    s.run()
    s.get_prob()
    bet = Bet()
    bet.which(s)
    
(0, 0) = 10%
(1, 0) = 20%


#5-futsal
import sympy as sym

#pitch = {
#    'width' : sym.Symbol('w'),
#    'offside line' : sym.Symbol('l'),
#}
w, l, x, y, z, k = sym.symbols('w l x y z k')
#solution = sym.solve((-k*z + x*y + sym.Rational(3,2)*k*y, -pitch['width'] + 2*x + k, -pitch['offside line'] + z + 3*y), (x, y, z, k))
solution = sym.solve((-k*z + x*y + sym.Rational(3,2)*k*y, -w + 2*x + k, -l + z + 3*y), (x, y, z, k))


print(solution)
from sympy import Function
x_func, y_func, z_func, k_func = solution[0][0], solution[0][1], solution[0][2], solution[0][3]
x_func = x_func.subs({w : 18.45})
y_func = y_func.subs({w : 18.45})
z_func = z_func.subs({w : 18.45})
k_func = k_func.subs({w : 18.45})
print(x_func, y_func, z_func, k_func)

from sympy.plotting import plot

p1 = plot(x_func, show=False)
p2 = plot(y_func, show=False)
p3 = plot(z_func, show=False)
p4 = plot(k_func, show=False)
p1.append(p2[0])
p1.append(p3[0])
p1.append(p4[0])

p1.show()
exit()


############

import itertools
class A:
    pass
    
x = A()
y = A()
x = A()
print(globals().values())

h = [i.__repr__ for i in globals().values()]
print(h)
exit()
print(isinstance(type(x)))
print(type(y))
print(isinstance(x, A))
#print(isinstance(x, A()))
print(globals().values())
print(globals())
AHA = [(type(i), i) for i in globals().keys()]
print(AHA)
exit()
h = [type(i) for i in globals().values()]
print(h)
n = [i for i in h if isinstance(i)]
print(n)

exit()

import sympy as sym
a = sym.Rational(1, 2)

#t = sym.Symbol('t')

from sympy.vector import CoordSys3D
N = CoordSys3D('N')

class Camera:
    def __init__(self, pos_x, pos_y, pos_z):
        self.position = pos_x*N.i + pos_y*N.j + pos_z*N.k
        number_of_cameras_already_defn = 9
        self.omega, self.theta = sym.symbols('\omega, \theta')


exit()
A = sym.Matrix([[1, x], [y, 1]])

pitch = {
    'width' : 68,
    'length' : 105,
}
area = {
    'width' : 40.3,
    'length' : 16.5,
}
key_distance = {
    'offside line' : 80,
    'last man' : 25,
}
spacing = (key_distance['offside line'] - key_distance['last man'])/5
sections = {
    'defensive line' : key_distance['last man'] + 1*spacing,
}
    
# importing the required module
#import matplotlib.pyplot as plt
  
# x axis values
#x = [1,2,3]
# corresponding y axis values#
#y = [2,4,1]
  
# plotting the points 
#plt.plot(x, y)
  
# naming the x axis
#plt.xlabel('x - axis')
# naming the y axis
#plt.ylabel('y - axis')
  
# giving a title to my graph
#plt.title('My first graph!')
  
# function to show the plot
#plt.show()

# importing the modules
import matplotlib.pyplot as plt
import numpy as np

# specifying the plot size
plt.figure(figsize = (pitch['length'], pitch['width']))

plt.axvline(x = key_distance['last man'], color = 'b', label = 'last defender')
plt.axvline(x = key_distance['offside line'], color = 'b', label = 'offside line')
plt.axhline(y = (pitch['width'] - area['width'])/2, color = 'b')
plt.axhline(y = (pitch['width'] + area['width'])/2, color = 'b')




# only one line may be specified; full height
 
# rendering plot
plt.show()


