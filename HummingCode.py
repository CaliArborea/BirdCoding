cv =[]

class Aves():

	def __init__(self, flying, name):

		self.classe = 'Aves'
		self.blood = 'Warm-blooded'
		self.vertebrates = True
		self.skin = 'Feathers'
		self.locomotion = 'Wings'
		self.jaw = 'Toothless beak'
		self.reproduction = 'hard-shelled eggs'
		self.heartChamber = 4
		self.fly = flying
		self.temporalRange = 'Late Cretaceous - Present (72 - 0 Ma)'
		self.antiquity = 72000000
		self.metabolism = 'High'
		self.nombre = name
		cv.append(name)

	def estado(self):

		pass



class Trochilidae(Aves):

	def __init__(self, flyingTrochilidae, name):

		super().__init__(flyingTrochilidae, name)
		self.vernacularNames = 'Hummingbirds'
		self.nombresComunes = 'Colibries'
		self.order = 'Apodiformes'
		self.origin = 'South America'
		self.feeding = 'Flower nectar'
		self.species = 361
		self.genera = 113


class Tinamidae(Aves):

	def __init__(self, flyingTinamidae, nameTinamidae):

		super().__init__(flyingTinamidae, nameTinamidae)
		self.vernacularNames = 'Tinamous'
		self.nombresComunes = 'Tinamus'
		self.order = 'Tinamiformes'
		self.size = 'Small to medium'
		self.tail = 'Short'


hum = Trochilidae('Short', 'Tin')

print(Tin.fly)
print(Tin.heartChamber)
print(Tin.tail)
print(Tin.antiquity)
print(Tin.vernacularNames)




class Anatidae(Aves):

	def __init__(self, flyingAnatidae, name):

		super().__init__(flyingAnatidae, name)
		self.vernacularNames = 'Ducks'
		self.nombresComunes = 'Patos y gansos'
		self.order = 'Anseriformes'
		self.size = 'Medium to big'


class Cracidae(Aves):

	def __init__(self, flyingCracidae, name):

		super().__init__(flyingCracidae, name)
		self.vernacularNames = 'Guans and chachalacas'
		self.nombresComunes = 'Guacharacas y pavones'
		self.order = 'Galliformes'
		self.size = 'Big'


class Odontophoridae(Aves):

	def __init__(self, flyingodontophoridae, name):

		super().__init__(flyingOdontophoridae, name)
		self.vernacularNames = 'New World Quails'
		self.nombresComunes = 'Perdices del Nuevo Mundo'
		self.order = 'Galliformes'

class Podicipedidae(Aves):

	def __init__(self, flyingPodicipedidae, name):

		super().__init__(flyingPodicipedidae, name)
		self.vernacularNames = 'Grebes'
		self.nombresComunes = 'Zambullidores'
		self.order = 'Podicipediformes'

class Columbidae(Aves):

	def __init__(self, flyingColumbidae, name):

		super().__init__(flyingColumbidae, name)
		self.vernacularNames = 'Pidgeons and doves'
		self.nombresComunes = 'Palomas y tortolas'
		self.order = 'Columbiformes'


class Cuculidae(Aves):

	def __init__(self, flyingCuculidae, name):

		super().__init__(flyingCuculidae, name)
		self.vernacularNames = 'Cuckoos and anis'
		self.nombresComunes = 'Cucos y garrapateros'
		self.order = 'Cuculiformes'



class Nictibiidae(Aves):

	def __init__(self, flyingNictibiidae, name):

		super().__init__(flyingNictibiidae, name)
		self.vernacularNames = 'Potoos'
		self.nombresComunes = 'Bienparados'
		self.order = 'Nictibiiformes'


class Caprimulgidae(Aves):

	def __init__(self, flyingCaprimulgidae, name):

		super().__init__(flyingCaprimulgidae, name)
		self.vernacularNames = 'Nightjars'
		self.nombresComunes = 'Chotacabras y guardacaminos'
		self.order = 'Caprimulgiformes'


class Apodidae(Aves):

	def __init__(self, flyingApodidae, name):

		super().__init__(flyingCuculidae, name)
		self.vernacularNames = 'Swifts'
		self.nombresComunes = 'Vencejos'
		self.order = 'Apodiformes'


