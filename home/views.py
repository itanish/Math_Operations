from django.shortcuts import render, redirect
from django.template import RequestContext
import requests
from sympy import *

def get_mc(c,q):
    #This function is used to calculate Marginal Cost
    mc = diff(c, q)/diff(q,q)
    return mc

def get_elasticity(c,q_final,q):
    #This function is used to calculate Elasticity = (c/q)*(dc/dq)
    
    #Calculating dc/dq
    dcdq = diff(q)/diff(c, q)
    print ('DC/DQ: ', dcdq)

    #Substituting q in DC/DQ
    dcdq = sympify(dcdq)
    dcdq = dcdq.subs(q,q_final)
    print ('DC/DQ: ', dcdq)

    #Substituting q in C
    c = sympify(c)
    c = c.subs(q,q_final)
    print(c,q_final)
    print (dcdq)
    elasticity = (c/q_final) * dcdq
    return [elasticity, dcdq, c]

def home(request):

    c = request.GET.get('c')
    p = request.GET.get('p')

    if c is None or p is None:
        return render(request, 'home/index.html', {'ans':0})

    else:
        print('here')

        q = Symbol('q')

        p = int(p)

        mc = get_mc(c,q)

        #Equating to P use value of mc from get_mc function
        qq = solve(Eq(mc,p), q)

        print('Qq', qq)

        #Take the maximum q if Q>0 else minimum

        if max(qq)>0:
            q_final = max(qq)
        else:
            q_final = min(qq)

        q_final = int(q_final)
        print(q_final)

        exp = c


        output = get_elasticity(c,q_final,q)

        elasticity = output[0]
        dcdq = output[1]
        c_final = output[2]
        print('Output', elasticity)
        ans=1
        return render(request, 'home/index.html', {'ans':ans,'c':c, 'p':p, 'qq':qq, 'mc':mc, 'elasticity':elasticity, 'dcdq':dcdq, 'c_final': c_final, 'q':q, 'q_final':q_final})


    


