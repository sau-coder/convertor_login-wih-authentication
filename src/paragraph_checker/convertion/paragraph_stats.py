import datetime
import string

import nltk
import readability
import spacy
import textstat
import yake


class TextStats:
    def __init__(self, text):
        self.NER_IMG_DIR = "output_imgs/"
        self.TTS_AUD_DIR = "output_voices/"
        self.text = text
        self.spacy_nlp = spacy.load("en_core_web_sm")
        self.datetimeobj = datetime.datetime.now()
        self.sentences = []

    def get_sent_tokenize(self):
        sents = nltk.tokenize.sent_tokenize(self.text)
        self.sentenses = sents
        return sents

    def get_word_freq(self, word_list):
        unique_words = set(word_list)
        return {
            words.capitalize(): word_list.count(words)
            for words in unique_words
            if not words.isnumeric()
        }

    def get_textstat_stats(self, ms_per_char):
        data = {}
        if ms_per_char:
            data["reading_time"] = textstat.reading_time(
                self.text, ms_per_char=ms_per_char
            )
        else:
            data["reading_time"] = textstat.reading_time(self.text)
        data["flesch_reading_ease"] = textstat.flesch_reading_ease(self.text)
        data["flesch_kincaid_grade"] = textstat.flesch_kincaid_grade(self.text)
        data["gunning_fog"] = textstat.gunning_fog(self.text)
        data["smog_index"] = textstat.smog_index(self.text)
        data["automated_readability_index"] = textstat.automated_readability_index(
            self.text
        )
        data["coleman_liau_index"] = textstat.coleman_liau_index(self.text)
        data["linsear_write_formula"] = textstat.linsear_write_formula(self.text)
        data["dale_chall_readability_score"] = textstat.dale_chall_readability_score(
            self.text
        )
        data["text_standard"] = textstat.text_standard(self.text)
        data["spache_readability"] = textstat.spache_readability(self.text)
        data["fernandez_huerta"] = textstat.fernandez_huerta(self.text)
        data["szigriszt_pazos"] = textstat.szigriszt_pazos(self.text)
        data["gutierrez_polini"] = textstat.gutierrez_polini(self.text)
        data["crawford"] = textstat.crawford(self.text)
        data["osman"] = textstat.osman(self.text)
        data["gulpease_index"] = textstat.gulpease_index(self.text)
        data["wiener_sachtextformel"] = textstat.wiener_sachtextformel(
            self.text, variant=2
        )
        data["syllable_count"] = textstat.syllable_count(self.text)
        data["lexicon_count"] = textstat.lexicon_count(self.text, removepunct=True)
        data["sentence_count"] = textstat.sentence_count(self.text)
        data["char_count"] = textstat.char_count(self.text, ignore_spaces=True)
        data["letter_count"] = textstat.letter_count(self.text, ignore_spaces=True)
        data["polysyllabcount"] = textstat.polysyllabcount(self.text)
        data["monosyllabcount"] = textstat.monosyllabcount(self.text)

        return data

    def get_word_tokenize(self):
        tokens = nltk.tokenize.regexp_tokenize(
            self.text.lower().translate(str.maketrans("", "", string.punctuation)),
            r"[\w']+",
        )
        return tokens

    def get_keywords_extracter(self):
        custom_kw_extractor = yake.KeywordExtractor(n=3, dedupLim=0.3, top=30)
        yake_keywords = custom_kw_extractor.extract_keywords(self.text)

        return yake_keywords

    def get_text_measures(self):
        data = {}
        measures = readability.getmeasures(self.text)
        data["readability_grades"] = measures["readability grades"]
        data["sentence_info"] = measures["sentence info"]
        data["word_usage"] = measures["word usage"]
        data["sentence_beginnings"] = measures["sentence beginnings"]

        return data

    def get_ner(self):
        # unique_file_name = (
        #     str(self.datetimeobj)
        #     .replace(" ", "")
        #     .replace(".", "")
        #     .replace(":", "")
        #     .replace("-", "")
        #     + "-"
        #     + str(uuid.uuid4()).replace("-", "")
        # )
        # svg_filedir = self.NER_IMG_DIR + f"{unique_file_name}.svg"
        # png_filedir = self.NER_IMG_DIR + f"{unique_file_name}.png"
        # svgPath = Path(svg_filedir)
        # pngPath = Path(png_filedir)
        nlpText = self.spacy_nlp(self.text.replace("’", ""))
        ner_list = [{"text": word.text, "entity": word.label_} for word in nlpText.ents]
        ner_list = [dict(t) for t in {tuple(d.items()) for d in ner_list}]
        # try:

        #     displacy_img = displacy.render(nlpText,  style='dep')
        #     with open(svg_filedir, 'w') as f:
        #         f.write(displacy_img)

        #     drawing = svg2rlg(svg_filedir)
        #     renderPM.drawToFile(drawing, png_filedir, fmt='PNG')
        #     os.remove(svgPath)

        #     img = Image.open(png_filedir)
        #     s3 = S3Events()
        #     s3_img_url = s3.process_and_upload(
        #         'images/', img, unique_file_name, "IMAGE")
        #     img.close()
        #     os.remove(pngPath)

        #     return {"ner": ner_list, "s3_img_url": s3_img_url, "error": False, "ner_msg": "N.E.R. for given text is successfully done.", "error_message": []}
        # except Exception as e:
        #     try:
        #         os.remove(svgPath)
        #     except Exception as err:
        #         pass
        return {"ner": ner_list, "s3_img_url": ""}

    def get_pos_tags(self):
        myVar = self.spacy_nlp(self.text)
        return [{"text": word.text, "tag": word.pos_} for word in myVar]

    def get_coherence(self):
        self.get_sent_tokenize()
        coherence_ = 0
        for i in range(1, len(self.sentences)):
            search_ = self.spacy_nlp(self.sentences[i - 1].lower())
            main_ = self.spacy_nlp(self.sentences[i].lower())
            sim = search_.similarity(main_)
            coherence_ += sim

        if len(self.sentences) != 0:
            coherence_score = coherence_ / len(self.sentences) * 10
        else:
            coherence_score = 0

        return coherence_score
