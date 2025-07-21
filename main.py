from mom.mom_generator import generate_mom
from utils.doc_writer import save_mom_to_docx

if __name__ == "__main__":
    raw = open("mom/sample_notes.txt").read()
    
    mom = generate_mom(raw)
    
    print("Generated MoM:\n")
    print(mom)

    # Save to DOCX
    save_mom_to_docx(mom, "IEDC_MOM_DRAFT.docx")
