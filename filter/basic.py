import math
# w is the digital frq and T is the sampling time period
def analog_freq(w,T):
    # convert the digital freq into analog

    W = (2/T)* math.tan(w/2)
    return W

    
