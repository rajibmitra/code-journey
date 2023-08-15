---

# LeetCode Journey

Track and visualize your progress on LeetCode with a tree-like structure representing different topics and problems.

## Overview

This Django-based web application provides a visual representation of a user's programming journey on LeetCode. Starting with foundational topics like Arrays, the tree branches out into subtopics, each containing specific problems the user has tackled.

## Features

- **Tree Structure Visualization**: Navigate through different programming topics and see which problems have been solved under each.
- **Responsive Design**: Built with Bootstrap for a clean, mobile-friendly user experience.
- **Dynamic Content**: Easily update and expand the tree as you progress in your LeetCode journey.

## Setup & Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rajibmitra/leetcode-journey.git
   cd leetcode-journey
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser to view the app.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

 Apache-2.0 license

---

