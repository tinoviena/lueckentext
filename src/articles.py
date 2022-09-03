import enum

bestimmte_artikel_einzahl_table = \
                    [["fall", "maskulin", "feminin", "neutral"],
                     ["nominativ", "der", "die", "das"],
                     ["genetiv", "des", "der", "des"],
                     ["dativ", "dem", "der", "dem"],
                     ["akkusativ", "den", "die", "das"]
                    ]

bestimmte_artikel_mehrzahl_table = \
                    [["fall",      "maskulin", "feminin", "neutral"],
                     ["nominativ", "die",      "die",     "die"],
                     ["genetiv",   "der",      "der",     "der"],
                     ["dativ",     "den",      "den",     "den"],
                     ["akkusativ", "die",      "die",     "die"]
                    ]

class faelle(enum.Enum):
    NOMINATIV = "nominativ"
    GENETIV = "genetiv"
    DATIV = "dativ"
    AKKUSATIV = "akkusativ"
class genus(enum.Enum):
    MASKULIN = "maskulin"
    FEMININ = "feminin"
    NEUTRUM = "neutral"

def all() -> [str]:
    flat_list1 = set([item for sublist in bestimmte_artikel_einzahl_table[1:] for item in sublist[1:]])
    flat_list2 = set([item for sublist in bestimmte_artikel_mehrzahl_table[1:] for item in sublist[1:]])
    return(flat_list1.union(flat_list2))

def get_article(fall :str, genus: str) -> str:
    row_filter = filter(lambda x : x[0] == fall.value, bestimmte_artikel_einzahl_table)
    row = list(row_filter)[0] # list(row) is sth like [['akkusativ', 'den', 'die', 'das']]
    genus_index = bestimmte_artikel_einzahl_table[0].index(genus.value)

    cell = row[genus_index] 
    
    return cell