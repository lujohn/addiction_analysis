# https://www.drugrehab.org/common-street-names-illegal-drugs/
# drug_names = ['cocaine','aunt nora', 'bernice', 'blow', 'bump', 'c', 'candy', 'coke', 'dust',
#               'nose candy', 'rock', 'snow', 'flake', 'mojo', 'white',
#               'crack', 'sleet','snow coke', 'ice', 'barbituates', 'barbs', 'phennies', 
#               'pill','pills', 'valium', 'roofies', 'roofie', 'rophies', 'benzos', 
#               'sleeping pills', 'downers', 'rohypnol', 'benzodiazepines', 
#               'date rape drug', 'drug', 'drugs', 'rope', 'ketamine', 'green', 'k', 
#               'special k', 'acid', 'super acid', 'vitamin k', 'lsd', 'blotter', 
#               'dots', 'zen', 'peyote', 'mescaline', 'pcp', 'angel dust', 'psilocybin', 
#               'smoke', 'mushrooms', 'shrooms', 'shroom', 'purple passion', 
#               'magic mushrooms','ecstasy', 'mdma','e', 'molly', 'love drug', 
#               'love pill', 'snowball', 'cloud','devil drug', 'kool-aid', 
#               'electric kool-aid', 'kool aid', 'reds', 'yellows', 
#               'flunitrazepam', 'r2', 'roaches', 'tranks', 'sleep medications', 
#               'jet', 'tab', 'pane', 'sunshine', 'mesc', 'cactus', 'buttons', 'boat', 
#               'x', 'xe', 'xtc', 'speed', 'heroin', 'brown sugar', 'dope', 'h', 'hell dust',
#               'skunk', 'skag', 'junk', 'smack', 'thunder', 'inhalants', 'blast', 
#               ' bolt', 'aroma', 'boppers', 'highball', 'huff', 'gas', 'snotballs', 
#               'spray', 'thrust', 'shoot the breeze', 'oz', 'kat', 'oat', 'chat', 'catha', 
#               'khat', 'kratom', 'speedball', 'ketum', 'kahuam', 'thom','biak-biak',
#               'marijuana', 'bhang', 'blunt', 'bud', 'blaze', 'dagga', 'dope', 'high', 
#               'ganja', 'grass', 'dagga', 'green', 'hemp', 'herb', 'j', 'joint', 
#               'mary jane', 'pot', 'puff', 'reefer', 'roach', 'skunk', 'smoke', 'weed',
#               'hashish', 'boom', 'hash', 'methamphetamine', 'beanies', 'crank', 'chalk',
#               'chicken feed', 'crink', 'crypto', 'crystal', 'fire', 'glass', 'ice', 'meth',
#               'tweak', 'wash', 'crystal meth', 'blade', 'crystal glass', 'quartz', 
#               'over-the-counter', 'ccc', 'dxm', 'robo', 'tripping', 
#               'opioids', 'codeine', 'cody', 'lean', 'loads', 'schoolboy', 
#               'purple drank', 'sizzurp', 'fentanyl', 'apache', 'goodfella', 'jackpot', 
#               'tango and cash', 'tnt', 'hydrocodone', 'dihydrocodeinone', 'hydromorphone', 
#               'd', 'dillies', 'juice', 'footballs', 'meperidine', 'painkiller', 'demmies',
#               'methadone', 'amidone', 'fizzies', 'morphine', 'm', 'monkey', 'white stuff',
#               'oxycodone', 'o.c.', 'oxy 80', 'oxycat', 'oxycet', 'oxy', 'percs', 'oxycotton',
#               'oxymorphone', 'blues', 'octagons', 'o','blues', 'stimulants', 'amphetamine',
#               'adderall', 'benzedrine', 'bennies', 'crosses', 'black beauties', 'uppers',
#               'methylphenidate', 'concerta', 'ritalin', 'diet coke', 'kiddie cocaine',
#               'skippy', 'skittles', 'vitamin R', 'smarties', 'r-ball', 'mph', 'jif', 'synthetic',
#               'k2', 'spice', 'bath salts', 'bliss', 'bloom', 'euphoria', 'wave', 'sextasy', 
#               'stardust', 'powder', 'alcohol', 'booze', 'sauce', 'hooch', 'juice', 'vivitrol', 
#              'clonidine','zoloft', 'prozac', 'inhalants', 'inhalant', 'vicodine', 'benzo']


