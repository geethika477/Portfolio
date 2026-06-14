import streamlit as st
from streamlit_option_menu import option_menu
import base64

st.set_page_config(
    page_title="Geethika Portfolio",
    page_icon="✨",
    layout="wide"
)


def get_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()


photo = get_base64("red.jpeg")


st.markdown(
    f"""

    <style>

    html, body, [class*="css"] {{
        font-family: 'Poppins', sans-serif;
    }}

    .stApp {{
        background: linear-gradient(-45deg,#020617,#0f172a,#111827,#1e293b);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
        color: white;
    }}

    @keyframes gradientBG {{
        0% {{
            background-position: 0% 50%;
        }}
        50% {{
            background-position: 100% 50%;
        }}
        100% {{
            background-position: 0% 50%;
        }}
    }}

    section[data-testid="stSidebar"] {{
        background: rgba(255,255,255,0.03);
        border-right: 1px solid rgba(255,255,255,0.08);
    }}

    .hero-card {{
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(18px);
        border-radius: 30px;
        padding: 45px;
        box-shadow: 0px 10px 40px rgba(0,0,0,0.4);
        animation: fadeUp 1s ease;
    }}

    .main-card {{
        background: rgba(255,255,255,0.06);
        backdrop-filter: blur(14px);
        border-radius: 25px;
        padding: 35px;
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
        animation: fadeUp 1s ease;
    }}

    .project-card {{
        background: rgba(255,255,255,0.05);
        border-radius: 25px;
        padding: 30px;
        margin-bottom: 25px;
        border: 1px solid rgba(255,255,255,0.08);
        transition: 0.4s;
        backdrop-filter: blur(14px);
        animation: fadeUp 1s ease;
    }}

    .project-card:hover {{
        transform: translateY(-10px);
        border: 1px solid #38bdf8;
        box-shadow: 0px 0px 35px rgba(56,189,248,0.35);
    }}

    .skill-card {{
        background: rgba(255,255,255,0.05);
        padding: 30px;
        border-radius: 25px;
        border: 1px solid rgba(255,255,255,0.08);
        transition: 0.4s;
        height: 100%;
        backdrop-filter: blur(14px);
        animation: fadeUp 1s ease;
        min-height: 367px;
    }}

    .skill-card:hover {{
        transform: translateY(-10px);
        box-shadow: 0px 0px 30px rgba(99,102,241,0.35);
        border: 1px solid #818cf8;
    }}

    .section-title {{
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 25px;
        background: linear-gradient(to right,#38bdf8,#818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .stDownloadButton{{
        display: flex;
        justify-content: center;
    }}

    .stDownloadButton button{{
        background: linear-gradient(135deg,#0ea5e9,#6366f1);
        color: white;
        border: none;
        padding: 14px 28px;
        border-radius: 18px;
        font-size: 17px;
        font-weight: 600;
        transition: 0.35s;
        box-shadow: 0px 0px 20px rgba(56,189,248,0.25);
    }}

    .stDownloadButton button:hover{{
        transform: translateY(-5px);
        box-shadow: 0px 0px 35px rgba(99,102,241,0.45);
    }}

    .name-title {{
        font-size: clamp(34px, 6vw, 59px);
        font-weight: 800;
        color: white;
        line-height: 1;
    }}

    .gradient-text {{
        background: linear-gradient(to right,#38bdf8,#818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    .hero-subtitle {{
        font-size: 24px;
        color: #cbd5e1;
        margin-top: 20px;
    }}

    .hero-description {{
        font-size: 18px;
        line-height: 1.9;
        color: #dbeafe;
        margin-top: 25px;
    }}

    .social-buttons {{
        display: flex;
        gap: 15px;
        flex-wrap: wrap;
        margin-top: 35px;
    }}

    .social-btn {{
        padding: 13px 26px;
        border-radius: 15px;
        background: linear-gradient(to right,#0ea5e9,#6366f1);
        color: white !important;
        text-decoration: none;
        font-weight: 600;
        transition: 0.3s;
    }}

    .social-btn:hover {{
        transform: translateY(-5px);
        box-shadow: 0px 0px 25px rgba(56,189,248,0.5);
    }}

    .profile-wrapper {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }}

    .profile-ring {{
        width: 282px;
        height: 282px;
        border-radius: 50%;
        background: linear-gradient(45deg,#38bdf8,#818cf8,#0ea5e9,#6366f1);
        padding: 6px;
        animation: None;
        box-shadow: 0px 0px 40px rgba(56,189,248,0.45);
    }}

    .profile-wrapper img{{
        border-radius: 50%;
        width: 270px !important;
        height: 270px !important;
        object-fit: cover;
        border: 7px solid #020617;
    }}

    .floating {{
        animation: floating 4s ease-in-out infinite;
    }}
    .edu-card{{
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(14px);
        border-radius: 25px;
        padding: 30px;
        margin-bottom: 20px;
        border: 1px solid rgba(255,255,255,0.08);
        transition: 0.4s;
    }}

    .edu-card:hover{{
        transform: translateY(-8px);
        border: 1px solid #38bdf8;
        box-shadow: 0px 0px 30px rgba(56,189,248,0.35);
    }}
    .cert-btn {{
        padding: 6px 18px;
        border-radius: 10px;
        text-decoration: none;
        color: white !important;
        background: linear-gradient(135deg,#0ea5e9,#6366f1);
        font-weight: 600;
        transition: 0.3s;
    }}

    .cert-btn:hover {{
        transform: translateY(-3px);
        box-shadow: 0 0 20px rgba(56,189,248,0.5);
    }}

    .gallery-image img {{
        border-radius: 20px;
        transition: 0.4s;
    }}

    .gallery-image img:hover {{
        transform: scale(1.04);
    }}

    @keyframes rotate {{
        0% {{
            transform: rotate(0deg);
        }}
        100% {{
            transform: rotate(360deg);
        }}
    }}

    @keyframes floating {{
        0% {{
            transform: translateY(0px);
        }}
        50% {{
            transform: translateY(-15px);
        }}
        100% {{
            transform: translateY(0px);
        }}
    }}

    @keyframes fadeUp {{
        from {{
            opacity: 0;
            transform: translateY(30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0px);
        }}
    }}
    .main-card-spacing{{
        text-align: right;
    }}
    .st-emotion-cache-1r6slb0{{
    background: transparent !important;
    }}
    /* ========================= */
/* MOBILE RESPONSIVE DESIGN */
/* ========================= */

@media (max-width: 768px) {{

    .hero-card,
    .main-card,
    .project-card,
    .skill-card,
    .edu-card {{
        padding: 20px !important;
        border-radius: 20px !important;
    }}

    .name-title {{
        font-size: 36px !important;
        line-height: 1.15 !important;
    }}

    .hero-subtitle {{
        font-size: 17px !important;
        line-height: 1.5;
    }}

    .hero-description {{
        font-size: 15px !important;
        line-height: 1.7;
    }}

    .section-title {{
        font-size: 28px !important;
        text-align: center;
    }}

    .profile-ring {{
        width: min(220px, 70vw) !important;
        height: min(220px, 70vw) !important;
    }}

    .profile-wrapper img {{
        width: calc(min(220px, 70vw) - 12px) !important;
        height: calc(min(220px, 70vw) - 12px) !important;
    }}

    .social-buttons {{
        justify-content: center;
    }}

    .social-btn {{
        font-size: 14px !important;
        padding: 10px 16px !important;
    }}

    .skill-card {{
        min-height: auto !important;
    }}

    h1, h2, h3 {{
        word-break: break-word;
    }}
}}

@media (max-width: 480px) {{

    .name-title {{
        font-size: 30px !important;
    }}

    .hero-subtitle {{
        font-size: 15px !important;
    }}

    .hero-description {{
        font-size: 14px !important;
    }}

    .section-title {{
        font-size: 24px !important;
    }}

    .social-btn {{
        width: 100%;
        text-align: center;
    }}
}}
    @media (max-width: 768px){{

    .hero-mobile-order {{
        display: flex;
        flex-direction: column;
    }}

    .hero-mobile-order > div:nth-child(2) {{
        order: -1;
        margin-bottom: 20px;
    }}
}}
    /* ========================= */
    /* PROJECT BUTTONS (GLOW UI) */
    /* ========================= */

    .project-buttons {{
        display: flex;
        gap: 15px;
        margin-top: 15px;
    }}

    .glow-btn {{
        flex: 1;
        text-align: center;
        padding: 12px 16px;
        border-radius: 14px;
        text-decoration: none;
        font-weight: 600;
        color: white !important;
        background: linear-gradient(135deg,#0ea5e9,#6366f1);
        box-shadow: 0 0 15px rgba(14,165,233,0.25);
        transition: all 0.3s ease;
        display: inline-block;
    }}

    /* Hover glow effect */
    .glow-btn:hover {{
        transform: translateY(-6px) scale(1.03);
        box-shadow: 
            0 0 20px rgba(14,165,233,0.6),
            0 0 40px rgba(99,102,241,0.4);
    }}

    /* GitHub specific (darker glow tone) */
    .glow-btn.github {{
        background: linear-gradient(135deg,#1f2937,#111827);
        box-shadow: 0 0 15px rgba(0,0,0,0.4);
    }}

    .glow-btn.github:hover {{
        box-shadow:
            0 0 20px rgba(0,0,0,0.7),
            0 0 35px rgba(56,189,248,0.25);
    }}

    </style>

    """,
    unsafe_allow_html=True
)


