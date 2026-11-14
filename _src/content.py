"""
All site content lives here. Edit this file, then run:  python3 _src/build.py
Every statement below comes from Jesse's existing portfolio, CV or project brief.
Do not add anything here that isn't true.
"""

SITE = {
    "base_url": "https://jesse-cloud515.github.io/portfolio/",  # change if you host elsewhere
    "name": "Jesse Nasamu",
    "full_name": "Jesse Esimenavhe Nasamu",
    "role_line": "UI/UX designer, data analyst and cybersecurity graduate",
    "location": "Abuja, Nigeria",
    "email": "nasamujesse@gmail.com",
    "phone_display": "+234 704 669 6654",
    "phone_link": "+2347046696654",
    "cv": "assets/files/jesse-nasamu-cv.pdf",
    # Contact form endpoint (FormSubmit). After the first submission, FormSubmit emails you an
    # activation link. Once activated you can swap the address below for the random alias it gives you.
    "form_endpoint": "https://formsubmit.co/ajax/nasamujesse@gmail.com",
    "profiles": [
        ("LinkedIn", "https://www.linkedin.com/in/jesse-nasamu003"),
        ("GitHub", "https://github.com/Jesse-cloud515"),
        ("X", "https://x.com/JesseNasamu"),
    ],
    "description": "Jesse Nasamu is a UI/UX designer, data analyst and cybersecurity graduate in Abuja, Nigeria. "
                   "Case studies in product design, Power BI dashboards and security-focused web design.",
}

HERO = {
    "statement": "I design interfaces people find easy to use, analyse the data that shows whether they work, "
                 "and look at them the way an attacker would.",
    "sub": "UI/UX and graphic designer, data analyst and cybersecurity graduate based in Abuja, Nigeria. "
           "Chief Product Officer at Zap24. Open to full-time roles and freelance projects.",
}

ABOUT = {
    "lead": "Most products are designed by one team, measured by another and secured by a third. "
            "I've trained across all three, so I tend to ask the questions that fall between them.",
    "paragraphs": [
        "I studied cybersecurity at Bingham University, graduating with a 2:1 in 2024 and writing my thesis on "
        "threats and vulnerabilities in healthcare IoT. Alongside the degree I was designing interfaces, and a 2023 "
        "internship at the National Centre for Artificial Intelligence and Robotics (NCAIR) gave me hands-on practice "
        "in user research, prototyping and interaction design.",
        "Since then my work has moved between the screen and the server room. I installed network and surveillance "
        "infrastructure at Jetra Limited, and at Galaxy Backbone I supported clients while analysing incident and "
        "service request tickets every week and month to find recurring issues and bottlenecks. Today I'm Chief "
        "Product Officer at Zap24, where I set product direction, research customers and decide what gets built next.",
        "The common thread is how I approach a problem. I start with the people who'll use the thing, check what the "
        "data actually says, and think about how it could fail or be misused before it ships.",
    ],
    "questions": [
        ("Will people understand it?", "Research, clear hierarchy and accessible interfaces."),
        ("What does the data say?", "Clean data, honest measures and dashboards that answer real questions."),
        ("How could it break?", "Security awareness from network cabling up to the login screen."),
    ],
    "affiliations": [
        "Associate member, Cyber Security Experts Association of Nigeria (CSEAN)",
        "Cisco CyberOps Associate",
        "Data Analysis certification, Axia Africa",
        "Phishing certification, Forage",
        "AI and Python certification, NCAIR",
        "Mind the Gap: AI Training",
        "IELTS overall band 7.5",
        "NYSC certificate",
    ],
    "interests": ["Reading", "Lo-fi music", "Baking", "Gaming"],
}

SKILLS = [
    ("UI/UX and product design", ["Figma", "User research", "Wireframing", "Prototyping", "Interaction design",
                                  "Usability testing", "Accessibility and inclusive design", "Product strategy"]),
    ("Graphic design", ["Brand and logo design", "Visual hierarchy and typography", "Event flyers and backdrops",
                        "Posters and print", "Social graphics"]),
    ("Data analysis", ["Power BI", "DAX", "Power Query", "Data modelling", "Microsoft Excel", "SQL",
                       "Python (pandas, SciPy)", "Exploratory and statistical analysis"]),
    ("Cybersecurity", ["Security monitoring and incident response", "Vulnerability assessment",
                       "Threat and risk assessment", "Network security", "Kali Linux", "IoT security"]),
    ("Web and infrastructure", ["HTML", "CSS", "JavaScript", "PHP", "Responsive layouts", "Structured cabling",
                                "NVR, CCTV and server setup"]),
]

