# <img src="https://img.icons8.com/color/48/000000/training.png" width="32" height="32"/> EduPlat

> **A Comprehensive Educational Platform for Online Learning**

[![Django](https://img.shields.io/badge/Django-4.1.7-092E20?logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap)](https://getbootstrap.com/)
[![QR Code](https://img.shields.io/badge/QR_Code-7.4.2-000000?logo=qrcode)](https://pypi.org/project/qrcode/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

![EduPlat Demo](https://placehold.co/800x400/092E20/FFFFFF/png?text=EduPlat+Educational+Platform&font=montserrat)

## 🎓 Overview

EduPlat is a comprehensive educational platform designed to facilitate online learning between teachers and students. The platform provides a rich set of features for course management, interactive learning, assignments, and communication, empowering educators to create engaging learning experiences while giving students easy access to educational content.

<b>🌟 Key Features</b>

- 🌐 **Multilingual Support** - Available in both Arabic (default) and English
- 👥 **User Management** - Student and teacher roles with customizable profiles
- 📚 **Course Management** - Create, organize, and sell lectures and courses
- 🎬 **Content Delivery** - Video lessons, PDF files, and attachments
- ✅ **Interactive Assessment** - Quizzes, homework, and assignments with analytics
- 💬 **Discussion Forum** - Q&A system for students to ask questions
- 👫 **Group Collaboration** - Create and manage study groups
- 💳 **Payment Integration** - Purchase courses using wallet or discount codes
- 📱 **QR Code Access** - Quick access to courses via QR codes
- 🏆 **Leaderboard System** - Gamification with student rankings
- 📊 **Analytics Dashboard** - Track student progress and engagement
- 🖌️ **Theme Customization** - Personalized platform appearance
- 📱 **Responsive Design** - Mobile-friendly interface for learning on any device

## 🔧 Tech Stack

<div align="center">
  <table>
    <tr>
      <td align="center" width="96">
        <img src="https://techstack-generator.vercel.app/python-icon.svg" alt="Python" width="48" height="48" />
        <br/>Python
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" alt="Django" width="48" height="48" />
        <br/>Django
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" alt="SQLite" width="48" height="48" />
        <br/>SQLite
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" alt="HTML5" width="48" height="48" />
        <br/>HTML5
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" alt="CSS3" width="48" height="48" />
        <br/>CSS3
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript" width="48" height="48" />
        <br/>JavaScript
      </td>
    </tr>
    <tr>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" alt="Bootstrap" width="48" height="48" />
        <br/>Bootstrap
      </td>
      <td align="center" width="96">
        <img src="https://avatars.githubusercontent.com/u/7886706" alt="QR Code" width="48" height="48" />
        <br/>QR Code
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pillow/pillow-original.svg" alt="Pillow" width="48" height="48" />
        <br/>Pillow
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jquery/jquery-original.svg" alt="jQuery" width="48" height="48" />
        <br/>jQuery
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" alt="Git" width="48" height="48" />
        <br/>Git
      </td>
      <td align="center" width="96">
        <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="Postman" width="48" height="48" />
        <br/>Postman
      </td>
    </tr>
  </table>
</div>

<b>⚙️ Backend</b>

- Django 4.1.7 - High-level Python web framework
- SQLite - Embedded, serverless database engine
- Python 3.x - Programming language
- Django Auth - Authentication system
- Django ORM - Object-relational mapping

<b>🎨 Frontend</b>

- HTML5 - Structure and content
- CSS3 - Styling and animations
- JavaScript - Client-side interactivity
- Bootstrap - Responsive UI components
- jQuery - JavaScript library for DOM manipulation

<b>📦 Additional Libraries</b>

- Pillow - Python Imaging Library for image processing
- QR Code (7.4.2) - QR code generation
- Django Unfold - Admin interface customization

## 📂 Project Structure

```
eduplat/
├── main/               # Core functionality
│   ├── models.py       # Database models
│   ├── views.py        # View controllers
│   ├── urls.py         # URL routing
│   └── middleware.py   # Custom middleware
├── student/            # Student-related features
├── dashboard/          # Analytics and admin dashboard
├── assignment/         # Assignment system
├── templates/          # HTML templates
│   ├── main/           # Main app templates
│   ├── dark/           # Dark mode templates
│   └── profile/        # User profile templates
├── static/             # Static files
│   ├── css/            # CSS files
│   ├── js/             # JavaScript files
│   └── images/         # Static images
├── media/              # User-uploaded files
├── plat/               # Project configuration
│   ├── settings.py     # Project settings
│   ├── urls.py         # Main URL routing
│   └── wsgi.py         # WSGI configuration
├── manage.py           # Django command-line utility
└── requirements.txt    # Project dependencies
```

## 👥 User Roles and Permissions

<table>
  <tr>
    <th>Feature</th>
    <th>Students</th>
    <th>Teachers</th>
    <th>Admins</th>
  </tr>
  <tr>
    <td>Access Learning Content</td>
    <td align="center">✅</td>
    <td align="center">✅</td>
    <td align="center">✅</td>
  </tr>
  <tr>
    <td>Create Courses</td>
    <td align="center">❌</td>
    <td align="center">✅</td>
    <td align="center">✅</td>
  </tr>
  <tr>
    <td>Submit Assignments</td>
    <td align="center">✅</td>
    <td align="center">❌</td>
    <td align="center">❌</td>
  </tr>
  <tr>
    <td>Grade Assignments</td>
    <td align="center">❌</td>
    <td align="center">✅</td>
    <td align="center">✅</td>
  </tr>
  <tr>
    <td>Join Groups</td>
    <td align="center">✅</td>
    <td align="center">✅</td>
    <td align="center">✅</td>
  </tr>
  <tr>
    <td>Create Groups</td>
    <td align="center">❌</td>
    <td align="center">✅</td>
    <td align="center">✅</td>
  </tr>
  <tr>
    <td>System Configuration</td>
    <td align="center">❌</td>
    <td align="center">❌</td>
    <td align="center">✅</td>
  </tr>
</table>

## 🚀 Installation

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Git

### Setup Instructions

1️⃣ **Clone the repository:**
```bash
git clone https://github.com/yourusername/eduplat.git
cd eduplat
```

2️⃣ **Create and activate virtual environment:**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

3️⃣ **Install dependencies:**
```bash
pip install -r requirements.txt
```

4️⃣ **Run database migrations:**
```bash
python manage.py migrate
```

5️⃣ **Create a superuser:**
```bash
python manage.py createsuperuser
```

6️⃣ **Start the development server:**
```bash
python manage.py runserver
```

7️⃣ **Access the application:**
- Open your browser and navigate to `http://127.0.0.1:8000/`
- Admin panel: `http://127.0.0.1:8000/admin/`

## 📱 Mobile Responsiveness

EduPlat is designed to work seamlessly across all devices:

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://placehold.co/250x500/092E20/FFFFFF/png?text=Mobile+View" alt="Mobile View" width="180"/>
        <br/>Mobile View
      </td>
      <td align="center">
        <img src="https://placehold.co/350x500/092E20/FFFFFF/png?text=Tablet+View" alt="Tablet View" width="250"/>
        <br/>Tablet View
      </td>
      <td align="center">
        <img src="https://placehold.co/600x400/092E20/FFFFFF/png?text=Desktop+View" alt="Desktop View" width="400"/>
        <br/>Desktop View
      </td>
    </tr>
  </table>
</div>

## 🌐 Localization

EduPlat currently supports the following languages:

- 🇪🇬 Arabic (default)
- 🇬🇧 English

Language preferences can be easily adjusted in the user interface.

## 🔒 Security Features

- User authentication and authorization
- Password hashing and security
- Role-based access control (RBAC)
- CSRF protection
- Secure content delivery
- Protected payment processing
- Data validation and sanitization

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/eduplat/issues).

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For questions or support, please contact [your-email@example.com](mailto:your-email@example.com)

---

<div align="center">
  <img src="https://img.icons8.com/color/48/000000/training.png" width="24" height="24"/>
  <p>Empowering education through technology</p>
</div> 
