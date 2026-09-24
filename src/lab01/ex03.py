price=int(input('ЦЕНА:'))
discount=int(input("ПРОЦЕНТ СКИДКИ:"))
vat=int(input("НДС:"))
base=price* (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'{"База после скидки:":<22}{base:>20.2f} ₽')
print(f'{"НДС:":<22}{vat_amount:>20.2f} ₽')
print(f'{"Итого к оплате:":<22}{total:>20.2f} ₽')
