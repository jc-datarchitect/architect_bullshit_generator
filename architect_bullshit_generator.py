# ------------------------------
# 0 IMPORTS
# ------------------------------
import pandas as pd
import random

# ------------------------------
# 1 ABSTRACT CONCEPTS
# ------------------------------
abstract_concepts = pd.DataFrame({
    "word": [

        # 🔵 LEVEL 1 (Architectural Reality Layer)
        "composition",
        "space",
        "light",
        "form",
        "materiality",
        "surface",
        "depth",
        "scale",
        "boundary",
        "context",
        "geometry",
        "rhythm",
        "transparency",
        "circulation",
        "orientation",
        "alignment",
        "edge",
        "tectonics",
        "proportion",
        "mass",
        "void",
        "texture",
        "program",

        # 🟡 LEVEL 2 (Conceptual Drift Layer)
        "ambiguity",
        "permeability",
        "liminality",
        "tension",
        "fragmentation",
        "fluidity",
        "hybridity",
        "temporality",
        "density",
        "instability",
        "continuity",
        "disruption",
        "transition",
        "interaction",
        "negotiation",
        "overlap",
        "spatial condition",
        "threshold condition",
        "relationality",
        "multiplicity",
        "adaptability",
        "responsiveness",
        "relational field",

        # 🔴 LEVEL 3 (Pritzker / Theory Overdose Layer)
        "epistemology",
        "post-materiality",
        "ontological instability",
        "speculative spatiality",
        "tectonic discourse",
        "post-territorial condition",
        "phenomenological excess",
        "semiotic collapse",
        "architectural fictionality",
        "non-linear spatiality",
        "hyper-contextuality",
        "critical abstraction",
        "radical indeterminacy",
        "theoretical excess",
        "infrastructural poetics",
        "conceptual hypertrophy",
        "cognitive spatiality",
        "post-functional logic",
        "discursive architecture",
        "systemic ambiguity",
        "spatial deconstruction",
        "concept juxtaposition",
        "abstract territoriality"
    ],

    "bullshit_level": (
        [1] * 23 +
        [2] * 23 +
        [3] * 23
    )
})

# ------------------------------
# 2 VERBS
# ------------------------------
verbs = pd.DataFrame({
    "word": [

        # 🔵 LEVEL 1 (Functional Architectural Verbs)
        "organizes",
        "defines",
        "frames",
        "connects",
        "structures",
        "aligns",
        "supports",
        "contains",
        "separates",
        "joins",
        "forms",
        "builds",
        "shapes",
        "creates",
        "distributes",
        "divides",
        "orders",
        "layers",
        "positions",
        "extends",
        "holds",
        "reveals",
        "structures",

        # 🟡 LEVEL 2 (Architectural Discourse Verbs)
        "negotiates",
        "articulates",
        "curates",
        "juxtaposes",
        "bifurcates",
        "mediates",
        "reframes",
        "reinterprets",
        "disrupts",
        "overlaps",
        "interacts",
        "transitions",
        "modulates",
        "amplifies",
        "dissolves",
        "reorganizes",
        "hybridizes",
        "reconfigures",
        "redefines",
        "permeates",
        "activates",
        "questions",
        "connects",

        # 🔴 LEVEL 3 (Theory / Pritzker Overload Verbs)
        "problematizes",
        "destabilizes",
        "deconstructs",
        "interrogates",
        "abstracts",
        "transcends",
        "reconceptualizes",
        "theorizes",
        "dislocates",
        "fragmentalizes",
        "ontologizes",
        "epistemologizes",
        "simulates",
        "speculates",
        "provokes",
        "suspends",
        "reframes",
        "dissolves",
        "unsettles",
        "hypercontextualizes",
        "dematerializes",
        "conceptualizes",
        "extrapolates"
    ],

    "bullshit_level": (
        [1] * 23 +
        [2] * 23 +
        [3] * 23
    )
})

# ------------------------------
# 3 SPATIAL NOUNS
# ------------------------------
spatial_nouns = pd.DataFrame({
    "word": [

        # 🔵 LEVEL 1 (Physical / Architectural Elements)
        "transparency",
        "rhythm",
        "composition",
        "wall",
        "column",
        "beam",
        "floor",
        "ceiling",
        "roof",
        "alignment",
        "atrium",
        "geometry",
        "orientation",
        "stair",
        "ramp",
        "courtyard",
        "threshold",
        "corridor",
        "opening",
        "tectonics",
        "partition",
        "depth",
        "plan",

        # 🟡 LEVEL 2 (Spatial Conditions / Architectural Constructs)
        "spatial field",
        "urban fabric",
        "circulation system",
        "programmatic zone",
        "threshold space",
        "interstitial space",
        "void condition",
        "spatial envelope",
        "public realm",
        "transitional space",
        "hybrid zone",
        "edge condition",
        "in-between space",
        "layered system",
        "spatial network",
        "tectonic field",
        "occupiable surface",
        "permeable boundary",
        "sectional space",
        "spatial hierarchy",
        "gradient field",
        "relational space",
        "constructed landscape",

        # 🔴 LEVEL 3 (Theoretical / Abstract Spatial Constructs)
        "epistemic field",
        "post-spatial condition",
        "ontological space",
        "speculative territory",
        "non-linear field",
        "phenomenological zone",
        "discursive space",
        "critical territory",
        "abstracted landscape",
        "semiotic field",
        "hyper-spatial system",
        "post-material void",
        "conceptual environment",
        "radical interiority",
        "externalized interior",
        "infrastructural matrix",
        "cognitive landscape",
        "simulated space",
        "deterritorialized field",
        "spatial fiction",
        "systemic environment",
        "fluid topology",
        "invisible architecture"
    ],

    "bullshit_level": (
        [1] * 23 +
        [2] * 23 +
        [3] * 23
    )
})

