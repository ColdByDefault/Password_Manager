import sys
from PyQt5.QtWidgets import QApplication
from db_manager import init_db
from gui_manager import PasswordManagerApp

if __name__ == "__main__":
    init_db()  # Ensure the database is initialized before running the app
    app = QApplication(sys.argv)
    main_window = PasswordManagerApp()
    main_window.show()
    sys.exit(app.exec())
