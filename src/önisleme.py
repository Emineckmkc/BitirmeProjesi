# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 21:23:57 2020

@author: Emine
"""


import jpype
from jpype import JClass, JString, getDefaultJVMPath, shutdownJVM, startJVM, java
import csv
import itertools
data=[]

ZEMBEREK_PATH = r'D:\0.17.1\zemberek-full.jar'
jpype.startJVM(jpype.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s' % (ZEMBEREK_PATH))

TurkishMorphology = jpype.JClass('zemberek.morphology.TurkishMorphology')
TurkishSpellChecker= jpype.JClass('zemberek.normalization.TurkishSpellChecker')
TurkishSentenceExtractor: JClass = JClass(
'zemberek.tokenization.TurkishSentenceExtractor')
TurkishSentenceNormalizer= jpype.JClass('zemberek.normalization.TurkishSentenceNormalizer')

morphology = TurkishMorphology.createWithDefaults()

spell=TurkishSpellChecker(morphology)
deneme=[]
pos=[]   


with open('korona3-17.csv',newline='', encoding='utf-8') as csvfile:
    
    reader = csv.reader(csvfile)
    for row in itertools.islice(reader, 10000):    
        if(row.__len__()==3):
           data.append(row[2]) 
           
           
       
    for x in data:
       analysis: java.util.ArrayList = (
       morphology.analyzeAndDisambiguate(x).bestAnalysis())
       spell.suggestForWord(x)
     
       
       for i, analysis in enumerate(analysis, start=1):
           
        f'\nAnalysis {i}: {analysis}',
        f'\nPrimary POS {i}: {analysis.getPos()}'
        f'\nPrimary POS (Short Form) {i}: {analysis.getPos().shortForm}'
       
       pos.append(f'{str(analysis.getLemmas()[0])}')
print(f'\n Kelime Kökleri: {" ".join(pos)}')


