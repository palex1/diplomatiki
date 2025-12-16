import streamlit as st
# Custom CSS για πιο επαγγελματική εμφάνιση
st.markdown(
    """
    <style>
    /* 1. ΓΕΝΙΚΟ ΣΤΥΛ ΚΑΙ ΦΟΝΤΟ */
    .stApp {
        background-color: #f0f2f6; /* Πολύ ανοιχτό γκρι */
        color: #1f2937; /* Σκούρο γκρι κείμενο */
        font-family: 'Roboto', sans-serif; 
    }

    /* 2. ΣΤΥΛ ΤΙΤΛΩΝ */
    h1 {
        color: #1f2937; 
        font-size: 2.5rem;
        border-bottom: 2px solid #007bff; /* Μπλε γραμμή κάτω από τον βασικό τίτλο */
        padding-bottom: 10px;
    }

    /* 3. ΣΤΥΛ ΚΟΥΜΠΙΟΥ */
    /* Στοχεύουμε στο κουμπί 'Δημιουργία Υλικού' */
    div.stButton > button:first-child {
        background-color: #007bff; /* Έντονο Μπλε */
        color: white;
        font-size: 1.1rem;
        border-radius: 12px; /* Στρογγυλεμένες γωνίες */
        border: none;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }
    
    div.stButton > button:first-child:hover {
        background-color: #0056b3; /* Σκούρο μπλε στο hover */
        transform: scale(1.05); /* Ελαφρύ ζουμ */
    }

    /* 4. ΣΤΥΛ ΠΛΑΙΣΙΩΝ (INFO BOXES) */
    .stAlert {
        border-radius: 12px;
        border-left: 5px solid #007bff;
    }

    /* 5. ΣΤΥΛ TABS (ΚΑΡΤΕΛΕΣ) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        border-bottom: 1px solid #ccc;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: nowrap;
        border-radius: 4px 4px 0 0;
        font-size: 1.05rem;
        color: #495057;
    }
    .stTabs [aria-selected="true"] {
        background-color: #f0f2f6; 
        color: #007bff; /* Μπλε επιλεγμένη καρτέλα */
        border-bottom: 3px solid #007bff;
        font-weight: bold;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)
# Ρυθμίσεις σελίδας και εμφάνιση
st.set_page_config(
    page_title="Αρχική Σελίδα | AI Lesson Planner",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------
# Κεντρικός Τίτλος
# ------------------------------------
col_title, col_logo = st.columns([6, 1])

with col_title:
    st.title("🤖 AI Εκπαιδευτικός Σχεδιαστής")
    st.subheader("Διπλωματική Εργασία: Μετατροπή Ιδεών σε Ολοκληρωμένα Μαθήματα.")

#with col_logo:
 #   st.image("https://upload.wikimedia.org/wikipedia/commons/0/07/Google_Gemini_logo.svg", width=100) # Λογότυπο Gemini

st.markdown("---")

# ------------------------------------
# Επεξήγηση - Δομημένη Παρουσίαση
# ------------------------------------
st.header("💡 Σκοπός και Αξία του Εργαλείου")

st.markdown("""
Αυτή η εφαρμογή αναπτύχθηκε στο πλαίσιο της διπλωματικής εργασίας [Τίτλος ΠΜΣ] και έχει ως στόχο:
""")

# Χρήση Columns για ωραία διάταξη των πλεονεκτημάτων
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 🚀 Αυτόματος Σχεδιασμός")
    st.info("Δημιουργία ολοκληρωμένων διδακτικών σεναρίων σε δευτερόλεπτα, εξοικονομώντας πολύτιμο χρόνο στους εκπαιδευτικούς Πληροφορικής.", icon="⏰")

with col2:
    st.markdown("#### 🧠 Παιδαγωγική Ακρίβεια")
    st.info("Ενσωμάτωση αναγνωρισμένων μοντέλων όπως η **Ταξινομία του Bloom** (στόχοι γνώσης, κατανόησης, εφαρμογής) για τεκμηριωμένο σχεδιασμό.", icon="🎯")

with col3:
    st.markdown("#### 📦 Ολοκληρωμένο Πακέτο")
    st.info("Παραγωγή όχι μόνο του σεναρίου, αλλά και συνοδευτικού υλικού (Φύλλα Εργασίας & Quiz Αξιολόγησης).", icon="📚")

st.markdown("---")

st.header("👉 Πώς Λειτουργεί;")
st.markdown("""
1.  **Επιλογή Παραμέτρων:** Μεταβείτε στην ενότητα **"Σχεδιασμός"** στο αριστερό μενού.
2.  **Εστίαση Bloom:** Επιλέξτε το επίπεδο γνωστικής εμβάθυνσης που επιθυμείτε (π.χ. Εφαρμογή ή Σύνθεση).
3.  **Δημιουργία:** Το εργαλείο χρησιμοποιεί το Gemini AI για να παράγει δομημένο εκπαιδευτικό υλικό.
""")

st.markdown("---")
st.caption("Διπλωματική Εργασία: [Το Όνομά Σου] - [Έτος]")