cocaine = ['Aunt Nora','Bernice','Binge','Blow','Bump','C','Candy','Charlie','Coke','Dust','Flake','Mojo','Nose Candy','Paradise',
		   'Rock', 'Sneeze','Sniff','Snow','Toot','24-7','Apple jacks','Badrock','Ball','Base','Beat','Candy','Chemical',
		   'Cloud','Cookies','Crack','Crumbs','Crunch and munch','Devil drug','Dice','Electric kool-aid','Fat bags','French fries','Glo','Gravel','Grit','Hail',
			  'Hard ball','Hard rock','Hotcakes','Ice cube','Jelly beans','Kryptonite','Nuggets','Paste','Piece','Prime time','Product,Raw',
			  'Rock','Rockstar','Roxanne','Scrabble','Sleet','Snow coke','Sugar block', 'Topo','Tornado','Troop', 'kool-aid',
		  'kool aid', 'cocaine']

cocaine = [x.lower() for x in cocaine]

# cocaine = set(cocaine) & set(drug_names)
cocaine = list(cocaine)


barbituates = ['Barbs','Phennies','Red birds', 'Reds', 'Tooies', 'Yellow jackets', 'Yellows', 'barbituates']
barbituates = [x.lower() for x in barbituates]
# barbituates = set(barbituates) & set(drug_names)
barbituates = list(barbituates)


benzodiazepines = ['Rohypnol', 'Flunitrazepam','Circles', 'Date rape drug', 'Forget pill', 'Forget-me pill', 'La Rocha',
				   'Lunch money', 'Mexican Valium','Mind eraser','Pingus', 'R2', 'Reynolds', 'Rib', 'Roach', 'Roach 2',
				   'Roaches','Roachies', 'Roapies', 'Rochas Dos', 'Roofies', 'Rope', 'Rophies', 'Row-shay', 'Ruffies',
				   'Trip-and-fall', 'Wolfies', 'Benzos', 'Candy', 'Downers', 'Sleeping pills', 'Tranks', 'roofie', 
				   'benzodiazepine', 'benzodiazepines', 'valium', 'benzo']
benzodiazepines = [x.lower() for x in benzodiazepines]
# benzodiazepines = list(set(benzodiazepines) & set(drug_names))

ketamine = ['Cat Valium', 'Jet', 'Special K', 'Super acid', 'Super C', 'Vitamin K', 'ketamine']
ketamine = [x.lower() for x in ketamine]
# ketamine = list(set(ketamine) & set(drug_names))

lsd = ['Acid', 'Battery acid', 'Blotter', 'Bloomers', 'Blue heaven', 'California Sunshine', 'Cid', 'Cubes', 'Doses',
	   'Dots', 'Golden dragon', 'Heavenly blue', 'Hippie', 'Loony toons', 'Lucy in the sky with diamonds', 'Microdot',
	   'Pane', 'Purple Heart', 'Superman', 'Tab', 'Window pane', 'Yellow sunshine', 'Zen', 'lsd']
lsd = [x.lower() for x in lsd]
#lsd = list(set(lsd) & set(drug_names))

mescaline = ['Buttons', 'Cactus', 'Mesc', 'mescaline', 'peyote']
mescaline = [x.lower() for x in mescaline]
#mescaline = list(set(mescaline) & set(drug_names))

pcp = ['Angel dust', 'Boat', 'Hog', 'Love boat', 'Peace pill','pcp']
pcp = [x.lower() for x in pcp]
#pcp = list(set(pcp) & set(drug_names))

psilocybin = ['Little smoke', 'Magic mushrooms', 'Purple passion', 'Shrooms', 'psilocybin', 'mushrooms']
psilocybin = [x.lower() for x in psilocybin]
#psilocybin = list(set(psilocybin) & set(drug_names))

ecstasy = ['Adam', 'Beans', 'Cadillac', 'California sunrise', 'Clarity', 'Essence', 'Elephants', 'Eve', 'Hug',
		   'Hug drug', 'Love drug', 'Love pill', 'Lover’s speed', 'Molly', 'Peace', 'Roll', 'Scooby snacks', 'Snowball',
		   'Uppers', 'XE', 'XTC', 'ecstasy', 'mdma']
ecstasy = [x.lower() for x in ecstasy]
#ecstasy = list(set(ecstasy) & set(drug_names))

heroin = ['Brown sugar', 'China White', 'Dope', 'Hell dust', 'Horse', 'Junk', 'Nose drops', 'Skag', 'Skunk',
	  'Smack', 'Thunder', 'White horse', 'Cheese', 'heroin']


heroin = [x.lower() for x in heroin]
#heroin = list(set(heroin) & set(drug_names)) 

