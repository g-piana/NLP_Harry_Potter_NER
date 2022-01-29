
"""
Example using the components provided by spacy-streamlit in an existing app.
Prerequisites:
specially trained model: training/NER_Book_03/model-best
"""
import spacy_streamlit
import streamlit as st


DEFAULT_TEXT = """Hagrid had a lovely pet called Fluffy. Harry Potter fought against a basilisk. Ronan was a centaur while Ron Weasley and Hermione Granger were Harry's friends. Dobby was a house-elf, a mythological creature such as Griphook, a goblin. The model has been custom trained to identify human-ish characters such as Lord Voldemort from mythological creatures such as the Phoenix. \n \n I can develop NLP machine learning models for any specialized domain, with custom-defined entity types (such as MYTH in this example) that must be identified through documents."""


spacy_model = "training/NER_Book_03/model-best"

st.title("Harry Potter | Humans and Myths")
text = st.text_area("Write your text below, mixing humans and myths from Harry Potter novels.", DEFAULT_TEXT, height=200)
doc = spacy_streamlit.process_text(spacy_model, text)

spacy_streamlit.visualize_ner(
    doc,
    labels=["PERSON", "MYTH"],
    show_table=False,
    title="Persons and mythological creatures",
    colors={"MYTH": "green"}
)
st.text(f"Developed by Giulio Piana - https://giuliopiana.com")
st.text(f"Analyzed using spaCy model {spacy_model}")