selected = option_menu(
    menu_title=None,
    options=["Home", "Skills", "Projects", "Gallery"],
    orientation="horizontal",

    styles={
        "icon": {
            "display": "none"
        },
        "container": {
            "padding": "10px",
            "background-color": "rgba(255,255,255,0.05)",
            "border-radius": "20px",
            "backdrop-filter": "blur(14px)",
            "border": "1px solid rgba(255,255,255,0.08)"
        },

        "nav-link": {
            "font-size": "16px",
            "font-weight": "600",
            "text-align": "center",
            "color": "#2C77CE",
            "border-radius": "12px",
            "margin": "0px 5px",
        },

        "nav-link-selected": {
            "background": "linear-gradient(135deg,#0ea5e9,#6366f1)",
            "color": "white",
        }
    }
)


if selected == "Home":

    st.markdown('<div class="hero-mobile-order">', unsafe_allow_html=True)

    col1, col2 = st.columns([1.7,1])

    st.markdown('</div>', unsafe_allow_html=True)

    with col1:

        st.markdown(
            """
            <div class="hero-card">

            <div class="name-title">
            Hi, I'm
            <span class="gradient-text">
            Geethika Kethagani
            </span>
            </div>

            <div class="hero-subtitle">
            B.Tech CSE Student • Python Developer • Aspiring Software Engineer
            </div>

            <div class="hero-description">
           
            Passionate about software development and problem-solving through technology.

            I build projects using Python, Streamlit, and SQL, and I'm actively exploring Machine Learning. I enjoy turning ideas into practical applications and continuously improving my technical and problem-solving skills.

            </div>

            <div class="social-buttons">

            <a href="https://github.com/geethika477"
            target="_blank"
            class="social-btn">
            GitHub
            </a>

            <a href="https://www.linkedin.com/in/geethika-sai-kethagani-731808333/"
            target="_blank"
            class="social-btn">
            LinkedIn
            </a>

            <a href="https://docs.google.com/forms/d/e/1FAIpQLSerF_Z5134Pge8yutzK3pTukwxCUF82FDJO6o7yB2qqd1deng/viewform?usp=publish-editor" 
            target="_blank" 
            class="social-btn">
            Contact
            </a>

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
        f"""
        <div class="profile-wrapper floating">
            <div class="profile-ring">
                <img src="data:image/jpeg;base64,{photo}" />
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    st.markdown(
        """
        <div class="section-title">
        Education
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
        <div class="edu-card">
        <h2>🎓 B.Tech in Computer Science & Engineering</h2>
        <p><strong>Nadimpalli Satyanarayana Raju Institute of Technology</strong></p>
        <p>2024 - 2028</p>
        <p>CGPA: <strong>9.23</strong></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="edu-card">
        <h2>📚 Intermediate</h2>
        <p><strong>Dalton Junior College</strong></p>
        <p>2022 – 2024</p>
        <p>Percentage: <strong>89%</strong></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="edu-card">
        <h2>🏫 Secondary Education</h2>
        <p><strong>Sri T.V.S. Rao Sri Krishna Vidya Mandir (CBSE)</strong></p>
        <p>2021 – 2022</p>
        <p>Percentage: <strong>82%</strong></p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")
    with open("Geethika_Resume.pdf","rb") as f:
        resume = f.read()
    c1, c2, c3 = st.columns([2.2,2,1])
    with c2:
        st.download_button(
            label="Download Resume",
            data=resume,
            file_name="Geethika_Resume.pdf",
            mime="application/pdf"
        )


if selected == "Skills":

    st.markdown(
        """
        <div class="section-title">
        Skills & Technologies
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="skill-card">

            <h2>Programming</h2>

            <ul>
                <li>Python</li>
                <li>C</li>
                <li>Java</li>
                <li>SQL</li>
            </ul>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="skill-card">

            <h2>Libraries</h2>

            <ul>
                <li>Streamlit</li>
                <li>Pandas</li>
                <li>NumPy</li>
                <li>Matplotlib</li>
            </ul>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="skill-card">

            <h2>Web Technologies & Tools</h2>

            <ul>
                <li>HTML5</li>
                <li>CSS</li>
                <li>Git</li>
                <li>GitHub</li>
                <li>VS Code</li>
                <li>Jupyter Notebook</li>
            </ul>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    st.markdown(
        """
        <div class="section-title">
        Certifications
        </div>
        """,
        unsafe_allow_html=True
    )

    certifications = [
    ("Python Zero To Hero (Udemy)", "https://www.udemy.com/certificate/UC-ec7fe6c8-0d99-434f-b88a-7dadaa0c793b/"),
    ("Joy Of Computing Using Python (NPTEL)", "https://www.hackerrank.com/certificates/iframe/d830fd3f0af7"),
    ("Python Basic (HackerRank)", "https://drive.google.com/file/d/1g0_TJHe8QgiyjcdiTm2AUfYHBN8M0GWE/view?usp=sharing"),
]

    for cert, link in certifications:
        c1, c2 = st.columns([5,1])

        with c1:
            st.write(f"✅ {cert}")

        with c2:
            st.markdown(f"""
            <a href="{link}" target="_blank" class="cert-btn">
                View
            </a>
            """, unsafe_allow_html=True)

    with st.expander("View all certifications"):

        certifications = [
        ("Excel for Beginners (Udemy)", "https://www.udemy.com/certificate/UC-104c338b-5a59-4ee5-aca9-bafe36977954/"),
        ("SQL Foundations (Microsoft)", "https://coursera.org/share/e1eacb69b8257a29d684e7cec14cd2c7"),
        ("Machine Learning Introduction for Everyone (IBM)", "https://coursera.org/share/7848bc4eb91e1006dccb803dcd8d837f"),
        ("Pandas (Kaggle)","https://www.kaggle.com/learn/certification/geethikasaikethagani/pandas")
        ]

        for cert, link in certifications:
            c1, c2 = st.columns([5,1])

            with c1:
                st.write(f"✅ {cert}")

            with c2:
                st.markdown(f"""
                <a href="{link}" target="_blank" class="cert-btn">
                    View
                </a>
                """, unsafe_allow_html=True)

if selected == "Projects":

    st.markdown(
        """
        <div class="section-title">
        Featured Projects
        </div>
        """,
        unsafe_allow_html=True
    )

    tab1, tab2, tab3 = st.tabs(
        [
            "Mini Projects",
            "Currently Working On",
            "Main Projects"
        ]
    )

    with tab1:

        st.markdown(
            """
            <div class="project-card">

            <h2>QR Code Generator (Python)</h2>

            <p>
            A Python-powered QR Code Generator that allows users to instantly create QR codes from text, links, or custom input. Built with a focus on simplicity and usability, the tool generates high-quality scannable QR images that can be used for sharing information, websites, or digital content. This project demonstrates practical use of Python libraries for automation and real-world utility applications.
            </p>
            <div class="project-buttons">

            <a href="https://github.com/geethika477/QR_Code_Generator" target="_blank" class="glow-btn github">
            🔗 GitHub
            </a>

            <a href="https://github.com/geethika477/QR_Code_Generator/blob/master/README.md" target="_blank" class="glow-btn github">
            Description
            </a>
            
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="project-card">

            <h2>Voice-to-Text Converter</h2>

            <p>
            A simple Python desktop app that converts speech to text. You can record your voice or upload a .wav file, and it transcribes it for you. Built with Tkinter, SpeechRecognition, PyAudio, and Google Web Speech API to explore how voice recognition works in desktop apps.
            </p>

            <div class="project-buttons">

            <a href="https://github.com/geethika477/Speech_to_text_Converter" target="_blank" class="glow-btn github">
            🔗 GitHub
            </a>

            <a href="https://github.com/geethika477/Speech_to_text_Converter/blob/master/README.md" target="_blank" class="glow-btn github">
            Description
            </a>

            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with tab2:

        st.markdown(
            """
            <div class="project-card">

            <h2>Professional Portfolio</h2>

            <p>
            Modern interactive Streamlit portfolio with animations,
            glassmorphism UI, and responsive sections.
            </p>
            <div class="project-buttons">

            <a href="https://github.com/geethika477/Portfolio" target="_blank" class="glow-btn github">
            🔗 GitHub
            </a>
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with tab3:

        st.markdown(
            """
            <div class="project-card">

            <h2>Leetcode Tracker</h2>

            <p>
            A LeetCode Tracker application designed to help users systematically track their coding practice and problem-solving progress. It records solved problems, organizes practice history, and encourages consistency in Data Structures and Algorithms preparation. This project focuses on productivity, habit-building, and structured learning.
            </p>
            <div class="project-buttons">

            <a href="https://github.com/geethika477/Leetcode_Tracker" target="_blank" class="glow-btn github">
            🔗 GitHub
            </a>

            <a href="https://github.com/geethika477/Leetcode_Tracker/blob/master/README.md" target="_blank" class="glow-btn github">
            Description
            </a>
            <a href="https://leetcode-trackerr.streamlit.app/" target="_blank" class="glow-btn">
            Live Demo
            </a>

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="project-card">

            <h2>Youtube Clone</h2>

            <p>
            Developed a responsive YouTube clone using HTML and CSS, replicating the core interface of YouTube. Implemented CSS Grid and Flexbox for structured layouts, responsive design principles for different screen sizes, and interactive UI components for an enhanced user experience.
            </p>
            <div class="project-buttons">

            <a href="https://github.com/geethika477/Youtube_Clone" target="_blank" class="glow-btn github">
            🔗 GitHub
            </a>

            <a href="https://geethika477.github.io/Youtube_Clone/" target="_blank" class="glow-btn">
            Live Demo
            </a>

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


if selected == "Gallery":

    st.markdown("""
        <div class="section-title">
        Achievements & Gallery
        </div>
    """, unsafe_allow_html=True)

    def achievement(title, images):
        st.markdown(f"""
        <div class="main-card">
            <h2>{title}</h2>
        </div>
        """, unsafe_allow_html=True)

        cols = st.columns(3)

        for i, img in enumerate(images):
            with cols[i % 3]:
                st.image(img, use_container_width=True)


    with st.expander("🏆 SheHack Achievement"):
        achievement("2nd Place in SheHack", ["a.jpeg", "f.jpeg", "g.jpeg"])

    with st.expander("🏆 Code Vinyas"):
        achievement("2nd Place in Code Vinyas", ["b.jpeg", "c.jpeg"])

    with st.expander("🥇 Codeathon"):
        achievement("1st Place in Codeathon", ["h.jpeg"])

    with st.expander("🥇 IntroCode"):
        achievement("1st Place in IntroCode", ["e.jpeg"])

    with st.expander("✨ Hack With Vizag"):
        achievement("Consolation Prize", ["l.jpeg", "d.jpeg"])