inhalants = ['Air blast', 'Ames', 'Amys', 'Aroma of men', 'Bolt', 'Boppers', 'Bullet', 'Bullet bolt', 'Buzz bomb',
			 'Discorama', 'Hardware', 'Heart-on', 'Hiagra-in-a-bottle', 'Highball', 'Hippie crack', 'Huff',
			 'Locker room', 'Medusa', 'Moon gas', 'Oz', 'Pearls', 'Poor man’s pot', 'Poppers','Quicksilver', 'Rush snappers',
			 'Satan’s secret', 'Shoot the breeze', 'Snappers', 'Snotballs', 'Spray', 'Texas shoe shine', 'Thrust',
			 'Toilet water', 'Toncho', 'Whippets', 'Whiteouts', 'inhalant', 'inhalants']

inhalants = [x.lower() for x in inhalants]
#inhalants = list(set(inhalants) & set(drug_names)) 

khat = ['Abyssinian tea', 'African salad', 'Catha', 'Chat', 'Kat', 'Oat', 'khat']

khat = [x.lower() for x in khat]
#khat = list(set(khat) & set(drug_names)) 



kratom = ['Biak-biak', 'Herbal speedball', 'Ketum', 'Kahuam', 'Ithang', 'Thom', 'kratom']

kratom = [x.lower() for x in kratom]
#kratom = list(set(kratom) & set(drug_names)) 



marijuana = ['Astro Yurf','Bhang', 'Blunt', 'Bud', 'Blaze', 'Dagga', 'Dope', 'Dry high', 'Ganja', 'Grass', 'Green',
			 'Hemp', 'Herb', 'Home grown', 'Joint', 'Mary Jane', 'Pot', 'Puff', 'Reefer', 'Roach', 'Sinsemilla', 
			 'Skunk', 'Smoke', 'Texas tea', 'Trees', 'Weed', 'White widow', 'marijuana', 'k2', 'spice']
marijuana = [x.lower() for x in marijuana]
#marijuana = list(set(marijuana) & set(drug_names)) 



hashish = ['Boom', 'Chocolate', 'Gangster', 'Hash', 'Hemp', 'hashish']

hashish = [x.lower() for x in hashish]
#hashish = list(set(hashish) & set(drug_names))



methamphetamine = ['Beanies', 'Brown', 'Crank', 'Chalk', 'Chicken feed', 'Cinnamon', 'Crink', 'Crypto', 'Crystal',
				   'Get go', 'Glass', 'Go fast', 'Ice', 'Meth', 'Methlies quick', 'Mexican crack',
				   'Redneck cocaine', 'Speed', 'Tick tick', 'Tweak', 'Wash', 'Yellow powder', 'methamphetamine',
				 ' Batu', 'blade', 'cristy',' crystal', 'crystal glass', 'hot ice', 
				 'shabu',' shards', 'stove top', 'Tina', 'ventana']
methamphetamine = [x.lower() for x in methamphetamine]
#methamphetamine = list(set(methamphetamine) & set(drug_names))



over_counter = ['CCC', 'DXM', 'Poor man’s PCP', 'Robo', 'Robotripping', 'Skittles', 'Triple C']
over_counter = [x.lower() for x in over_counter]
#over_counter = list(set(over_counter) & set(drug_names))


codeine = ['Captain Cody', 'Cody', 'Doors and fours', 'Lean','Loads', 'Pancakes and syrup', 'Purple drank', 
		   'Schoolboy', 'Sizzurp', 'codeine']

codeine = [x.lower() for x in codeine]
#codeine = list(set(codeine) & set(drug_names))


fentanyl = ['Apache', 'China girl', 'China white', 'Dance fever', 'Goodfella', 'Jackpot', 'Murder 8', 
			'Tango and Cash', 'TNT', 'Hydrocodone', 'Dihydrocodeinone','Vike', 'Watson 387', 'fentanyl', 'vicodine']

fentanyl = [x.lower() for x in fentanyl]
#fentanyl = list(set(fentanyl) & set(drug_names))


hydromorphone = ['Dillies', 'Footballs', 'Juice', 'Smack', 'hydromorphone']
hydromorphone = [x.lower() for x in hydromorphone]
#hydromorphone = list(set(hydromorphone) & set(drug_names))



meperidine = ['Demmies', 'meperidine']
meperidine = [x.lower() for x in meperidine]
#meperidine= list(set(meperidine) & set(drug_names))


methadone = ['Amidone', 'Fizzies', 'methadone']

methadone = [x.lower() for x in methadone]
#methadone = list(set(methadone) & set(drug_names))


morphine = ['Miss Emma', 'Monkey', 'White stuff', 'morphine']

morphine = [x.lower() for x in morphine]
#morphine = list(set(morphine) & set(drug_names))


oxycodone = ['O.C.', 'Oxy 80', 'Oxycat', 'Oxycet', 'Oxycotton', 'Oxy', 'Hillbilly heroin', 'Percs', 'Perks', 'oxy', 'oxycodone']
oxycodone = [x.lower() for x in oxycodone]
#oxycodone = list(set(oxycodone) & set(drug_names))


