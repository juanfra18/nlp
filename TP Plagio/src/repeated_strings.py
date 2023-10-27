import difflib
import itertools
import re


def get_repeated(data):
    f = lambda x: re.sub(r"[^a-z ]", "", re.sub("\s+", " ", x.lower())).split()
    #print([d["filename"] for d in data])

    data = [{"filename": d["filename"], "text": f(d["text"])} for d in data]
    #print(data)


    output = {}
    for d1, d2 in itertools.combinations(data, 2):
        matcher = difflib.SequenceMatcher(None, d1["text"], d2["text"])

        for i1, _, size in matcher.get_matching_blocks():
            seq = " ".join(d1["text"][i1:i1 + size])

            if size < 2:
                continue

            if seq not in output:
                output[seq] = {"freq": 1, "files": set()}

            freq, files = output[seq]["freq"], output[seq]["files"]

            output[seq]["files"] = output[seq]["files"].union({d1["filename"]}, {d2["filename"]})
            output[seq]["freq"] = len(output[seq]["files"])


    print(output.keys())

if __name__=="__main__":
    data = [
        {"filename": "text_a", "text": """Lorem ipsum dolor sit amet, connectum adipiscing elit. 
    Sed do eisumodus temporis incididunt ut labore dororis magnum alida."""},

        {"filename": "text_b", "text": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""},

        {"filename": "text_c", "text": """Lorem ipsum dolor sit amet, consectetor adipiscat elit, 
    sid du eisumodos tempor incididunt at laboris et dolor magnum aliquos."""}
    ]
    get_repeated(data)