class Payment(object):
  money_pay = 50 # 50 pesos la hora

  def __init__(self, hours_worked=0, shift="n/a"):
    self.hours_worked = hours_worked
    self.shift = shift

    1750 + 900
    
  def getTotal(self):
    total = 0

    if self.shift == "diurno" :
      total = self.getDiurnoTotal()
    elif self.shift == "nocturno":
      total = self.getNocturnoTotal()
    elif self.shift == "mixto":
      total = self.getMixtoTotal()

    return total

  def getDiurnoTotal(self)
    total = 0
    weekly_hours = 40

    if self.hours_worked > weekly_hours :
      total = weekly_hours * Payment.money_pay
      extra_hours = self.hours_worked - weekly_hours
      
      if extra_hours > 9 :
        total += 9 * (Payment.money_pay * 2) + (extra_hours - 9) * (Payment.money_pay * 3)
      else:
        total += extra_hours * (Payment.money_pay * 2)
    else:
      total = self.hours_worked * Payment.money_pay

    return total

  def getNocturnoTotal(self)
    total = 0
    weekly_hours = 35

    if self.hours_worked > weekly_hours :
      total = weekly_hours * Payment.money_pay
      extra_hours = self.hours_worked - weekly_hours
      
      if extra_hours > 9 :
        total += 9 * (Payment.money_pay * 2) + (extra_hours - 9) * (Payment.money_pay * 3)
      else:
        total += extra_hours * (Payment.money_pay * 2)
    else:
      total = self.hours_worked * Payment.money_pay

    return total

  def getMixtoTotal(self)
    total = 0
    weekly_hours = 37.5

    if self.hours_worked > weekly_hours :
      total = weekly_hours * Payment.money_pay
      extra_hours = self.hours_worked - weekly_hours
      
      if extra_hours > 9 :
        total += 9 * (Payment.money_pay * 2) + (extra_hours - 9) * (Payment.money_pay * 3)
      else:
        total += extra_hours * (Payment.money_pay * 2)
    else:
      total = self.hours_worked * Payment.money_pay

    return total  