oxymorphone = ['Biscuits', 'Blue heaven', 'Blues', 'Heavenly blues', 'Mrs. O', 'O bombs', 'Octagons', 'Stop signs', 'oxymorphone']

oxymorphone = [x.lower() for x in oxymorphone]
#oxymorphone = list(set(oxymorphone) & set(drug_names))


amphetamine = ['Bennies', 'Black beauties', 'Crosses', 'Hearts', 'LA Turnaround', 'Truck drivers', 'Uppers', 'adderall', 
			  'benzedrine', 'amphetamine']

amphetamine = [x.lower() for x in amphetamine]
#amphetamine = list(set(amphetamine) & set(drug_names))



methylphenidate = ['concerta', 'ritalin','Diet coke','JIF', 'Kiddie cocaine', 'Kiddie coke', 'MPH', 'Poor man’s cocaine',
				   'R-ball', 'Skippy', 'Skittles', 'Smarties', 'The Smart Drug', 'Vitamin R', 'methylphenidate']

methylphenidate = [x.lower() for x in methylphenidate]
#methylphenidate = list(set(methylphenidate) & set(drug_names))


bath_salts = ['bath salts', 'Arctic blasts', 'Aura', 'Avalance', 'Avalanche', 'Bliss', 'Blizzard', 'Bloom',
			  'Blue silk', 'Bolivian bath', 'Cloud nine', 'Cotton cloud', 'Drone', 'Dynamite', 'Dynamite plus', 'Euphoria',
			  'Glow stick', 'Hurricane Charlie', 'Ivory snow', 'Ivory wave', ' Ivory wave ultra', 'Lunar wave','Mexxy',
			  'Mind change', 'Mino Charge', 'Monkey dust', 'Mystic', 'Natural energy powder', 'Ocean snow', 'Purple wave',
			  'Quicksilver', 'Recharge', 'Red dawn', 'Red dove', 'Rock on', 'Rocky Mountain High', 'Route 69', 'Sandman Party Powder',
			  'Scarface', 'Sextasy', 'Shock wave', 'Snow day', 'Snow leopard', 'Speed freak miracle', 'Stardust',
			  'Super coke', 'Tranquility', 'UP energizing', 'UP Supercharged', 'Vanilla Sky', 'White burn', 'White China',
			  'White dove', 'White lightning', 'White rush', 'White Sands', 'Wicked X', 'XX', 'Zoom']

bath_salts = [x.lower() for x in bath_salts]
#bath_salts = list(set(bath_salts) & set(drug_names))

alcohol = ['alcohol', 'booze', 'sauce', 'hooch', 'juice']

vivitrol = ['vivitrol']

clonidine = ['clonidine']
antidepressants = ['zoloft', 'prozac'] 


def get_drugs_dict():
	# creating lookup table: 
	all_names = {'cocaine': cocaine,
			  'heroin': heroin,
				'barbituates' : barbituates,
				'benzodiazepines': benzodiazepines,
				'ketamine': ketamine, 
				'lsd': lsd, 
				'mescaline': mescaline,
				'pcp': pcp, 
				'marijuana': marijuana,
				'psilocybin': psilocybin,
				'ecstasy': ecstasy, 
				'inhalants': inhalants, 
				'khat': khat, 
				'kratom': kratom, 
				'hashish': hashish, 
				'methamphetamine': methamphetamine,
				'over_counter': over_counter,
				'codeine': codeine,
				'fentanyl': fentanyl,
				'hydromorphone': hydromorphone,
				'meperidine': meperidine, 
				'methadone':methadone, 
				'morphine': morphine,
				'oxycodone': oxycodone, 
				'oxymorphone': oxymorphone, 
				'amphetamine': amphetamine, 
				'methylphenidate': methylphenidate,
				'bath_salts': bath_salts, 
				'alcohol': alcohol, 
				'vivitrol': vivitrol, 
				'clonidine': clonidine, 
				'antidepressants': antidepressants}
	return all_names


def get_drugs_list():
	all_drugs = set()
	DRUGS_DICT = get_drugs_dict()
	for official_name in DRUGS_DICT:
		all_drugs |= (set([official_name]) | set(DRUGS_DICT[official_name]))

	return all_drugs


def get_support_groups():
	return ['12-step',
		  '12 step',
		  'Alcoholics Anonymous',
		  'AA',
		  'Heroin Anonymous',
		  'HA',
		  'Cocaine Anonymous',
		  'CA',
		  'Crystal Meth Anonymous',
		  'CMA',
		  'Narcotics Anonymous',
		  'NA',
		  'Secular Organizations for Sobriety',
		  'SOS',
		  'Rational Recovery',
		  'RR',
		  'Self Management and Recovery Training',
		  'SMART']