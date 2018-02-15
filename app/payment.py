class Payment(object):
  money_pay = 50 # 50 pesos la hora

  def __init__(self, hours_worked=0, shift="n/a"):
    self.hours_worked = hours_worked
    self.shift = shift

    1750 + 900
    
  def getTotal(self):
    total = 0
    if self.shift == "diurno" :
      if self.hours_worked > 40 :
        total = 40 * Payment.money_pay
        extra_hours = self.hours_worked - 40
        if extra_hours > 9 :
          total += 9 * (Payment.money_pay * 2) + (extra_hours - 9) * (Payment.money_pay * 3)
        else:
          total += extra_hours * (Payment.money_pay * 2)
      else:
        total = self.hours_worked * Payment.money_pay
    elif self.shift == "nocturno":
      if self.hours_worked > 35 :
        total = 35 * Payment.money_pay
        extra_hours = self.hours_worked - 35
        if extra_hours > 9 :
          total += 9 * (Payment.money_pay * 2) + (extra_hours - 9) * (Payment.money_pay * 3)
        else:
          total += extra_hours * (Payment.money_pay * 2)
      else:
        total = self.hours_worked * Payment.money_pay
    elif self.shift == "mixto":
      if self.hours_worked > 37.5 :
        total = 37.5 * Payment.money_pay
        extra_hours = self.hours_worked - 37.5
        if extra_hours > 9 :
          total += 9 * (Payment.money_pay * 2) + (extra_hours - 9) * (Payment.money_pay * 3)
        else:
          total += extra_hours * (Payment.money_pay * 2)
      else:
        total = self.hours_worked * Payment.money_pay

    return total