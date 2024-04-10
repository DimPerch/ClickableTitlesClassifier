from sumy.summarizers.lsa import LsaSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer


class Summarizer:
    def __init__(self, document=''):
        self.summarizer = LsaSummarizer()

    def summarize(self, document='', sentences_count=8):
        parser = PlaintextParser.from_string(document, Tokenizer("russian"))
        summary = self.summarizer(parser.document, sentences_count=sentences_count)
        lsa_summary = ""
        for sentence in summary:
            lsa_summary += str(sentence)
        return lsa_summary