class Aramidae(Aves):

	def __init__(self, flyingAramidae, name):

		super().__init__(flyingAramidae, name)
		self.vernacularNames = 'Limpkin'
		self.nombresComunes = 'Carrao'
		self.order = 'Gruiformes'


class Rallidae(Aves):

	def __init__(self, flyingRallidae, name):

		super().__init__(flyingRallidae, name)
		self.vernacularNames = 'Rails: crakes, coots, and gallinules'
		self.nombresComunes = 'Pollas de agua,  fochas, gallinetas, polluelas, rascones o calamones'
		self.order = 'Gruiformes'


class Charadriidae(Aves):

	def __init__(self, flyingCharadriidae, name):

		super().__init__(flyingCharadriidae, name)
		self.vernacularNames = 'Plovers, dotterels, and lapwings'
		self.nombresComunes = 'Pellares y chorlos'
		self.order = 'Charadriiformes'


class Recurvirostridae(Aves):

	def __init__(self, flyingRecurvirostridae, name):

		super().__init__(flyingRecurvirostridae, name)
		self.vernacularNames = 'Avocets and stilts'
		self.nombresComunes = 'Cigueñuelas'
		self.order = 'Charadriiformes'


class Scolopacidae(Aves):

	def __init__(self, flyingScolopacidae, name):

		super().__init__(flyingScolopacidae, name)
		self.vernacularNames = 'Sandpipers'
		self.nombresComunes = 'Andarrios y caicas'
		self.order = 'Scolopaciformes'


class Jacanidae(Aves):

	def __init__(self, flyingJacanidae, name):

		super().__init__(flyingJacanidae, name)
		self.vernacularNames = 'Jacanas'
		self.nombresComunes = 'Gallitos de cienaga'
		self.order = 'Charadriiformes'


class Anhingidae(Aves):

	def __init__(self, flyingAnhingidae, name):

		super().__init__(flyingAnhingidae, name)
		self.vernacularNames = 'Darters, anhingas or snakebirds'
		self.nombresComunes = 'Pato aguja'
		self.order = 'Suliformes'


class Phalacrocoracidae(Aves):

	def __init__(self, flyingPhalacrocoracidae, name):

		super().__init__(flyingPhalacrocoracidae, name)
		self.vernacularNames = 'Cormorants and shags'
		self.nombresComunes = 'Cormoranes'
		self.order = 'Suliformes'

class Ardeidae(Aves):

	def __init__(self, flyingArdeidae, name):

		super().__init__(flyingArdeidae, name)
		self.vernacularNames = 'Herons'
		self.nombresComunes = 'Garzas'
		self.order = 'Pelecaniformes'


class Threskiornithidae(Aves):

	def __init__(self, flyingThreskiornithidae, name):

		super().__init__(flyingThreskiornithidae, name)
		self.vernacularNames = 'Ibises and spoonbills;'
		self.nombresComunes = 'Ibis'
		self.order = 'Pelecaniformes'


class Cathartidae(Aves):

	def __init__(self, flyingCathartidae, name):

		super().__init__(flyingCathartidae, name)
		self.vernacularNames = 'New World vulture or condor'
		self.nombresComunes = 'Gallinazos'
		self.order = 'Cathartiformes'


class Pandionidae(Aves):

	def __init__(self, flyingPandionidae, name):

		super().__init__(flyingPandionidae, name)
		self.vernacularNames = 'Ospreys'
		self.nombresComunes = 'Aguila pescadora'
		self.order = 'Accipitriformes'


class Accipitridae(Aves):

	def __init__(self, flyingAccipitridae, name):

		super().__init__(flyingAccipitridae, name)
		self.vernacularNames = 'Hawks, eagles, kites, harriers and Old World vultures'
		self.nombresComunes = 'Aguilas y gavilanes'
		self.order = 'Accipitriformes'


class Strigidae(Aves):

	def __init__(self, flyingStrigidae, name):

		super().__init__(flyingStrigidae, name)
		self.vernacularNames = 'Owls'
		self.nombresComunes = 'Buhos'
		self.order = 'Strigiformes'


class Trogonidae(Aves):

	def __init__(self, flyingTrogonidae, name):

		super().__init__(flyingTrogonidae, name)
		self.vernacularNames = 'Trogons and quetzals'
		self.nombresComunes = 'Trogones y quetzales'
		self.order = 'Trogoniformes'