# ------------------------------
# 4 STRUCTURES LVL 1
# ------------------------------
structures_lvl1 = [
    "The {spatial_noun} defines the {concept}.",
    "The {concept} is part of the {spatial_noun}.",
    "The {spatial_noun} connects to {concept}.",
    "Within the {spatial_noun}, the {concept} appears.",
    "The {concept} shapes the {spatial_noun}.",
    "The {spatial_noun} organizes the {concept}."
]

# ------------------------------
# 5 STRUCTURES LVL 2
# ------------------------------
structures_lvl2 = [
    "The {spatial_noun} negotiates {concept}.",
    "{concept} emerges through the {spatial_noun}.",
    "Within the {spatial_noun}, {concept} is articulated.",
    "The {spatial_noun} reinterprets {concept}.",
    "{concept} reconfigures the {spatial_noun}.",
    "The {spatial_noun} mediates {concept}."
]

# ------------------------------
# 6 STRUCTURES LVL 3
# ------------------------------
structures_lvl3 = [
    "{concept} dissolves within the {spatial_noun}.",
    "The {spatial_noun} destabilizes {concept}.",
    "Within the {spatial_noun}, {concept} collapses into discourse.",
    "The {spatial_noun} interrogates the ontological limits of {concept}.",
    "{concept} is recontextualized through the epistemic condition of the {spatial_noun}.",
    "The {spatial_noun} transcends the material logic of {concept}."
]

# ------------------------------
# 7 WORD USAGE
# ------------------------------
word_usage = {
    "concept": {},
    "verb": {},
    "spatial": {}
}

recent_sentences = []

MAX_SENTENCES = 5

# ------------------------------
# 8 RECENT STRUCTURES
# ------------------------------
recent_structures = {
    1: [],
    2: [],
    3: []
}

MAX_STRUCTURE_MEMORY = 2

# ------------------------------
# 9 WEIGHTED SAMPLE
# ------------------------------
def weighted_sample(pool, usage_dict):

    weights = []

    for w in pool:
        count = usage_dict.get(w, 0)
        weight = 1 / (1 + count)
        weights.append(weight)

    chosen = random.choices(pool, weights=weights, k=1)[0]

    usage_dict[chosen] = usage_dict.get(chosen, 0) + 1

    return chosen

# ------------------------------
# 10 GENERATE SENTENCE
# ------------------------------
def generate_sentence(level):

    concepts_list = abstract_concepts[abstract_concepts["bullshit_level"] == level]["word"].tolist()
    verbs_list = verbs[verbs["bullshit_level"] == level]["word"].tolist()
    spatial_list = spatial_nouns[spatial_nouns["bullshit_level"] == level]["word"].tolist()

    # 1. seleccionar pool de estructuras según nivel
    if level == 1:
        pool = structures_lvl1
    elif level == 2:
        pool = structures_lvl2
    elif level == 3:
        pool = structures_lvl3
    else:
        raise ValueError("Level must be 1, 2 or 3")

    attempts = 0

    while True:

        # 2. evitar repetición de estructura reciente
        structure = random.choice(pool)

        if structure in recent_structures[level]:
            attempts += 1
            if attempts > 10:
                break
            continue

        # 3. generar tokens
        concept = weighted_sample(concepts_list, word_usage["concept"])
        verb = weighted_sample(verbs_list, word_usage["verb"])
        spatial_noun = weighted_sample(spatial_list, word_usage["spatial"])

        # 4. construir frase
        sentence = structure.format(
            concept=concept,
            verb=verb,
            spatial_noun=spatial_noun
        )

        # 5. evitar repetición exacta de frase
        if sentence not in recent_sentences:
            break

        attempts += 1
        if attempts > 5:
            break

    # 6. actualizar memoria de frases
    recent_sentences.append(sentence)
    if len(recent_sentences) > MAX_SENTENCES:
        recent_sentences.pop(0)

    # 7. actualizar memoria de estructuras
    recent_structures[level].append(structure)
    if len(recent_structures[level]) > MAX_STRUCTURE_MEMORY:
        recent_structures[level].pop(0)

    return sentence

# ------------------------------
# 11 STREAMLIT (CÓDIGO DE LA INTERFAZ)
# ------------------------------
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Architect Bullshit Generator", page_icon="🏗️")

# Cargar y mostrar el logo
try:
    logo = Image.open("abg_logo.jpg") 
    st.image(logo, use_container_width=True)
except:
    st.title("Architect Bullshit Generator")

st.write("---")

# Texto centrado debajo del logo
st.markdown(
    """
    <div style="text-align: center;">
        <p style="font-style: italic; font-size: 1.2em;">"When you have nothing intelligent to say about architecture, ABG will say it for you."</p>
    </div>
    """, 
    unsafe_allow_html=True
)
st.write("") 

# Selector de nivel con descripciones graciosas
level = st.selectbox(
    "SELECT YOUR BULLSHIT LEVEL:", 
    [1, 2, 3], 
    format_func=lambda x: {
        1: "🔵 STUDENT: 'Fuelled by redbull, coffee, and the existential dread of a closing deadline.'", 
        2: "🟡 PROFESSOR: 'The 'Condescending' Professor (Ego larger than your site plan).'", 
        3: "🔴 PRITZKER: 'The 'God Complex' Pritzker Juror (I don't know what I'm saying, but it sounds expensive).'"
    }[x]
)

st.write("")
if st.button("Generate Bullshit"):
    sentence = generate_sentence(level)
    st.success(sentence)
