import streamlit as st
st.markdown(
    """
    <style>
    
    /* 1. ΣΤΥΛ SIDEBAR (Πιο Σκούρο) */
    [data-testid="stSidebar"] {
        background-color: #2c3e50; /* Σκούρο γκρι/μπλε για το sidebar */
        color: white; 
    }
    
    /* 2. ΣΤΥΛ ΣΤΟΙΧΕΙΩΝ SIDEBAR */
    [data-testid="stSidebar"] * {
        color: white !important; /* Λευκό κείμενο/τίτλοι/κουμπιά στο sidebar */
    }
    
    /* 3. ΦΟΝΤΟ ΚΥΡΙΟΥ ΣΩΜΑΤΟΣ */
    .stApp {
        background-color: #f8f9fa; /* Πολύ ανοιχτό γκρι */
        font-family: 'Roboto', sans-serif;
    }

    /* 4. ΣΤΥΛ ΤΙΤΛΩΝ */
    h1 {
        color: #1a2a3a; 
        font-size: 2.8rem; /* Μεγαλύτερος τίτλος */
        border-bottom: 3px solid #007bff;
        padding-bottom: 15px;
        margin-top: 0;
    }

    /* 5. ΣΤΥΛ ΚΟΥΜΠΙΟΥ */
    div.stButton > button:first-child {
        background-color: #007bff; 
        color: white;
        font-size: 1.1rem;
        border-radius: 12px;
        border: none;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Σκιά στο κουμπί */
        transition: all 0.3s ease;
    }
    
    div.stButton > button:first-child:hover {
        background-color: #0056b3; 
        transform: translateY(-2px); /* Ελαφριά κίνηση προς τα πάνω */
    }
    
    /* 6. ΣΤΥΛ TABS */
    .stTabs [aria-selected="true"] {
        color: #007bff; 
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
