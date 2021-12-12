#### built-in math module               (theres more these are just some)
import math

##constants
math.pi                             #pi 
math.e                              #e
math.inf                            #float pos infinity
math.nan                            #float not a number
math.tau                            #2pi

##methods
#x and y = numbers (or var of number)
#a and b = list of numbers

math.log(x)			                  	#natural log of x
math.log10(x)			                 	#base 10 logarithm of x
math.sin(x)                         #sin x -------> (same for math.cos() and math.tan())
math.asin(x)                        #arcsin x --------> (same for math.acos() and math.atan())
math.asin2(x,y)                     #arcsin of x/y in rad
math.sinh(x)                        #hyperbolic sin x
math.asinh(x)                       #inverse hyberbolic sin x
math.sqrt(x)                        #sqare root of x
math.ceil(x)	                      #rounds x up to the nearest integer
math.floor(x)	 	                    #rounds x down to the nearest integer
math.comb(x,y)		                  #possible combinations (x = # of items to choose from, y = # of possibilities)
math.perm(x)			                  #number of ways to choose k items from n items with order and without repetition
math.degrees(x)			                #converts radians to degrees
math.radians(x)				              #converts degrees to radians
math.fabs(x)			                  #absolute value of a number
math.copysign(x,y)                  #returns float w value of x and sign of y
math.dist(a,b)                      #distance between a and b (where a and b are coordinates of the point)
math.exp(x)                         #e^x
math.isfinite(x)                    #check if x finite
math.isinf(x)                       #check if x infinite
math.isnan(x)                       #check if x not a number
math.gcd(x)                         #greatest common divisor of x
math.pow(x,y)                       #x to the power of y
