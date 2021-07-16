from classes.Tree import tree
from classes.Druid import Ximba as Druida
from classes.Hunter import Elias as Hunter
from classes.Mage import Strombf as Mage
from classes.Warrior import Orcud as Warriors

#Druid
jogador1 = Druida_ginsumef = Druida.xim(name="Ginsumef", life=535,atack=123,defense=316,heal=278)
jogador2 = Druida_eightica = Druida.xim(name="Eightica", life=540,atack=96,defense=324,heal=290)

#Hunter
jogador3 = Hunter_sethy = Hunter.eli(name="Sethy", life=623,atack=143,defense=198,heal=0)
jogador4 = Hunter_micksp = Hunter.eli(name="Micksp", life=587,atack=139,defense=183,heal=0)
jogador11 = Hunter_ranteral = Hunter.eli(name="Ranteral", life=487,atack=239,defense=193,heal=0)

#Mage
jogador5 = Mage_caym = Mage.strom(name="Caym", life=356,atack=125,defense=154,heal=0)
jogador6 = Mage_dicho = Mage.strom(name="Dicho", life=319,atack=143,defense=203,heal=0)
jogador10 = Mage_prectrad = Mage.strom(name="Prectrad", life=329,atack=142,defense=213,heal=0)

#Warriors
jogador7 = Warriors_anieba = Warriors.orc(name="Anieba", life=750,atack=134,defense=320,heal=0)
jogador8 = Warriors_terthe = Warriors.orc(name="Terthe", life=789,atack=110,defense=298,heal=0)
jogador9 = Warriors_ify = Warriors.orc(name="Ify", life=779,atack=112,defense=288,heal=0)

tree.heal(jogador1)


