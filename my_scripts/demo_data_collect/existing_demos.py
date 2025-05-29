
list_propose_demos = [

    {
        "input": """Current Board:
_____
_____
_____
_____
_____

Unfilled:
h1. _____ -- Presented; revealed

h2. _____ -- An interjection expressing sorrow

h3. _____ -- Benefit; result

h4. _____ -- A cigarette

h5. _____ -- Chased up a tree

v1. _____ -- Swarthy; tawny

v2. _____ -- An apiarist or bee keeper

v3. _____ -- To speak formally

v4. _____ -- To indite; to scribble

v5. _____ -- An insecticide

Filled:

Changed:

Response: """,
        "output": """h1. shown (high)
h2. wirra (medium)
h3. avail (high)
h4. rette (medium)
h5. treed (high)
v1. swart (high)
v2. hiver (high)
v3. orate (high)
v4. write (medium)
v5. naled (high)""" },
    {"input": "current board:\n__es_\n__do_\n__en_\n__ma_\n__ar_\n\nunfilled:\nh2. __do_ -- an oxidation/reduction reaction\n\nv1. _____ -- a crwth\n\nh1. __es_ -- to choose\n\nv5. _____ -- to praise; to raise higher\n\nh4. __ma_ -- the blue titmouse\n\nv2. _____ -- to praise; to worship\n\nh3. __en_ -- an indian mallow\n\nh5. __ar_ -- a center; a body organ\n\nfilled:\nv3. edema -- excessive fluid accumulation\n\nv4. sonar -- an underwater detection system (sound navigation ranging)\n\nchanged:\n\n", "output": "h1. chose (high)\nh2. redox (certain)\nh3. mall (medium)\nh4. chick (low), titma (low)\nv1. crwth (certain)\nv2. laud (high), venerate (medium) \nv3. edema (certain) \nv4. sonar (certain) \nv5. heart, liver, lung, etc., organ in general terms but needs to fit the 5-letter constraint and be a center or body organ which fits best with \"heart\" or \"liver\" as common organs that are centers.\nh5 heart(certain) \n\nNote: For h4 and v2, multiple options are provided due to the constraints of fitting a 5-letter word that matches the given definitions accurately within the crossword format.\n\nChanged:\nh4: titma -> chick\nv2: laud -> venerate"},
{"input": "current board:\n_aes_\n_ddo_\n_oen_\n_rma_\nheart\n\nunfilled:\nv1. ____h -- a crwth\n\nh3. _oen_ -- an indian mallow\n\nh2. _ddo_ -- an oxidation/reduction reaction\n\nv5. ____t -- to praise; to raise higher\n\nh1. _aes_ -- to choose\n\nh4. _rma_ -- the blue titmouse\n\nfilled:\nv2. adore -- to praise; to worship\n\nv4. sonar -- an underwater detection system (sound navigation ranging)\n\nv3. edema -- excessive fluid accumulation\n\nh5. heart -- a center; a body organ\n\nchanged:\n\nsuggestions:\nplan the strategy to focus on valid 5-letter words.\nstart with a common vowel in the middle column to maximize connections.\navoid using words that are already marked as incorrect.\nchoose words that can serve multiple meanings or have high versatility.\nensure each word fits both horizontally and vertically before placing.\n\n", "output": "h1. case (medium)\nh2. redo (high)\nh3. oleo (high)\nv1. crwth (certain)\nv5. level (certain)"},
{"input": "current board:\n_____\n_____\n_____\n_____\n_____\n\nunfilled:\nh5. _____ -- a center; a body organ\n\nv5. _____ -- to praise; to raise higher\n\nv3. _____ -- excessive fluid accumulation\n\nv1. _____ -- a crwth\n\nv4. _____ -- an underwater detection system (sound navigation ranging)\n\nh4. _____ -- the blue titmouse\n\nh2. _____ -- an oxidation/reduction reaction\n\nv2. _____ -- to praise; to worship\n\nh3. _____ -- an indian mallow\n\nh1. _____ -- to choose\n\nfilled:\n\nchanged:\n\nsuggestions:\nplan the approach by focusing on correct placements for known letters.\nreplace redox with a word that fits the clue and letter constraints.\nchoose a word for w___a that aligns with the vertical and horizontal clues.\nselect an appropriate word for c___e that connects well with the surrounding words.\nreview and adjust choices to ensure all words are correct and fit their respective clues.\n\n", "output": "h1. pick (high)\nh2. redox (medium) / react (high)\nh3. abram (low) / abaca (medium)\nh4. titme (low) / titmo (low) / titch (medium)\nv1. crwth (certain)\nv2. laudn (low) / lauds (high)\nv3. edema (certain)\nv4. sonar (certain)\nv5. hearten (low) / hearted(certain)\n\nfilled:\ncrwth\n_____\nedema\nsonar\nhearted"},
{"input": "current board:\n_____\n_____\n_____\n_____\n_____\n\nunfilled:\nv1. _____ -- to impress; to brand; to mark\n\nv3. _____ -- oorali, a poison used on arrows\n\nh5. _____ -- a torture instrument similar to the knout\n\nv2. _____ -- flat; a stage; to be honest with\n\nh4. _____ -- a mill\n\nv5. _____ -- to fillet\n\nh1. _____ -- to discard; to slough\n\nv4. _____ -- to collapse; barely detectable\n\nh2. _____ -- a wide-brimmed sun hat; nepalese lowlands; a bamboo-like plant\n\nh3. _____ -- benefit; result\n\nfilled:\n\nchanged:\n\n", "output": "h1. sluff (high)\nv1. stamp (high)\nv2. level (high)\nv3. urali (certain)\nh5. knout (high)\nv4. faint (medium)\nh2. topee (high), tarai (medium), bamboo (low) \nh3. avail (certain) \nv5. filly (medium), filer (low)"},
{"input": "current board:\n_lu__\n_er__\navail\n_el__\n_li__\n\nunfilled:\nv1. __a__ -- to impress; to brand; to mark\n\nv4. __i__ -- to collapse; barely detectable\n\nh5. _li__ -- a torture instrument similar to the knout\n\nh1. _lu__ -- to discard; to slough\n\nh4. _el__ -- a mill\n\nv5. __l__ -- to fillet\n\nh2. _er__ -- a wide-brimmed sun hat; nepalese lowlands; a bamboo-like plant\n\nfilled:\nh3. avail -- benefit; result\n\nv3. urali -- oorali, a poison used on arrows\n\nv2. level -- flat; a stage; to be honest with\n\nchanged:\n\n", "output": "h1. sluff (high)\nh2. sombr (medium), terai (low), canna (low)\nh4. mill (certain)\nv1. mark (high)\nv4. fail (high), thin (medium)\nv5. filet (certain)"}



                      ]


