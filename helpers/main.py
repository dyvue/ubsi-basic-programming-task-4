def currency(amount):
  if amount >= 0:
    return 'Rp{:,.0f}'.format(amount)
  else:
    return '-Rp{:,.0f}'.format(-amount)