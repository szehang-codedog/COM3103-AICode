hk_popu = 7390000
hk_area = 1108

nor_popu = 5260000
nor_area = 385205

hk_den = float(hk_popu) / float(hk_area)
nor_den = float(nor_popu) / float(nor_area)

if hk_den < nor_den:
    print(" {} has population density {}".format("Norway", nor_den))
    print(" {} has population density {}".format("Hong Kong", hk_den))
else:
    print(" {} has population density {}".format("Hong Kong", hk_den))
    print(" {} has population density {}".format("Norway", nor_den))


input();