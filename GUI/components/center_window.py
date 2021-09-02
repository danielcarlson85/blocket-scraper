def center(self):
    qr = self.frameGeometry()
    cp = self.screen().availableGeometry().center()

    qr.moveCenter(cp)
    self.move(qr.topLeft())