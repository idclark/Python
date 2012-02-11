from numpy import log, sqrt, square, diagonal
from scipy import c_, ones, dot, stats, diff
from scipy.linalg import qr, inv,solve, det

#need to create a y vector and x matrix
# how to do this with np and sp 

class Regression:

    """
    Adapted from Vincent Nijs' 2007 script.

    script for calculating OLS regression. I'd like to eventually add more m    ethods for logit and probit regressions.
    
    uses a DV y and matrix of predictors x - intercept is added automatically.

    use the summary method to print coef and se estimates.


    """
    def __init__ (self, y, x, y_varname="y", x_varname = ''):
        self.y = y
        self.x = c_[ones(x.shape[0]),x]

        #attach collum of 1s for regression constant
        self.y_varname = y_varname
        if not isinstance(x_varname,list):
            self.x_varname = ["intercept"] + list(x_varname)
        else:
            self.x_varname = ["intercept"] + x_varname
            self.ols()

    def ols(self):
        self.inverse = inv(dot(self.x.T,self.x))

        #inverse of x-prime * x
        xy = dot(self.x.T,self.y)
        self.coef = dot(self.inverse, xy)
        #gives beta coefs

        self.e = self.y - dot(self.x, self.coef)
        #residuals
        self.sse = dot(self.e, self.e) / self.y.shape[0] - self.x.shape[1]
        self.se = sqrt(diagonal(self.sse * self.inverse))
        #standard errors

        self.t = self.coef / self.se
        # calculate t-score

    def summary(self):
        print 'Variable Coefficient   std. error   t-stat'
        for i in range(len(self.x_varname)):
            print ''' %-5s       %-5.6f     %5.6f     %-5.6f''' %tuple([self.x_varname[i], self.coef[i], self.se[i], self.t[i]])

            
    

