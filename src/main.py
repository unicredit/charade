import sys

import services.allen
import services.gensim
import services.misc
import services.pytorch
import services.regex
import services.spacy
import services.nltk
import services.sklearn
import services.textrank
import services.opennmt
import services.bert
from server import Server


if __name__ == '__main__':
    server = Server()

    server.add(services.spacy.Parse(['it', 'en', 'de']))
    server.add(services.spacy.Ner(['it', 'en', 'de']))
    server.add(services.allen.PretrainedNer())
    # server.add(services.allen.Ner())
    # server.add(services.allen.Sentiment())
    # server.add(services.allen.SentimentRegression())
    server.add(services.textrank.Summarize())
    server.add(services.textrank.Keywords())
    server.add(services.misc.Dates(['it', 'en']))
    server.add(services.misc.Names())
    server.add(services.regex.Parse())
    server.add(services.regex.Codes())
    server.add(services.misc.FiscalCode())
    server.add(services.nltk.Parse())
    server.add(services.nltk.Ner())
    # server.add(services.opennmt.Summarization())
    # server.add(services.opennmt.Translation())
    # server.add(services.sklearn.Classifier())
    # server.add(services.sklearn.NMF())
    # server.add(services.gensim.Lda())
    # server.add(services.pytorch.Ner(['it', 'de']))
    # server.add(services.bert.SentenceClassification())
    # server.add(services.bert.NextSentencePrediction())

    server.run_http(debug=True)