class Momotidae(Aves):

	def __init__(self, flyingMomotidae, name):

		super().__init__(flyingMomotidae, name)
		self.vernacularNames = 'Motmots'
		self.nombresComunes = 'Barranqueros'
		self.order = 'Coraciiformes'


class Alcedinidae(Aves):

	def __init__(self, flyingAlcedinidae, name):

		super().__init__(flyingAlcedinidae, name)
		self.vernacularNames = 'Kingfishers'
		self.nombresComunes = 'Martin pescadores'
		self.order = 'Coraciiformes'



class Bucconidae(Aves):

	def __init__(self, flyingBucconidae, name):

		super().__init__(flyingBucconidae, name)
		self.vernacularNames = 'Puffbirds'
		self.nombresComunes = 'Bobos y monjitas'
		self.order = 'Galbuliformes'


class Capitonidae(Aves):

	def __init__(self, flyingCapitonidae, name):

		super().__init__(flyingCapitonidae, name)
		self.vernacularNames = 'New World barbets'
		self.nombresComunes = 'Toritos'
		self.order = 'Piciformes'


class Ramphastidae(Aves):

	def __init__(self, flyingRamphastidae, name):

		super().__init__(flyingRamphastidae, name)
		self.vernacularNames = 'Toucans'
		self.nombresComunes = 'Tucanes'
		self.order = 'Piciformes'


class Picidae(Aves):

	def __init__(self, flyingPicidae, name):

		super().__init__(flyingPicidae, name)
		self.vernacularNames = 'Woodpeckers'
		self.nombresComunes = 'Carpinteros'
		self.order = 'Piciformes'


class Falconidae(Aves):

	def __init__(self, flyingFalconidae, name):

		super().__init__(flyingFalconidae, name)
		self.vernacularNames = 'Falcons and caracaras'
		self.nombresComunes = 'Halcones'
		self.order = 'Falconiformes'


class Psittacidae(Aves):

	def __init__(self, flyingPsittacidae, name):

		super().__init__(flyingPsittacidae, name)
		self.vernacularNames = 'Parrots'
		self.nombresComunes = 'Guacamayas, pericos y loras'
		self.order = 'Psittaciformes'

class Thamnophilidae(Aves):

	def __init__(self, flyingThamnophilidae, name):

		super().__init__(flyingThamnophilidae, name)
		self.vernacularNames = 'Antbirds'
		self.nombresComunes = 'Hormigueros'
		self.order = 'Passeriformes'

class Conopophagidae(Aves):

	def __init__(self, flyingConopophagidae, name):

		super().__init__(flyingConopophagidae, name)
		self.vernacularNames = 'Gnateaters'
		self.nombresComunes = 'Zumbadores'
		self.order = 'Passeriformes'


class Grallariidae(Aves):

	def __init__(self, flyingGrallariidae, name):

		super().__init__(flyingGrallariidae, name)
		self.vernacularNames = 'Antpittas'
		self.nombresComunes = 'Tororois'
		self.order = 'Passeriformes'


class Rhinocryptidae(Aves):

	def __init__(self, flyingRhinocryptidae, name):

		super().__init__(flyingRhinocryptidae, name)
		self.vernacularNames = 'Tapaculos'
		self.nombresComunes = 'Tapaculos'
		self.order = 'Passeriformes'


class Furnariidae(Aves):

	def __init__(self, flyingFurnariidae, name):

		super().__init__(flyingFurnariidae, name)
		self.vernacularNames = 'Ovenbirds'
		self.nombresComunes = 'Horneros, coluditos y rastrojeros'
		self.order = 'Passeriformes'


class Tyrannidae(Aves):

	def __init__(self, flyingTyrannidae, name):

		super().__init__(flyingTyrannidae, name)
		self.vernacularNames = 'Tyrant flycatchers'
		self.nombresComunes = 'Atrapamoscas'
		self.order = 'Passeriformes'


class Cotingidae(Aves):

	def __init__(self, flyingCotingidae, name):

		super().__init__(flyingCotingidae, name)
		self.vernacularNames = 'Cotingas'
		self.nombresComunes = 'Cotingas'
		self.order = 'Passeriformes'


class Pipridae(Aves):

	def __init__(self, flyingPipridae, name):

		super().__init__(flyingPipridae, name)
		self.vernacularNames = 'Manakins'
		self.nombresComunes = 'Saltarines'
		self.order = 'Passeriformes'

