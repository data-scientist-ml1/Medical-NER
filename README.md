# Medical-NER
I had to present a demo for Named Entity Recognition NER on Medical text Data. I found [Stanza](https://stanfordnlp.github.io/stanza/biomed_model_usage.html) NLP Package suitable for my task but I was not able to integrate it with Spacy Displacy to show highlighted Entities because Spacy Model output and Stanza Model output for NER were very different. So I created this little script for the demo. I used [Streamlit](https://streamlit.io/) for UI.


![Demo NER](Demo_ner.PNG?raw=true "Title")



# NER Model:
I have used i2b2 clinical NER model trained on publicly available [MIMIC-III database](https://mimic.mit.edu/). It has been trained to extract following NER: 
- PROBLEM
- TEST
- TREATMENT

For more information, you can visit [stanza website](https://stanfordnlp.github.io/stanza/available_biomed_models.html).

## Steps:
I tested only in Python 3.7.13 in Linux.
- pip install -r requirements.txt <br>
Execute the following statement
- streamlit run ner.py <br>
Open URL in browser.
Note: It will download some packages for the first time. So it might take some time to start. See terminal output for that.