EXPERIENCE = [
    {
        "when": "Aug 2025 – present", "title": "Chief Product Officer",
        "org": "Zap24 Ltd", "place": "Jos",
        "points": [
            "Set the long-term product direction in line with business goals, revenue targets and market position.",
            "Run customer research, interviews and competitor analysis to find needs and growth opportunities.",
            "Decide which products and features to pursue based on impact, feasibility and strategic fit.",
            "Own products from idea to launch, and work with sales and marketing on pricing and go-to-market.",
        ],
    },
    {
        "when": "Dec 2025 – Oct 2026", "title": "Data Analyst and Customer Service Representative",
        "org": "Galaxy Backbone", "place": "Abuja",
        "points": [
            "Analysed incident and service request tickets weekly and monthly in Excel to find trends and bottlenecks.",
            "Prepared periodic reports on ticket volumes and resolution patterns for performance monitoring.",
            "Flagged recurring complaints and service bottlenecks as areas for process improvement.",
            "Supported clients directly, resolving complaints and service issues.",
        ],
    },
    {
        "when": "Nov 2025", "title": "Graphic designer (contract)",
        "org": "Africa Field Innovation Center for Agricultural Technology (AFICAT)", "place": "",
        "points": ["Designed brand-aligned seminar materials, including the event flyer and stage backdrop."],
    },
    {
        "when": "Jun – Sep 2025", "title": "ICT Network Technician",
        "org": "Jetra Limited", "place": "Jos",
        "points": [
            "Installed and maintained surveillance cameras, wireless radio systems, structured cabling and network racks.",
            "Configured NVRs and servers for video surveillance and monitoring.",
        ],
    },
    {
        "when": "Jun – Sep 2025", "title": "Executive facility network setup (project)",
        "org": "", "place": "",
        "points": [
            "Installed and configured core network devices, CCTV cameras and structured cabling for an executive facility.",
            "Tested connectivity and troubleshot network and surveillance faults.",
        ],
    },
    {
        "when": "Apr – Sep 2023", "title": "UI/UX Design Intern",
        "org": "National Centre for Artificial Intelligence and Robotics (NCAIR)", "place": "Abuja",
        "points": [
            "Practised user research, prototyping and interaction design on real projects.",
            "Worked with IoT devices for the first time.",
        ],
    },
]

EDUCATION = [
    {"when": "2020 – 2024", "title": "BSc Cybersecurity, Second Class Upper (2:1)", "org": "Bingham University",
     "note": "Thesis: IoT in Healthcare: Threats and Vulnerabilities, covering threats, vulnerabilities, data privacy and risks in connected medical devices."},
    {"when": "", "title": "Data Analysis certification", "org": "Axia Africa",
     "note": "Data cleaning, visualisation and insight generation."},
]

SERVICES = [
    ("UI/UX design", "Research, flows, wireframes and Figma prototypes you can test with real users before a line of code is written."),
    ("Product design", "Turning a rough idea into a product people understand: who it's for, what they need to do and the screens that get them there."),
    ("Web design and development", "Responsive, accessible websites and web apps in HTML, CSS, JavaScript and PHP, from learning platforms to event registration with QR check-in."),
    ("Graphic design", "Logos, flyers, event backdrops and social graphics that stay consistent with your brand."),
    ("Data analysis", "Cleaning messy data and building Power BI or Excel dashboards that answer the questions your team actually asks."),
    ("Cybersecurity analysis", "A security-minded review of your site or setup, from reconnaissance and vulnerability checks to clear, prioritised recommendations."),
]

TESTIMONIALS = [
    ("Nasamu Jesse Esimenavhe ranks in the top 25% of his class in the Cybersecurity program at Bingham University. "
     "As both his lecturer and program coordinator, I have observed his strong interest and consistent improvement in "
     "his academics and practical skills in the fields of cybersecurity, digital forensics, and computing in general.",
     "Adelaye Ishaya", "Lecturer and programme coordinator, Bingham University"),
    ("I had the pleasure of working with Jesse on the Sirenecare projects, where his data analysis and UI/UX design "
     "skills shone brightly. Jesse's designs consistently impressed the team and improved our users' experience. "
     "I highly recommend Jesse as a talented UI/UX designer and data analyst for any project.",
     "Nathaniel Handan", "Founder, AI Bauchi"),
    ("Working with Jesse is an absolute pleasure. Their expertise in web design, graphic design and cybersecurity is "
     "exceptional. Jesse seamlessly combines creativity with technical skills, creating stunning and secure websites.",
     "Amina Shiga", "Microsoft Student Ambassador"),
    ("Jesse's work ethic is exemplary, consistently approaching tasks with enthusiasm and a solutions-oriented mindset. "
     "His positive attitude not only boosts team morale but also contributes to the success of every project.",
     "Ahmed Bature", "Entrepreneur"),
]

