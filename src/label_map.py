# Each AudioSet label belongs to at most one ESC-50 class. Shared parents like
# "Chicken, rooster", "Insect", "Vehicle" or "Aircraft" are left out on purpose:
# a label used by two classes gives both the same score, so e.g. every hen/rooster
# mix-up would come from the mapping instead of the model.
# Empty list = AudioSet has no label for this class, it can never be predicted.
ESC_TO_AUDIOSET = {
    # animals
    "dog": ["Dog", "Bark", "Bow-wow", "Yip", "Howl", "Growling", "Whimper (dog)", "Canidae, dogs, wolves"],
    "rooster": ["Crowing, cock-a-doodle-doo"],
    "pig": ["Pig", "Oink"],
    "cow": ["Cattle, bovinae", "Moo"],
    "frog": ["Frog", "Croak"],
    "cat": ["Cat", "Meow", "Purr", "Hiss", "Caterwaul"],
    "hen": ["Cluck"],
    "insects": ["Fly, housefly", "Bee, wasp, etc.", "Mosquito", "Buzz"],
    "sheep": ["Sheep", "Bleat"],
    "crow": ["Crow", "Caw"],
    # natural soundscapes
    "rain": ["Rain", "Raindrop", "Rain on surface"],
    "sea_waves": ["Ocean", "Waves, surf"],
    "crackling_fire": ["Fire", "Crackle"],
    "crickets": ["Cricket"],
    "chirping_birds": ["Bird", "Bird vocalization, bird call, bird song", "Chirp, tweet"],
    "water_drops": ["Drip", "Plop"],
    "wind": ["Wind", "Wind noise (microphone)", "Rustling leaves"],
    "pouring_water": ["Pour", "Fill (with liquid)", "Water tap, faucet"],
    "toilet_flush": ["Toilet flush"],
    "thunderstorm": ["Thunder", "Thunderstorm"],
    # human, non-speech
    "crying_baby": ["Baby cry, infant cry"],
    "sneezing": ["Sneeze"],
    "clapping": ["Clapping", "Applause"],
    "breathing": ["Breathing", "Gasp", "Pant", "Snort", "Sigh", "Wheeze"],
    "coughing": ["Cough", "Throat clearing"],
    "footsteps": ["Walk, footsteps"],
    "laughing": ["Laughter", "Giggle", "Snicker", "Chuckle, chortle", "Belly laugh", "Baby laughter"],
    "brushing_teeth": ["Toothbrush"],
    "snoring": ["Snoring"],
    "drinking_sipping": [],
    # domestic
    "door_wood_knock": ["Knock"],
    "mouse_click": ["Clicking"],
    "keyboard_typing": ["Computer keyboard", "Typing"],
    "door_wood_creaks": ["Creak", "Squeak"],
    "can_opening": [],
    "washing_machine": [],
    "vacuum_cleaner": ["Vacuum cleaner"],
    "clock_alarm": ["Alarm clock"],
    "clock_tick": ["Tick-tock", "Tick"],
    "glass_breaking": ["Glass", "Shatter", "Breaking", "Chink, clink"],
    # urban
    "helicopter": ["Helicopter"],
    "chainsaw": ["Chainsaw"],
    "siren": ["Siren", "Civil defense siren", "Police car (siren)", "Ambulance (siren)",
              "Fire engine, fire truck (siren)", "Emergency vehicle"],
    "car_horn": ["Vehicle horn, car horn, honking", "Toot"],
    "engine": ["Engine", "Idling", "Engine starting", "Accelerating, revving, vroom",
               "Light engine (high frequency)", "Medium engine (mid frequency)", "Heavy engine (low frequency)"],
    "train": ["Train", "Rail transport", "Railroad car, train wagon", "Train wheels squealing",
              "Train horn", "Train whistle"],
    "church_bells": ["Church bell", "Change ringing (campanology)"],
    "airplane": ["Fixed-wing aircraft, airplane", "Aircraft engine", "Jet engine"],
    "fireworks": ["Fireworks", "Firecracker"],
    "hand_saw": ["Sawing", "Filing (rasp)"],
}

# Everything in the AudioSet "Animal" subtree that the 527 labels expose, mapped or not
ANIMAL_LABELS = sorted(
    {l for c in ["dog", "rooster", "pig", "cow", "frog", "cat", "hen", "insects", "sheep", "crow",
                 "crickets", "chirping_birds"] for l in ESC_TO_AUDIOSET[c]}
    | {"Animal", "Domestic animals, pets", "Livestock, farm animals, working animals", "Chicken, rooster",
       "Fowl", "Insect", "Wild animals", "Roaring cats (lions, tigers)", "Bird", "Pigeon, dove", "Owl",
       "Goat", "Horse", "Mouse", "Rodents, rats, mice", "Snake", "Whale vocalization", "Duck", "Goose"}
)
