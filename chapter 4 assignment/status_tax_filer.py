def status_tax_filer(status,taxable_income):

	if status == 0 and taxable_income <= 8350:
		tax_amount = 0.1 * taxable_income
	
	if status == 0 and taxable_income >= 8350 and taxable_income <= 33950:
		tax_amount = (0.1 * 8350) + (0.15 * (taxable_income - 8350))
	if status == 0 and taxable_income >= 33951 and taxable_income <= 82250:
		tax_amount = (0.1 * 8350) + (0.15 * 25590) + (0.25 * (taxable_income - 33950))
	
	if status == 0 and taxable_income >= 82251 and taxable_income <= 171550:
		tax_amount = (0.1 * 8350) + (0.15 * 25590) + (0.25 *  48299) + (0.28 * (taxable_income - 82251))
	if status == 0 and taxable_income >= 171551 and taxable_income <= 372950:
		tax_amount = (0.1 * 8350) + (0.15 * 25590) + (0.25 *  48299) + (0.28 * 89299) + (0.33 * (taxable_income - 171551))
	if status == 0 and taxable_income >= 372951:
		tax_amount = (0.1 * 8350) + (0.15 * 25590) + (0.25 *  48299) + (0.28 * 89299) + (0.33 * 201399) + (0.35* (taxable_income - 372951))
	

	if status == 1 and taxable_income <= 16700:
		tax_amount = 0.1 * taxable_income
	
	if status == 1 and taxable_income >= 16701 and taxable_income <= 67900:
		tax_amount = (0.1 * 16700) + (0.15 * (taxable_income - 16700))
	if status == 1 and taxable_income >= 67901 and taxable_income <= 137050:
		tax_amount = (0.1 * 16701) + (0.15 * 51199) + (0.25 * (taxable_income - 67901))
	
	if status == 1 and taxable_income >= 137051 and taxable_income <= 208850:
		tax_amount = (0.1 * 16701) + (0.15 * 51199) + (0.25 * 69150) + (0.28 * (taxable_income - 137051))
	if status == 1 and taxable_income >= 208851 and taxable_income <= 372950:
		tax_amount = (0.1 * 16700) + (0.15 * 51199) + (0.25 *  69150) + (0.28 * 71799) + (0.33 * (taxable_income - 208851))
	if status == 1 and taxable_income >= 372951:
		tax_amount = (0.1 * 16700) + (0.15 * 51199) + (0.25 *  68150) + (0.28 * 71799) + (0.33 * 164099) + (0.35* (taxable_income - 372950))


	if status == 2 and taxable_income <= 8350:
		tax_amount = 0.1 * taxable_income
	
	if status == 2 and taxable_income >= 8351 and taxable_income <= 33950:
		tax_amount = (0.1 * 8350) + (0.15 * (taxable_income - 8350))
	if status == 2 and taxable_income >= 33951 and taxable_income <= 68525:
		tax_amount = (0.1 * 8350) + (0.15 * 25600) + (0.25 * (taxable_income - 33851))
	
	if status == 2 and taxable_income >= 68526 and taxable_income <= 104425:
		tax_amount = (0.1 * 8350) + (0.15 * 25600) + (0.25 * 34574) + (0.28 * (taxable_income - 68526))
	if status == 2 and taxable_income >= 104426 and taxable_income <= 186475:
		tax_amount = (0.1 * 8350) + (0.15 * 25600) + (0.25 *  34574) + (0.28 * 35899) + (0.33 * (taxable_income - 104426))
	if status == 2 and taxable_income >= 186476:
		tax_amount = (0.1 * 8350) + (0.15 * 25600) + (0.25 *  34574) + (0.28 * 35899) + (0.33 * 82049) + (0.35* (taxable_income - 186475))


	if status == 3 and taxable_income <= 11950:
		tax_amount = 0.1 * taxable_income
	
	if status == 3 and taxable_income >= 11950 and taxable_income <= 45500:
		tax_amount = (0.1 * 11950) + (0.15 * (taxable_income - 11950))
	if status == 3 and taxable_income >= 45501 and taxable_income <= 117450:
		tax_amount = (0.1 * 11950) + (0.15 * 33550) + (0.25 * (taxable_income - 45501))
	
	if status == 3 and taxable_income >= 115451 and taxable_income <= 190200:
		tax_amount = (0.1 * 11950) + (0.15 * 33550) + (0.25 * 71949) + (0.28 * (taxable_income - 117450))
	if status == 3 and taxable_income >= 190201 and taxable_income <= 372950:
		tax_amount = (0.1 * 11950) + (0.15 * 33550) + (0.25 *  71949) + (0.28 * 182749) + (0.33 * (taxable_income - 190201))
	if status == 3 and taxable_income >= 372951:
		tax_amount = (0.1 * 11950) + (0.15 * 33550) + (0.25 *  71949) + (0.28 * 182749) + (0.33 * 182749) + (0.35* (taxable_income - 372951))

	return tax_amount

print(status_tax_filer(0, 432778))
print(status_tax_filer(2, 432778))
print(status_tax_filer(1, 432778))
print(status_tax_filer(3, 432778))


	