# ---------------------------------------------------------------------------------------------
# PROJECTS. Story fields are optional: any field left empty is simply not shown on the page.
# images: list of (file stem in assets/img/work, alt text)
# ---------------------------------------------------------------------------------------------
PROJECTS = [
    {
        "slug": "agriconnect-events", "title": "AgriConnect Events",
        "discipline": "Web development · Security", "year": "2026", "dates": "Aug 2026",
        "role": "Design and development of the whole platform. Nathaniel Handan built the database.",
        "summary": "A seminar registration and QR check-in platform: register once, get a unique QR pass, get scanned and checked in at the door.",
        "challenge": "Agricultural seminars still run on paper lists at the door. Organisers needed a way to take registrations online, issue each attendee a pass, "
                     "and check people in quickly on the day without exposing anyone's personal details.",
        "approach": "The QR code carries only an opaque random token, never a name, email or phone number. Registration and attendance are kept separate: "
                    "submitting the form makes someone registered, and only an authenticated staff member can check them in.",
        "process": ["Built the public side: event page, registration form, a confirmation page with the QR pass, and a 'find my registration' lookup.",
                    "Built the organiser console: dashboard, registrations table with filters and export, waiting list, attendance reports and a seven-step event wizard.",
                    "Designed the check-in console for event day: camera scanning, manual search when a camera or phone fails, and a full-screen result for each outcome.",
                    "Every scan answers five questions before anything is written: does the registration exist, is it for this event, is it cancelled, is it confirmed, has it already been used.",
                    "Added role-based access (owner, organiser, check-in staff), an audit log, and a PHP 8 backend connected to the database Nathaniel Handan set up."],
        "tools": ["HTML", "CSS", "JavaScript", "PHP 8", "Playwright"],
        "solution": "A working platform with a public registration site and a staff console. Scanning a pass shows one of five clear results: confirmed, already checked in, not found, cancelled or wrong event.",
        "results": "The front-end build ships with an end-to-end Playwright test suite covering registration, duplicate prevention, all five check-in outcomes, waiting list, exports and role restrictions; all 55 checks pass.",
        "findings": [], "recommendations": [], "note": "",
        "links": [("Visit the live site", "https://agriconnect.nathaniel.name.ng/"),
                  ("Open the check-in console (staff sign-in)", "https://agriconnect.nathaniel.name.ng/admin/checkin")],
        "images": [("agriconnect-1", "AgriConnect event page for the Good Agronomic Practices Agricultural Seminar 2026"),
                   ("agriconnect-2", "Registration successful page showing the attendee's QR event pass"),
                   ("agriconnect-3", "Event-day check-in console with QR scanner and manual search"),
                   ("agriconnect-4", "Organiser dashboard with registration totals, sign-up trend and capacity")],
    },
    {
        "slug": "minaa-edu-e-learning-platform", "title": "Minaa Edu e-learning platform",
        "discipline": "Web development · UI/UX design", "year": "2026", "dates": "Aug 2026",
        "role": "Design and development",
        "summary": "A self-paced learning platform for Good Agronomic Practice, with courses, a lesson player, assessments and verifiable certificates.",
        "challenge": "Farmers, students and extension workers need practical agronomy training they can take at their own pace, with proof of what they've learned.",
        "approach": "A plain HTML, CSS and JavaScript site with no framework or server, so it loads fast and can be hosted anywhere. All course content lives in editable data files.",
        "process": ["Built a course catalogue with live search and filters for learning area, difficulty and duration, kept in the URL so a filtered view can be shared.",
                    "Built the lesson player: video, reading and exercise stages, a curriculum sidebar with progress, notes, resources and transcripts.",
                    "Added assessments that draw scenario questions at random from a question bank, with explanations, review and retakes.",
                    "Added a learner dashboard, printable certificates and a public page to verify a certificate by its ID.",
                    "Added a community section, pricing and checkout pages, and a small build script that writes shared navigation and course data into every page."],
        "tools": ["HTML", "CSS", "JavaScript", "Node.js (build script)", "Netlify"],
        "solution": "A complete learning site: five learning areas, course pages, the lesson player, exams, a dashboard and certificates, published on Netlify.",
        "results": "",
        "findings": [], "recommendations": [], "note": "",
        "links": [("Visit the live site", "https://e-africulture.netlify.app/")],
        "images": [("minaa-edu-1", "Minaa Edu home page with the headline Learn better. Farm better. Grow sustainably."),
                   ("minaa-edu-2", "Course page for Integrated Crop Production Systems"),
                   ("minaa-edu-3", "Certificate verification page")],
    },
    {
        "slug": "michalo-e-learning-website", "title": "Michalo e-learning website",
        "discipline": "UI/UX design", "year": "2024", "dates": "Nov – Dec 2024",
        "summary": "A learning platform designed so students can find a course, start it and keep going without friction.",
        "challenge": "Online learning only works if people stay with it. The aim was to make online education intuitive "
                     "and enjoyable, with a smooth journey from the first visit to finishing a course.",
        "approach": "I designed around the learner: easy navigation, a personalised learning experience and consistent, "
                    "accessible interactions across the platform.",
        "process": ["Designed user-centred interfaces in Figma with a focus on ease of navigation.",
                    "Shaped the experience around personalised learning.",
                    "Prioritised consistency and accessibility across every screen."],
        "tools": ["Figma"],
        "solution": "A desktop website with a clear welcome, course discovery and sign-up flow, delivered as an interactive Figma prototype.",
        "results": "",
        "findings": [], "recommendations": [], "note": "",
        "links": [("Open the Figma prototype", "https://www.figma.com/proto/sP9dLTmpeZbIxOM4rSqu9b/Michalo?page-id=0%3A1&node-id=7-3446&viewport=1090%2C791%2C0.05&t=NaujxFuvurywib9u-1&scaling=scale-down&content-scaling=fixed&starting-point-node-id=7%3A3446")],
        "images": [("michalo-1", "Michalo e-learning homepage shown on a desktop monitor"),
                   ("michalo-2", "Michalo sign-up screen inviting students to join the platform")],
    },
    {
        "slug": "cybersecurity-awareness-website", "title": "Cybersecurity awareness website",
        "discipline": "UI/UX design · Cybersecurity", "year": "", "dates": "",
        "summary": "A website and mobile design that helps ordinary users recognise online threats and get help.",
        "challenge": "Security advice is often written for specialists. This site needed to speak to everyday users "
                     "about online theft and ransomware, and point them to services when something goes wrong.",
        "approach": "I combined my cybersecurity training with UI design: plain headlines, strong contrast and a clear "
                    "path from awareness content to services such as penetration testing and incident response.",
        "process": ["Planned content around common threats, including online theft and ransomware.",
                    "Designed desktop and mobile layouts in Figma.",
                    "Added a services area and a community forum for questions."],
        "tools": ["Figma"],
        "solution": "Responsive designs covering the homepage, threat articles, services, a password generator tool and a forum.",
        "results": "",
        "findings": [], "recommendations": [], "note": "",
        "links": [("Open the Figma file", "https://www.figma.com/design/4HGuuv9Ph4F47nVovjvgXf/Cyber-Security-Awareness-Website?node-id=0-1&t=XxiRTPjsEXlAwVMh-1")],
        "images": [("cyber-awareness-1", "Cybersecurity awareness homepage with the headline Stop Online Theft"),
                   ("cyber-awareness-2", "Desktop view of the awareness site on a monitor"),
                   ("cyber-awareness-3", "Article page about a ransomware attack"),
                   ("cyber-awareness-4", "Mobile screens showing the homepage and the services menu"),
                   ("cyber-awareness-5", "Mobile screen with the password generator and forum")],
    },
    {
        "slug": "preview-event-booking-app", "title": "PreView event booking app",
        "discipline": "UI/UX design", "year": "2024", "dates": "Sep – Oct 2024",
        "summary": "A mobile app that makes discovering, scheduling and managing events simple for attendees and organisers.",
        "challenge": "Finding events, booking them and keeping track of plans usually means juggling several apps. "
                     "Organisers have the same problem from the other side.",
        "approach": "A clean, modern interface that puts navigation first and follows accessibility best practice, "
                    "so the app works for as many people as possible.",
        "process": ["Designed the onboarding, discovery and booking screens in Figma.",
                    "Built an interactive prototype to walk through the full flow."],
        "tools": ["Figma"],
        "solution": "An intuitive platform where users can manage events, stay informed and take part in event planning.",
        "results": "",
        "findings": [], "recommendations": [], "note": "",
        "links": [("Open the Figma prototype", "https://www.figma.com/proto/qGNy3syL9fDkT5BPxXqBTh/PreView?page-id=0%3A1&node-id=28-2137&p=f&viewport=1072%2C-48%2C0.09&t=jVc6lGrVjuk5WGhr-1&scaling=scale-down&content-scaling=fixed&starting-point-node-id=1%3A465")],
        "images": [("preview-1", "PreView app home and splash screens on two phones"),
                   ("preview-2", "PreView event listing screens on a phone"),
                   ("preview-3", "PreView onboarding screen"),
                   ("preview-4", "PreView event discovery screens")],
    },
    {
        "slug": "bike-sales-analysis", "title": "Bike sales analysis",
        "discipline": "Data analysis", "year": "2026", "dates": "Feb 2026",
        "summary": "Who buys bikes and who doesn't: purchase behaviour by age, income, commute distance, region and marital status.",
        "challenge": "The Europe bike sales data had 18 columns but gave decision-makers little visibility into which "
                     "regions sell best, how customer groups behave, or whether things like children or commute "
                     "distance influence a purchase.",
        "approach": "I cleaned and prepared the data in Excel and Power Query, answered a fixed set of business questions "
                    "with pivot analysis, then built an interactive Power BI dashboard so the answers could be explored.",
        "process": ["Kept an untouched copy of the raw table, then cleaned a duplicate in Power Query.",
                    "Removed duplicates, checked missing values and standardised inconsistent entries.",
                    "Analysed purchase rate by age, gender, income, marital status, commute distance and region.",
                    "Built a Power BI dashboard with KPI cards, charts and filters."],
        "findings": ["More customers did not buy a bike than did, so conversion is the main opportunity.",
                     "Middle-aged customers were the most likely to buy.",
                     "Higher-income customers bought more often.",
                     "Customers with shorter commutes bought more often than those travelling further.",
                     "Married customers were slightly more likely to buy than single customers; the gender gap was small.",
                     "Purchases varied noticeably by region."],
        "recommendations": ["Focus marketing on middle-aged, higher-income customers with short commutes.",
                            "Sell bikes on convenience, cost savings and health for short commutes.",
                            "Invest more in strong regions and investigate why weaker ones lag.",
                            "Offer instalments and entry-level models to reach lower-income customers."],
        "tools": ["Microsoft Excel", "Power Query", "Power BI"],
        "solution": "",
        "results": "",
        "note": "",
        "links": [("View project files on Google Drive", "https://drive.google.com/drive/folders/1JGjv68sfsgXspN9xBG2w-avgG1EJYsmp?usp=drive_link")],
        "images": [("bike-sales-1", "Bike sales dashboard with KPI cards, charts and filter buttons"),
                   ("bike-sales-2", "Bike sales summary charts by customer group")],
    },
    {
        "slug": "fraud-detection-analysis", "title": "Fraud detection analysis",
        "discipline": "Data analysis · Cybersecurity", "year": "2026", "dates": "2026",
        "summary": "A Power BI dashboard for spotting fraud patterns in customer payment transactions.",
        "challenge": "Fraud costs money, reputation and customer trust, and rule-based checks often miss it. The "
                     "questions: which customers, categories, amounts, months and merchants carry the most fraud risk?",
        "approach": "I worked from a simulated four-month (May to August) set of payment transactions with customer age "
                    "band, gender, postcode, merchant, purchase category, amount and a fraud label, and framed the "
                    "analysis around five lenses: demographics, amount, monthly trend, merchant and category.",
        "process": ["Checked data quality, missing values, data types and fraud labels, and standardised categories.",
                    "Defined KPIs: total transactions, fraudulent transactions, fraud rate, total amount, fraud loss and average transaction.",
                    "Built a Power BI dashboard with slicers for gender, month and purchase category.",
                    "Broke fraud down by age band, gender and category, with a drill table of fraudulent transactions by age."],
        "findings": ["The dashboard covers 200 transactions across 9 purchase categories, of which 92 are labelled fraudulent.",
                     "Transportation accounts for most of the transactions, far ahead of Health and Food."],
        "recommendations": ["Automated alerts for high-risk categories and merchants.",
                            "Extra verification for unusually large transactions.",
                            "Customer risk scores built from age, history and behaviour.",
                            "Regular reviews of merchants with elevated fraud rates."],
        "tools": ["Power BI", "Microsoft Excel"],
        "solution": "",
        "results": "",
        "note": "The dataset is simulated, so the project shows the method rather than describing a real bank.",
        "links": [("Read the project brief (PDF)", "assets/files/fraud-detection-analysis.pdf"),
                  ("View project files on Google Drive", "https://drive.google.com/drive/folders/1M6C45nYtpPYzEnqHVERSa0PEv70UmQXt?usp=drive_link")],
        "images": [("fraud-1", "Fraud detection dashboard with KPI cards, fraud by age and gender, and a fraud table")],
    },
    {
        "slug": "sb4-kids-website", "title": "SB4 Kids website",
        "discipline": "UI/UX design", "year": "", "dates": "",
        "summary": "Web and mobile designs for SB4 Kids, including a page for its artificial intelligence class.",
        "challenge": "",
        "approach": "A simple layout that works on desktop and mobile, with photos of the classes up front.",
        "process": ["Designed the homepage, services and gallery pages in Figma.",
                    "Adapted each layout for mobile."],
        "tools": ["Figma"],
        "solution": "Desktop and mobile designs for the full site.",
        "results": "",
        "findings": [], "recommendations": [], "note": "",
        "links": [("Open the Figma file", "https://www.figma.com/design/r6wcVHHHiIun6s7uOh11P4/SB4KIDS?node-id=11-41&t=YZRixSAAqbQmYCRv-1")],
        "images": [("sb4kids-1", "SB4 Kids homepage on a laptop"),
                   ("sb4kids-2", "SB4 Kids page welcoming students to the artificial intelligence class"),
                   ("sb4kids-3", "SB4 Kids gallery page on a laptop"),
                   ("sb4kids-4", "SB4 Kids mobile screens"),
                   ("sb4kids-5", "SB4 Kids mobile home screen")],
    },
    {
        "slug": "front-end-developer-portfolio", "title": "Front-end developer portfolio",
        "discipline": "UI/UX design · Web design", "year": "2025", "dates": "Jan 2025",
        "summary": "A portfolio site for a front-end developer, designed to put the projects and skills first.",
        "challenge": "A developer's portfolio has seconds to show what they can do. It needs to be readable, "
                     "accessible and easy to navigate on any device.",
        "approach": "I studied leading portfolios to understand current layouts and features, then chose a clean, "
                    "modern style built on readability, hierarchy and visual storytelling.",
        "process": ["Analysed top developer portfolios for design trends and layouts.",
                    "Sketched low-fidelity layouts for the homepage, project pages and about and contact sections.",
                    "Designed high-fidelity desktop and mobile screens and a working prototype.",
                    "Implemented the designs in HTML, CSS and JavaScript."],
        "tools": ["Figma", "HTML", "CSS", "JavaScript"],
        "solution": "An engaging, accessible portfolio that highlights the developer's projects and technical skills.",
        "results": "",
        "findings": [], "recommendations": [], "note": "",
        "links": [("Open the Figma prototype", "https://www.figma.com/proto/WsXlubCiQbNuY1oCVdIjRQ/Sheriff?page-id=2%3A3&node-id=565-8410&viewport=251%2C124%2C0.04&t=qrlhu2zD08pqcS0N-1&scaling=scale-down&content-scaling=fixed&starting-point-node-id=565%3A8410&show-proto-sidebar=1")],
        "images": [("sheriff-1", "Portfolio blog screen on a phone"),
                   ("sheriff-2", "Portfolio skills and projects screens on two phones"),
                   ("sheriff-3", "Portfolio dark-theme mobile screens"),
                   ("sheriff-4", "Portfolio shown on a laptop"),
                   ("sheriff-5", "Portfolio blog page on a desktop monitor")],
    },
    {
        "slug": "regional-sales-performance", "title": "Regional sales performance analysis",
        "discipline": "Data analysis", "year": "2026", "dates": "Mar 2025 – Apr 2026",
        "summary": "Where a year of sales came from: by month, region, sales rep and product category.",
        "challenge": "The business had no clear view of what drives sales across products, people, regions, customers "
                     "and channels, which made it hard to decide where to put sales effort.",
        "approach": "I cleaned the data in Excel and Power Query, then ran exploratory analysis around eight business "
                    "questions covering seasonality, rep performance, regions, categories, customer types and channel.",
        "process": ["Kept a raw backup, then removed duplicates and checked for missing values in Power Query.",
                    "Standardised inconsistent entries and checked formats.",
                    "Compared revenue by month, sales rep, region and category in Excel."],
        "findings": ["Total revenue came to ₦12.35 million.",
                     "November was the peak month at ₦1.89 million; April was the lowest at ₦0.21 million.",
                     "The top sales rep brought in ₦3.86 million against ₦1.17 million for the lowest, and led three of the four regions.",
                     "North (₦3.36 million) and East (₦3.35 million) were almost level; West trailed at ₦2.61 million.",
                     "Clothing was the strongest category at ₦3.88 million; Electronics the weakest at ₦2.01 million."],
        "recommendations": ["Document the top rep's approach and train the team on it.",
                            "Investigate the West region gap before moving resources there.",
                            "Check Electronics margins before deciding whether to invest or scale back.",
                            "Assign territories based on proven regional performance."],
        "tools": ["Microsoft Excel", "Power Query"],
        "solution": "",
        "results": "",
        "note": "The dataset is simulated (500+ transactions across 2023), so the figures show the method rather than a real store.",
        "links": [("View project files on Google Drive", "https://drive.google.com/drive/folders/1SkPWAJfDVfV2NwUgt-i50Mi2f5sIlyFQ?usp=drive_link")],
        "images": [("regional-sales-1", "Sales analysis charts broken down by region and category")],
    },
    {
        "slug": "aficat-seminar-design", "title": "AFICAT seminar design",
        "listed": False,  # hidden from the Selected work list (page still exists)
        "discipline": "Graphic design", "year": "2025", "dates": "Nov 2025 (contract)",
        "summary": "Flyer and stage backdrop for a seminar on agricultural mechanisation in Nigeria.",
        "challenge": "The Africa Field Innovation Center for Agricultural Technology needed event materials that "
                     "carried its brand and gave equal space to several partner organisations.",
        "approach": "A clean layout built on the centre's green, with the seminar theme as the main message and partner logos in a consistent strip.",
        "process": [], "tools": [],
        "solution": "A printed flyer and a large-format backdrop for the seminar on 10 November 2025.",
        "results": "",
        "findings": [], "recommendations": [], "note": "",
        "links": [],
        "images": [("aficat-1", "AFICAT seminar flyer with a tractor and the event details"),
                   ("aficat-4", "AFICAT seminar stage backdrop with partner logos"),
                   ("aficat-2", "Wide version of the AFICAT stage backdrop"),
                   ("aficat-3", "Alternative AFICAT backdrop layout")],
    },
    {
        "slug": "customer-segmentation-dashboard", "title": "Customer segmentation dashboard",
        "discipline": "Data analysis", "year": "2026", "dates": "2026",
        "summary": "A one-page Power BI dashboard profiling 500 customers by region, gender, occupation, segment and age group.",
        "challenge": "Management wanted to understand customer growth and how the customer base is spread across "
                     "regions and demographic groups, to target marketing better.",
        "approach": "I built a single interactive Power BI page with headline figures, a growth trend and breakdowns, "
                    "filterable by region, gender, segment and age group.",
        "process": ["Summarised customer count, average tenure, average age and average income.",
                    "Charted new customers per year from 2016 to 2024.",
                    "Broke customers down by region, gender, occupation, segment and age group."],
        "findings": ["Customer acquisition peaked between 2016 and 2018 at more than 60 new customers a year, then fluctuated and declined after 2024.",
                     "The South region has the most customers and the West the fewest.",
                     "The gender split is close to even: 51.2% female and 48.8% male.",
                     "Engineering is the largest occupation group (78 customers) and Trading the smallest (59).",
                     "The customer base leans older: seniors are the largest age group and youth the smallest."],
        "recommendations": ["Steady acquisition with sustained, data-driven marketing.",
                            "Targeted campaigns in under-represented regions.",
                            "Products and channels aimed at younger customers.",
                            "Loyalty rewards for customers approaching five years' tenure."],
        "tools": ["Power BI"],
        "solution": "", "results": "", "note": "",
        "links": [("View project files on Google Drive", "https://drive.google.com/drive/folders/1BXY36bRm2rEH4d6VYBjz7-7BPdcNzBiK?usp=drive_link")],
        "images": [("customer-segmentation-1", "Customer segmentation dashboard with growth trend, regional bars and segment charts")],
    },
    {
        "slug": "global-layoff-analysis", "title": "Global layoff analysis",
        "discipline": "Data analysis", "year": "2026", "dates": "Apr 2026",
        "summary": "SQL analysis of layoffs across industries, countries, company stages and time.",
        "challenge": "Layoff data is messy and inconsistent. It needed cleaning before it could say anything reliable "
                     "about which industries, countries and kinds of company were cutting jobs, and when.",
        "approach": "I used SQL for the whole pipeline: a staging table for cleaning, then exploratory queries grouped by "
                    "industry, company, country, stage and month.",
        "process": ["Removed duplicates, handled missing values and fixed inconsistent entries.",
                    "Ranked industries, companies, countries and funding stages by layoffs with GROUP BY and aggregate queries.",
                    "Tracked layoffs by country and industry per year, and by month.",
                    "Built a rolling total to show the cumulative effect over time."],
        "findings": ["The largest single layoff in the data came from the Consumer industry, at 12,000 people.",
                     "Some companies laid off 100% of staff, pointing to closures or market exits.",
                     "A small number of companies account for a large share of all layoffs.",
                     "Layoffs come in monthly spikes rather than a steady trend, and the rolling total keeps rising."],
        "recommendations": ["Flexible staffing and demand forecasting in high-risk industries.",
                            "Cash reserves and more diverse revenue to absorb shocks.",
                            "Hiring for early-stage companies that tracks realistic revenue."],
        "tools": ["SQL"],
        "solution": "", "results": "", "note": "",
        "links": [("View project files on Google Drive", "https://drive.google.com/drive/folders/1UVuvaxOTpoXtZOjyhLa56GzcV5zlw6M_?usp=drive_link")], "images": [("layoffs-sql-1", "SQL from Data Cleaning.sql: a ROW_NUMBER() window over every column to find duplicate layoff records"),
                   ("layoffs-sql-2", "SQL from Exploratory Data Analysis.sql: monthly layoffs with a rolling total using a CTE and a window function"),
                   ("layoffs-sql-3", "SQL from Data Cleaning.sql: converting text dates with STR_TO_DATE and changing the column type to DATE")],
    },
]

