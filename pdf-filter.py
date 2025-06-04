import pymupdf



FILE_NAME = ''
TARGET_WORDS = [
    "accessible", "activism", "activists", "advocacy", "advocate", "advocates",
    "affirming care", "all-inclusive", "allyship", "anti-racism", "antiracist",
    "assigned at birth", "assigned female at birth", "assigned male at birth",
    "at risk", "barrier", "barriers", "belong", "bias", "biased", "biased toward",
    "biases", "biases towards", "biologically female", "biologically male",
    "BIPOC", "Black", "breastfeed + people", "discriminated", "discrimination",
    "discriminatory", "disparity", "diverse", "diverse backgrounds",
    "diverse communities", "diverse community", "diverse group", "diverse groups",
    "diversified", "diversify", "diversifying", "diversity", "enhance the diversity",
    "enhancing diversity", "environmental quality", "equal opportunity", "equality",
    "equitable", "equitableness", "equity", "ethnicity", "excluded", "exclusion",
    "expression", "female", "females", "inclusive", "inclusive leadership",
    "inclusiveness", "inclusivity", "increase diversity", "increase the diversity",
    "indigenous community", "inequalities", "inequality", "inequitable",
    "inequities", "inequity", "injustice", "institutional", "intersectional",
    "intersectionality", "key groups", "key people", "key populations", "Latinx",
    "LGBT", "LGBTQ", "marginalize", "marginalized", "men who have sex with men",
    "mental health", "minorities", "privilege", "privileges", "promote diversity",
    "promoting diversity", "pronoun", "pronouns", "prostitute", "race",
    "race and ethnicity", "racial", "racial diversity", "racial identity",
    "racial inequality", "racial justice", "racially", "racism", "segregation",
    "sense of belonging", "sex", "sexual preferences", "sexuality", "social justice",
    "sociocultural", "socioeconomic", "status", "stereotype", "stereotypes",
    "systemic"
]








file = pymupdf.open(FILE_NAME)
highlighted_pdf = pymupdf.open()                 
highlighted_pdf.insert_pdf(file, to_page = len(file)) 

for page in highlighted_pdf:
    for word in TARGET_WORDS:
        rects = page.search_for(word)
        print(rects)
        annot = page.add_highlight_annot(rects)
        annot.set_colors(stroke=(1, 0, 0))
        annot.update()


highlighted_pdf.save("highlighted.pdf")




