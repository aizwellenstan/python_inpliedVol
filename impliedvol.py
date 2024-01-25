#
#
from QuantLib import *

valuation_date = Date(31,8,2020)
Settings.instance().evaluationDate = valuation_date

calendar = UnitedStates()
market_price=10

exercise = EuropeanExercise(Date(31,August,2021))
payoff = PlainVanillaPayoff(Option.Call, 100.0)
option = EuropeanOption(payoff,exercise)

S = QuoteHandle(SimpleQuote(100.0))
r = YieldTermStructureHandle(FlatForward(0, calendar, 0.02, Actual360()))
q = YieldTermStructureHandle(FlatForward(0, calendar, 0.01, Actual360()))
sigma = BlackVolTermStructureHandle(BlackConstantVol(0, calendar, 0.20, Actual360()))
process = BlackScholesMertonProcess(S,q,r,sigma)

implied_volatility=option.impliedVolatility(market_price, process)

print ("Implied Volatility: ",implied_volatility)