list_if_correct_demos = [
    {
        "input": 'Does EERIE has meaning "To seek"? Respond only Yes or No.',
        "output": "No",
    },
{
        "input": 'Does RENOX has meaning "An oxidation/reduction reaction"? Respond only Yes or No.',
        "output": "No",
    },
{
        "input": 'Does ABOMA has meaning "A South American boa constrictor"? Respond only Yes or No.',
        "output": "No",
    },
{
        "input": 'Does ABOMA has meaning "A South American boa constrictor"? Respond only Yes or No.',
        "output": "Yes",
    },
{
        "input": 'Does CRAVE has meaning "To crave"? Respond only Yes or No.',
        "output": "Yes",
    },
{
        "input": 'Does UNAPT has meaning "Unfit; clumsy"? Respond only Yes or No.',
        "output": "Yes",
    },

]

list_suggest_demos = [
    {"input": "\nGiven the current status:\ncurrent board:\nscurf\nelver\nbouse\nunlit\nmeant\n\n\nThe target words are classified as Correct Words, and Incorrect Words.\n---Correct Words:\nh1. SCURF -- Dandruff; scum; the bull-trout\nh2. ELVER -- A baby eel\nh5. MEANT -- Implied; intended\nv1. SEBUM -- An oily gland secretion\nv2. CLONE -- A genetic duplicate\n---\nIncorrect Words:\nh3. BOUSE -- Booze; to haul via tackle\nh4. UNLIT -- Not lit\nv3. UVULA -- The soft palate\nv4. RESIN -- A sticky plant sap\nv5. FRETT -- Ore refuse; to prepare material for glass by heat\n---You will retry the game. Write a plan for the next time. \nRespond at most five sentences, one sentence per line.\nDo not include the phrase \"next time\" in your response.\n\nResponse: ", "output": "Replace BOUSE with a correct 5-letter word that fits the vertical intersections.\nChoose a word for UNLIT that aligns with both horizontal and vertical constraints.\nSelect a valid 5-letter word for UVULA that matches the intersecting letters from horizontal words.\nFind an appropriate 5-letter word for RESIN that fits the puzzle's current structure.\nEnsure FRETT is replaced with a correct term that meets all crossword rules."},
    {"input": "\nGiven the current status:\ncurrent board:\n__u__\n__r__\navail\n__l__\n__i__\n\n\nThe target words are classified as Correct Words, and Incorrect Words.\n---Correct Words:\nv3. URALI -- Oorali, a poison used on arrows\n---\nIncorrect Words:\nh3. AVAIL -- Benefit; result\n---You will retry the game. Write a plan for the next time. \nRespond at most five sentences, one sentence per line.\nDo not include the phrase \"next time\" in your response.\n\nResponse: ", "output": "Start with a word that has a high probability of matching the given clues.\nFor the vertical slot, consider using 'OMBRE' since it fits two different clues.\nEnsure to cross-check each letter placement with potential horizontal words.\nChoose words that can interlock well, like 'LEVEL' for the horizontal if it fits.\nReview all possible 5-letter words that match the remaining clues before finalizing."},
    {"input": "\nGiven the current status:\ncurrent board:\nsluff\nte_a_\navail\nme_n_\npl_t_\n\n\nThe target words are classified as Correct Words, and Incorrect Words.\n---Correct Words:\nh1. SLUFF -- To discard; to slough\nv1. STAMP -- To impress; to brand; to mark\nv4. FAINT -- To collapse; barely detectable\n---\nIncorrect Words:\nh3. AVAIL -- Benefit; result\nv2. LEVEL -- Flat; a stage; to be honest with\n---You will retry the game. Write a plan for the next time. \nRespond at most five sentences, one sentence per line.\nDo not include the phrase \"next time\" in your response.\n\nResponse: ", "output": "I will aim to replace 'AVAIL' with a correct 5-letter word that fits the horizontal and vertical constraints. For the vertical word crossing 'AVAIL', I will choose a term that aligns with the given clues and does not conflict with 'SLUFF'. I will consider using 'SLEER' for the vertical word at position v2, matching the clue for mocking or sneering. The horizontal word at h3 should then be adjusted to fit this new configuration properly."},
    {"input": "\nGiven the current status:\ncurrent board:\n_o__k\novine\nlinen\n_l__t\n_e__e\n\n\nThe target words are classified as Correct Words, and Incorrect Words.\n---Correct Words:\nh2. OVINE -- Relating to sheep\nh3. LINEN -- A fabric made from flax\nv2. OVILE -- Relating to sheep\n---\nIncorrect Words:\nv5. KENTE -- A brightly colored hand-woven African silk cloth\n---You will retry the game. Write a plan for the next time. \nRespond at most five sentences, one sentence per line.\nDo not include the phrase \"next time\" in your response.\n\nResponse: ", "output": "Start by correcting the vertical word in column 5, aiming for a valid 5-letter word that fits the clue or context.\nConsider replacing 'K' with a different letter to form a correct word in the bottom row.\nEvaluate if 'OVILE' can be placed correctly in column 2, ensuring it aligns with horizontal words.\nCheck if 'LINEN' can remain unchanged or needs adjustment based on intersecting letters from corrected words.\nReview all possible intersections to ensure consistency across both directions."},
    {"input": "\nGiven the current status:\ncurrent board:\no____\nvvine\niaxle\nnaffe\ne____\n\n\nThe target words are classified as and Incorrect Words.\n---Incorrect Words:\nh2. VVINE -- Relating to sheep\nh3. IAXLE -- A fabric made from flax\nh4. NAFFE -- Unfit; clumsy\nv1. OVINE -- The city; the police\n---You will retry the game. Write a plan for the next time. \nRespond at most five sentences, one sentence per line.\nDo not include the phrase \"next time\" in your response.\n\nResponse: ", "output": "Plan the moves carefully, ensuring each word fits the given clues.\nReplace VVINE with OVINE, relating to sheep correctly.\nChange IAXLE to FLAXE, a fabric made from flax.\nSubstitute NAFFE with a fitting word that means unfit or clumsy.\nEnsure the first vertical word accurately describes a city or police."},
    {"input": "\nGiven the current status:\ncurrent board:\nccc__\nlll__\nooo__\nnnn__\neee__\n\n\nThe target words are classified as Correct Words, and Incorrect Words.\n---Correct Words:\nv2. CLONE -- A genetic duplicate\n---\nIncorrect Words:\nv1. CLONE -- An oily gland secretion\nv3. CLONE -- The soft palate\n---You will retry the game. Write a plan for the next time. \nRespond at most five sentences, one sentence per line.\nDo not include the phrase \"next time\" in your response.\n\nResponse: ", "output": "I will focus on the correct definition for CLONE as a genetic duplicate. For the other words, I will ensure they fit their accurate definitions. I will double-check each word's meaning before placing it on the board. If unsure, I will research to avoid incorrect placements."},
]


