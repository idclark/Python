from numpy import log, sqrt, square, diagonal
from scipy import c_, ones, dot, stats, diff
from scipy.linalg import qr, inv,solve, det

#need to create a y vector and x matrix
# how to do this with np and sp 

class Regression:
        
    def __init__ (self, y, x,y_varname='y',xvarname=''):
           self.y = y
           self.x= c_[ones(x.shape[0]),x]
           #attach collumn of 1s for the regression constant.
           self.y_varname = y_varname
           if not isinstance(x_varname,list):
               self.x_varname = ['intercept'] + list(x_varname)
           else:
               self.x_varname = ['intercept'] + x_varname

            self.ols()

    def ols(self):
        self.inverse = inv(dot(self.x.T,self.x))
        #inverse of x-prime * x
        xy = dot(self.x.T,self.y)
        self.coef = dot(self.inverse, xy)
        # inverse * x-prime*y estimates the beta coeficients

        #need to estimate standard errors
        self.e = self.y - dot(self.x,self.coef)
        #residuals
        self.sse = dot(self.e,self.e) / self.y.shape[0] - self.x.shape[1]
                                        #calculate degrees of freedom
        self.se = sqrt(diagonal(self.sse*self.inverse))
        # our coefs of standard errors

        self.t = self.coef / self.se
        #calculate t-score


    def summary(self):
        print self.coef, self.se, self.t 
            