# save as flashcards_app.py
import streamlit as st
import random

# Flashcards list (abbreviated here; include all 34 in your version)
flashcards = [
    {
        "question": "Have you considered that phenotypic differences can also be caused by epigenetic drivers?",
        "answer": [
            "Yes I am aware of it",
            "I decided to start with genomics and transcriptional approaches",
            "Worked very well in other apicomplexans",
            "Transcriptomics might hint towards epigenetics, different accessibility of genes between strains",
            "Ultimately, my goal is to uncover the molecular basis of persistence and virulence"
        ]
    },
    {
        "question": "Mechanistically, how do you think these host modulators work?",
        "answer": [
            "Parasites are intracellular and do not directly interact with the immune system",
            "Epithelial cells have to signal to the host",
            "TLR, inflammasome, apoptosis, MHC presentation",
            "Block of transmitted or received host signals"
        ]
    },
    {
        "question": "No great in vitro systems. Why should we fund this?",
        "answer": [
            "In vitro model is suited for studies that take 2–3 days",
            "Alternatively organoids systems, however they are still at a very early stage",
            "I want to do experiments in vivo, where it matters",
            "Whole environment present: metabolome, immune system",
            "Outcome includes better understanding to inform organoids for Crypto"
        ]
    },
    {
        "question": "Why gamma knock out mice? Don’t you miss aspects of immunity?",
        "answer": [
            "The phenotypic differences appear in a IFN gamma independent manner",
            "Opens up opportunities to study other aspects of the immune system",
            "Many other immune pathways that can be studied"
        ]
    },
    {
        "question": "WP2 goes into host stuff, where do you see yourself in 5 years?",
        "answer": [
            "Interested and excited about the basic biology of effectors that drive persistence and virulence",
            "WP2 goes into Host response which in turn, I can use to explore immunological selective gates",
            "This will bring me back to the parasite and its effectors that modulate the immune system",
            "Overall interest in host parasite interactions"
        ]
    },
    {
        "question": "Why Zurich? Big picture",
        "answer": [
            "Outstanding environment for research in molecular parasitology",
            "Excellent groups working on related Apicomplexa",
            "State-of-the-art infrastructure and core facilities",
            "Clear commitment from both myself and the host institution to a long-term strategy"
        ]
    },
    {
        "question": "How is your future research different from your current PI?",
        "answer": [
            "Genetic crosses: I opened up a new niche to study phenotypes in Cryptosporidium",
            "The KO library screen is all new, and other researchers will use it",
            "5 new PIs within the last five years from Striepen lab",
            "Built a strong foundation, takes it into a new mechanistic and conceptual space",
            "Creates competitive niche in Europe and beyond"
        ]
    },
    {
        "question": "What are your back up plans?",
        "answer": [
            "WP1: Allelic replacements will provide validation",
            "WP1: eQTL could provide better resolution in case more than one gene is responsible for a phenotype",
            "WP1: Independent of results, I built a rigorous pipeline that can be used for WP2 and WP3 too",
            "WP2: alternative regulatory layers (proteomics, ATAC-seq)",
            "WP2: Support scRNAseq with bulk RNAseq",
            "WP3: hybrid model (guides transiently transfected with editor + resistance to CFZ)",
            "WP3: Decrease pool size if 20 in one go won’t work"
        ]
    },
    {
        "question": "Why did you do a postdoc in the US?",
        "answer": [
            "Learn from a leader in the field",
            "Developing my own line of research",
            "UPenn: cutting-edge tools and a vibrant research environment"
        ]
    },
    {
        "question": "Is this not just a fishing expedition?",
        "answer": [
            "No, grounded in biological rationale",
            "WP2: specific questions that I want to address",
            "WP3: specific family of proteins I want to investigate"
        ]
    },
    {
        "question": "You’re a senior postdoc, are you ready to become a PI?",
        "answer": [
            "Have consistently taken leadership to prepare manuscripts",
            "Developed and led my own research directions",
            "Initiated projects and established collaborations",
            "Mentored students",
            "Manages complex experiments",
            "I have both the vision and the experience to start my own group"
        ]
    },
    {
        "question": "Transcriptome and then what?",
        "answer": [
            "Validate findings",
            "Parasite effectors: loop into WP1",
            "Host response: Mutant mouse models",
            "Spatial transcriptomics"
        ]
    },
    {
        "question": "How will you manage the project and the individual WPs?",
        "answer": [
            "Aim 1: PhD student, perfectly suited to acquire skills and discover parasites",
            "Aim 2: Postdoc: quickly generates data for analysis and functional characterization",
            "Aim 3: collective effort",
            "I will be involved in all Aims"
        ]
    },
    {
        "question": "What is the next step once you find a persistence/virulence factor?",
        "answer": [
            "Functional characterization, interaction map",
            "Depending on the protein, drug discovery"
        ]
    },
    {
        "question": "How would you go after a drug once you have a virulence or persistence factor?",
        "answer": [
            "Check feasibility with experts (Mattie Pawlovic, Drug Discovery Unit Dundee)",
            "Initiate Collaborations",
            "My main interest lies in basic research"
        ]
    },
    {
        "question": "What is the interplay between IFNg and the parasites? How is it regulated?",
        "answer": [
            "Key protective cytokine",
            "Activating intestinal epithelial cells",
            "Coordinating innate and adaptive immunity",
            "Upstream IL-12/IL-18-driven activation",
            "IL-10-mediated restraint",
            "Enhances antigen presentation and cross-talk with immune cells"
        ]
    },
    {
        "question": "You found 8 genes… How did you select them?",
        "answer": [
            "Located in close proximity to the peak of the locus",
            "Large structural variants (insertions/deletions)",
            "Analyzed SNPs, focusing on non-synonymous variants",
            "Examined predicted subcellular localization",
            "Presence of signal peptides and transmembrane domains"
        ]
    },
    {
        "question": "You focused on two strains, why not more?",
        "answer": [
            "One vision is to collect more strains and investigate more phenotypes",
            "I have characterized 4 other strains",
            "It was sufficient to use one pair, since genetic crosses in Cryptosporidium are so powerful",
            "Logistical limitations due to lack of cryo protocol"
        ]
    },
    {
        "question": "Epistasis might complicate the discovery of a specific gene responsible for a phenotype. How will you handle this?",
        "answer": [
            "eQTL could provide better resolution in case more than one gene is responsible"
        ]
    },
    {
        "question": "Is there potential genetic instability or shutdown of luciferase-expressing parasites?",
        "answer": [
            "Not that I know of. I made dozens of transgenic parasites and never observed instability or shutdown"
        ]
    },
    {
        "question": "Isn’t the most interesting strain difference the parasite load? Why is it not mentioned?",
        "answer": [
            "Phenotype virulence is a culmination of parasite load, pathology and mortality",
            "It is interesting and I am considering it a phenotype"
        ]
    },
    {
        "question": "Aim3 has never been done before and has limited contingency planning. Alternatives?",
        "answer": [
            "Hybrid approach",
            "Reduce size of guide RNA pools",
            "I have prelim data → feasible"
        ]
    },
    {
        "question": "scRNAseq, limited sensitivity, low abundance of transcripts… How do you tackle that?",
        "answer": [
            "No problem for host transcripts",
            "Striepen’s lab just published the first Crypto single cell atlas → feasible",
            "Parasite transcripts can be supplemented with bulk RNAseq"
        ]
    },
    {
        "question": "CRISPR base editing is new, incomplete edits or off target effects are possible",
        "answer": [
            "Incomplete edits are impossible because each parasite expresses a guide → successful edit guaranteed by selection",
            "Off target effects must be evaluated",
            "New editors published frequently → backup options"
        ]
    },
    {
        "question": "Strains differences could complicate transcriptomic analyses",
        "answer": [
            "My genetic cross paper also publishes a reference genome for virulent strain",
            "Synteny between genomes is high",
            "Can align transcript reads to ref genomes (or sequence new strains)"
        ]
    },
    {
        "question": "Library bias, is there a way to normalise it?",
        "answer": [
            "Guide abundance will be determined before and after selection → allows normalization"
        ]
    },
    {
        "question": "Does apoptosis play a role in virulence and persistence?",
        "answer": [
            "Recent work: Crypto infection confers enhanced resistance to induced apoptosis of host cell",
            "Measured by Casp3 levels in infected host cells"
        ]
    },
    {
        "question": "Do you consider back crossing to reduce the QTL size?",
        "answer": [
            "Considered it, not possible earlier due to missing 3rd selection marker",
            "I recently established a 3rd marker → now possible"
        ]
    },
    {
        "question": "Does the meiotic crossing within the host affect the screen methodology?",
        "answer": [
            "No, I will integrate the guide RNA cassettes in one locus"
        ]
    },
    {
        "question": "What do you do if the Base editor strain cannot be generated?",
        "answer": [
            "Emphasize that it works",
            "Hybrid option",
            "Test other editors",
            "Knockout genes the conventional way"
        ]
    },
    {
        "question": "Do you have collaborators? Where do you need collaborators?",
        "answer": [
            "RNAseq analysis: Matthias Marti and Functional Genomics Center Zurich",
            "FGCZ offers training and supervision"
        ]
    },
    {
        "question": "People working on immunity in Zurich?",
        "answer": [
            "Institute of Experimental Immunology",
            "Mucosal Immunology, Prof. Isabelle Arnold"
        ]
    },
    {
        "question": "Is the Institute of Infection Biology in Zurich at the forefront of zoonotic disease research?",
        "answer": [
            "National reference center for zoonotic parasites (crypto, echinococcus)",
            "Multidisciplinary research across vet, med, epidemiology",
            "Strong collaborations in Zurich Infection & Immunity network (UZH & ETH)"
        ]
    },
    {
        "question": "How do you sort for Immune cells?",
        "answer": [
            "CD45+ to gate leukocytes",
            "Interested in lymphocytes and monocytes",
            "Known transcriptional signatures to identify subsets later"
        ]
    }
]

