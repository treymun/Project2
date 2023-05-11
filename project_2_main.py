from project_2_controller import *

def main():
    app = QApplication([])
    window = Controller()
    window.setGeometry(900, 450, 585, 370)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()


