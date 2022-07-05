import streamlit as st
import streamlit.components.v1 as components
import stanza
from collections import namedtuple

@st.cache
def ent_setup():   
    stanza.download('en', package='mimic', processors={'ner': 'i2b2'})         

# Only download once
ent_setup()

st.title("Named Entity Recognition")
DEFAULT_TEXT = 'The patient had a sore throat and was treated with Cepacol lozenges.'
text = st.text_area("Text to analyze", DEFAULT_TEXT, height=200)

# html formatting
text = '<div style="line-height: 40px;">' + text + '</div>'
style_end = "</span>"
ent_type_style = """ <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; 
                    vertical-align: middle; margin-left: 0.5rem;"> """


colors = ['rgb(191, 225, 217)', 'rgb(170, 156, 252)', 'rgb(254, 202, 116)']
style = """ <span style="background: {color}; padding: 0.45em 0.6em; margin: 0px 0.25em; 
                               line-height: 1; border-radius: 0.35em;"> """

# NER Extraction
nlp = stanza.Pipeline('en', package='mimic', processors={'ner': 'i2b2'})
doc = nlp(text)

# convert to dict from span for subscripting
ents = [ner.to_dict() for ner in doc.ents]

# Used namedTuple for readability
text_entity = namedtuple('Text_Entity', ['text', 'ent_type'])
# (Entity_Text, Entity_Type)
unique_ents = set([ text_entity( ent['text'], ent['type'] ) for ent in ents])

# replace entity text & type with HTML format for highlighting
for ent in unique_ents:        
    if ent.ent_type == 'PROBLEM':
        text_sub = style.format(color = colors[0]) + ent.text
        text_sub = text_sub + ent_type_style + ent.ent_type + style_end + style_end
        text = text.replace(ent.text, text_sub)
        
    if ent.ent_type == 'TREATMENT': 
        text_sub = style.format(color = colors[1]) + ent.text
        text_sub = text_sub + ent_type_style + ent.ent_type + style_end + style_end
        text = text.replace(ent.text, text_sub)
        
    if ent.ent_type == 'TEST': 
        text_sub = style.format(color = colors[2]) + ent.text
        text_sub = text_sub + ent_type_style + ent.ent_type + style_end + style_end
        text = text.replace(ent.text, text_sub)                                
    
components.html(
    text,
    height=600,
)