# Initialize session state
if "cards" not in st.session_state:
    st.session_state.cards = random.sample(flashcards, len(flashcards))
    st.session_state.wrong = []
    st.session_state.round = 1
    st.session_state.index = 0
    st.session_state.show_answer = False

def next_card(got_it: bool):
    if not got_it:
        st.session_state.wrong.append(st.session_state.cards[st.session_state.index])
    
    st.session_state.index += 1
    st.session_state.show_answer = False

    if st.session_state.index >= len(st.session_state.cards):
        if st.session_state.wrong:
            st.session_state.cards = st.session_state.wrong
            st.session_state.wrong = []
            st.session_state.round += 1
            st.session_state.index = 0
            st.success(f"Starting round {st.session_state.round} with {len(st.session_state.cards)} cards to review!")
        else:
            st.balloons()
            st.success("🎉 Congrats, you got all questions right!")
            st.session_state.index = 0
            st.session_state.cards = []
            return

# UI
st.title(f"🔀 Flashcard Trainer — Round {st.session_state.round}")

if st.session_state.index < len(st.session_state.cards):
    card = st.session_state.cards[st.session_state.index]
    st.subheader(f"Q: {card['question']}")
    
    if st.button("Show Answer"):
        st.session_state.show_answer = True

    if st.session_state.show_answer:
        st.write("\n".join(f"- {a}" for a in card["answer"]))
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Got it"):
            next_card(True)
    with col2:
        if st.button("❌ Didn't get it"):
            next_card(False)

    st.progress((st.session_state.index + 1) / len(st.session_state.cards))