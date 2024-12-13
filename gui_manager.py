from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QWidget,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
)
from db_manager import init_db, add_password, get_passwords


class PasswordManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Manager")
        self.setGeometry(100, 100, 600, 400)

        init_db()  # Initialize the database

        self.initUI()

    def initUI(self):
        """Set up the UI components."""
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Title
        title_label = QLabel("Password Manager")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; text-align: center;")
        layout.addWidget(title_label)

        # Service input
        self.service_input = QLineEdit()
        self.service_input.setPlaceholderText("Enter service (e.g., Gmail, Facebook)")
        layout.addWidget(self.service_input)

        # Username input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter username/email")
        layout.addWidget(self.username_input)

        # Password input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        # Save button
        save_button = QPushButton("Save Password")
        save_button.clicked.connect(self.save_password)
        layout.addWidget(save_button)

        # Password table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Service", "Username", "Password"])
        layout.addWidget(self.table)

        # View button
        view_button = QPushButton("View Passwords")
        view_button.clicked.connect(self.load_passwords)
        layout.addWidget(view_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def save_password(self):
        """Save a password to the database."""
        service = self.service_input.text().strip()
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not service or not username or not password:
            QMessageBox.warning(self, "Error", "All fields must be filled!")
        else:
            add_password(service, username, password)
            QMessageBox.information(self, "Success", "Password saved successfully!")
            self.service_input.clear()
            self.username_input.clear()
            self.password_input.clear()

    def load_passwords(self):
        """Load all passwords from the database and display them in the table."""
        passwords = get_passwords()
        self.table.setRowCount(len(passwords))

        for row_num, row_data in enumerate(passwords):
            for col_num, col_data in enumerate(row_data):
                self.table.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))
