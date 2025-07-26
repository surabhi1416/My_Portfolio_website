from datetime import datetime
from models.portfolio import Portfolio, PersonalInfo, Project, Experience

# Seed data based on the existing mock data
def get_portfolio_seed_data():
    personal_info = PersonalInfo(
        name="Surabhi Santosh Pilane",
        title="Final-Year Computer Engineering Student",
        subtitle="Focused on Data Science, Analytics & AI | Passionate about solving real-world problems through data.",
        email="pilanesurabhi14@gmail.com",
        phone="9326879089",
        location="Navi Mumbai",
        linkedin="https://www.linkedin.com/in/surabhi-pilane-852a622b6",
        github="https://github.com/surabhi1416"
    )

    projects = [
        Project(
            id=1,
            title="Sales Insights Dashboard",
            description="Analyzed 10K+ records using Power BI for data-driven decision making.",
            image="https://images.unsplash.com/photo-1551288049-bebda4e38f71?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzF8MHwxfHNlYXJjaHwxfHxkYXRhJTIwZGFzaGJvYXJkfGVufDB8fHx8MTc1MzU0MzUzM3ww&ixlib=rb-4.1.0&q=85",
            github="https://github.com/surabhi1416/Sales-Insights-Using-PowerBi",
            technologies=["Power BI", "Data Analytics", "SQL"],
            category="Data Analytics"
        ),
        Project(
            id=2,
            title="HR Data Analytics",
            description="Visualized HR trends like attrition and salary using Power BI dashboards.",
            image="https://images.unsplash.com/photo-1666875753105-c63a6f3bdc86?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzF8MHwxfHNlYXJjaHwyfHxkYXRhJTIwZGFzaGJvYXJkfGVufDB8fHx8MTc1MzU0MzUzM3ww&ixlib=rb-4.1.0&q=85",
            github="https://github.com/surabhi1416/HR-DATA-ANALYTICS",
            technologies=["Power BI", "HR Analytics", "Data Visualization"],
            category="Data Analytics"
        ),
        Project(
            id=3,
            title="Potato Disease Detection",
            description="Used CNN with TensorFlow to detect potato leaf diseases from images.",
            image="https://images.unsplash.com/photo-1557562645-4eee56b29bc1?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1NzZ8MHwxfHNlYXJjaHwxfHxtYWNoaW5lJTIwbGVhcm5pbmd8ZW58MHx8fHwxNzUzNTQzNTQ2fDA&ixlib=rb-4.1.0&q=85",
            github="https://github.com/surabhi1416/Potato_leafs_detection_project/tree/main",
            technologies=["TensorFlow", "CNN", "Image Processing", "Python"],
            category="Machine Learning"
        ),
        Project(
            id=4,
            title="Indian City GDP Analysis",
            description="Created Power BI dashboard highlighting economic zones & trends.",
            image="https://images.unsplash.com/photo-1585123607190-72ec2979a269?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzZ8MHwxfHNlYXJjaHwyfHxhbmFseXRpY3MlMjB2aXN1YWxpemF0aW9ufGVufDB8fHx8MTc1MzU0MzU0MHww&ixlib=rb-4.1.0&q=85",
            github="https://github.com/surabhi1416/INDIAN-CITIES-GDP-ANALYSIS",
            technologies=["Power BI", "Economic Analysis", "Data Visualization"],
            category="Data Analytics"
        ),
        Project(
            id=5,
            title="Network Intrusion Detection System",
            description="Built ML models (SVM, Random Forest) to detect anomalies with 90%+ accuracy.",
            image="https://images.unsplash.com/photo-1495592822108-9e6261896da8?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1NzZ8MHwxfHNlYXJjaHwzfHxtYWNoaW5lJTIwbGVhcm5pbmd8ZW58MHx8fHwxNzUzNTQzNTQ2fDA&ixlib=rb-4.1.0&q=85",
            github="https://github.com/surabhi1416/Network_Intrusion_Detection_System-",
            technologies=["SVM", "Random Forest", "Anomaly Detection", "Python"],
            category="Machine Learning"
        )
    ]

    experience = [
        Experience(
            id=1,
            title="Data Visualization Intern",
            company="Infosys Springboard",
            duration="Feb 2024 – Apr 2024",
            description="Developed Power BI dashboards for GDP trends using public datasets and Power Query.",
            technologies=["Power BI", "Power Query", "Data Visualization"]
        ),
        Experience(
            id=2,
            title="AI/ML Intern",
            company="ONGC",
            duration="June 2024 – July 2024",
            description="Worked on ML-based anomaly detection system (NIDS) using SVM and Random Forest.",
            technologies=["Machine Learning", "SVM", "Random Forest", "Python"]
        )
    ]

    return Portfolio(
        personal=personal_info,
        projects=projects,
        experience=experience
    )