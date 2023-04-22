import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import * 
from textblob import TextBlob 
from nltk import tokenize

df = pd.read_csv('D:\Ing. Sistemas\Semestre\Electiva\Reviews.csv') 
df.head()


import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.offline as py 
import plotly.graph_objs as go 
import plotly.tools as tls 
import plotly.express as px 
matplotlib inline color = sns.color_palette() 
py.init_notebook_mode(connected=True) #Calificaciones de los productos fig = px.histogram(df, x = "Score") fig.update_layout(title_text = "Calificación del Producto") fig.show()