# (image stem, alt text, caption, optional link)
GALLERY = [
    ("chick-co", "Chick Co logo", "Logo design", ""),
    ("aficat-flyer", "AFICAT seminar flyer with a tractor and the event details", "AFICAT seminar flyer", ""),
    ("aficat-backdrop", "AFICAT seminar stage backdrop with partner logos", "AFICAT stage backdrop", ""),
    ("danfo", "Danfo poster with a Lagos bus", "Poster", ""),
    ("adopt-a-dog", "Adopt a Dog poster displayed on a wall", "Adopt a Dog branding",
     "https://www.figma.com/proto/T9pW9cYE0mkrHijooeXbsW/Practice-1?page-id=0%3A1&node-id=17-4&viewport=185%2C147%2C0.14&t=sG34GnqlQTbm8QBz-1&scaling=contain&content-scaling=fixed"),
    ("eid", "Eid festival brochure mockup", "Eid festival brochure",
     "https://www.figma.com/proto/TqCRWz9jpW654k295RIcfA/Untitled?page-id=0%3A1&node-id=1-6&viewport=208%2C254%2C0.13&t=f8JJUxe76CKtWQtc-1&scaling=contain&content-scaling=fixed"),
    ("africa-2", "Africa typographic poster with zebra on the savannah", "Africa series", ""),
    ("africa-1", "Africa typographic poster with hippos in water", "Africa series", ""),
    ("africa-3", "Africa typographic poster with a baobab tree", "Africa series", ""),
    ("africa-4", "Africa typographic poster with lions", "Africa series", ""),
]

