from mom.mom_generator import generate_mom
from utils.doc_writer import save_mom_to_docx
from utils.drive_uploader import upload_to_drive
from mom.refiner import formalize_sentences, clarify_attributions  # 👈 import refiners

if __name__ == "__main__":
    raw = open("mom/sample_notes.txt").read()

    # Step 1: Generate initial MoM
    mom = generate_mom(raw)

    # Step 2: Refine MoM
    mom = clarify_attributions(mom)
    mom = formalize_sentences(mom)

    print("Refined MoM:\n")
    print(mom)

    # Step 3: Save to DOCX
    save_mom_to_docx(mom, "IEDC_MOM_DRAFT.docx")
