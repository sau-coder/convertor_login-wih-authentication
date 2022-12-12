from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse

from src.paragraph_checker.convertion.paragraph_stats import TextStats

paragraph_stats = APIRouter()


@paragraph_stats.post("/paragraph_stats")
def controller_paragraph_stats(
    paragraph: str = Form(""), ms_per_char: float = Form(0.0)
) -> any:
    try:
        data = {}
        if paragraph.strip():
            text_stats = TextStats(paragraph)
            tokens = text_stats.get_word_tokenize()
            words = list(set(tokens))
            data["words"] = [w for w in words if w and (not w.isnumeric())]
            data["total_number_of_words"] = len(tokens)
            data["total_number_of_unique_words"] = len(data["words"])
            data["word_frequency"] = text_stats.get_word_freq(tokens)
            data["keywords"] = text_stats.get_keywords_extracter()
            data["coherence_score"] = text_stats.get_coherence()
            data["name_entity_recognition"] = text_stats.get_ner()
            data["pos_tags"] = text_stats.get_pos_tags()
            data.update(text_stats.get_text_measures())
            data.update(text_stats.get_textstat_stats(ms_per_char))
            response = {
                "success": True,
                "status_code": 200,
                "message": "Responded successfully.",
                "data": data,
            }
        else:
            response = {
                "success": False,
                "status_code": 400,
                "message": "Paragraph not received.",
            }

    except Exception as e:
        response = {
            "success": False,
            "status_code": 400,
            "message": "Something went wrong.",
            "error": str(e),
        }
    return JSONResponse(response)