# ---------------------------------------------------------------------------------------------
# CYBERSECURITY THREAT INTELLIGENCE DASHBOARD CASE STUDY
# Source: "Cybersecurity Attacks Analysis – Final Report" and the project README.
# ---------------------------------------------------------------------------------------------
CASE = {
    "slug": "cybersecurity-threat-intelligence-dashboard",
    "title": "Cybersecurity Threat Intelligence Dashboard",
    "category": "Data analysis · Business intelligence · Cybersecurity",
    "year": "2026",
    "dates": "Nov 2026",
    "tools": ["Microsoft Power BI", "DAX", "Power Query (M)", "Data modelling", "Python (pandas, SciPy)", "Jupyter"],
    "summary": "40,000 security events, cleaned and tested in Python, then turned into a seven-page Power BI dashboard. "
               "The finding that matters: response did not follow risk.",
    "headline": "A High-severity attack was as likely to be ignored as a Low-severity one.",
    "overview": "An end-to-end analytics project on 40,000 recorded security events from 1 January 2020 to 11 October 2023. "
                "I cleaned and explored the data in Python, tested the patterns statistically, and built a seven-page "
                "interactive Power BI dashboard with a star-schema model and 52 DAX measures. Every headline figure was "
                "cross-checked against an independent Python calculation.",
    "problem": "The aim was to show what was attacked, how, when, and how each event was handled, in a form security "
               "analysts and managers can explore themselves. Raw event logs can't answer that. They need cleaning, "
               "a proper model and measures that update with every filter.",
    "questions": [
        "Which attack types, severities, protocols and traffic types dominate?",
        "Are some attack types riskier than others?",
        "Do anomaly scores separate high-risk events from low-risk ones?",
        "Is the response (Blocked, Logged, Ignored) matched to risk?",
        "Are there time-of-day, weekday, yearly, device or geographic patterns?",
    ],
    "dataset": [
        ("Size", "40,000 events, one per row, 33 columns"),
        ("Period", "1 Jan 2020 to 11 Oct 2023 (2023 is partial)"),
        ("Network", "IPs, ports, protocol, packet length, traffic type, segment, proxy"),
        ("Threat", "Attack type, signature, severity, anomaly score (0–100), malware indicators"),
        ("Response", "Alerts, IDS/IPS alerts, firewall logs, log source, action taken"),
        ("User and device", "User, browser user-agent, city and state"),
    ],
    "dataset_note": "Five indicator columns were about half empty, stored as empty strings. An empty value only means "
                    "the indicator wasn't recorded.",
    "process": [
        ("Data cleaning", "Python notebook producing a cleaned file with derived time columns: year, month, weekday, hour and time period."),
        ("Exploratory analysis", "Univariate, categorical, bivariate and multivariate analysis, plus a correlation matrix and about 15 presentation charts."),
        ("Statistical testing", "Chi-square tests of independence and a Kruskal–Wallis test in SciPy, to check whether differences in the charts are bigger than chance."),
        ("Power Query", "Quote-aware loading, en-GB date typing, empty strings turned into real blanks, readable flag columns, city and state split, device OS and browser parsed, and bands for anomaly score, packet size and port range."),
        ("Model and measures", "A star schema: one fact table of events filtered by Date, Severity and Response Action tables, all one-to-many and single direction, with 52 DAX measures in seven folders."),
        ("Validation", "Every headline KPI recalculated in pandas and compared with the dashboard: 40,000 events, 13,382 High-severity, average anomaly score 50.11, 20,000 IoC-flagged, 33.8% block rate."),
    ],
    "pages": [
        ("Executive Overview", "KPI cards, monthly attack trend, severity mix, top attack types, response mix"),
        ("Attack Analysis", "Attack type share, weekday and year-to-month drill-down, type by severity, signatures, protocols"),
        ("Network Traffic", "Traffic type, protocol, packet-size bands, port ranges, traffic trend"),
        ("Threat & Severity", "Anomaly bands, anomaly score by severity, IoC flags, device OS, states"),
        ("Response & Operations", "Blocked, Logged and Ignored by severity and attack type, operational-gap table"),
        ("Investigation", "Row-level event log with IP and user search, used as a drill-through target"),
        ("Key Insights", "Findings, recommendations and limitations"),
    ],
    # Share of events by recorded action, per severity level (from the final report)
    "response": [
        ("High", 13382, 33.9, 32.8, 33.3),
        ("Medium", 13435, 33.6, 33.6, 32.8),
        ("Low", 13183, 34.0, 32.6, 33.4),
    ],
    "findings": [
        ("Response vs severity", "Not risk-based", "Blocked: High 33.9%, Medium 33.6%, Low 34.0%. Chi-square p = 0.49"),
        ("Gaps", "High-risk events left without action", "4,460 High-severity events ignored; 66.1% not blocked; 6,576 IoC-flagged events ignored"),
        ("Attack types", "Even split", "DDoS 33.6%, Malware 33.3%, Intrusion 33.2%"),
        ("Attack type vs severity", "No type is riskier", "Chi-square p = 0.77"),
        ("Anomaly scores", "Uniform and unrelated to severity", "Mean 50.11, median 50.35. Kruskal–Wallis p = 0.32"),
        ("Volume over time", "Steady, no trend", "About 29 events a day (range 15–49)"),
        ("Time of day", "No real peak", "Busiest hour 13:00 (1,737) vs quietest 12:00 (1,588)"),
        ("Numeric columns", "No correlation", "All Pearson |r| ≤ 0.005"),
        ("IP addresses", "No repeats", "All 40,000 source and destination IPs unique"),
        ("Devices", "Windows leads", "Windows 44.9%, Linux 17.9%, macOS 14.5%, iOS 14.4%, Android 8.2%"),
    ],
    "synthetic": "Attack types, severities, protocols and responses each split almost exactly into thirds, and every IP "
                 "appears once. Real security logs cluster by time, source and target, so this points to a synthetic "
                 "dataset. I treat the project as a demonstration of method, not a description of a real network.",
    "recommendations": [
        ("Block High-severity and IoC-flagged events automatically", "66.1% of High-severity events were not blocked."),
        ("Send every ignored High-severity or IoC event to a review queue with an owner", "4,460 High-severity events were ignored with no recorded follow-up."),
        ("Validate or recalibrate the anomaly model before using it for triage", "Scores are uniform from 0 to 100 and unrelated to severity."),
        ("Record outcomes: true or false positive, time to contain", "\u201cLogged\u201d can't currently be told apart from \u201cresolved\u201d."),
        ("Add asset criticality and stable host and account keys", "Every IP is unique, so repeat attackers can't be ranked."),
        ("Log benign traffic as well", "Without non-attack events, a true detection rate can't be measured."),
    ],
    "lessons": [
        ("Pin the date culture", "Without en-GB, dates like 05/07 load as May on some machines and July on others."),
        ("Load with quote handling", "Line breaks inside the payload text split rows until the CSV was read with proper quoting."),
        ("Empty strings aren't blanks", "Five columns counted half-empty strings as values until I converted them."),
        ("Accept the honest result", "It took several tests to accept that the finding was \u201cno pattern\u201d and say the data is probably synthetic, rather than talk up 33.6% against 33.2%."),
        ("Not every requested measure is valid", "There is no Critical level and no benign events, so I built IDS/IPS detection coverage instead of a detection rate."),
    ],
    "limitations": [
        "The data looks synthetic, so the findings show the method, not real attack behaviour.",
        "Labels are as recorded. Nothing confirms an event was malicious or that a block worked.",
        "The tests show associations or their absence, not causes.",
        "2023 stops on 11 October, so its totals aren't comparable with full years.",
    ],
    "screenshots": [("cyber-overview", "Executive Security Overview page with KPI cards, monthly attack trend and severity distribution"),
                    ("cyber-model", "Data model: one Security Events fact table filtered by Date, Severity and Response Action tables")],
    "links": [("Download the full report (PDF)", "assets/files/cybersecurity-attacks-analysis-report.pdf"),
              ("View project files on Google Drive", "https://drive.google.com/drive/folders/1Q3TmErx_EPh4RjQwT8K4n2Yrruf1KzJ_?usp=drive_link")],
}