list_value_demos = [
    {
        "input": """Incorrect; to injure: w _ o _ g
Response: """,
        "output": """The letter constraint is: 5 letters, letter 1 is w, letter 3 is o, letter 5 is g.
Some possible words that mean "Incorrect; to injure":
wrong (w r o n g): 5 letters, letter 1 is w, letter 3 is o, letter 5 is g. fit!
sure"""
    },
    {
        "input": """A person with an all-consuming enthusiasm, such as for computers or anime: _ _ _ _ u
Response: """,
        "output": """The letter constraint is: 5 letters, letter 5 is u.
Some possible words that mean "A person with an all-consuming enthusiasm, such as for computers or anime":
geek (g e e k): 4 letters, not 5
otaku (o t a k u): 5 letters, letter 5 is u
sure""",
    },
    {
        "input": """Dewy; roscid: r _ _ _ l
Response: """,
        "output": """The letter constraint is: 5 letters, letter 1 is r, letter 5 is l.
Some possible words that mean "Dewy; roscid":
moist (m o i s t): 5 letters, letter 1 is m, not r
humid (h u m i d): 5 letters, letter 1 is h, not r
I cannot think of any words now. Only 2 letters are constrained, it is still likely
maybe""",
    },
    {
        "input": """A woodland: _ l _ d e
Response: """,
        "output": """The letter constraint is: 5 letters, letter 2 is l, letter 4 is d, letter 5 is e.
Some possible words that mean "A woodland":
forest (f o r e s t): 6 letters, not 5
woods (w o o d s): 5 letters, letter 2 is o, not l
grove (g r o v e): 5 letters, letter 2 is r, not l
I cannot think of any words now. 3 letters are constrained, and _ l _ d e seems a common pattern
maybe""",
    },
    {
        "input": """An inn: _ d _ w f
Response: """,
        "output": """The letter constraint is: 5 letters, letter 2 is d, letter 4 is w, letter 5 is f.
Some possible words that mean "An inn":
hotel (h o t e l): 5 letters, letter 2 is o, not d
lodge (l o d g e): 5 letters, letter 2 is o, not d
I cannot think of any words now. 3 letters are constrained, and it is extremely unlikely to have a word with pattern _ d _ w f to mean "An inn"
impossible""",
    },
    {
        "input": """Chance; a parasitic worm; a fish: w r a k _
Response: """,
        "output": """The letter constraint is: 5 letters, letter 1 is w, letter 2 is r, letter 3 is a, letter 4 is k.
Some possible words that mean "Chance; a parasitic worm; a fish":
fluke (f l u k e): 5 letters, letter 1 is f, not w
I cannot think of any words now. 4 letters are constrained, and it is extremely unlikely to have a word with pattern w r a k _ to mean "Chance; a parasitic worm; a fish"
impossible""",
    },

]