class Tityridae(Aves):

	def __init__(self, flyingTityridae, name):

		super().__init__(flyingTityridae, name)
		self.vernacularNames = 'Tityras'
		self.nombresComunes = 'Tityras'
		self.order = 'Passeriformes'


class Vireonidae(Aves):

	def __init__(self, flyingVireonidae, name):

		super().__init__(flyingVireonidae, name)
		self.vernacularNames = 'Vireos'
		self.nombresComunes = 'Verderones'
		self.order = 'Passeriformes'		

class Corvidae(Aves):

	def __init__(self, flyingCorvidae, name):

		super().__init__(flyingCorvidae, name)
		self.vernacularNames = ' crows, ravens, rooks, jackdaws, jays, magpies, treepies, choughs, and nutcrackers'
		self.nombresComunes = 'Cuervos, urracas y carriquies'
		self.order = 'Passeriformes'


class Hirundinidae(Aves):

	def __init__(self, flyingHirundinidae, name):

		super().__init__(flyingHirundinidae, name)
		self.vernacularNames = 'Swallows, martins, and saw-wings'
		self.nombresComunes = 'Golondrinas'
		self.order = 'Passeriformes'

class Troglodytidae(Aves):

	def __init__(self, flyingTroglodytidae, name):

		super().__init__(flyingTroglodytidae, name)
		self.vernacularNames = 'Wrens'
		self.nombresComunes = 'Cucaracheros'
		self.order = 'Passeriformes'


class Cinclidae(Aves):

	def __init__(self, flyingCinclidae, name):

		super().__init__(flyingCinclidae, name)
		self.vernacularNames = 'Dippers'
		self.nombresComunes = 'Mirlo acuatico'
		self.order = 'Passeriformes'

class Turdidae(Aves):

	def __init__(self, flyingTurdidae, name):

		super().__init__(flyingTurdidae, name)
		self.vernacularNames = 'Thrushes'
		self.nombresComunes = 'Solitarios, zorzales y mirlas'
		self.order = 'Passeriformes'


class Mimidae(Aves):

	def __init__(self, flyingMimidae, name):

		super().__init__(flyingMimidae, name)
		self.vernacularNames = 'Thrashers, mockingbirds, tremblers, and the New World catbirds'
		self.nombresComunes = 'Sinsontes'
		self.order = 'Passeriformes'


class Estrildidae(Aves):

	def __init__(self, flyingEstrildidae, name):

		super().__init__(flyingEstrildidae, name)
		self.vernacularNames = 'Estrildid finches'
		self.nombresComunes = 'Pinzones'
		self.order = 'Passeriformes'

class Fringillidae(Aves):

	def __init__(self, flyingFringillidae, name):

		super().__init__(flyingFringillidae, name)
		self.vernacularNames = 'True finches'
		self.nombresComunes = 'Pinzones'
		self.order = 'Passeriformes'


class Passerellidae(Aves):

	def __init__(self, flyingPasserellidae, name):

		super().__init__(flyingPasserellidae, name)
		self.vernacularNames = 'New World sparrows'
		self.nombresComunes = 'Gorriones'
		self.order = 'Passeriformes'


class Icteridae(Aves):

	def __init__(self, flyingIcteridae, name):

		super().__init__(flyingIcteridae, name)
		self.vernacularNames = 'New World blackbirds, New World orioles, the bobolink, meadowlarks, grackles, cowbirds, oropendolas, and caciques'
		self.nombresComunes = 'Chamones, oropoendolas y turpiales'
		self.order = 'Passeriformes'


class Parulidae(Aves):

	def __init__(self, flyingParulidae, name):

		super().__init__(flyingParulidae, name)
		self.vernacularNames = 'New World warblers'
		self.nombresComunes = 'Reinitas'
		self.order = 'Passeriformes'


class Cardinalidae(Aves):

	def __init__(self, flyingCardinalidae, name):

		super().__init__(flyingCardinalidae, name)
		self.vernacularNames = 'Cardinals'
		self.nombresComunes = 'Cardenales'
		self.order = 'Passeriformes'


class Thraupidae(Aves):

	def __init__(self, flyingThraupidae, name):

		super().__init__(flyingThraupidae, name)
		self.vernacularNames = 'Tanagers'
		self.nombresComunes = 'Tangaras'
		self.order = 'Passeriformes'


























